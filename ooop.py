import pygame
import random

# Ekran boyutları
WIDTH = 800
HEIGHT = 600

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Uzay gemisinin sınıfı
class SpaceShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# Meteorların sınıfı
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 8)
        self.speed_x = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)

# Oyun başlatma
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meteor Destroyer")
clock = pygame.time.Clock()

# Sprite grupları
all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()

# Uzay gemisi oluşturma
player = SpaceShip()
all_sprites.add(player)

# Meteor oluşturma
for i in range(8):
    meteor = Meteor()
    all_sprites.add(meteor)
    meteors.add(meteor)

# Oyun döngüsü
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kontroller
    all_sprites.update()

    # Çarpışma kontrolü
    hits = pygame.sprite.spritecollide(player, meteors, False)
    if hits:
        running = False

    # Ekranı temizleme
    screen.fill(BLACK)

    # Sprite'ları çizme
    all_sprites.draw(screen)

    # Ekranı güncelleme
    pygame.display.flip()

pygame.quit()