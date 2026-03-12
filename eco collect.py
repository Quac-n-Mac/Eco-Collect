import pygame, math, random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1210,908))
playing = True

score = 0

x = 10
y = 10

bg = pygame.image.load("images/ecobg.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =pygame.image.load("images/bin.png")
        self.image = pygame.transform.scale(self.image, (50,60))
        self.rect = self.image.get_rect()
    def update():
        pass

class Recycle(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (40, 55))
        self.rect = self.image.get_rect()

class NoRecycle(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (40, 55))
        self.rect = self.image.get_rect()

images=["images/paper_bag.png", "images/crate.png", "images/pencil.png"]

bag=["images/bag.png"]

recycled_items = pygame.sprite.Group()
unrecycled_items = pygame.sprite.Group()

for i in range(1500):
    item = Recycle(random.choice(images))
    item.rect.x = random.randint(0,1170)
    item.rect.y = random.randint(75,850)
    recycled_items.add(item)

for e in range(50):
    non_item = NoRecycle(random.choice(bag))
    non_item.rect.x = random.randint(0,1170)
    non_item.rect.y = random.randint(75,850)
    unrecycled_items.add(non_item)


player = Player()

sprites = pygame.sprite.Group()
sprites.add(player)



clock = pygame.time.Clock()

while playing:
    clock .tick(60)
    screen.blit(bg, (0,0))
    recycled_items.draw(screen)
    unrecycled_items.draw(screen)
    font = pygame.font.SysFont("arial", 75)
    text = font.render(("S  c  o  r  e  :   " + str(score)), True, "white")
    screen.blit(text, (375, 10))
    sprites.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_DOWN and player.rect.y <=850:
                player.rect.y += 10
            if event.key == K_UP and player.rect.y >=0:
                player.rect.y -= 10
            if event.key == K_LEFT and player.rect.x >=0:
                player.rect.x -= 10
            if event.key == K_RIGHT and player.rect.x <=1170:
                player.rect.x += 10
    pygame.display.update()