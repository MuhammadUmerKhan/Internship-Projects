# Snake AI Project

## Overview
The Snake AI project is an engaging reinforcement learning (RL) application that trains an artificial intelligence agent to play the classic Snake game using Q-learning with a deep neural network implemented in PyTorch. The project features a polished Pygame-based user interface (UI) with a grid, pulsing food effects, and a game-over screen, alongside a real-time Matplotlib plot to visualize training progress. Designed for both educational and demonstration purposes, it combines modularity, robust error handling, and an attractive UI to create a professional and distributable application.

The AI learns to navigate the game environment by balancing exploration and exploitation, using a neural network to approximate Q-values. Training progress is logged to both a file and the console, and plots are saved periodically for analysis. The project is structured for maintainability, with clear separation of concerns across game logic, RL agent, neural network, visualization, and configuration.

## Project Objectives
- Train an AI to play Snake using Q-learning with experience replay.
- Provide a visually appealing game UI with real-time interaction.
- Visualize training metrics (scores, mean scores, record) in a dynamic plot.
- Ensure robust logging and error handling for reliability.
- Organize the codebase for easy extension and distribution.

## Project Structure
The project is organized as follows, with the `src` folder containing the core Python modules and additional directories for assets, logs, models, and plots:

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
│   ├── arial.ttf         # Font file for Pygame UI
├── logs/
│   ├── training.log      # Training logs
├── model/
│   ├── model.pth         # Saved neural network weights
├── plot/
│   ├── training_plot_*.png  # Saved training plots
├── requirements.txt      # Python dependencies
├── README.md             # This documentation
```

### Directory and File Descriptions
1. **src/**:
   - Contains the core Python modules for the project, organized as a package for clean imports.
   - `__init__.py`: An empty file marking `src` as a Python package.
   - **agent.py**: Implements the RL agent and training loop.
     - Defines the `Agent` class for state processing, action selection, and learning.
     - Uses epsilon-greedy policy with linear decay (`EPSILON_START = 80`).
     - Stores experiences in a replay memory (`MAX_MEMORY = 100,000`) and trains on batches (`BATCH_SIZE = 1000`).
     - Integrates with `game.py` for environment interaction, `model.py` for learning, and `utils.py` for plotting.
   - **config.py**: Centralizes configuration parameters.
     - Includes game settings (`WINDOW_WIDTH = 640`, `WINDOW_HEIGHT = 480`, `BLOCK_SIZE = 20`, `SPEED = 40`).
     - Defines RL parameters (`LEARNING_RATE = 0.001`, `GAMMA = 0.9`).
     - Specifies model settings (`INPUT_SIZE = 11`, `HIDDEN_SIZE = 256`, `OUTPUT_SIZE = 3`).
     - Sets paths for logs (`logs/training.log`), model (`model/model.pth`), font (`assets/arial.ttf`), and plots (`plot/`).
   - **game.py**: Implements the Snake game and Pygame UI.
     - Manages game state, snake movement, food placement, and collisions.
     - Renders a grid, snake (two-tone blue), pulsing food, and score.
     - Displays a game-over screen with restart option (‘R’ key).
     - Returns rewards (`+10` for food, `-10` for collision) and game state.
   - **main.py**: Entry point for the application.
     - Parses command-line arguments (e.g., `--train`) using `argparse`.
     - Initializes logging and starts training via `agent.py`.
   - **model.py**: Defines the neural network and Q-learning trainer.
     - `Linear_QNet`: A two-layer feedforward neural network with ReLU activation.
     - `QTrainer`: Trains the network using Adam optimizer and MSE loss, implementing the Bellman equation.
     - Saves model weights when a new record score is achieved.
   - **utils.py**: Handles logging and visualization.
     - Sets up logging to file and console with a custom format.
     - Plots training progress in real-time with scores, mean scores, and record highlights.
     - Uses `seaborn`’s `darkgrid` style, neon green and orange lines, and annotations for latest and record scores.
     - Saves plots every 50 games to `plot/`.

2. **assets/**:
   - Stores static resources, currently containing `arial.ttf` for Pygame’s font rendering.
   - Ensures consistent text display in the game UI (score, game-over screen).

3. **logs/**:
   - Contains `training.log`, which records training events (e.g., game scores, errors, model saves).
   - Logs are also printed to the console for real-time monitoring.

4. **model/**:
   - Stores `model.pth`, the saved weights of the trained neural network.
   - Updated whenever a new record score is achieved during training.

5. **plot/**:
   - Stores PNG images of training plots (`training_plot_*.png`) saved every 50 games.
   - Visualizes scores, mean scores, and record scores for post-training analysis.

6. **requirements.txt**:
   - Lists Python dependencies:
     ```
     torch>=1.13.0
     pygame>=2.6.0
     matplotlib>=3.8.0
     numpy>=1.24.0
     seaborn>=0.13.0
     ```
   - Ensures consistent environment setup across systems.

7. **README.md**:
   - This file, providing detailed documentation for setup, usage, and project details.

## Key Technical Features
- **Reinforcement Learning**:
  - Implements Q-learning with a deep neural network to approximate Q-values for three actions (straight, right, left).
  - Uses experience replay (`MAX_MEMORY = 100,000`) and mini-batch training (`BATCH_SIZE = 1000`) for stable learning.
  - Employs an epsilon-greedy policy with linear decay (`EPSILON_START = 80`) to balance exploration and exploitation.
- **Game Environment**:
  - Built with Pygame, featuring a 640x480 window, 20x20 pixel grid, and 40 FPS gameplay.
  - Includes a dynamic UI with a gray grid, two-tone snake, pulsing food, and a semi-transparent game-over screen.
  - Supports restarting games with the ‘R’ key when game over.
- **Visualization**:
  - Real-time Matplotlib plot with `TkAgg` backend, showing scores (blue dash-dot with markers), mean scores (orange dashed), and record score (pink marker).
  - Annotations highlight the latest scores and record, using a neon green (`#00FFAA`) and orange (`#FFA500`) palette.
  - Saves high-quality PNGs every 50 games for analysis.
- **Modularity**:
  - Codebase is organized into a `src` package with distinct modules for game logic, RL agent, neural network, utilities, and configuration.
  - Uses `os.path.join` for cross-platform path compatibility.
- **Error Handling**:
  - Comprehensive try-except blocks in all modules to catch and log errors (e.g., Pygame initialization, tensor operations).
  - Gracefully handles user interrupts (`KeyboardInterrupt`, window close) with proper cleanup.
- **Logging**:
  - Centralized logging system outputs to `logs/training.log` and console with a timestamped format.
  - Logs game progress, model saves, errors, and user actions.
- **Performance**:
  - Optimized tensor handling in `model.py` to avoid PyTorch warnings.
  - Efficient Pygame rendering with a fixed frame rate.
  - Periodic plot saving to balance visualization and performance.

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
   Create or verify `requirements.txt` in the project root:
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
   # On Windows, Tkinter is included with Python
   ```
5. **Prepare Assets**:
   - Place `arial.ttf` in `assets/`. Download it from a font repository (e.g., Google Fonts) or use another TTF font, updating `FONT_PATH` in `src/config.py` if needed.
   - Ensure `assets/`, `logs/`, `model/`, and `plot/` directories exist (created automatically by the code if missing).
6. **Run the Application**:
   From the `snake-ai` directory:
   ```bash
   python src/main.py --train
   ```

## Usage
- **Training Mode**:
  - Command: `python src/main.py --train`
  - **Pygame Window**: Displays the Snake game with:
    - A gray grid for the game board.
    - A two-tone blue snake (`BLUE1`, `BLUE2`).
    - Pulsing red food that animates in size.
    - Score in the top-left corner.
    - Game-over screen with score and “Press R to Restart” prompt.
  - **Matplotlib Window**: Shows real-time training progress:
    - Blue dash-dot line with circle markers for scores.
    - Orange dashed line for mean scores.
    - Pink scatter point for the record score with annotation.
    - Title with game count and record score.
  - **Logs**: Saved to `logs/training.log` and printed to the console (e.g., `Game 1 Score 0 Record: 0`).
  - **Outputs**:
    - Model weights saved to `model/model.pth` on new record scores.
    - Plots saved to `plot/training_plot_*.png` every 50 games.
- **Stopping Training**:
  - Press `Ctrl+C` to interrupt training, closing Pygame and logging the interruption.
  - Close the Pygame window to exit the application.
- **Restarting Games**:
  - Press `R` in the Pygame window during the game-over screen to reset the game environment (continues training).

## Extending the Project
- **Play Mode**:
  - Add a `--play` argument to `main.py` to load `model.pth` and run the trained model without training.
  - Example implementation: Load the model in `agent.py` and disable training steps.
- **Hyperparameter Tuning**:
  - Adjust `LEARNING_RATE`, `GAMMA`, `EPSILON_START`, or `HIDDEN_SIZE` in `config.py` to optimize learning.
  - Experiment with `SPEED` for faster or slower gameplay.
- **UI Enhancements**:
  - Customize colors in `game.py` (e.g., snake, food) or `utils.py` (e.g., plot palette).
  - Add sound effects or background music to Pygame using `pygame.mixer`.
  - Enhance the plot with additional metrics (e.g., loss, epsilon).
- **Testing**:
  - Create a `tests` folder with `pytest` unit tests for game logic (e.g., collision detection) or agent behavior.
  - Example: Test `is_collision` in `game.py` with various inputs.
- **Deployment**:
  - Package the project with a `setup.py` for distribution via `pip install .`.
  - Use PyInstaller to create a standalone executable: `pyinstaller --add-data "assets;assets" src/main.py`.
- **Advanced RL**:
  - Implement Double Q-learning or Dueling DQN in `model.py` for better performance.
  - Add a convolutional neural network to process raw game frames instead of hand-crafted states.

## Troubleshooting
- **Pygame Issues**:
  - **Window Not Opening**: Ensure `pygame` is installed (`pip install pygame`) and `arial.ttf` is in `assets/`.
  - **Font Error**: Verify `FONT_PATH` in `config.py`. Alternatively, use a system font: `pygame.font.SysFont('arial', 25)`.
  - **Window Closes Unexpectedly**: Check `logs/training.log` for errors (e.g., initialization failures).
- **Matplotlib Issues**:
  - **Plot Not Displaying**: Confirm `python3-tk` is installed and the backend is `TkAgg` (`python -c "import matplotlib; print(matplotlib.get_backend())"`).
  - **Slow Plot Updates**: Increase `plt.pause(0.2)` in `utils.py` or plot less frequently (e.g., every 5 games in `agent.py`).
  - **Missing Seaborn**: Install it with `pip install seaborn`.
- **File Path Issues**:
  - **Logs/Models/Plots Not Saving**: Ensure `logs/`, `model/`, and `plot/` are writable. Verify paths in `config.py` (e.g., `MODEL_PATH`, `LOG_FILE`, `IMG_PATH`).
  - **Running from Wrong Directory**: Run `python src/main.py --train` from `snake-ai/`, or adjust paths in `config.py` to be absolute using `os.path.abspath`.
- **Training Issues**:
  - **Low Scores**: Run training for more games (e.g., 1000+). Tune `LEARNING_RATE` (e.g., 0.0005) or `EPSILON_START` (e.g., 100).
  - **No Learning**: Check `INPUT_SIZE` (11) matches the state vector in `agent.py`. Ensure `GAMMA` and `LEARNING_RATE` are reasonable.
- **Performance Issues**:
  - **Slow Gameplay**: Reduce `SPEED` in `config.py` (e.g., 20).
  - **High CPU Usage**: Plot less frequently by modifying `agent.py`:
    ```python
    if done and agent.n_games % 5 == 0:
        plot_scores.append(score)
        total_score += score
        mean_score = total_score / agent.n_games
        plot_mean_scores.append(mean_score)
        plot_training(plot_scores, plot_mean_scores, record)
    ```

## Technical Details
- **Q-Learning**:
  - The agent learns by updating Q-values using the Bellman equation: `Q_new = reward + gamma * max(next_Q)` for non-terminal states.
  - Rewards: `+10` for eating food, `-10` for collisions or timeouts (100 * snake length frames).
  - State: 11 features (3 danger indicators, 4 direction flags, 4 food position flags).
- **Neural Network**:
  - Two-layer feedforward network: 11 inputs → 256 hidden (ReLU) → 3 outputs.
  - Trained with Adam optimizer (`LEARNING_RATE = 0.001`) and MSE loss.
- **Experience Replay**:
  - Stores up to 100,000 experiences (state, action, reward, next_state, done).
  - Samples 1000 experiences for batch training to reduce correlation.
- **Pygame UI**:
  - 32x24 grid (640x480 pixels, 20x20 blocks).
  - Pulsing food effect using `pygame.time.get_ticks()` for animation.
  - Game-over screen with semi-transparent overlay and restart prompt.
- **Matplotlib Plot**:
  - Uses `TkAgg` backend for cross-platform compatibility.
  - Interactive mode (`plt.ion()`) for real-time updates.
  - Saves plots with a simple naming scheme (`training_plot_50.png`, etc.).
- **Logging**:
  - Format: `%(asctime)s - %(levelname)s - %(message)s` (e.g., `2025-05-13 23:25:00,123 - INFO - Game 1 Score 0 Record: 0`).
  - Ensures traceability of training progress and errors.

## System Requirements
- **Operating System**: Windows, macOS, or Linux.
- **Python**: Version 3.8 or higher.
- **Hardware**:
  - CPU: Any modern CPU (GPU optional, as training is lightweight).
  - RAM: At least 4 GB.
  - Disk Space: ~500 MB for dependencies and outputs.
- **Dependencies**: Listed in `requirements.txt` (PyTorch, Pygame, Matplotlib, NumPy, Seaborn).
- **Additional Software**: Tkinter for Matplotlib (`python3-tk` on Linux).

## License
MIT License. See `LICENSE` file (or add one to the repository) for details.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request with a detailed description.

Please report bugs or suggest features via GitHub issues.