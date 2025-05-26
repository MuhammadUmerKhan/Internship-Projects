import os

# Game settings
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BLOCK_SIZE = 20
SPEED = 40

# RL parameters
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LEARNING_RATE = 0.001
GAMMA = 0.9
EPSILON_START = 80
IMPROVEMENT_THRESHOLD = 0.1  # 10% improvement in average score
GAMES_PLAYED = 50  # Start checking average score after 150 games
CHECK_SCORE_AFTER = 10  # Check average score every 10 games

# Model settings
INPUT_SIZE = 11
HIDDEN_SIZE = 256
OUTPUT_SIZE = 3
MODEL_PATH = os.path.join("..", "model", "model.pth")

# Logging
LOG_FILE = os.path.join("..", "logs", "training.log")
os.makedirs(os.path.join("..", "logs"), exist_ok=True)

# Assets
FONT_PATH = os.path.join("..", "assets", "arial.ttf")
os.makedirs(os.path.join("..", "assets"), exist_ok=True)

# Image
IMG_PATH = os.path.join("..", "plot")
os.makedirs(IMG_PATH, exist_ok=True)