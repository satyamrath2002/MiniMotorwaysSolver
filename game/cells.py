from math import ceil, sqrt

import pygame
from pygame.sprite import Sprite


class SquareCell(Sprite):
    """A class for sqaure cells on simple square tessellation grid"""

    def __init__(self, mm_game):
        super().__init__()
        self.screen = mm_game.screen
        self.screen_rect = self.screen.get_rect()
        self.cell_size = mm_game.cell_size

        self.rect = pygame.Rect(0, 0, self.cell_size /
                                (1 + sqrt(2)), self.cell_size / (1 + sqrt(2)))
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.type = "base"
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.status = {"u": False, "r": False, "d": False, "l": False}

    def draw(self):
        self.rect.center = (self.x + self.cell_size / 2,
                            self.y + self.cell_size / 2)
        for i in range(4):
            pygame.draw.rect(self.screen, (200, 200, 200), (self.x,
                             self.y, self.cell_size, self.cell_size), width=1)
        if self.type == "base":
            color = (150, 150, 150, 0)
        elif self.type == "market-entry":
            color = (200, 0, 0)
        elif self.type == "market":
            color = (200, 200, 0)
        elif self.type == "house":
            color = (0, 200, 0)
        elif self.type == "road":
            color = (50, 50, 50)
        if self.status["u"]:
            pygame.draw.rect(self.screen, (50, 50, 50), (
                self.x + ceil(self.cell_size / (1 + sqrt(2)) / sqrt(2)),
                self.y,
                self.cell_size / (1 + sqrt(2)),
                ceil(self.cell_size / (1 + sqrt(2)) / sqrt(2)))
            )
        if self.status["l"]:
            pygame.draw.rect(self.screen, (50, 50, 50), (
                self.x,
                self.y + ceil(self.cell_size / (1 + sqrt(2)) / sqrt(2)),
                ceil(self.cell_size / (1 + sqrt(2)) / sqrt(2)),
                self.cell_size / (1 + sqrt(2)))
            )
        if self.status["d"]:
            pygame.draw.rect(self.screen, (50, 50, 50), (
                self.x + ceil(self.cell_size / (1 + sqrt(2)) / sqrt(2)),
                self.y + ceil(self.cell_size / sqrt(2)),
                self.cell_size / (1 + sqrt(2)),
                ceil(self.cell_size / (1 + sqrt(2)) / sqrt(2)))
            )
        if self.status["r"]:
            pygame.draw.rect(self.screen, (50, 50, 50), (
                self.x + ceil(self.cell_size / sqrt(2)),
                self.y + ceil(self.cell_size / (1 + sqrt(2)) / sqrt(2)),
                ceil(self.cell_size / (1 + sqrt(2)) / sqrt(2)),
                self.cell_size / (1 + sqrt(2)))
            )
        pygame.draw.rect(surface=self.screen, color=color, rect=self.rect)
