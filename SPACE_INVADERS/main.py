import pygame, sys, random
from game import Game

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 60

BLACK = (0, 0, 0)
YELLOW = (243, 216, 63)

font = pygame.font.Font("Font/monogram.ttf", 40)
level_surface = font.render("LEVEL 01", False, YELLOW)
game_over_surface = font.render("GAME OVER", False, YELLOW)
score_text_surface = font.render("SCORE", False, YELLOW)
highscore_text_surface = font.render("HIGH-SCORE", False, YELLOW)

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2*OFFSET))
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

game_won = False
restart_button = pygame.Rect(520, 500, 250, 70)

while True:
    #Checking for events
    for event in pygame.event.get():

        # Close the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Aliens shoot
        if event.type == SHOOT_LASER and game.run and not game_won:
            game.alien_shoot_laser()

        # Mystery ship event
        if event.type == MYSTERYSHIP and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

        # Restart button after winning OR losing
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (game_won or game.run == False) and restart_button.collidepoint(event.pos):
                game_won = False
                game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)
                game.run = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and game.run == False and not game_won:
        game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)
        game.run = True

    #Updating
    if game.run and not game_won:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collisions()
    if len(game.alien_group) == 0:
        if game.level == 1:
            game.start_next_level()
            game.obstacles = []   # removes barriers for Level 2

        elif game.level == 2:
            game_won = True

     #Drawing
    screen.fill(BLACK)

    #UI
    pygame.draw.rect(screen, YELLOW, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
    pygame.draw.line(screen, YELLOW, (25, 730), (775, 730), 3)

    if game.run:
        screen.blit(level_surface, (570, 740, 50, 50))
    else:
        screen.blit(game_over_surface, (570, 740, 50, 50))

    x = 50
    for life in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, 745))
        x += 50 

    screen.blit(score_text_surface, (50, 15, 50, 50)) 
    formatted_score = str(game.score).zfill(5)
    score_surface = font.render(formatted_score, False, YELLOW)
    screen.blit(score_surface, (50, 40, 50, 50))

    level_text_surface = font.render("LEVEL", False, YELLOW)
    screen.blit(level_text_surface, (330, 15))

    level_surface = font.render(str(game.level), False, YELLOW)
    screen.blit(level_surface, (365, 40))

    screen.blit(highscore_text_surface, (550, 15, 50, 50))
    formatted_highscore = str(game.highscore).zfill(5)
    highscore_surface = font.render(formatted_highscore, False, YELLOW)
    screen.blit(highscore_surface, (625, 40, 50, 50))

    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)

    for obstacle in game.obstacles:
            obstacle.blocks_group.draw(screen)

    game.alien_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)

    if game_won or game.run == False:
        screen.fill(BLACK)

        # GAME OVER text
        game_over_text = font.render("GAME OVER", False, YELLOW)
        game_over_rect = game_over_text.get_rect(
            center=((SCREEN_WIDTH + OFFSET) // 2, 280)
        )
        screen.blit(game_over_text, game_over_rect)

        # Show win message only if player beat level 2
        if game_won:
            win_text = font.render("YOU BEAT THE GAME!", False, YELLOW)
            win_rect = win_text.get_rect(
                center=((SCREEN_WIDTH + OFFSET) // 2, 360)
            )
            screen.blit(win_text, win_rect)

        # Restart button
        pygame.draw.rect(
            screen,
            (50, 100, 220),
            restart_button,
            border_radius=10
        )

        restart_text = font.render("RESTART", False, (255, 255, 255))
        restart_text_rect = restart_text.get_rect(
            center=restart_button.center
        )
        screen.blit(restart_text, restart_text_rect)

    pygame.display.update()
    clock.tick(60)
