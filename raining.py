import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aqua Rain Animation")

# Colors
BLACK = (0, 0, 0)
AQUA = (0, 255, 255)
TREE_BROWN = (139, 69, 19)
TREE_GREEN = (34, 139, 34)

# Raindrop class with enhanced tail (thicker near the drop, thinner toward the end)
class Raindrop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-100, 0)
        self.speed = random.uniform(5, 10)  # Speed of the falling raindrop
        self.radius = random.randint(3, 7)
        self.color = AQUA  # Aqua color for the raindrop
        self.trail = []  # A list to hold the raindrop's previous positions for tail

    def move(self):
        self.trail.append((self.x, self.y))  # Save current position before moving
        if len(self.trail) > 15:  # Limit the length of the trail
            self.trail.pop(0)  # Remove the oldest position to create a tail

        self.y += self.speed

    def draw(self):
        # Draw the main raindrop
        pygame.draw.circle(screen, self.color, (self.x, int(self.y)), self.radius)

        # Draw the tail, making older positions thinner and more transparent
        for i, (trail_x, trail_y) in enumerate(reversed(self.trail)):
            trail_radius = max(1, self.radius - i // 2)  # Start large, then shrink for older trail positions
            alpha = max(50, 255 - (i * 20))  # Gradually reduce opacity
            trail_color = (*self.color, alpha)  # Set the trail color with transparency

            trail_surface = pygame.Surface((trail_radius * 2, trail_radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(trail_surface, trail_color, (trail_radius, trail_radius), trail_radius)
            screen.blit(trail_surface, (trail_x - trail_radius, trail_y - trail_radius))

    def is_below_screen(self):
        return self.y - self.radius > HEIGHT

# Horizontal Wave class (simple circle without tail)
class HorizontalWave:
    def __init__(self, x, y, x_radius, y_radius):
        self.x = x
        self.y = y
        self.x_radius = x_radius  # Horizontal radius
        self.y_radius = y_radius  # Vertical radius
        self.color = AQUA  # Aqua color for the waves
        self.grow_speed_x = 3  # Horizontal expansion speed
        self.grow_speed_y = 1.5  # Vertical expansion speed
        self.max_x_radius = 150  # Max horizontal radius

    def grow(self):
        self.x_radius += self.grow_speed_x
        self.y_radius += self.grow_speed_y

    def draw(self):
        # Draw an expanding ellipse (circle when equal radii) for the wave
        pygame.draw.ellipse(screen, self.color, 
                            (self.x - self.x_radius, self.y - self.y_radius, 
                             self.x_radius * 2, self.y_radius * 2), 2)

    def is_done(self):
        return self.x_radius > self.max_x_radius

# Function to draw a simple tree on the left side of the screen
def draw_tree(x, y):
    # Draw the trunk (rectangle)
    trunk_width, trunk_height = 40, 100
    pygame.draw.rect(screen, TREE_BROWN, (x, y - trunk_height, trunk_width, trunk_height))
    
    # Draw the foliage (green circle)
    foliage_radius = 70
    pygame.draw.circle(screen, TREE_GREEN, (x + trunk_width // 2, y - trunk_height - foliage_radius // 2), foliage_radius)

# Main game loop
raindrops = []
waves = []
clock = pygame.time.Clock()

running = True
while running:
    # Clear the screen for a fresh draw (with black background)
    screen.fill(BLACK)

    # Draw the tree on the left side of the screen
    # draw_tree(100, HEIGHT - 100)

    # Create new raindrops randomly
    if random.randint(0, 10) < 2:
        raindrops.append(Raindrop())

    # Move and draw raindrops
    for drop in raindrops[:]:
        drop.move()
        drop.draw()
        if drop.is_below_screen():
            # Create a wave (without trail) when raindrop hits the bottom
            waves.append(HorizontalWave(drop.x, HEIGHT, 1, 1))
            raindrops.remove(drop)

    # Draw waves (on top of trail layer, so they don't get affected)
    for wave in waves[:]:
        wave.grow()
        wave.draw()
        if wave.is_done():
            waves.remove(wave)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()






























































































































































#########################################################


# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Screen dimensions
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Aqua Rain Animation")

# # Colors
# BLACK = (0, 0, 0)
# AQUA = (0, 255, 255)
# TREE_BROWN = (139, 69, 19)
# TREE_GREEN = (34, 139, 34)
# BRANCH_COLOR = (102, 51, 0)  # Dark brown for the branches

# # Raindrop class with enhanced tail (thicker near the drop, thinner toward the end)
# class Raindrop:
#     def __init__(self):
#         self.x = random.randint(0, WIDTH)
#         self.y = random.randint(-100, 0)
#         self.speed = random.uniform(5, 10)  # Speed of the falling raindrop
#         self.radius = random.randint(3, 7)
#         self.color = AQUA  # Aqua color for the raindrop
#         self.trail = []  # A list to hold the raindrop's previous positions for tail

#     def move(self):
#         self.trail.append((self.x, self.y))  # Save current position before moving
#         if len(self.trail) > 15:  # Limit the length of the trail
#             self.trail.pop(0)  # Remove the oldest position to create a tail

#         self.y += self.speed

#     def draw(self):
#         # Draw the main raindrop
#         pygame.draw.circle(screen, self.color, (self.x, int(self.y)), self.radius)

#         # Draw the tail, making older positions thinner and more transparent
#         for i, (trail_x, trail_y) in enumerate(reversed(self.trail)):
#             trail_radius = max(1, self.radius - i // 2)  # Start large, then shrink for older trail positions
#             alpha = max(50, 255 - (i * 20))  # Gradually reduce opacity
#             trail_color = (*self.color, alpha)  # Set the trail color with transparency

#             trail_surface = pygame.Surface((trail_radius * 2, trail_radius * 2), pygame.SRCALPHA)
#             pygame.draw.circle(trail_surface, trail_color, (trail_radius, trail_radius), trail_radius)
#             screen.blit(trail_surface, (trail_x - trail_radius, trail_y - trail_radius))

#     def is_below_screen(self):
#         return self.y - self.radius > HEIGHT

# # Horizontal Wave class (simple circle without tail)
# class HorizontalWave:
#     def __init__(self, x, y, x_radius, y_radius):
#         self.x = x
#         self.y = y
#         self.x_radius = x_radius  # Horizontal radius
#         self.y_radius = y_radius  # Vertical radius
#         self.color = AQUA  # Aqua color for the waves
#         self.grow_speed_x = 3  # Horizontal expansion speed
#         self.grow_speed_y = 1.5  # Vertical expansion speed
#         self.max_x_radius = 150  # Max horizontal radius

#     def grow(self):
#         self.x_radius += self.grow_speed_x
#         self.y_radius += self.grow_speed_y

#     def draw(self):
#         # Draw an expanding ellipse (circle when equal radii) for the wave
#         pygame.draw.ellipse(screen, self.color, 
#                             (self.x - self.x_radius, self.y - self.y_radius, 
#                              self.x_radius * 2, self.y_radius * 2), 2)

#     def is_done(self):
#         return self.x_radius > self.max_x_radius

# # Function to draw a tree with branches and leaves on the left side of the screen
# def draw_tree(x, y):
#     # Draw the trunk (rectangle)
#     trunk_width, trunk_height = 40, 100
#     pygame.draw.rect(screen, TREE_BROWN, (x, y - trunk_height, trunk_width, trunk_height))

#     # Draw branches
#     # Left branch
#     pygame.draw.line(screen, BRANCH_COLOR, (x + trunk_width // 2, y - trunk_height + 20),
#                      (x - 50, y - trunk_height + 70), 10)
#     # Right branch
#     pygame.draw.line(screen, BRANCH_COLOR, (x + trunk_width // 2, y - trunk_height + 20),
#                      (x + trunk_width + 50, y - trunk_height + 70), 10)

#     # Draw leaves (foliage)
#     foliage_radius = 60
#     pygame.draw.circle(screen, TREE_GREEN, (x + trunk_width // 2, y - trunk_height - foliage_radius // 2), foliage_radius)

#     # Draw more leaves on the branches
#     pygame.draw.circle(screen, TREE_GREEN, (x - 50, y - trunk_height + 70), 40)
#     pygame.draw.circle(screen, TREE_GREEN, (x + trunk_width + 50, y - trunk_height + 70), 40)

# # Main game loop
# raindrops = []
# waves = []
# clock = pygame.time.Clock()

# running = True
# while running:
#     # Clear the screen for a fresh draw (with black background)
#     screen.fill(BLACK)

#     # Draw the tree on the left side of the screen
#     draw_tree(100, HEIGHT - 100)

#     # Create new raindrops randomly
#     if random.randint(0, 10) < 2:
#         raindrops.append(Raindrop())

#     # Move and draw raindrops
#     for drop in raindrops[:]:
#         drop.move()
#         drop.draw()
#         if drop.is_below_screen():
#             # Create a wave (without trail) when raindrop hits the bottom
#             waves.append(HorizontalWave(drop.x, HEIGHT, 1, 1))
#             raindrops.remove(drop)

#     # Draw waves (on top of trail layer, so they don't get affected)
#     for wave in waves[:]:
#         wave.grow()
#         wave.draw()
#         if wave.is_done():
#             waves.remove(wave)

#     # Check for events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Update the display
#     pygame.display.flip()
#     clock.tick(60)

# # Quit Pygame
# pygame.quit()







#################################







# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Screen dimensions
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Aqua Rain Animation")

# # Colors
# BLACK = (0, 0, 0)
# AQUA = (0, 255, 255)
# TREE_BROWN = (139, 69, 19)
# TREE_GREEN = (34, 139, 34)
# BRANCH_COLOR = (102, 51, 0)  # Dark brown for the branches
# HOUSE_COLOR = (139, 69, 19)  # Brown for the house
# ROOF_COLOR = (255, 0, 0)  # Red for the roof
# STAIR_COLOR = (169, 169, 169)  # Gray for the stairs
# SUN_COLOR = (255, 255, 0)  # Yellow for the sun

# # Raindrop class with enhanced tail (thicker near the drop, thinner toward the end)
# class Raindrop:
#     def __init__(self):
#         self.x = random.randint(0, WIDTH)
#         self.y = random.randint(-100, 0)
#         self.speed = random.uniform(5, 10)  # Speed of the falling raindrop
#         self.radius = random.randint(3, 7)
#         self.color = AQUA  # Aqua color for the raindrop
#         self.trail = []  # A list to hold the raindrop's previous positions for tail

#     def move(self):
#         self.trail.append((self.x, self.y))  # Save current position before moving
#         if len(self.trail) > 15:  # Limit the length of the trail
#             self.trail.pop(0)  # Remove the oldest position to create a tail

#         self.y += self.speed

#     def draw(self):
#         # Draw the main raindrop
#         pygame.draw.circle(screen, self.color, (self.x, int(self.y)), self.radius)

#         # Draw the tail, making older positions thinner and more transparent
#         for i, (trail_x, trail_y) in enumerate(reversed(self.trail)):
#             trail_radius = max(1, self.radius - i // 2)  # Start large, then shrink for older trail positions
#             alpha = max(50, 255 - (i * 20))  # Gradually reduce opacity
#             trail_color = (*self.color, alpha)  # Set the trail color with transparency

#             trail_surface = pygame.Surface((trail_radius * 2, trail_radius * 2), pygame.SRCALPHA)
#             pygame.draw.circle(trail_surface, trail_color, (trail_radius, trail_radius), trail_radius)
#             screen.blit(trail_surface, (trail_x - trail_radius, trail_y - trail_radius))

#     def is_below_screen(self):
#         return self.y - self.radius > HEIGHT

# # Horizontal Wave class (simple circle without tail)
# class HorizontalWave:
#     def __init__(self, x, y, x_radius, y_radius):
#         self.x = x
#         self.y = y
#         self.x_radius = x_radius  # Horizontal radius
#         self.y_radius = y_radius  # Vertical radius
#         self.color = AQUA  # Aqua color for the waves
#         self.grow_speed_x = 3  # Horizontal expansion speed
#         self.grow_speed_y = 1.5  # Vertical expansion speed
#         self.max_x_radius = 150  # Max horizontal radius

#     def grow(self):
#         self.x_radius += self.grow_speed_x
#         self.y_radius += self.grow_speed_y

#     def draw(self):
#         # Draw an expanding ellipse (circle when equal radii) for the wave
#         pygame.draw.ellipse(screen, self.color, 
#                             (self.x - self.x_radius, self.y - self.y_radius, 
#                              self.x_radius * 2, self.y_radius * 2), 2)

#     def is_done(self):
#         return self.x_radius > self.max_x_radius

# # Function to draw a tree with branches and leaves on the left side of the screen
# def draw_tree(x, y):
#     # Draw the trunk (rectangle)
#     trunk_width, trunk_height = 40, 100
#     pygame.draw.rect(screen, TREE_BROWN, (x, y - trunk_height, trunk_width, trunk_height))

#     # Draw branches
#     # Left branch
#     pygame.draw.line(screen, BRANCH_COLOR, (x + trunk_width // 2, y - trunk_height + 20),
#                      (x - 50, y - trunk_height + 70), 10)
#     # Right branch
#     pygame.draw.line(screen, BRANCH_COLOR, (x + trunk_width // 2, y - trunk_height + 20),
#                      (x + trunk_width + 50, y - trunk_height + 70), 10)

#     # Draw leaves (foliage)
#     foliage_radius = 60
#     pygame.draw.circle(screen, TREE_GREEN, (x + trunk_width // 2, y - trunk_height - foliage_radius // 2), foliage_radius)

#     # Draw more leaves on the branches
#     pygame.draw.circle(screen, TREE_GREEN, (x - 50, y - trunk_height + 70), 40)
#     pygame.draw.circle(screen, TREE_GREEN, (x + trunk_width + 50, y - trunk_height + 70), 40)

# # Function to draw a simple village house with two stairs on the right
# def draw_house(x, y):
#     # Draw the house (a simple rectangle)
#     house_width, house_height = 120, 100
#     pygame.draw.rect(screen, HOUSE_COLOR, (x, y - house_height, house_width, house_height))

#     # Draw the roof (a triangle)
#     roof_points = [(x, y - house_height), (x + house_width // 2, y - house_height - 40), 
#                    (x + house_width, y - house_height)]
#     pygame.draw.polygon(screen, ROOF_COLOR, roof_points)

#     # Draw windows (simple small rectangles)
#     pygame.draw.rect(screen, (255, 255, 255), (x + 20, y - house_height + 20, 30, 30))  # Left window
#     pygame.draw.rect(screen, (255, 255, 255), (x + 70, y - house_height + 20, 30, 30))  # Right window

#     # Draw the door (rectangle)
#     pygame.draw.rect(screen, (150, 75, 0), (x + 45, y - house_height + 50, 30, 50))  # Door

#     # Draw the stairs (two rectangles, one on top of the other)
#     stair_width, stair_height = 40, 10
#     pygame.draw.rect(screen, STAIR_COLOR, (x + 40, y - 20, stair_width, stair_height))  # Bottom stair
#     pygame.draw.rect(screen, STAIR_COLOR, (x + 40, y - 30, stair_width, stair_height))  # Top stair

# # Function to draw the sun
# def draw_sun(x, y, radius):
#     pygame.draw.circle(screen, SUN_COLOR, (x, y), radius)

# # Main game loop
# raindrops = []
# waves = []
# clock = pygame.time.Clock()

# running = True
# while running:
#     # Clear the screen for a fresh draw (with black background)
#     screen.fill(BLACK)

#     # Draw the sun in the sky (top center)
#     draw_sun(WIDTH // 2, 100, 50)

#     # ** DO NOT redraw mountains here, only keep the trees and house **
#     draw_tree(100, HEIGHT - 100)
#     draw_house(WIDTH - 220, HEIGHT - 100)

#     # Create new raindrops randomly
#     if random.randint(0, 10) < 2:
#         raindrops.append(Raindrop())

#     # Move and draw raindrops
#     for drop in raindrops[:]:
#         drop.move()
#         drop.draw()
#         if drop.is_below_screen():
#             # Create a wave (without trail) when raindrop hits the bottom
#             waves.append(HorizontalWave(drop.x, HEIGHT, 0, 20))
#             raindrops.remove(drop)

#     # Move and draw waves
#     for wave in waves[:]:
#         wave.grow()
#         wave.draw()
#         if wave.is_done():
#             waves.remove(wave)

#     # Update the screen
#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()
