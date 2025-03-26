"""
Simple Snake game implementation using Pygame.
This is the initial version with basic functionality.
"""

import pygame
import random
import sys
from typing import List, Tuple, Dict, Optional
from enum import Enum


class PowerUpType(Enum):
    """Types of power-ups available in the game."""
    NORMAL = "normal"  # Regular food
    SPEED_BOOST = "speed_boost"  # Temporarily increases speed
    DOUBLE_POINTS = "double_points"  # Doubles points for a short time
    INVINCIBILITY = "invincibility"  # Makes snake invincible temporarily


class PowerUp:
    """Represents a power-up in the game."""
    
    def __init__(self, position: Tuple[int, int], power_type: PowerUpType):
        """
        Initialize a power-up.
        
        Args:
            position: Position of the power-up
            power_type: Type of power-up
        """
        self.position = position
        self.type = power_type
        self.duration = 0  # Duration in frames
        self.active = False
        
        # Set duration based on power-up type
        if power_type == PowerUpType.SPEED_BOOST:
            self.duration = 300  # 5 seconds at 60 FPS
            self.color = (255, 165, 0)  # Orange
        elif power_type == PowerUpType.DOUBLE_POINTS:
            self.duration = 600  # 10 seconds at 60 FPS
            self.color = (255, 215, 0)  # Gold
        elif power_type == PowerUpType.INVINCIBILITY:
            self.duration = 180  # 3 seconds at 60 FPS
            self.color = (0, 255, 255)  # Cyan
        else:  # NORMAL
            self.color = (255, 0, 0)  # Red
    
    def update(self) -> None:
        """Update the power-up state."""
        if self.active and self.duration > 0:
            self.duration -= 1
            if self.duration <= 0:
                self.active = False


class Snake:
    """Represents the snake in the game."""
    
    def __init__(self):
        """Initialize the snake with a starting position."""
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = "RIGHT"
        self.grow = False
        self.invincible = False
    
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
            return not self.invincible
        # Check self collision
        if head in self.body[1:]:
            return not self.invincible
        return False


class Food:
    """Represents the food in the game."""
    
    def __init__(self):
        """Initialize food with a random position."""
        self.power_up = self.generate_power_up()
    
    def generate_position(self) -> Tuple[int, int]:
        """
        Generate a random position for the food.
        
        Returns:
            Tuple of (x, y) coordinates
        """
        x = random.randrange(0, 800, 10)
        y = random.randrange(0, 600, 10)
        return (x, y)
    
    def generate_power_up(self) -> PowerUp:
        """
        Generate a new power-up with random type.
        
        Returns:
            New PowerUp instance
        """
        # 70% chance for normal food, 30% for power-ups
        if random.random() < 0.7:
            power_type = PowerUpType.NORMAL
        else:
            power_type = random.choice([
                PowerUpType.SPEED_BOOST,
                PowerUpType.DOUBLE_POINTS,
                PowerUpType.INVINCIBILITY
            ])
        
        return PowerUp(self.generate_position(), power_type)
    
    def respawn(self) -> None:
        """Respawn the food at a new random position."""
        self.power_up = self.generate_power_up()


class Game:
    """Main game class that manages the game state."""
    
    # Difficulty settings
    DIFFICULTY_SETTINGS: Dict[str, Dict[str, float]] = {
        "EASY": {"base_speed": 8, "speed_increment": 0.2, "max_speed": 15},
        "MEDIUM": {"base_speed": 10, "speed_increment": 0.3, "max_speed": 20},
        "HARD": {"base_speed": 12, "speed_increment": 0.4, "max_speed": 25}
    }
    
    def __init__(self, difficulty: str = "MEDIUM"):
        """
        Initialize the game.
        
        Args:
            difficulty: Game difficulty level ("EASY", "MEDIUM", or "HARD")
        """
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
        self.points_multiplier = 1
        
        # Speed management
        self.difficulty = difficulty.upper()
        self.settings = self.DIFFICULTY_SETTINGS[self.difficulty]
        self.current_speed = self.settings["base_speed"]
        self.speed_increment = self.settings["speed_increment"]
        self.max_speed = self.settings["max_speed"]
        self.base_speed = self.settings["base_speed"]
    
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
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()
    
    def update(self) -> None:
        """Update the game state."""
        self.snake.move()
        self.food.power_up.update()
        
        # Check for food collision
        if self.snake.body[0] == self.food.power_up.position:
            self.snake.grow = True
            self.food.respawn()
            
            # Handle power-up effects
            if self.food.power_up.type == PowerUpType.NORMAL:
                self.score += 1 * self.points_multiplier
                self.current_speed = min(
                    self.current_speed + self.speed_increment,
                    self.max_speed
                )
            elif self.food.power_up.type == PowerUpType.SPEED_BOOST:
                self.current_speed = min(self.current_speed * 1.5, self.max_speed)
                self.food.power_up.active = True
            elif self.food.power_up.type == PowerUpType.DOUBLE_POINTS:
                self.points_multiplier = 2
                self.food.power_up.active = True
            elif self.food.power_up.type == PowerUpType.INVINCIBILITY:
                self.snake.invincible = True
                self.food.power_up.active = True
        
        # Update power-up states
        if self.food.power_up.active and self.food.power_up.duration <= 0:
            if self.food.power_up.type == PowerUpType.SPEED_BOOST:
                self.current_speed = self.base_speed
            elif self.food.power_up.type == PowerUpType.DOUBLE_POINTS:
                self.points_multiplier = 1
            elif self.food.power_up.type == PowerUpType.INVINCIBILITY:
                self.snake.invincible = False
        
        # Check for game over
        if self.snake.check_collision():
            self.game_over = True
    
    def reset_game(self) -> None:
        """Reset the game to its initial state."""
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
        self.current_speed = self.settings["base_speed"]
        self.points_multiplier = 1
    
    def draw(self) -> None:
        """Draw the game state to the screen."""
        self.screen.fill((0, 0, 0))  # Black background
        
        # Draw snake
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), 
                           (segment[0], segment[1], 10, 10))
        
        # Draw food/power-up
        pygame.draw.rect(self.screen, self.food.power_up.color,
                        (self.food.power_up.position[0], 
                         self.food.power_up.position[1], 10, 10))
        
        # Draw score and speed
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        speed_text = font.render(f"Speed: {self.current_speed:.1f}", True, (255, 255, 255))
        difficulty_text = font.render(f"Difficulty: {self.difficulty}", True, (255, 255, 255))
        
        # Draw active power-ups
        power_up_text = ""
        if self.food.power_up.active:
            if self.food.power_up.type == PowerUpType.SPEED_BOOST:
                power_up_text = "Speed Boost Active!"
            elif self.food.power_up.type == PowerUpType.DOUBLE_POINTS:
                power_up_text = "Double Points Active!"
            elif self.food.power_up.type == PowerUpType.INVINCIBILITY:
                power_up_text = "Invincibility Active!"
        
        if power_up_text:
            power_up_surface = font.render(power_up_text, True, self.food.power_up.color)
            self.screen.blit(power_up_surface, (10, 130))
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(speed_text, (10, 50))
        self.screen.blit(difficulty_text, (10, 90))
        
        if self.game_over:
            game_over_text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
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
            self.clock.tick(self.current_speed)


if __name__ == "__main__":
    # You can change the difficulty here: "EASY", "MEDIUM", or "HARD"
    game = Game(difficulty="MEDIUM")
    game.run() 