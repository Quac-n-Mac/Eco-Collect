import pygame, math, random, time
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

for i in range(100):
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

str_time = time.time()

clock = pygame.time.Clock()

while playing:
    clock .tick(60)
    screen.blit(bg, (0,0))
    timeelapsed = time.time()-str_time
    recycled_items.draw(screen)
    unrecycled_items.draw(screen)
    font = pygame.font.SysFont("arial", 30)
    text = font.render(("S  c  o  r  e  :   " + str(score)), True, "white")
    screen.blit(text, (375, 10))
    text2 = font.render(str(60-int(timeelapsed)), True, "white")
    screen.blit(text2, (100, 10))
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
    good_hit = pygame.sprite.spritecollide(player, recycled_items, True)
    bad_hit = pygame.sprite.spritecollide(player, unrecycled_items, True)
    for y in good_hit:
        score +=2
    for k in bad_hit:
        score -=4
    if timeelapsed >= 60:
        font2 = pygame.font.SysFont("arial", 100)
        if score >= 40:
            screen.fill((0,255,0))
            text3 = font2.render(("S c o r e :  " + str(score)), True, "white")
            text4 = font2.render("You did good", True, "white")
            screen.blit(text4, (50, 500))
        elif score <=39:
            screen.fill((255,0,0))
            text3 = font2.render(("S c o r e :  " + str(score)), True, "white")
            text5 = font2.render("You didn't do good", True, "white")
            screen.blit(text5, (50, 500))
        screen.blit(text3, (50, 400))
    pygame.display.update()
