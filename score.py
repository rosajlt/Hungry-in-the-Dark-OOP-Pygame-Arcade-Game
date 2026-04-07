import pygame
import random


class Item:
    def __init__(self, x, y, img, size=20):
        self.x = x
        self.y = y
        self.size = size
        self.img = pygame.transform.scale(img, (size, size))
        self.rect = pygame.Rect(x, y, size, size)

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))


class ScoreSystem:
    def __init__(self, maze, tile_size, ghost_img, apple_img, banana_img, eat_sound, eat_channel): 
        self.score = 0
        self.level = 1
        self.maze = maze
        self.tile_size = tile_size
        self.eat_sound = eat_sound
        self.eat_channel = eat_channel

        self.ghost_img = ghost_img
        self.apple_img = apple_img
        self.banana_img = banana_img
        self.eat_sound = eat_sound

        self.current_item_img = self.apple_img
        self.items = self.spawn_items(10)

        self.leveling = False  # flag untuk mencegah level up berulang saat item masih ada

    def spawn_items(self, jumlah): 
        items = []
        rows = len(self.maze)
        cols = len(self.maze[0])

        while len(items) < jumlah: # spawn item di posisi acak yang bukan tembok
            row = random.randint(0, rows - 1)
            col = random.randint(0, cols - 1)

            if self.maze[row][col] == 0: # 0 = jalan, jadi bisa spawn item
                x = col * self.tile_size + 10
                y = row * self.tile_size + 10
                items.append(Item(x, y, self.current_item_img))

        return items

    def update(self, player, ghosts, GhostClass):
        player_rect = pygame.Rect(player.x, player.y, player.size, player.size)

        # ambil item
        for item in self.items[:]:
            if player_rect.colliderect(item.rect):
                self.items.remove(item)
                self.score += 10

                # SOUND MULTI (nyam nyam nyam)
                channel = pygame.mixer.find_channel()
                if channel:
                    channel.play(self.eat_sound)

        # level up
        if len(self.items) == 0 and not self.leveling:
            self.leveling = True
            self.level += 1

            # ganti item apple/banana
            if self.level % 2 == 1:
                self.current_item_img = self.apple_img
            else:
                self.current_item_img = self.banana_img

            # spawn item baru
            self.items = self.spawn_items(10 + self.level * 2)

            # tambah ghost
            ghosts.append(GhostClass(300, 300, self.ghost_img, 25))

        # reset leveling setelah item muncul
        if len(self.items) > 0:
            self.leveling = False
    def draw(self, screen):
        for item in self.items:
            item.draw(screen)

        font = pygame.font.SysFont(None, 30)

        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        level_text = font.render(f"Level: {self.level}", True, (255, 255, 255))

        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))