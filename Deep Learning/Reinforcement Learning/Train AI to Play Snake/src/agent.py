import torch
import random
import pygame
import numpy as np
from collections import deque
import logging
from game import SnakeGameAI, Direction, Point
from model import Linear_QNet, QTrainer
from utils import plot_training
from config import MAX_MEMORY, BATCH_SIZE, LEARNING_RATE, GAMMA, EPSILON_START, INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE

class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0
        self.gamma = GAMMA
        self.memory = deque(maxlen=MAX_MEMORY)
        try:
            self.model = Linear_QNet(INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE)
            self.trainer = QTrainer(self.model, lr=LEARNING_RATE, gamma=self.gamma)
        except Exception as e:
            logging.error(f"Error initializing agent: {e}")
            raise

    def get_state(self, game):
        try:
            head = game.snake[0]
            point_l = Point(head.x - 20, head.y)
            point_r = Point(head.x + 20, head.y)
            point_u = Point(head.x, head.y - 20)
            point_d = Point(head.x, head.y + 20)

            dir_l = game.direction == Direction.LEFT
            dir_r = game.direction == Direction.RIGHT
            dir_u = game.direction == Direction.UP
            dir_d = game.direction == Direction.DOWN

            state = [
                (dir_r and game.is_collision(point_r)) or
                (dir_l and game.is_collision(point_l)) or
                (dir_u and game.is_collision(point_u)) or
                (dir_d and game.is_collision(point_d)),

                (dir_u and game.is_collision(point_r)) or
                (dir_d and game.is_collision(point_l)) or
                (dir_l and game.is_collision(point_u)) or
                (dir_r and game.is_collision(point_d)),

                (dir_d and game.is_collision(point_r)) or
                (dir_u and game.is_collision(point_l)) or
                (dir_r and game.is_collision(point_u)) or
                (dir_l and game.is_collision(point_d)),

                dir_l, dir_r, dir_u, dir_d,
                game.food.x < game.head.x,
                game.food.x > game.head.x,
                game.food.y < game.head.y,
                game.food.y > game.head.y
            ]
            return np.array(state, dtype=int)
        except Exception as e:
            logging.error(f"Error in get_state: {e}")
            raise

    def remember(self, state, action, reward, next_state, done):
        try:
            self.memory.append((state, action, reward, next_state, done))
        except Exception as e:
            logging.error(f"Error in remember: {e}")
            raise

    def train_long_memory(self):
        try:
            if len(self.memory) > BATCH_SIZE:
                mini_sample = random.sample(self.memory, BATCH_SIZE)
            else:
                mini_sample = self.memory
            states, actions, rewards, next_states, dones = zip(*mini_sample)
            self.trainer.train_step(states, actions, rewards, next_states, dones)
        except Exception as e:
            logging.error(f"Error in train_long_memory: {e}")
            raise

    def train_short_memory(self, state, action, reward, next_state, done):
        try:
            self.trainer.train_step(state, action, reward, next_state, done)
        except Exception as e:
            logging.error(f"Error in train_short_memory: {e}")
            raise

    def get_action(self, state):
        try:
            self.epsilon = EPSILON_START - self.n_games
            final_move = [0, 0, 0]
            if random.randint(0, 200) < self.epsilon:
                move = random.randint(0, 2)
                final_move[move] = 1
            else:
                state0 = torch.tensor(state, dtype=torch.float)
                prediction = self.model(state0)
                move = torch.argmax(prediction).item()
                final_move[move] = 1
            return final_move
        except Exception as e:
            logging.error(f"Error in get_action: {e}")
            raise

def train():
    try:
        logger = logging.getLogger(__name__)
        plot_scores = []
        plot_mean_scores = []
        total_score = 0
        record = 0
        agent = Agent()
        game = SnakeGameAI()
        logger.info("Starting training")
        while True:
            state_old = agent.get_state(game)
            final_move = agent.get_action(state_old)
            reward, done, score = game.play_step(final_move)
            state_new = agent.get_state(game)
            agent.train_short_memory(state_old, final_move, reward, state_new, done)
            agent.remember(state_old, final_move, reward, state_new, done)

            if done:
                game.reset()
                agent.n_games += 1
                agent.train_long_memory()

                if score > record:
                    record = score
                    agent.model.save()

                logger.info(f"Game {agent.n_games} Score {score} Record: {record}")

                plot_scores.append(score)
                total_score += score
                mean_score = total_score / agent.n_games
                plot_mean_scores.append(mean_score)
                plot_training(plot_scores, plot_mean_scores, record)
    except KeyboardInterrupt:
        logger.info("Training interrupted by user")
        pygame.quit()
    except Exception as e:
        logger.error(f"Error in training: {e}")
        pygame.quit()
        raise