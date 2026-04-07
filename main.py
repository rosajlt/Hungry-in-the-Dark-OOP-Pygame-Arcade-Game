import pygame
import sys

from ghost import Ghost
from hero import Player, an1_img, find_spawn_front_house
from maze import draw_maze, maze
from config import TILE_SIZE
from score import ScoreSystem
from menu import show_menu
from gameover_menu import show_gameover

pygame.mixer.pre_init(22050, -16, 1, 64) # PRE-INIT UNTUK MENGURANGI LATENSI SUARA
pygame.init()

pygame.mixer.set_num_channels(16) # MENAMBAHKAN CHANNEL UNTUK SUARA, DEFAULT 8, KITA BUTUH LEBIH BANYAK UNTUK EFEK SUARA YANG BERBEDA

WIDTH, HEIGHT = 850, 650
BLACK = (0, 0, 0)


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hungry in the Dark")

    # MENU
    show_menu(screen, WIDTH, HEIGHT)

    screen.fill(BLACK)
    pygame.display.flip()

    ghost_img = pygame.image.load("assets/ghost.png")
    apple_img = pygame.image.load("assets/apple.png")
    banana_img = pygame.image.load("assets/banana.png")

    eat_sound = pygame.mixer.Sound("assets/eat.wav")
    eat_sound.set_volume(1.0) 

    gameover_sound = pygame.mixer.Sound("assets/gameOver.wav")
    gameover_sound.set_volume(1.0)

    pygame.mixer.music.load("assets/music.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1) # LOOPING MUSIC

    eat_sound.play()
    pygame.time.delay(5)
    eat_sound.stop()

    eat_channel = pygame.mixer.Channel(0)

    score_system = ScoreSystem( # INISIALISASI SCORE SYSTEM
        maze, 
        TILE_SIZE,
        ghost_img,
        apple_img,
        banana_img,
        eat_sound,
        eat_channel
    )

    spawn_x, spawn_y = find_spawn_front_house(maze, TILE_SIZE) # MENCARI POSISI SPAWN DEPAN RUMAH UNTUK HERO

    player = Player(spawn_x, spawn_y, an1_img, 25)
    ghosts = [Ghost(300, 300, ghost_img, 25)]

    game_over = False
    music_stopped = False
    gameover_played = False

    clock = pygame.time.Clock() #mengatur fps agar game berjalan dengan lancar dan tidak terlalu cepat atau lambat

    while True:
        screen.fill(BLACK)

        # INPUT
        for event in pygame.event.get(): #MENGECEK EVENT, SEPERTI TOMBOL KELUAR
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

        # UPDATE jika game belum berakhir
        if not game_over: 
            keys = pygame.key.get_pressed() 
            player.move(keys, maze)

            for g in ghosts: #ghost mengikuti player
                g.update(player, maze)

            for g in ghosts: #jika player menyentuh ghost maka game over
                if abs(player.x - g.x) < 20 and abs(player.y - g.y) < 20:
                    game_over = True
                    player.hit()

            score_system.update(player, ghosts, Ghost) #player memakan item dan mendapatkan skor, serta memeriksa apakah level naik

        # SOUND GAME OVER
        if game_over:
            if not music_stopped:
                pygame.mixer.music.fadeout(500) #memudar musik secara perlahan selama 500ms
                music_stopped = True

            if not gameover_played: #memainkan suara game over hanya sekali
                gameover_sound.play()
                gameover_played = True

        # DRAW
        draw_maze(screen) 
        score_system.draw(screen)
        player.draw(screen)

        for g in ghosts: 
            g.draw(screen)

        pygame.display.flip()  #tampilkan semua gambar yang sudah digambar di layar
        clock.tick(60)

        # GAME OVER MENU (di luar draw utama)
        if game_over:
            choice = show_gameover(
                screen,
                WIDTH,
                HEIGHT,
                score_system.score,
                score_system.level
            )

            if choice == 0:
                return main()
            else:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()