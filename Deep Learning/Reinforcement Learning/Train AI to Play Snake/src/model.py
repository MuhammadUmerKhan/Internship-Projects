import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os
import numpy as np
import logging
from config import MODEL_PATH

class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x

    def save(self, file_name=MODEL_PATH):
        try:
            model_folder_path = os.path.dirname(file_name)
            if not os.path.exists(model_folder_path):
                os.makedirs(model_folder_path)
            torch.save(self.state_dict(), file_name)
            logging.info(f"Model saved to {file_name}")
        except Exception as e:
            logging.error(f"Error saving model: {e}")
            raise

class QTrainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        try:
            self.optimizer = optim.Adam(model.parameters(), lr=self.lr)
            self.criterion = nn.MSELoss()
        except Exception as e:
            logging.error(f"Error initializing optimizer or criterion: {e}")
            raise

    def train_step(self, state, action, reward, next_state, done):
        try:
            if isinstance(state, list):
                state = np.array(state, dtype=np.float32)
            if isinstance(next_state, list):
                next_state = np.array(next_state, dtype=np.float32)
            if isinstance(action, list):
                action = np.array(action, dtype=np.int64)
            if isinstance(reward, list):
                reward = np.array(reward, dtype=np.float32)

            state = torch.tensor(state, dtype=torch.float)
            next_state = torch.tensor(next_state, dtype=torch.float)
            action = torch.tensor(action, dtype=torch.long)
            reward = torch.tensor(reward, dtype=torch.float)

            if len(state.shape) == 1:
                state = torch.unsqueeze(state, 0)
                next_state = torch.unsqueeze(next_state, 0)
                action = torch.unsqueeze(action, 0)
                reward = torch.unsqueeze(reward, 0)
                done = (done, )

            pred = self.model(state)
            target = pred.clone()
            for idx in range(len(done)):
                Q_new = reward[idx]
                if not done[idx]:
                    Q_new = reward[idx] + self.gamma * torch.max(self.model(next_state[idx]))
                target[idx][torch.argmax(action[idx]).item()] = Q_new

            self.optimizer.zero_grad()
            loss = self.criterion(target, pred)
            loss.backward()
            self.optimizer.step()
        except Exception as e:
            logging.error(f"Error in train_step: {e}")
            raise