TILE_SIZE = 35 #menggambar maze agar sesuai dengan ukuran tile yang diinginkan, dan memudahkan perhitungan posisi item dan musuh dalam maze

import pygame

class Entity: #class induk
    def __init__(self, x, y, img, size): #INISIALISASI ENTITY DENGAN POSISI, GAMBAR, DAN UKURAN
        self.x = float(x)
        self.y = float(y)
        self.size = size
        self.img = pygame.transform.scale(img, (size, size))

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))