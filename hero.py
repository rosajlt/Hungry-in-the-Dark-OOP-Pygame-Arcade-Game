import pygame
import random
from config import TILE_SIZE, Entity

# load gambar (pakai ukuran tile dulu)
an1_img = pygame.image.load("assets/an1.png")
ghost_img = pygame.image.load("assets/ghost.png")


class Player(Entity):
    def __init__(self, x, y, img, size=25):
        super().__init__(x, y, img, size)
        
        self.speed = 5

        # SHAKE SYSTEM
        self.shake_timer = 0
        self.shake_duration = 30  # durasi getar (frame)

    def move(self, keys, maze):
        new_x = self.x
        new_y = self.y

        # movement
        if keys[pygame.K_LEFT]:
            new_x -= self.speed
        if keys[pygame.K_RIGHT]:
            new_x += self.speed
        if keys[pygame.K_UP]:
            new_y -= self.speed
        if keys[pygame.K_DOWN]:
            new_y += self.speed

        # collision horizontal
        if not self.is_colliding(new_x, self.y, maze): 
            self.x = new_x

        # collision vertical
        if not self.is_colliding(self.x, new_y, maze): 
            self.y = new_y

    # fungsi untuk trigger getar
    def hit(self):
        self.shake_timer = self.shake_duration

    def draw(self, screen):
        # SHAKE SYSTEM
        if self.shake_timer > 0:
            intensity = self.shake_timer // 5 + 1  # makin kecil seiring waktu
            offset_x = random.randint(-intensity, intensity) 
            offset_y = random.randint(-intensity, intensity)
            self.shake_timer -= 1 #kurangi timer getar setiap frame
        else:
            offset_x = 0
            offset_y = 0

        screen.blit(self.img, (self.x + offset_x, self.y + offset_y)) #gambar player dengan offset untuk efek getar

    def is_colliding(self, x, y, maze): 
        size = self.size

        points = [
            (x, y),
            (x + size - 1, y),
            (x, y + size - 1),
            (x + size - 1, y + size - 1)
        ]

        for px, py in points:
            col = int(px // TILE_SIZE)
            row = int(py // TILE_SIZE)

            if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]):
                return True

            if maze[row][col] == 1:
                return True

        return False


def find_spawn_front_house(maze, tile_size): #posisi spawn hero di depan rumah (tile 3) 
    for row in range(len(maze)): 
        for col in range(len(maze[row])): 
            if maze[row][col] == 3:  # pintu
                x = col * tile_size
                y = row * tile_size
                return x, y

    return 200, 200