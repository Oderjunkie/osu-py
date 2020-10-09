from osucircle import *
class Slider(OsuObject, pg.sprite.Sprite):
    def __init__(self, settings, images={}, obj=['0','0','0'], num=0, color=[255,0,0]):
        x = int(obj[0])
        y = int(obj[1])
        sound = int(obj[4])
        t = int(obj[2])
        timing = [i for i in settings.importing.timingpoints if (int(i[0])<=t and i[6]=='1')].pop()
        timing = timing[1]
        length = int(obj[7])
        self.anchor = [i.split(':') for i in obj[5][2:].split('|')]
        length = float(length / (float(settings.importing.difficulty['SliderMultiplier']) * 100)) * float(timing)
        tn = t + length * (int(obj[6])+1)
        super().__init__(x, y, (t, tn), sound)
        pg.sprite.Sprite.__init__(self)
        self.images = images
        self.num = num
        self.points = None
        self.color = color
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
        hitcircle.fill(tuple(self.color), special_flags=pg.BLEND_RGB_MULT)
        screen = pg.Surface([640, 480], pg.SRCALPHA, 32)
        screen = screen.convert_alpha()
        pos = [int(int(i)+cs) for i in self.anchor[-1]]
        pg.draw.line(screen, (self.color[0], self.color[1], self.color[2]), [int(self.x+cs), int(self.y+cs)], pos, cs)
        [screen.blit(*i) for i in [\
                     [big_boi, [int((self.x-cs*size/2)+cs), int((self.y-cs*size/2)+cs)]],\
                     [hitcircle, [int(self.x+cs/2), int(self.y+cs/2)]],\
                     [hitcircleoverlay, [int(self.x+cs/2), int(self.y+cs/2)]],\
                     [number, [int(self.x+(3*cs/8)+cs/2), int(self.y+(76*cs/256)+cs/2)]],\
                     [hitcircle, [int(pos[0]-cs/2),int(pos[1]-cs/2)]],\
                     [hitcircleoverlay, [int(pos[0]-cs/2),int(pos[1]-cs/2)]]\
                 ]]
        screen.fill((255, 255, 255, alpha), special_flags=pg.BLEND_RGBA_MULT)
        window.blit(screen, [0,0])
