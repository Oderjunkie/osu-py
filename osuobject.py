from osusettings import *
class OsuObject():
    def __init__(self, x=0, y=0, t=(0, 0), sound=0):
        self.x = x
        self.y = y
        self.t = t
        self.sound = self.sounddec(sound)
    def sounddec(self, soundint):
        if soundint & 8: return 3
        if soundint & 4: return 2
        if soundint & 2: return 1
        return 0
    def __repr__(self):
        return f'An osu!hitobject at position ( {self.x}, {self.y} ), {self.t[0]}ms from the start of the song.'
    def opac(self, objar, last, mills):
        """ Returns the opacity based on several factors. """
        star = self.t[0]
        endt = self.t[1]+last
        lenh = star-objar[0]
        fade = star-objar[1]
        if lenh<mills<fade:
            return (mills-lenh)/(fade-lenh)
        elif fade<mills<endt:
            return 1
        elif endt<mills<endt+1500:
            return 1-(mills-endt)/1500
        else:
            return 0
    def appr(self, objar, last, mills):
        """ Returns the approach circle size based on several factors. """
        star = self.t[0]
        endt = self.t[1]+last
        lenh = star-objar[0]
        if lenh<mills<star:
            return 3-((mills-lenh)/(star-lenh))*2
        elif star<mills<endt:
            return 1
        else:
            return 0
    def prog(self, last, mills):
        """ Returns the progress amount based on several factors, Only used for sliders. """
        star = self.t[0]
        endt = self.t[1]+last
        lenh = star-objar[0]
        if mills<star:
            return 0
        elif star<mills<endt:
            return (mills-star)/(endt-star)
        else:
            return 1
    def lerp(self, a, b, x):
        y = 1-x
        return [a[0]*y+b[0]*x, a[1]*y+b[1]*x]
