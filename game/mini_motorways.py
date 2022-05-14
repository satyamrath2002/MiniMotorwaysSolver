import sys

import pygame
from pygame.constants import QUIT
from pygame.display import update

from utilities import *
from cells import SquareCell

SCREEN_HEIGHT = 800
BACKGROUND_COLOR = (150, 150, 150)


class MiniMotorways:
    """Overall class to manage the game"""

    def __init__(self, mode: str):
        """Initializes the game"""
        pygame.init()
        self.mode = mode

        # dimensions
        self.dim = tuple(int(i) for i in input().split(" "))

        # setting up the screen
        self.screen_height = SCREEN_HEIGHT
        self.cell_size = self.screen_height / self.dim[0]
        self.screen_width = self.cell_size * self.dim[1]
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("Mini Motorways")
        self.bg_colour = BACKGROUND_COLOR

        self.cells = []
        self.to_be_updated = []
        self._create_cells()

        # Markets
        n = int(input())
        self.markets = []
        while n:
            n -= 1
            s = [int(i) for i in input().split(" ")]
            self.markets.append(
                tuple((s[i], s[i+1]) for i in range(0, 6, 2)))

        # Houses
        n = int(input())
        self.houses = []
        while n:
            n -= 1
            self.houses.append(tuple(int(i) for i in input().split(" ")))

        # Roads
        n = int(input())
        self.roads = []
        while n:
            n -= 1
            s = [int(i) for i in input().split(" ")]
            self.roads.append(
                tuple((s[i], s[i+1]) for i in range(0, 4, 2)))

        for road in self.roads:
            self.cells[road[0][0]][road[0][1]].type = "road"
            self.cells[road[1][0]][road[1][1]].type = "road"
            if road[0][0] == road[1][0]:
                if road[0][1] < road[1][1]:
                    self.cells[road[0][0]][road[0][1]].status["r"] = True
                    self.cells[road[1][0]][road[1][1]].status["l"] = True
                elif road[0][1] > road[1][1]:
                    self.cells[road[0][0]][road[0][1]].status["l"] = True
                    self.cells[road[1][0]][road[1][1]].status["r"] = True
            elif road[0][1] == road[1][1]:
                if road[0][0] < road[1][0]:
                    self.cells[road[0][0]][road[0][1]].status["d"] = True
                    self.cells[road[1][0]][road[1][1]].status["u"] = True
                elif road[0][0] > road[1][0]:
                    self.cells[road[0][0]][road[0][1]].status["u"] = True
                    self.cells[road[1][0]][road[1][1]].status["d"] = True

        for market in self.markets:
            for x in range(market[0][0], market[1][0]+1):
                for y in range(market[0][1], market[1][1]+1):
                    self.cells[x][y].type = "market"
            self.cells[market[2][0]][market[2][1]].type = "market-entry"

        for house in self.houses:
            self.cells[house[0]][house[1]].type = "house"

        self.road_network = self._make_graph()
        # print(self.road_network.adjDict)

    def _create_cells(self):
        """Create all cells"""
        for row_number in range(self.dim[0]):
            row_cells = []
            row_to_be_updated = []
            for cell_number in range(self.dim[1]):
                row_cells.append(self._create_cell(row_number, cell_number))
                row_to_be_updated.append(False)
            self.cells.append(row_cells)
            self.to_be_updated.append(row_to_be_updated)

    def _create_cell(self, row_number, cell_number):
        """Creates a cell at given position"""
        cell = SquareCell(self)
        cell.x = cell_number * self.cell_size
        cell.y = row_number * self.cell_size
        return cell

    def _make_graph(self):
        """Will create a graph modelling the current road network"""
        if self.mode == "sim-bfs":
            return simple_graph_maker(self.dim, self.roads)
        elif self.mode == "dfs-djk":
            return dfs_graph_maker(self.dim, self.roads)

    def run(self):
        """Runs the game loop"""
        q = int(input())

        self.screen.fill(self.bg_colour)
        for row in self.cells:
            for cell in row:
                cell.draw()

        pygame.display.flip()

        while q:
            q -= 1
            src, trg = tuple(int(i) for i in input().split(" "))
            path = self._shortest_path(src, trg)
            print(path)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _shortest_path(self, src, trg):
        if self.mode == "sim-bfs":
            return bfs_path_finder(self.road_network, self.houses[src], self.markets[trg][2])
        elif self.mode == "dfs-djk":
            return dijkstras_path_finder(self.road_network, self.houses[src], self.markets[trg][2])
