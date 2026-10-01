import os
import pygame


WIDTH, HEIGHT = 900, 500
FPS = 60

SHIP_WIDTH, SHIP_HEIGHT = 50, 40
SHIP_SPEED = 5
BULLET_SPEED = 7
MAX_BULLETS = 3
STARTING_HEALTH = 10

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


class SpaceBattleGame:
    """Two-player spaceship battle game."""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Spaceship War Game")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("comicsans", 40)
        self.winner_font = pygame.font.SysFont("comicsans", 80)

        self.load_assets()
        self.reset_game()

    def load_assets(self):
        """Load and prepare the game images."""
        assets_path = os.path.join(os.path.dirname(__file__), "Assets")

        yellow_image = pygame.image.load(
            os.path.join(assets_path, "Yellow_Spaceship.png")
        ).convert_alpha()

        red_image = pygame.image.load(
            os.path.join(assets_path, "Red_Spaceship.png")
        ).convert_alpha()

        space_image = pygame.image.load(
            os.path.join(assets_path, "space.jpg")
        ).convert()

        self.yellow_ship = pygame.transform.rotate(
            pygame.transform.scale(
                yellow_image, (SHIP_WIDTH, SHIP_HEIGHT)
            ),
            90,
        )

        self.red_ship = pygame.transform.rotate(
            pygame.transform.scale(
                red_image, (SHIP_WIDTH, SHIP_HEIGHT)
            ),
            -90,
        )

        self.background = pygame.transform.scale(
            space_image, (WIDTH, HEIGHT)
        )

        self.border = pygame.Rect(
            WIDTH // 2 - 5, 0, 10, HEIGHT
        )

    def reset_game(self):
        """Reset players, bullets and health."""
        self.yellow = pygame.Rect(
            100,
            HEIGHT // 2 - SHIP_HEIGHT // 2,
            SHIP_WIDTH,
            SHIP_HEIGHT,
        )

        self.red = pygame.Rect(
            700,
            HEIGHT // 2 - SHIP_HEIGHT // 2,
            SHIP_WIDTH,
            SHIP_HEIGHT,
        )

        self.yellow_bullets = []
        self.red_bullets = []

        self.yellow_health = STARTING_HEALTH
        self.red_health = STARTING_HEALTH

    def handle_movement(self, keys):
        """Move both spaceships while keeping them inside their areas."""
        if keys[pygame.K_a] and self.yellow.left - SHIP_SPEED > 0:
            self.yellow.x -= SHIP_SPEED

        if (
            keys[pygame.K_d]
            and self.yellow.right + SHIP_SPEED < self.border.left
        ):
            self.yellow.x += SHIP_SPEED

        if keys[pygame.K_w] and self.yellow.top - SHIP_SPEED > 0:
            self.yellow.y -= SHIP_SPEED

        if (
            keys[pygame.K_s]
            and self.yellow.bottom + SHIP_SPEED < HEIGHT
        ):
            self.yellow.y += SHIP_SPEED

        if (
            keys[pygame.K_LEFT]
            and self.red.left - SHIP_SPEED > self.border.right
        ):
            self.red.x -= SHIP_SPEED

        if keys[pygame.K_RIGHT] and self.red.right + SHIP_SPEED < WIDTH:
            self.red.x += SHIP_SPEED

        if keys[pygame.K_UP] and self.red.top - SHIP_SPEED > 0:
            self.red.y -= SHIP_SPEED

        if keys[pygame.K_DOWN] and self.red.bottom + SHIP_SPEED < HEIGHT:
            self.red.y += SHIP_SPEED

    def fire_bullet(self, player):
        """Create a bullet for the selected player."""
        if player == "yellow" and len(self.yellow_bullets) < MAX_BULLETS:
            bullet = pygame.Rect(
                self.yellow.right,
                self.yellow.centery - 2,
                10,
                5,
            )
            self.yellow_bullets.append(bullet)

        elif player == "red" and len(self.red_bullets) < MAX_BULLETS:
            bullet = pygame.Rect(
                self.red.left - 10,
                self.red.centery - 2,
                10,
                5,
            )
            self.red_bullets.append(bullet)

    def update_bullets(self):
        """Move bullets and detect collisions."""
        for bullet in self.yellow_bullets[:]:
            bullet.x += BULLET_SPEED

            if bullet.colliderect(self.red):
                self.red_health -= 1
                self.yellow_bullets.remove(bullet)
            elif bullet.left > WIDTH:
                self.yellow_bullets.remove(bullet)

        for bullet in self.red_bullets[:]:
            bullet.x -= BULLET_SPEED

            if bullet.colliderect(self.yellow):
                self.yellow_health -= 1
                self.red_bullets.remove(bullet)
            elif bullet.right < 0:
                self.red_bullets.remove(bullet)

    def draw(self):
        """Render the current game state."""
        self.screen.blit(self.background, (0, 0))

        pygame.draw.rect(self.screen, WHITE, self.border)

        red_health = self.font.render(
            f"Health: {self.red_health}",
            True,
            WHITE,
        )
        yellow_health = self.font.render(
            f"Health: {self.yellow_health}",
            True,
            WHITE,
        )

        self.screen.blit(
            yellow_health,
            (10, 10),
        )

        self.screen.blit(
            red_health,
            (
                WIDTH - red_health.get_width() - 10,
                10,
            ),
        )

        self.screen.blit(
            self.yellow_ship,
            self.yellow,
        )

        self.screen.blit(
            self.red_ship,
            self.red,
        )

        for bullet in self.yellow_bullets:
            pygame.draw.rect(self.screen, YELLOW, bullet)

        for bullet in self.red_bullets:
            pygame.draw.rect(self.screen, RED, bullet)

        pygame.display.flip()

    def get_winner(self):
        """Return the winner when a player's health reaches zero."""
        if self.red_health <= 0:
            return "Yellow Wins!"

        if self.yellow_health <= 0:
            return "Red Wins!"

        return None

    def show_winner(self, winner):
        """Display the winner and pause briefly."""
        message = self.winner_font.render(
            winner,
            True,
            WHITE,
        )

        self.screen.blit(
            message,
            (
                WIDTH // 2 - message.get_width() // 2,
                HEIGHT // 2 - message.get_height() // 2,
            ),
        )

        pygame.display.flip()
        pygame.time.delay(3000)

    def run(self):
        """Run the main game loop."""
        running = True

        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL:
                        self.fire_bullet("yellow")

                    elif event.key == pygame.K_RCTRL:
                        self.fire_bullet("red")

            keys = pygame.key.get_pressed()
            self.handle_movement(keys)
            self.update_bullets()

            winner = self.get_winner()

            if winner:
                self.draw()
                self.show_winner(winner)
                running = False
                continue

            self.draw()

        pygame.quit()


def main():
    game = SpaceBattleGame()
    game.run()


if __name__ == "__main__":
    main()
    