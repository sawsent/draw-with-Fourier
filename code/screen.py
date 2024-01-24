import pygame
from settings import *

class Screen:
    def __init__(self, stateManager):
        self.screen = pygame.display.get_surface()
        self.stateManager = stateManager

        # general
        self.cvs_surf = pygame.Surface((CVS_WIDTH, CVS_HEIGTH))
        self.cvs_rect = self.cvs_surf.get_rect(topleft=(CVS_OFFSET_X, CVS_OFFSET_Y))
        self.cvs_font = pygame.font.Font('freesansbold.ttf', 16)

        self.info_font = pygame.font.Font('freesansbold.ttf', 25)

         # canvas text
        self.texts = [
            # real numbers
            {'text': self.cvs_font.render( "-2", True, 'blue'), 'pos': (1*CVS_WIDTH//10 + 5, CVS_HEIGTH//2 + 5)},
            {'text': self.cvs_font.render( "-1", True, 'blue'), 'pos': (3*CVS_WIDTH//10 + 5, CVS_HEIGTH//2 + 5)},
            {'text': self.cvs_font.render(  "0", True, 'blue'), 'pos': (CVS_WIDTH//2 + 5, CVS_HEIGTH//2 + 5)},
            {'text': self.cvs_font.render(  "1", True, 'blue'), 'pos': (7*CVS_WIDTH//10 + 5, CVS_HEIGTH//2 + 5)},
            {'text': self.cvs_font.render(  "2", True, 'blue'), 'pos': (9*CVS_WIDTH//10 + 5, CVS_HEIGTH//2 + 5)},
            # imag numbers
            {'text': self.cvs_font.render( "2i", True, 'blue'), 'pos': (CVS_WIDTH//2 + 5, 1*CVS_HEIGTH//10 + 5)},
            {'text': self.cvs_font.render( "1i", True, 'blue'), 'pos': (CVS_WIDTH//2 + 5, 3*CVS_HEIGTH//10 + 5)},
            {'text': self.cvs_font.render( "0i", True, 'blue'), 'pos': (CVS_WIDTH//2 + 5, CVS_HEIGTH//2 + 5)},
            {'text': self.cvs_font.render("-1i", True, 'blue'), 'pos': (CVS_WIDTH//2 + 5, 7*CVS_HEIGTH//10 + 5)},
            {'text': self.cvs_font.render("-2i", True, 'blue'), 'pos': (CVS_WIDTH//2 + 5, 9*CVS_HEIGTH//10 + 5)},
        ]
        for text in self.texts:
            text['rect'] = text['text'].get_rect(topleft = text['pos'])
    
    def draw_number_line(self):
        if not DRAW_NUMBER_LINE: return
        pygame.draw.line(self.cvs_surf, 'blue', (CVS_WIDTH//2, 0),( CVS_WIDTH//2, CVS_HEIGTH), 3)
        pygame.draw.line(self.cvs_surf, 'blue', (0, CVS_HEIGTH//2),(CVS_WIDTH, CVS_HEIGTH//2), 3)
        for text_object in self.texts:
            self.cvs_surf.blit(text_object['text'], text_object['rect'])