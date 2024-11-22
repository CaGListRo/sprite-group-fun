import pygame as pg
from random import randint, choice

from typing import Final

class Square(pg.sprite.Sprite):
    def __init__(self, pos: tuple, color: str) -> None:
        """
        Initialize a Square sprite.
        Args:
        pos (tuple): Position of the square.
        color (str): Color of the square.
        """
        pg.sprite.Sprite.__init__(self)
        self.image: pg.Surface = pg.Surface((55, 55))
        self.image.fill(color)
        self.rect: pg.Rect = self.image.get_rect()
        self.rect.center = pos
        self.x_direction: int = choice([-1, 1])
        self.y_direction: int = choice([-1, 1])
        self.speed: int = randint(1, 6)

    def update(self) -> None:
        """ Update the square's position. """
        self.rect.x += self.x_direction * self.speed
        if self.rect.left < 0:
            self.rect.left = 0
            self.x_direction *= -1
        if self.rect.right > 1400:
            self.rect.right = 1400
            self.x_direction *= -1
        
        self.rect.y += self.y_direction * self.speed
        if self.rect.top < 0:
            self.rect.top = 0
            self.y_direction *= -1
        if self.rect.bottom > 700:
            self.rect.bottom = 700
            self.y_direction *= -1

class Fun:
    FPS: Final[int] = 60

    def __init__(self) -> None:
        """ Initialize the game. """
        pg.init()
        self.screen: pg.display = pg.display.set_mode((1400, 700))
        pg.display.set_caption("Sprite Group Fun")
        self.running: bool = True
        self.clock: pg.time.Clock = pg.time.Clock()
        self.square_group: pg.sprite.Group = pg.sprite.Group()
        self.clicked: bool = False
        self.colors: list[str] = ["crimson", "chartreuse", "coral", "darkorange", "forestgreen", "lime", "navy", "purple", "cyan", "yellow"]

    def check_collision(self) -> None:
        """ Check for collision between squares. """
        collisions = pg.sprite.groupcollide(self.square_group, self.square_group, False, False)
        for square_list in collisions.values():
            for square in square_list:
                square.x_direction *= -1
                square.y_direction *= -1

    def create_square(self) -> None:
        """ Create a new square. """
        mouse_pos: tuple[int] = pg.mouse.get_pos()
        square: Square = Square(mouse_pos, choice(self.colors))
        self.square_group.add(square)

    def event_handler(self) -> None:
        """ Handle events. """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                self.clicked = True
            if event.type == pg.MOUSEBUTTONUP and self.clicked == True:
                self.create_square()

    def draw_screen(self) -> None:
        """ Draw the screen. """
        self.screen.fill((23, 123, 223))
        self.square_group.update()
        self.square_group.draw(self.screen)
        pg.display.update()

    def run(self) -> None:
        """ Run the game. """
        while self.running:
            self.clock.tick(self.FPS)
            self.event_handler()
            self.draw_screen()
            if len(self.square_group) > 10:
                self.check_collision()


if __name__ == "__main__":
    fun = Fun()
    fun.run()