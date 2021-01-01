### Draw Number & Predict
import install_requirements
try:
    import sys, os
    stdout = sys.__stdout__
    stderr = sys.__stderr__
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')
    import pygame
    import tensorflow as tf
    import matplotlib.pyplot as plt
    import numpy as np
    from tkinter import *
    from tkinter import messagebox
    sys.stdout = stdout
    sys.stderr = stderr

except:
    import install_requirements
    import sys, os
    stdout = sys.__stdout__
    stdout = sys.__stderr__
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')
    import pygame
    import tensorflow as tf
    import matplotlib.pyplot as plt
    import numpy as np
    from tkinter import *
    from tkinter import messagebox
    sys.stdout = stdout
    sys.stderr = stderr

# Draw a digit using pyGame
class pixel(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 255, 255)
        self.neighbors = []
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.x + self.width, self.y + self.height))

    def getNeighbors(self, g):
        # Get the neighbours of each pixel in the grid, this is used for drawing thicker lines
        j = self.x // 20    # the var i is responsible for denoting the current col value in the grid
        i = self.y // 20    # the var j is responsible for denoting thr current row value in the grid
        rows = 28
        cols = 28

        # Horizontal & Vertical Neighbors
        if i < cols - 1:    # Right
            self.neighbors.append(g.pixels[i + 1][j])
        if i > 0:           # Left
            self.neighbors.append(g.pixels[i - 1][j])
        if j < rows - 1:    # Up
            self.neighbors.append(g.pixels[i][j + 1])
        if j > 0:           # Down
            self.neighbors.append(g.pixels[i][j - 1])
        
        # Diagonal Neighbors
        if j > 0 and i > 0:     # Top Left
            self.neighbors.append(g.pixels[i - 1][j + 1])
        if j + 1 < rows and i > - 1 and i - 1 > 0:     # Bottom Left
            self.neighbors.append(g.pixels[i - 1][j + 1])
        if j - 1 < rows and i < cols - 1 and j - 1 > 0:     # Top Right
            self.neighbors.append(g.pixels[i + 1][j - 1])
        if j < rows - 1 and i < cols - 1:       # Bottom Right
            self.neighbors.append(g.pixels[i + 1][j + 1])
    
    






