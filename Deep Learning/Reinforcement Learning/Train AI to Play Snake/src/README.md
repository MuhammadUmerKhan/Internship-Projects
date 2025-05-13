# Snake AI Project

## Overview
The Snake AI project is a reinforcement learning (RL) application that trains an artificial intelligence agent to play the classic Snake game using a Q-learning algorithm implemented with PyTorch. The project features a visually appealing Pygame-based game interface and a real-time Matplotlib plot to visualize training progress. The codebase is organized in a modular, professional structure within the `src` folder, with robust logging, error handling, and an enhanced user interface (UI) to make it suitable for both learning and demonstration purposes.

The project leverages a deep neural network to approximate Q-values, enabling the AI to learn optimal actions through exploration and exploitation. The training process is logged to both a file and the console, and training plots are periodically saved for analysis. The UI includes a dynamic game grid, pulsing food effects, and a game-over screen, making the project engaging and visually appealing.

This README focuses on the `src` folder, which contains the core Python modules driving the project. Below, we detail each file, its purpose, key components, and how they integrate to form the complete application.

## Project Structure
The `src` folder contains the following files, each serving a distinct role in the project:

```
snake-ai/
├── src/
│   ├── __init__.py       # Marks src as a Python package
│   ├── agent.py          # RL agent and training logic
│   ├── config.py         # Configuration parameters
│   ├── game.py           # Snake game logic and Pygame UI
│   ├── main.py           # Entry point for running the application
│   ├── model.py          # Neural network and Q-learning trainer
│   ├── utils.py          # Logging setup and training plot visualization
├── assets/
│   ├── arial.ttf         # Font file for Pygame
├── logs/
│   ├── training.log      # Training logs
├── model/
│   ├── model.pth         # Saved model weights
├── plot/
│   ├── training_plot_*.png  # Saved training plots
├── README.md             # This file
├── requirements.txt      # Dependencies
```

## Detailed Description of `src` Folder Files

### 1. `__init__.py`
- **Purpose**: An empty file that designates the `src` directory as a Python package, allowing modules within it to be imported using package notation (e.g., `from src.game import SnakeGameAI`).
- **Key Points**:
  - Ensures modularity and proper import paths.
  - No active code; serves as a structural marker.

### 2. `agent.py`
- **Purpose**: Implements the reinforcement learning agent and the main training loop for the Snake AI.
- **Key Components**:
  - **Agent Class**:
    - **Initialization**: Sets up the agent's properties, including game counter (`n_games`), exploration rate (`epsilon`), discount factor (`gamma`), and a replay memory (`memory`) with a maximum size defined by `MAX_MEMORY` (100,000).
    - **Neural Network**: Instantiates a `Linear_QNet` (from `model.py`) with 11 input features (state size), 256 hidden units, and 3 output actions (straight, right, left).
    - **QTrainer**: Uses a `QTrainer` (from `model.py`) for training the neural network with a learning rate (`LEARNING_RATE = 0.001`) and discount factor (`GAMMA = 0.9`).
    - **Methods**:
      - `get_state`: Computes the game state as an 11-element vector, including danger indicators (straight, right, left), current direction, and food location relative to the snake's head.
      - `get_action`: Balances exploration (random moves) and exploitation (model-predicted moves) using an epsilon-greedy strategy, with `epsilon` decreasing linearly from `EPSILON_START` (80).
      - `remember`: Stores experiences (state, action, reward, next_state, done) in the replay memory.
      - `train_short_memory`: Trains the model on a single experience (short-term memory).
      - `train_long_memory`: Trains the model on a batch of experiences (batch size `BATCH_SIZE = 1000`) sampled from memory.
  - **train Function**:
    - Orchestrates the training loop, interacting with the `SnakeGameAI` (from `game.py`) to play steps, collect rewards, and update the agent.
    - Saves the model when a new record score is achieved.
    - Logs game progress (game number, score, record) using the logger from `utils.py`.
    - Calls `plot_training` (from `utils.py`) to visualize scores and mean scores after each game.
- **Error Handling**: Uses try-except blocks to catch and log errors in initialization, state retrieval, action selection, memory storage, and training.
- **Key Points**:
  - Implements Q-learning with experience replay for stable training.
  - Dynamically adjusts exploration via `epsilon` decay.
  - Integrates with `game.py` for environment interaction, `model.py` for learning, and `utils.py` for visualization and logging.
  - Handles `KeyboardInterrupt` to gracefully exit training and close Pygame.

### 3. `config.py`
- **Purpose**: Centralizes configuration parameters for the project, making it easy to tweak settings without modifying core code.
- **Key Components**:
  - **Game Settings**:
    - `WINDOW_WIDTH = 640`, `WINDOW_HEIGHT = 480`: Dimensions of the Pygame window.
    - `BLOCK_SIZE = 20`: Size of each game grid cell.
    - `SPEED = 40`: Game speed (frames per second).
  - **RL Parameters**:
    - `MAX_MEMORY = 100_000`: Maximum size of the agent's replay memory.
    - `BATCH_SIZE = 1000`: Number of experiences sampled for long-term memory training.
    - `LEARNING_RATE = 0.001`: Learning rate for the neural network optimizer.
    - `GAMMA = 0.9`: Discount factor for future rewards.
    - `EPSILON_START = 80`: Initial exploration rate for epsilon-greedy policy.
  - **Model Settings**:
    - `INPUT_SIZE = 11`: Number of state features.
    - `HIDDEN_SIZE = 256`: Number of units in the neural network's hidden layer.
    - `OUTPUT_SIZE = 3`: Number of possible actions.
    - `MODEL_PATH`: Path to save the trained model (`../model/model.pth`).
  - **Logging and Assets**:
    - `LOG_FILE`: Path for training logs (`../logs/training.log`).
    - `FONT_PATH`: Path to the font file (`../assets/arial.ttf`).
    - `IMG_PATH`: Path for saved plots (`../plot`).
  - **Directory Creation**: Uses `os.makedirs` to ensure directories for logs, assets, and plots exist.
- **Key Points**:
  - Provides a single source of truth for all configurable parameters.
  - Uses `os.path.join` for cross-platform path compatibility.
  - Paths are relative to the project root, assuming execution from the `src` folder or project root.

### 4. `game.py`
- **Purpose**: Implements the Snake game environment and Pygame-based UI for visualization.
- **Key Components**:
  - **Direction Enum**: Defines four directions (`RIGHT`, `LEFT`, `UP`, `DOWN`) for snake movement.
  - **Point NamedTuple**: Represents coordinates (`x`, `y`) for the snake and food.
  - **SnakeGameAI Class**:
    - **Initialization**: Sets up the Pygame window (640x480), display caption, clock, and font (`arial.ttf`). Initializes the game state via `reset`.
    - **reset**: Resets the game state, placing the snake at the center, setting the initial direction to `RIGHT`, and spawning food.
    - **play_step**: Executes one game step based on the provided action (straight, right, left):
      - Handles Pygame events (e.g., window close, restart on 'R' key when game over).
      - Updates the snake’s position, checks for collisions or food consumption, and computes rewards (`+10` for food, `-10` for collision).
      - Updates the UI and enforces the game speed (`SPEED = 40`).
      - Returns reward, game-over status, and current score.
    - **is_collision**: Checks for collisions with the game boundaries or the snake’s body.
    - **_place_food**: Randomly places food, ensuring it doesn’t overlap with the snake.
    - **_update_ui**: Renders the game:
      - Draws a gray grid for the game board.
      - Renders the snake with two shades of blue (`BLUE1`, `BLUE2`) for a layered effect.
      - Draws food with a pulsing animation (size varies based on time).
      - Displays the score in the top-left corner.
      - Shows a semi-transparent game-over screen with the final score and restart prompt.
    - **_move**: Updates the snake’s direction and position based on the action.
- **Error Handling**: Uses try-except blocks to catch and log errors during Pygame initialization and game steps.
- **Key Points**:
  - Provides a rich, interactive UI with a grid, animations, and game-over feedback.
  - Integrates with `agent.py` by accepting actions and returning states, rewards, and scores.
  - Ensures smooth gameplay with a fixed frame rate.
  - Gracefully handles user-initiated exits (e.g., closing the window).

### 5. `main.py`
- **Purpose**: Serves as the entry point for the application, parsing command-line arguments and initiating training.
- **Key Components**:
  - **main Function**:
    - Parses arguments using `argparse` to support a `--train` flag for training mode.
    - Initializes logging via `setup_logging` (from `utils.py`).
    - Calls the `train` function (from `agent.py`) if `--train` is specified, otherwise logs a message prompting mode selection.
  - **Error Handling**: Wraps the main logic in a try-except block to catch and log errors.
- **Key Points**:
  - Provides a clean, extensible interface for running the application.
  - Supports future modes (e.g., `--play` for testing a trained model) via additional arguments.
  - Ensures logging is set up before any operations begin.

### 6. `model.py`
- **Purpose**: Defines the neural network architecture and Q-learning trainer for the RL agent.
- **Key Components**:
  - **Linear_QNet Class** (inherits `nn.Module`):
    - **Initialization**: Creates a two-layer feedforward neural network with `input_size` (11), `hidden_size` (256), and `output_size` (3) units.
    - **forward**: Applies ReLU activation after the first layer and outputs Q-values for each action.
    - **save**: Saves the model’s weights to `MODEL_PATH`, creating the directory if needed.
  - **QTrainer Class**:
    - **Initialization**: Sets up the Adam optimizer with `LEARNING_RATE` and MSE loss function for Q-value updates.
    - **train_step**: Performs a single training step:
      - Converts inputs (state, action, reward, next_state, done) to NumPy arrays if they are lists, then to PyTorch tensors.
      - Handles both single experiences (short-term memory) and batches (long-term memory) by adjusting tensor shapes.
      - Computes predicted Q-values, updates target Q-values using the Bellman equation (`Q_new = reward + gamma * max(next_Q)` for non-terminal states), and applies gradient descent.
  - **Error Handling**: Uses try-except blocks to catch and log errors during model saving, optimizer setup, and training.
- **Key Points**:
  - Implements a simple yet effective neural network for Q-value approximation.
  - Supports both immediate and batch training for stability.
  - Integrates with `agent.py` for training and action prediction.
  - Optimizes tensor creation to avoid performance warnings.

### 7. `utils.py`
- **Purpose**: Provides utility functions for logging setup and real-time training visualization.
- **Key Components**:
  - **setup_logging Function**:
    - Configures logging with a custom format (`%(asctime)s - %(levelname)s - %(message)s`).
    - Outputs logs to both a file (`LOG_FILE`) and the console.
    - Returns a logger instance for use across modules.
  - **plot_training Function**:
    - Creates a real-time plot of training progress using Matplotlib with `TkAgg` backend and interactive mode (`plt.ion()`).
    - Clears the figure (`plt.clf()`) before each update to prevent overlap.
    - Uses `seaborn`’s `darkgrid` style for a professional look.
    - Plots:
      - Scores (blue, dash-dot line with circle markers) and mean scores (orange, dashed line).
      - Latest score and mean score with text annotations (`+2` offset for visibility).
      - Record score with a pink scatter point and text annotation.
    - Sets dynamic title (`Snake AI Training | Games Played: {len(scores)} | Record: {record}`) and bold axis labels.
    - Uses a neon green (`#00FFAA`) and orange (`#FFA500`) color palette for visibility.
    - Saves plots every 50 games to `IMG_PATH/training_plot_{len(scores)}.png`.
    - Updates the plot with `plt.draw()` and `plt.pause(0.1)` for real-time rendering.
  - **Error Handling**: Catches and logs plotting errors to prevent crashes.
- **Key Points**:
  - Delivers an engaging, real-time visualization of training progress.
  - Saves high-quality plots for post-training analysis.
  - Ensures robust logging for debugging and monitoring.
  - Integrates with `agent.py` to display training metrics.

## Key Technical Points
- **Reinforcement Learning**:
  - Uses Q-learning with a deep neural network to approximate Q-values.
  - Implements experience replay (`MAX_MEMORY = 100,000`) and mini-batch training (`BATCH_SIZE = 1000`) for stable learning.
  - Balances exploration and exploitation via an epsilon-greedy policy with linear decay.
- **Modularity**:
  - Separates concerns into distinct modules (game, agent, model, utils, config) for maintainability.
  - Uses a package structure (`src`) for clean imports.
- **UI/UX**:
  - Pygame UI features a grid, pulsing food, and a game-over screen with restart functionality.
  - Matplotlib plot provides real-time feedback with annotated scores and a modern aesthetic.
- **Error Handling**:
  - Comprehensive try-except blocks across all modules to catch and log errors.
  - Graceful handling of user interrupts (e.g., `KeyboardInterrupt`, window close).
- **Logging**:
  - Centralized logging system outputs to both file and console for easy debugging.
  - Logs critical events like game progress, model saving, and errors.
- **Performance**:
  - Optimized tensor creation in `model.py` to avoid PyTorch warnings.
  - Efficient Pygame rendering with a fixed frame rate (`SPEED = 40`).
  - Periodic plot saving (every 50 games) to balance visualization and performance.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd snake-ai
   ```
2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**:
   Ensure `requirements.txt` is in the project root with:
   ```
   torch>=1.13.0
   pygame>=2.6.0
   matplotlib>=3.8.0
   numpy>=1.24.0
   seaborn>=0.13.0
   ```
   Install them:
   ```bash
   pip install -r requirements.txt
   ```
4. **Install Tkinter** (for Matplotlib’s `TkAgg` backend):
   ```bash
   sudo apt-get install python3-tk  # On Ubuntu/Debian
   ```
5. **Prepare Assets**:
   - Place `arial.ttf` in `assets/`. Download it from a font repository or use another TTF font, updating `FONT_PATH` in `config.py` if needed.
6. **Run the Application**:
   From the `snake-ai` directory:
   ```bash
   python src/main.py --train
   ```

## Usage
- **Training Mode**:
  - Run `python src/main.py --train` to start training.
  - The Pygame window displays the Snake game with a grid, pulsing food, and score.
  - The Matplotlib window shows real-time training progress (scores, mean scores, record).
  - Logs are saved to `logs/training.log` and printed to the console.
  - The trained model is saved to `model/model.pth` when a new record score is achieved.
  - Plots are saved to `plot/training_plot_*.png` every 50 games.
- **Stopping Training**:
  - Press `Ctrl+C` to interrupt training, which closes Pygame and logs the interruption.
  - Close the Pygame window to exit the application.
- **Restarting Games**:
  - When the game is over, press `R` in the Pygame window to restart the game (resets the environment but continues training).

## Extending the Project
- **Play Mode**:
  - Add a `--play` argument to `main.py` to load a trained model (`model.pth`) and play without training.
- **Hyperparameter Tuning**:
  - Modify `config.py` to adjust `LEARNING_RATE`, `GAMMA`, `EPSILON_START`, or `SPEED` for better performance.
- **UI Enhancements**:
  - Customize colors or fonts in `game.py` or `utils.py`.
  - Add animations or sound effects to the Pygame UI.
- **Testing**:
  - Create a `tests` folder with unit tests using `pytest` to verify game logic or agent behavior.
- **Deployment**:
  - Package the project with a `setup.py` for distribution via `pip install`.
  - Use PyInstaller to create a standalone executable.

## Troubleshooting
- **Pygame Window Not Opening**:
  - Ensure `pygame` is installed and `arial.ttf` is in `assets/`.
  - Check `FONT_PATH` in `config.py` and verify the file exists.
- **Matplotlib Plot Not Displaying**:
  - Confirm `python3-tk` is installed and the backend is `TkAgg` (`python -c "import matplotlib; print(matplotlib.get_backend())"`).
  - Ensure `seaborn` and `matplotlib` are installed.
- **Logs or Plots Not Saving**:
  - Verify `logs/`, `model/`, and `plot/` directories are writable.
  - Check `LOG_FILE`, `MODEL_PATH`, and `IMG_PATH` in `config.py` for correct paths.
- **Low Scores**:
  - Run training for more games (e.g., 1000+) to allow learning.
  - Tune `LEARNING_RATE` or `EPSILON_START` in `config.py`.
- **Performance Issues**:
  - Reduce `SPEED` in `config.py` for slower gameplay.
  - Plot less frequently by modifying `agent.py` (e.g., plot every 5 games).

## License
MIT License

## Contributing
Contributions are welcome! Please open an issue or submit a pull request on the repository for bug fixes, features, or improvements.

## Contact
For questions or support, contact the project maintainer at [your-email@example.com] or open an issue on the repository.


### Explanation of Key Points
1. **Comprehensive Overview**:
   - The README starts with a clear project description, highlighting the RL approach, UI features, and modularity.
   - It emphasizes the project’s purpose (training an AI to play Snake) and its appeal (visualizations, professional structure).
2. **Detailed File Breakdown**:
   - Each file in `src` is described with its purpose, key components, and technical details (e.g., class methods, error handling).
   - Interactions between files (e.g., `agent.py` calling `game.py` and `utils.py`) are explained to show the system’s flow.
3. **Technical Highlights**:
   - Covers RL concepts (Q-learning, experience replay, epsilon-greedy), modularity, UI features, logging, and performance optimizations.
   - Explains critical parameters (e.g., `MAX_MEMORY`, `LEARNING_RATE`) and their roles.
4. **Setup and Usage**:
   - Provides step-by-step instructions for cloning, setting up a virtual environment, installing dependencies, and running the project.
   - Includes usage details for training mode, stopping training, and restarting games.
5. **Extensibility**:
   - Suggests future enhancements (play mode, hyperparameter tuning, testing) to guide developers.
6. **Troubleshooting**:
   - Addresses common issues (e.g., Pygame or Matplotlib failures, missing files) with actionable solutions.
7. **Professional Tone**:
   - Uses clear, concise language suitable for both technical and non-technical audiences.
   - Includes standard sections (License, Contributing, Contact) for completeness.