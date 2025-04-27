import pygame
import time

pygame.init()
pygame.font.init()


pygame.init()
TI_WIDTH, TI_HEIGHT = 320, 210
display_surface = pygame.display.set_mode((TI_WIDTH, TI_HEIGHT))
pygame.display.set_caption("TI 84 Plus CE Python Emulator")
a = True


#works
def draw_line(x1, y1, x2, y2):
        pygame.draw.line(display_surface, (0, 0, 0), (x1, y1), (x2, y2))


#works
def draw_rect(x, y, w, h):
        pygame.draw.rect(display_surface, (0,0,0), (x, y, w, h), 1)


#works
def fill_rect(x, y, w, h):
        pygame.draw.rect(display_surface, (0,0,0), (x, y, w, h))

#works
def draw_circle(x, y, r):
        pygame.draw.circle(display_surface, (0,0,0), (x, y), r, 1)

#works
def fill_circle(x, y, r):
        pygame.draw.circle(display_surface, (0,0,0), (x, y), r)

#works
def draw_text(x, y, string):
        myfont = pygame.font.SysFont('microsoftsansserif',12)
        mytext = myfont.render(string, 1, (0, 0, 0))
        display_surface.blit(mytext, (x,y))
        pygame.display.flip()
        
def draw_poly(xlist, ylist):
        pointlist = str(xlist) + str(", ") + str(ylist)
        pygame.draw.polygon(display_surface, (0,0,0), pointlist, 1)


