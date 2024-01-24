import pygame
import math
from screen import Screen
from settings import *
import csv
from time import sleep

class Canvas(Screen):
    def __init__(self, stateManager, drawer):
        super().__init__(stateManager)
        self.drawer = drawer

        self.CVS_BG_COLOR = 'white'
        self.cvs_surf.fill(self.CVS_BG_COLOR)
        self.drawn_pixels = []

        # defaults
        self.brush_color = 'black'
        self.brush_size = 1
        self.brush_size_float = 1
        self.drawing = False
        self.outline_rect = pygame.Rect(CVS_OFFSET_X, CVS_OFFSET_Y, PIXEL_SIZE * self.brush_size, PIXEL_SIZE * self.brush_size)

        self.coming_back = True
    
    def update_canvas(self):
        self.cvs_surf.fill(self.CVS_BG_COLOR)
        for rect_object in self.drawn_pixels:
            pygame.draw.rect(self.cvs_surf, rect_object['color'], rect_object['rect'])
        self.draw_number_line()
        self.pixels_drawn_text = self.info_font.render(f"Pixels Drawn: {len(self.drawn_pixels)}", True, 'black')
        self.cvs_surf.blit(self.pixels_drawn_text, self.pixels_drawn_text.get_rect(topleft=(5, 5)))
        if self.coming_back:
            print("Available Canvas Commands:\n left click: draw\n c: clear canvas\n e: export to drawer\n s: save to file\n l: load from file")
            self.coming_back = False
    
    def save(self):
        filename = input("type the name for your save : \n >> ")
        if filename.lower() == 'cancel': return
        for_save = [{"posx": pixel["pos"][0], "posy": pixel["pos"][1]} for pixel in self.drawn_pixels]
        keys = for_save[0].keys()
        with open(f"../saves/{filename}.csv", "w", newline="") as output_file:
            dict_writer = csv.DictWriter(output_file, keys) 
            dict_writer.writeheader()
            dict_writer.writerows(for_save)

    def load(self):
        filename = input("type the filename to load : \n >> ")
        if filename.lower() == 'cancel': return
        with open(f'../saves/{filename}.csv') as input_file:
            to_load = [{k: float(v) for k, v in row.items()} for row in csv.DictReader(input_file, skipinitialspace=True)]
        self.drawn_pixels = [{  
                    'rect': pygame.Rect(pixel["posx"] + CVS_WIDTH//2, pixel["posy"] + CVS_HEIGTH//2, PIXEL_SIZE, PIXEL_SIZE), 
                    'color': "black",
                    'pos': pygame.math.Vector2(pixel["posx"], pixel["posy"])
                    } for pixel in to_load]
        
    def show_pencil_outline(self):
        if self.cvs_rect.collidepoint(self.m_pos):
            outline_coords = (self.m_coords - (self.brush_size//2, self.brush_size//2)) * PIXEL_SIZE
            self.outline_rect.topleft = outline_coords
            pygame.draw.rect(self.cvs_surf, self.brush_color, self.outline_rect, 2)
    
    def get_mouse_pos(self):
        self.m_pos = pygame.mouse.get_pos()
        self.m_coords = pygame.math.Vector2((self.m_pos[0]-CVS_OFFSET_X) // PIXEL_SIZE, (self.m_pos[1]-CVS_OFFSET_Y) // PIXEL_SIZE)
    
    def draw(self):
        if not self.drawing: return
        for rect_object in self.drawn_pixels:
            if rect_object['rect'].colliderect(self.outline_rect):
                return
        self.drawn_pixels.append({  'rect': pygame.Rect(self.outline_rect.left, self.outline_rect.top, PIXEL_SIZE, PIXEL_SIZE), 
                                    'color': 'black', 
                                    'pos': pygame.math.Vector2(((self.outline_rect.left - CVS_WIDTH//2), (self.outline_rect.top - CVS_HEIGTH//2)))} )

    def clear(self):
        self.drawn_pixels = []
    
    def export_to_drawer(self):
        self.coming_back = True
        for_export = [rect_obj["pos"] for rect_obj in self.drawn_pixels]
        self.drawer.set_up(for_export)
        self.stateManager.set_state('drawer')
        return for_export
    
    def input(self):
        pressed = pygame.key.get_pressed()
        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0]:
            self.drawing = True
        else:
            self.drawing = False

        if pressed[pygame.K_p]:
            self.brush_color = 'black'
        if pressed[pygame.K_c]:
            self.clear()
        if pressed[pygame.K_e]:
            self.export_to_drawer()
        if pressed[pygame.K_s]:
            self.save()
        if pressed[pygame.K_l]:
            self.load()

    def run(self):
        self.update_canvas()
        self.get_mouse_pos()
        self.input()
        self.show_pencil_outline()
        self.draw()
        self.screen.blit(self.cvs_surf, self.cvs_rect)
