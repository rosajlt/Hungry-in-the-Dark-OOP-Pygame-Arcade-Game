import pygame
import sys


def draw_button(screen, text, font, rect, selected): #menggambar tombol dengan warna yang berbeda saat dipilih
    color = (255, 50, 50) if selected else (50, 50, 50)
    border = (255, 255, 255)

    pygame.draw.rect(screen, color, rect, border_radius=10) 
    pygame.draw.rect(screen, border, rect, 2, border_radius=10)

    text_surf = font.render(text, True, (255, 255, 255)) 
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)


def show_gameover(screen, width, height, score, level): #menampilkan menu game over dengan skor dan level terakhir, serta pilihan untuk bermain lagi atau keluar
    clock = pygame.time.Clock()

    font_big = pygame.font.SysFont("arial", 70, bold=True)
    font_mid = pygame.font.SysFont("arial", 35)

    # LOAD BACKGROUND
    bg = pygame.image.load("assets/menu.png").convert()

    # BLUR EFFECT (fake blur)
    small = pygame.transform.smoothscale(bg, (width // 10, height // 10))
    bg_blur = pygame.transform.smoothscale(small, (width, height))

    selected = 0  # 0 = play again, 1 = exit

    # tombol
    play_btn = pygame.Rect(width//2 - 120, height//2 + 40, 240, 50)
    exit_btn = pygame.Rect(width//2 - 120, height//2 + 110, 240, 50)

    while True:
        # BACKGROUND BLUR
        screen.blit(bg_blur, (0, 0))

        # OVERLAY GELAP
        overlay = pygame.Surface((width, height))
        overlay.set_alpha(150)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        # GAME OVER
        title = font_big.render("GAME OVER", True, (255, 50, 50))
        screen.blit(title, title.get_rect(center=(width//2, height//2 - 120)))

        # SCORE & LEVEL
        score_text = font_mid.render(f"Score: {score}", True, (255, 255, 255))
        level_text = font_mid.render(f"Level: {level}", True, (255, 255, 255))

        screen.blit(score_text, score_text.get_rect(center=(width//2, height//2 - 30)))
        screen.blit(level_text, level_text.get_rect(center=(width//2, height//2)))

        mouse_pos = pygame.mouse.get_pos()

        # hover
        if play_btn.collidepoint(mouse_pos): 
            selected = 0
        elif exit_btn.collidepoint(mouse_pos):
            selected = 1

        # tombol
        draw_button(screen, "PLAY AGAIN", font_mid, play_btn, selected == 0)
        draw_button(screen, "EXIT", font_mid, exit_btn, selected == 1)

        pygame.display.flip()

        # input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % 2 
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 2

                if event.key == pygame.K_RETURN:
                    return selected

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(mouse_pos):
                    return 0
                if exit_btn.collidepoint(mouse_pos):
                    return 1

        clock.tick(60) #membatasi menu game over agar tidak berjalan terlalu cepat, sehingga input bisa terbaca dengan baik