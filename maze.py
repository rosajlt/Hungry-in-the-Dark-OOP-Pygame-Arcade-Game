import pygame
from config import TILE_SIZE

# load gambar pohon
tree_img = pygame.image.load("assets/tree.png")
tree_img = pygame.transform.scale(tree_img, (TILE_SIZE, TILE_SIZE))

# load gambar rumah
house2_img = pygame.image.load("assets/house2.png")
house2_img = pygame.transform.scale(house2_img, (TILE_SIZE, TILE_SIZE))

# Map rintangan
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1],
    [1,0,0,1,0,0,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,0,1],
    [1,0,0,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1],
    [1,1,1,1,0,0,1,1,0,0,1,1,1,0,0,0,1,0,1,0,1,0,0,1],
    [1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1],
    [1,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1,1],
    [1,0,0,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1],
    [1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,1,2,0,1],
    [1,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,3,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

def draw_maze(screen):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x = col * TILE_SIZE
            y = row * TILE_SIZE

            if maze[row][col] == 1:
                screen.blit(tree_img, (x, y))
            if maze[row][col] == 2:
                screen.blit(house2_img, (x, y))
            if maze[row][col] == 3:
                pass  # pintu, biar kosong

def can_move(x, y, maze, tile_size):
    col = x // tile_size
    row = y // tile_size

    # Batas biar tidak keluar map
    if row < 0 or row >= len(maze):
        return False
    if col < 0 or col >= len(maze[0]):
        return False

    # Cek tembok
    if maze[row][col] == 1:
        return False

    return True
    

            