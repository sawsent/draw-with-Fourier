from cmath import exp, tau
from math import floor
from settings import i, MAX_VECTORS

class ComputeDrawing:
    def __init__(self, points):
        if len(points) > MAX_VECTORS and MAX_VECTORS != 0:
            self.dt = 1/MAX_VECTORS
            self.points = []
            c = 0 
            for point in points:
                c -= 1
                if c < 0:
                    self.points.append(point)
                    c = floor(len(points) / MAX_VECTORS)
        else:
            self.dt = 1/(len(points))
            self.points = points
        self.point_objs = [{'n': idx - len(self.points)//2} for idx, _ in enumerate(self.points)]


    def get_discrete_func(self):
        discrete_func = {}
        t = 0
        for point in self.points:
            discrete_func[t] = complex(point[0], point[1])
            t += self.dt
        return discrete_func
    
    def compute_consts(self):
        discrete_func = self.get_discrete_func()
        for point in self.point_objs:
            const = 0
            for t, f_of_t in discrete_func.items():
                const += exp(-1 * point['n'] * tau * i * t) * f_of_t * self.dt
            point['const'] = const
        return self.point_objs
