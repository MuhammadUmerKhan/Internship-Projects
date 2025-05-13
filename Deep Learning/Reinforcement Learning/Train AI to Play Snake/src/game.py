import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np
import logging
from config import WINDOW_WIDTH, WINDOW_HEIGHT, BLOCK_SIZE, SPEED, FONT_PATH

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

# Colors
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE1 = (0, 120, 255)
BLUE2 = (0, 180, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)

class SnakeGameAI:
    def __init__(self, w=WINDOW_WIDTH, h=WINDOW_HEIGHT):
        self.w = w
        self.h = h
        try:
            pygame.init()
            self.display = pygame.display.set_mode((self.w, self.h))
            pygame.display.set_caption('Snake AI')
            self.clock = pygame.time.Clock()
            self.font = pygame.font.Font(FONT_PATH, 25)
            self.reset()
        except Exception as e:
            logging.error(f"Failed to initialize Pygame: {e}")
            raise

    def reset(self):
        self.direction = Direction.RIGHT
        self.head = Point(self.w/2, self.h/2)
        self.snake = [
            self.head,
            Point(self.head.x-BLOCK_SIZE, self.head.y),
            Point(self.head.x-(2*BLOCK_SIZE), self.head.y)
        ]
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0
        self.game_over = False

    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self, action):
        self.frame_iteration += 1
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    logging.info("Pygame window closed by user")
                    quit()
                elif event.type == pygame.KEYDOWN and self.game_over:
                    if event.key == pygame.K_r:
                        self.reset()

            if not self.game_over:
                self._move(action)
                self.snake.insert(0, self.head)

                reward = 0
                self.game_over = False
                if self.is_collision() or self.frame_iteration > 100*len(self.snake):
                    self.game_over = True
                    reward = -10
                    return reward, self.game_over, self.score

                if self.head == self.food:
                    self.score += 1
                    reward = 10
                    self._place_food()
                else:
                    self.snake.pop()

                self._update_ui()
                self.clock.tick(SPEED)

            return reward, self.game_over, self.score
        except Exception as e:
            logging.error(f"Error in play_step: {e}")
            raise

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        if pt in self.snake[1:]:
            return True
        return False

    def _update_ui(self):
        self.display.fill(BLACK)
        
        # Draw grid
        for x in range(0, self.w, BLOCK_SIZE):
            pygame.draw.line(self.display, GRAY, (x, 0), (x, self.h), 1)
        for y in range(0, self.h, BLOCK_SIZE):
            pygame.draw.line(self.display, GRAY, (0, y), (self.w, y), 1)

        # Draw snake
        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))

        # Draw food with pulse effect
        pulse = 8 + 4 * abs(pygame.time.get_ticks() % 1000 - 500) / 500
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x+pulse/2, self.food.y+pulse/2, BLOCK_SIZE-pulse, BLOCK_SIZE-pulse))

        # Draw score
        text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.display.blit(text, [10, 10])

        # Draw game over screen
        if self.game_over:
            overlay = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            self.display.blit(overlay, (0, 0))
            game_over_text = self.font.render(f"Game Over! Score: {self.score}", True, WHITE)
            restart_text = self.font.render("Press R to Restart", True, WHITE)
            self.display.blit(game_over_text, (self.w//2 - game_over_text.get_width()//2, self.h//2 - 40))
            self.display.blit(restart_text, (self.w//2 - restart_text.get_width()//2, self.h//2 + 20))

        pygame.display.flip()

    def _move(self, action):
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx]
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx]
        else:
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx]

        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)