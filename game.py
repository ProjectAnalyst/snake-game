"""
Simple Snake game implementation using Pygame.
This is the initial version with basic functionality.
"""

import pygame
import random
import sys
from typing import List, Tuple


class Snake:
    """Represents the snake in the game."""
    
    def __init__(self):
        """Initialize the snake with a starting position."""
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = "RIGHT"
        self.grow = False
    
    def move(self) -> None:
        """Move the snake in its current direction."""
        head = self.body[0]
        if self.direction == "UP":
            new_head = (head[0], head[1] - 10)
        elif self.direction == "DOWN":
            new_head = (head[0], head[1] + 10)
        elif self.direction == "LEFT":
            new_head = (head[0] - 10, head[1])
        else:  # RIGHT
            new_head = (head[0] + 10, head[1])
        
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
    
    def check_collision(self) -> bool:
        """
        Check if the snake has collided with itself or the walls.
        
        Returns:
            True if collision detected, False otherwise
        """
        head = self.body[0]
        # Check wall collision
        if (head[0] < 0 or head[0] >= 800 or 
            head[1] < 0 or head[1] >= 600):
            return True
        # Check self collision
        if head in self.body[1:]:
            return True
        return False


class Food:
    """Represents the food in the game."""
    
    def __init__(self):
        """Initialize food with a random position."""
        self.position = self.generate_position()
    
    def generate_position(self) -> Tuple[int, int]:
        """
        Generate a random position for the food.
        
        Returns:
            Tuple of (x, y) coordinates
        """
        x = random.randrange(0, 800, 10)
        y = random.randrange(0, 600, 10)
        return (x, y)
    
    def respawn(self) -> None:
        """Respawn the food at a new random position."""
        self.position = self.generate_position()


class Game:
    """Main game class that manages the game state."""
    
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
    
    def handle_input(self) -> None:
        """Handle user input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != "DOWN":
                    self.snake.direction = "UP"
                elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                    self.snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                    self.snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                    self.snake.direction = "RIGHT"
    
    def update(self) -> None:
        """Update the game state."""
        self.snake.move()
        
        # Check for food collision
        if self.snake.body[0] == self.food.position:
            self.snake.grow = True
            self.food.respawn()
            self.score += 1
        
        # Check for game over
        if self.snake.check_collision():
            self.game_over = True
    
    def draw(self) -> None:
        """Draw the game state to the screen."""
        self.screen.fill((0, 0, 0))  # Black background
        
        # Draw snake
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), 
                           (segment[0], segment[1], 10, 10))
        
        # Draw food
        pygame.draw.rect(self.screen, (255, 0, 0),
                        (self.food.position[0], self.food.position[1], 10, 10))
        
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        
        if self.game_over:
            game_over_text = font.render("Game Over!", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(400, 300))
            self.screen.blit(game_over_text, text_rect)
        
        pygame.display.flip()
    
    def run(self) -> None:
        """Main game loop."""
        while True:
            self.handle_input()
            if not self.game_over:
                self.update()
            self.draw()
            self.clock.tick(10)  # Control game speed


if __name__ == "__main__":
    game = Game()
    game.run() 