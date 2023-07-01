import  pygame
from pygame import *

racket_img = 'racket.png'
ball_img = 'tenis_ball.png'

class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)

        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # метод, що малює героя у вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    # метод для керування спрайтом стрілками клавіатури
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed


back = (200, 255, 255)
win_width = 600
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()

finish = False
game = True

racket1 = Player(racket_img, 30, 200, 4, 50, 150)
racket2 = Player(racket_img, 520, 200, 4, 50, 150)
ball = GameSprite(ball_img, 200, 200, 4, 50, 50)

speed_x = 3
speed_y = 3
font.init()
font = font.Font(None,50)

lose1 = font.render("prograla 1 raketa", True, (255, 35, 17))
lost2 = font.render("prograla 2 raketa", True, (25, 235, 117))


while game:

    for e in event.get():
        if e.type == pygame.QUIT:
            game = False


    if not finish:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()


        ball.rect.x += speed_x
        ball.rect.y += speed_y


        racket1.reset()
        racket2.reset()
        ball.reset()
        if ball.rect.colliderect(racket1.rect) or ball.rect.colliderect(racket2):
            speed_x *= -1
        elif ball.rect.y < 0 or ball.rect.y > win_height - ball.rect.height:
            speed_y *= -1
        if ball.rect.x > win_width:
            window.blit(lose1,(170,200))
        elif ball.rect.x < 0:
            window.blit(lost2,(170,200))


    display.update()
    clock.tick(60)