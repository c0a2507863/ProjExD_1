import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習1
    kk_img = pg.image.load("fig/3.png") #練習3
    kk_img = pg.transform.flip(kk_img, True, False) #練習3
    bg_img2 = pg.transform.flip(bg_img, True, False)

    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200

    tmr = 0
    x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        yoko = 0
        tate = 0

        x = tmr%3200
        screen.blit(bg_img, [-x, 0]) #練習2
        screen.blit(bg_img2, [-x + 1600, 0]) #練習2
        screen.blit(bg_img, [-x + 3200, 0]) #練習2
        screen.blit(kk_img, [-x + kk_rct[0], kk_rct[1]]) #練習4
        pg.display.update()

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            tate -= 1
        if key_lst[pg.K_DOWN]:
            tate += 1
        if key_lst[pg.K_LEFT]:
            yoko -=1
        if key_lst[pg.K_RIGHT]:
            yoko += 2
    
        kk_rct.move_ip((yoko,tate))

        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()