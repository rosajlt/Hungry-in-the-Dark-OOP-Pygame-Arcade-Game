import pygame
from pathfinding import bfs_path
from config import TILE_SIZE, Entity


class Ghost (Entity):
    def __init__(self, x, y, img, size=25): # INISIALISASI GHOST DENGAN POSISI, GAMBAR, DAN UKURAN
        super().__init__(x, y, img, size)
        
        self.speed = 1.5  # kecil biar halus
        self.dir_x = 1

        self.path = []
        self.target = None

    def update(self, player, maze): # UPDATE FUNGSI UNTUK MENGGERAKAN GHOST MENUJU HERO DENGAN PATHFINDING
        start = (int(self.x // TILE_SIZE), int(self.y // TILE_SIZE))
        goal = (int(player.x // TILE_SIZE), int(player.y // TILE_SIZE))

        # ambil path kalau kosong
        if not self.path:
            self.path = bfs_path(start, goal, maze)
            print("path:", self.path)

        # ambil target tile kalau belum ada
        if not self.target and self.path:
            self.target = self.path.pop(0) 

        # kalau ada target, gerak halus ke arah sana
        if self.target:
            tx = self.target[0] * TILE_SIZE
            ty = self.target[1] * TILE_SIZE

            dx = tx - self.x
            dy = ty - self.y

            dist = (dx**2 + dy**2) ** 0.5 # hitung jarak ke target tile menggunakan rumus pythagoras

            if dist < 2:  # sudah sampai tile
                self.x = tx
                self.y = ty
                self.target = None #target dihapus=berhenti bergerak ke tile itu, dan akan ambil target baru di update selanjutnya
            else:
                # normalize movement (smooth diagonal)
                self.x += (dx / dist) * self.speed
                self.y += (dy / dist) * self.speed

                self.dir_x = 1 if dx > 0 else -1 # untuk menentukan arah gambar (flip kalau ke kiri)

    def draw(self, screen):
        img = self.img

        if self.dir_x == -1: #flip gambar kalau ke kiri
            img = pygame.transform.flip(img, True, False)

        screen.blit(img, (self.x, self.y))