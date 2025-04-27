from ti_draw import *
a = True

while a:
    #remove before calculator import
    for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 a = False
    display_surface.fill("white")

    #put the code for the game here


    # draw_line(10, 10, 310, 200)
    # draw_rect(10, 10, 45, 63)
    # fill_rect(10, 10, 45, 63)
    #draw_circle(100, 100, 5)
    #fill_circle(120, 100, 5)
    #draw_text(40, 50, "Hello World")
    x=list[(12,32), (34, 87)]
    y=list[(21,23), (45, 76)]

    draw_poly(12, 54)

    #again, remove
    pygame.display.update()

    