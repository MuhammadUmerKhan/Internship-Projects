import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from config import LOG_FILE, IMG_PATH

plt.ion()  # Enable interactive mode

def setup_logging():
    """Set up logging to file and console."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def plot_training(scores, mean_scores, record):
    """Plot training progress with enhanced aesthetics."""
    try:
        plt.clf()  # Clear the current figure
        sns.set_style("darkgrid")
        
        # Title and labels
        plt.title(f"Snake AI Training | Games Played: {len(scores)} | Record: {record}",
                  fontsize=14, fontweight='bold')
        
        plt.xlabel('Number of Games', fontsize=14, fontweight='bold')
        plt.ylabel('Score', fontsize=14, fontweight='bold')
        
        palette = ['#00FFAA', '#FFA500']  # Neon green for score, orange for mean        
        
        # Plot score and mean score
        plt.plot(scores, label='Score', color="blue", linewidth=2, marker='o', markersize=3, linestyle='dashdot')
        plt.plot(mean_scores, label='Mean Score', color=palette[1], linewidth=2, linestyle='--')
                # Annotate latest score
        
        plt.text(len(scores) - 1, scores[-1] + 2, f'{scores[-1]}', fontsize=9, color=palette[0])
        plt.text(len(mean_scores) - 1, mean_scores[-1] + 2, f'{mean_scores[-1]:.1f}', fontsize=9, color=palette[1])

        # Annotate highest score
        max_score = max(scores)
        max_index = scores.index(max_score)
        plt.scatter(max_index, max_score, color='pink', s=100, edgecolors='white', zorder=5, label='Record')
        plt.text(max_index, max_score + 3, f'Record: {max_score}', ha='center', fontsize=10, color='pink')

        plt.ylim(ymin=0)
        plt.text(len(scores)-1, scores[-1], str(scores[-1]))
        plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
        plt.legend()  # Add legend for clarity
        plt.draw()  # Update the plot
        plt.pause(0.1)  # Allow the plot to render
        # Save the plot periodically
        if len(scores) % 50 == 0:
            plt.savefig(f'{IMG_PATH}/training_plot_{len(scores)}.png')
    except Exception as e:
        logging.error(f"Plotting error: {e}")