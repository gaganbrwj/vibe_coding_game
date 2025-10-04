import pygame
from game.game_engine import GameEngine

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Version")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60

def show_replay_menu():
    font = pygame.font.SysFont("Arial", 30)
    options = ["Best of 3", "Best of 5", "Best of 7", "Exit"]
    while True:
        SCREEN.fill(BLACK)
        for i, opt in enumerate(options):
            text = font.render(f"{i+1}. {opt}", True, WHITE)
            SCREEN.blit(text, (WIDTH//2 - 100, 200 + i*50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: return 3
                elif event.key == pygame.K_2: return 5
                elif event.key == pygame.K_3: return 7
                elif event.key == pygame.K_4: return None

def main():
    while True:
        best_of = show_replay_menu()
        if best_of is None:
            break

        engine = GameEngine(WIDTH, HEIGHT)
        engine.max_score = (best_of + 1)//2  # e.g., Best of 5 → first to 3 wins
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            engine.handle_input()
            engine.update()
            engine.render(SCREEN)
            pygame.display.flip()
            clock.tick(FPS)

            if engine.game_over:
                pygame.time.wait(2000)
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
