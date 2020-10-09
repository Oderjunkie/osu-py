from osuobject import *
class Circle(OsuObject, pg.sprite.Sprite):
    def __init__(self, images={}, obj=['0','0','0'], num=0, color=[255,0,0]):
        x = (int(obj[0])/1)+0
        y = (int(obj[1])/1)+0
        t = int(obj[2])
        sound = int(obj[4])
        super().__init__(x, y, (t, t), sound)
        pg.sprite.Sprite.__init__(self)
        self.images = images
        self.num = num
        self.points = None
        self.color = color
        if not 0<self.y<480:
            print('UH OH', self.y)
        if not 0<self.x<640:
            print('UH OH', self.x)
    def draw(self, settings, mills, window):
        cs = settings.cs()
        objar = settings.objar()
        last = settings.last()
        if self.opac(objar, last, mills)==0: return []
        size = self.appr(objar, last, mills)
        big_boi = pg.transform.scale(self.images['approachCircle'].copy(), (int(cs*size), int(cs*size)))
        hitcircle = pg.transform.scale(self.images['hitCircle'].copy(), (int(cs), int(cs)))
        hitcircleoverlay = pg.transform.scale(self.images['hitCircleOverlay'].copy(), (int(cs), int(cs)))
        number = pg.transform.scale(self.images[f'default-{(self.num%9)+1}'].copy(), (int(cs/4), int(52*cs/128)))
        alpha = self.opac(objar, last, mills) * 255
        big_boi.fill((255, 255, 255, alpha), special_flags=pg.BLEND_RGBA_MULT)
        number.fill((255, 255, 255, alpha), special_flags=pg.BLEND_RGBA_MULT)
        hitcircle.fill(tuple(self.color), special_flags=pg.BLEND_RGB_MULT)
        hitcircle.fill((255, 255, 255, alpha), special_flags=pg.BLEND_RGBA_MULT)
        hitcircleoverlay.fill((255, 255, 255, alpha), special_flags=pg.BLEND_RGBA_MULT)
        [window.blit(*i) for i in [[hitcircle, [int(self.x+cs/2), int(self.y+cs/2)]],\
                 [hitcircleoverlay, [int(self.x+cs/2), int(self.y+cs/2)]],\
                 [number, [int(self.x+(3*cs/8)+cs/2), int(self.y+(76*cs/256)+cs/2)]],\
                 [big_boi, [int((self.x-cs*size/2)+cs), int((self.y-cs*size/2)+cs)]]]]
