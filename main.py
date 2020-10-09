from osuslider import *
import easygui
extractbeatmaps()
def pimg(arg):
    print(f'loading image {arg}')
    return pg.image.load(arg).convert_alpha()
root = Tk()
menubar = Menu(root)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="you're on your own buckaroo", command=(lambda:print('i said you\'re on your own.')))
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.resizable(False, False)
embed = Frame(root, width=640, height=480)
embed.pack()

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
root.update()
pg.init()
pg.mixer.quit()
clock = pg.time.Clock()
window = pg.display.set_mode((640, 480), pg.DOUBLEBUF)
window.set_alpha(None)
window.fill((0,0,0))
CIRCLE_SPRITES = {
    'approachCircle':   (pimg('skin\\approachcircle@2x.png')),
    'hitCircle':        (pimg('skin\\hitcircle@2x.png')),
    'hitCircleOverlay': (pimg('skin\\hitcircleoverlay@2x.png')),
    'default-1':        (pimg('skin\\default-1@2x.png')),
    'default-2':        (pimg('skin\\default-2@2x.png')),
    'default-3':        (pimg('skin\\default-3@2x.png')),
    'default-4':        (pimg('skin\\default-4@2x.png')),
    'default-5':        (pimg('skin\\default-5@2x.png')),
    'default-6':        (pimg('skin\\default-6@2x.png')),
    'default-7':        (pimg('skin\\default-7@2x.png')),
    'default-8':        (pimg('skin\\default-8@2x.png')),
    'default-9':        (pimg('skin\\default-9@2x.png'))
}
MOUSE_CURSOR = pimg('skin\\cursor@2x.png')
def MOUSE(size):
    return pg.transform.scale(MOUSE_CURSOR, (int(size), int(size)))
tmp = easygui.fileopenbox()
print(tmp)
beat = Settings(tmp, '')
hitobjects = []
hitcolors = beat.importing.colors
col = 0
num = -1
for i in range(len(beat.importing.hitobjects)):
    if int(beat.importing.hitobjects[i][3])&4:
        col += int((int(beat.importing.hitobjects[i][3])&112)/16)+1
        num = 0
    else:
        num += 1
    if int(beat.importing.hitobjects[i][3])&1:
        hitobjects.append(\
            Circle(CIRCLE_SPRITES, beat.importing.hitobjects[i], num, hitcolors[col%len(hitcolors)])\
        )
    elif int(beat.importing.hitobjects[i][3])&2:
        hitobjects.append(\
            Slider(beat, CIRCLE_SPRITES, beat.importing.hitobjects[i], num, hitcolors[col%len(hitcolors)])\
        )
mills = int(beat.importing.hitobjects[0][2])-1000
objar = beat.objar()
last = beat.last()
cs = beat.cs()
running = True
mouse_pos = (0, 0)
print(beat.bg)
bg = pg.image.load(beat.bg).convert()
bg_pos = [0, 0]
window_size = window.get_rect().size
window_aspect = window_size[0]/window_size[1]
bg_size = bg.get_rect().size
bg_aspect = bg_size[0]/bg_size[1]
print(window_aspect)
if bg_aspect>window_aspect:
    ration = window_size[1]/bg_size[1]
    bg = pg.transform.scale(bg, (int(ration*bg_size[0]), int(ration*bg_size[1])))
    padding = ((ration*bg_size[0])-window_size[0])/2
    bg_pos[0] = int(-padding)
else:
    ration = window_size[0]/bg_size[0]
    bg = pg.transform.scale(bg, (int(ration*bg_size[0]), int(ration*bg_size[1])))
    padding = ((ration*bg_size[1])-window_size[1])/2
    bg_pos[1] = int(-padding)
print(bg.get_rect().size)
bg.fill((128, 128, 128), special_flags=pg.BLEND_RGB_MULT)
def done():
    global running
    running = False
frame = 0
root.protocol("WM_DELETE_WINDOW", done)
while running:
    frame = frame + 1
    clock.tick(60)
    window.blit(bg, bg_pos)
    click = False
    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        mills += 100/6
    if keys[pg.K_LEFT]:
        mills -= 100/6
    [hitobject.draw(beat, mills, window) for hitobject in hitobjects if -beat.objar()[1]-1500<hitobject.t[0]-mills<beat.objar()[0]]
    pg.display.update()
    root.update_idletasks()
    root.update()
root.destroy()
pg.quit()
