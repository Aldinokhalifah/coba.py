import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Warna
white = (255, 255, 255)
black = (0, 0, 0)

# Kecepatan permainan
clock = pygame.time.Clock()
fps = 30

# Mengatur gambar dan suara
bird_img = pygame.image.load('bird.png')
bg_img = pygame.image.load('background.jpg')
pipe_img = pygame.image.load('pipe.png')

# Kelas Burung
class Bird:
    def __init__(self):
        self.image = bird_img
        self.x = 50
        self.y = screen_height // 2
        self.gravity = 0.5
        self.lift = -10
        self.velocity = 0

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        if self.y > screen_height:
            self.y = screen_height
            self.velocity = 0

    def jump(self):
        self.velocity = self.lift

    def show(self):
        screen.blit(self.image, (self.x, self.y))

# Kelas Pipa
class Pipe:
    def __init__(self):
        self.x = screen_width
        self.width = pipe_img.get_width()
        self.top = random.randint(50, screen_height // 2)
        self.bottom = screen_height - (self.top + 150)

    def update(self):
        self.x -= 5

    def show(self):
        screen.blit(pipe_img, (self.x, 0), (0, 0, self.width, self.top))
        screen.blit(pipe_img, (self.x, screen_height - self.bottom), (0, 0, self.width, self.bottom))

# Fungsi utama
def game_loop():
    bird = Bird()
    pipes = []
    pipes.append(Pipe())
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        bird.update()

        if pipes[-1].x < screen_width // 2:
            pipes.append(Pipe())

        for pipe in pipes:
            pipe.update()

            if pipe.x < -pipe.width:
                pipes.remove(pipe)
                score += 1

        screen.blit(bg_img, (0, 0))
        bird.show()
        for pipe in pipes:
            pipe.show()

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
