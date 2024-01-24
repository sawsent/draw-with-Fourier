import pygame
from compute import ComputeDrawing
from screen import Screen
from arrow import Arrow
from settings import *

class Drawer(Screen):
    def __init__(self, stateManager):
        super().__init__(stateManager)
        self.draw_points_surf = pygame.Surface((CVS_WIDTH, CVS_HEIGTH), pygame.SRCALPHA, 32)
        self.draw_points_rect = self.draw_points_surf.get_rect()
        self.CVS_BG_COLOR = 'black'

        self.simulation_speed = DEFAULT_SIMULATION_SPEED

    def set_up(self, points):
        computer = ComputeDrawing(points)
        self.point_objs = computer.compute_consts()
        self.arrows = sorted([Arrow(point['const'], point['n']) for point in self.point_objs], key=lambda arrow: abs(arrow.n))
        self.arrow_count = len(self.arrows)
        self.counter_text = self.info_font.render(f"{self.arrow_count} vectors.", True, 'white', 'black')
        self.counter_text_rect = self.counter_text.get_rect(topleft = (5,5))
        print("Available commands in drawer: \n m: speed up sim speed\n n: slow down sim speed\n d: back to drawer")
        self.tick_offset = pygame.time.get_ticks()

    def input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_m]:
            self.simulation_speed += 0.005
        if pressed[pygame.K_n]:
            self.simulation_speed -= 0.005
        if pressed[pygame.K_d]:
            self.back_to_canvas()
    
    def update_canvas(self):
        self.cvs_surf.fill(self.CVS_BG_COLOR)
        self.draw(self.arrows)
        self.cvs_surf.blit(self.draw_points_surf, (0,0), self.draw_points_rect)

        if DRAW_CENTER:
            pygame.draw.circle(self.screen, 'red', (CVS_WIDTH//2, CVS_HEIGTH//2), 5)

        self.draw_number_line()
        
        self.speed_text = self.info_font.render(f"Simulation Speed: {self.simulation_speed}", True, 'white', 'black')
        self.time_text = self.info_font.render(f"Simulation Time: {self.get_time()} seconds", True, 'white', 'black')
        self.cvs_surf.blit(self.counter_text, self.counter_text_rect)
        self.cvs_surf.blit(self.speed_text, self.speed_text.get_rect(topleft=(5, 935)))
        self.cvs_surf.blit(self.time_text, self.time_text.get_rect(topleft=(5, 970)))

    def get_time(self):
        return (pygame.time.get_ticks()-self.tick_offset) / ((1/self.simulation_speed) * 1000)
    
    def draw(self, arrows):
        for idx, arrow in enumerate(arrows):
            arrow.updateVector(self.get_time())
            if idx != 0:
                arrow.starting_point = arrows[idx-1].starting_point + arrows[idx-1].vector
                
            if idx == len(arrows) - 1:
                posX, posY = arrow.starting_point + arrow.vector
                pygame.draw.circle(self.draw_points_surf, POINT_COLOR, (posX, posY), POINT_RADIUS)
            if DRAW_ARROWS:
                pygame.draw.line(self.cvs_surf, arrow.vec_color, arrow.starting_point, arrow.starting_point+arrow.vector, ARROW_WIDTH)
    
    def back_to_canvas(self):
        self.draw_points_surf = pygame.Surface((CVS_WIDTH, CVS_HEIGTH), pygame.SRCALPHA, 32)
        self.draw_points_rect = self.draw_points_surf.get_rect()
        self.stateManager.set_state("canvas")
    
    def run(self):
        self.input()
        self.update_canvas()
        self.screen.blit(self.cvs_surf, self.cvs_rect)
