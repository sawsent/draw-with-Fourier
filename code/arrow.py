from cmath import exp, tau, pi
from settings import *
from pygame.math import Vector2

class Arrow:
    color_index = 0
    def __init__(self, const, n, vec_color='white'):
        self.starting_point = (CVS_WIDTH//2, CVS_HEIGTH//2)
        self.const = const
        self.vec_color = vec_color
        self.n = n
        
        if AUTO_COLORS:
            self.vec_color = COLORS[Arrow.color_index]
            Arrow.color_index += 1
            if Arrow.color_index >= len(COLORS):
                Arrow.color_index = 0

    def func(self, time):
        return exp(self.n * tau * i * time) * self.const * SCALER

    def updateVector(self, time):
        self.vector_number = self.func(time)
        self.vector = Vector2(self.vector_number.real, self.vector_number.imag)