import pygame
import random
import math

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Love Animation")
clock = pygame.time.Clock()

# Colors
PINK = (255, 50, 120)
DARK_PINK = (200, 0, 80)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Sparkles
sparkles = []

def create_sparkle():
    return {
        "x": random.randint(0, WIDTH),
        "y": random.randint(HEIGHT, HEIGHT + 100),
        "speed": random.uniform(0.5, 2),
        "size": random.randint(1, 3)
    }

for _ in range(150):
    sparkles.append(create_sparkle())

# Heart function
def draw_heart(surface, x, y, size):
    for t in range(0, 360, 2):
        rad = math.radians(t)
        hx = size * 16 * math.sin(rad) ** 3
        hy = -size * (
            13 * math.cos(rad)
            - 5 * math.cos(2 * rad)
            - 2 * math.cos(3 * rad)
            - math.cos(4 * rad)
        )
        surface.set_at((int(x + hx), int(y + hy)), PINK)

# Main loop
running = True
beat = 0
while running:
    clock.tick(60)
    screen.fill((10, 0, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Galaxy sparkles
    for s in sparkles:
        s["y"] -= s["speed"]
        if s["y"] < 0:
            s.update(create_sparkle())
        pygame.draw.circle(screen, WHITE, (s["x"], int(s["y"])), s["size"])

    # Mouse parallax
    mx, my = pygame.mouse.get_pos()
    offset_x = (mx - WIDTH // 2) * 0.05
    offset_y = (my - HEIGHT // 2) * 0.05

    # Beating heart
    beat += 0.08
    scale = 1 + 0.08 * math.sin(beat)

    draw_heart(
        screen,
        WIDTH // 2 + offset_x,
        HEIGHT // 2 + offset_y,
        int(12 * scale)
    )

    pygame.display.flip()

pygame.quit()
