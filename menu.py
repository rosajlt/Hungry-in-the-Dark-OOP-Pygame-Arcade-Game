import pygame
import sys


def draw_button(screen, text, font, rect, is_selected):
    # warna tombol
    color = (255, 200, 50) if is_selected else (50, 50, 50)
    border_color = (255, 255, 255)

    # kotak tombol
    pygame.draw.rect(screen, color, rect, border_radius=10)
    pygame.draw.rect(screen, border_color, rect, 2, border_radius=10)

    # teks
    text_surf = font.render(text, True, (0, 0, 0) if is_selected else (255, 255, 255))
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)


def show_menu(screen, width, height):
    clock = pygame.time.Clock()

    font_title = pygame.font.SysFont("arial", 70, bold=True)
    font_menu = pygame.font.SysFont("arial", 35)

    # LOAD BACKGROUND
    bg = pygame.image.load("assets/menu.png").convert()

    # FAKE BLUR (scale kecil lalu dibesarkan lagi)
    small = pygame.transform.smoothscale(bg, (width//10, height//10))
    bg_blur = pygame.transform.smoothscale(small, (width, height))

    selected = 0  # 0 = start, 1 = exit

    # tombol posisi
    start_btn = pygame.Rect(width//2 - 120, height//2 - 20, 240, 50)
    exit_btn = pygame.Rect(width//2 - 120, height//2 + 50, 240, 50)

    while True:
        # background blur
        screen.blit(bg_blur, (0, 0))

        # overlay gelap
        overlay = pygame.Surface((width, height))
        overlay.set_alpha(120)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        mouse_pos = pygame.mouse.get_pos() 

        # TITLE
        title = font_title.render("HUNGRY IN THE DARK", True, (255, 255, 255))
        title_rect = title.get_rect(center=(width//2, height//2 - 150))
        screen.blit(title, title_rect)

        # hover detection
        if start_btn.collidepoint(mouse_pos): 
            selected = 0
        elif exit_btn.collidepoint(mouse_pos):
            selected = 1

        # DRAW BUTTONS
        draw_button(screen, "START GAME", font_menu, start_btn, selected == 0)
        draw_button(screen, "EXIT", font_menu, exit_btn, selected == 1)

        pygame.display.flip()

        # INPUT
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
                    if selected == 0:
                        return
                    elif selected == 1:
                        pygame.quit()
                        sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.collidepoint(mouse_pos):
                    return
                if exit_btn.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        clock.tick(60)