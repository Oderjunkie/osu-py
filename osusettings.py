import pygame as pg
from tkinter import *
import os
import os.path
from os import path
import shutil
import math
def func(beatmap):
    print('Extracting '+os.getcwd()+'\\maps\\osz\\'+beatmap+' to '+os.getcwd()+'\\maps\\folds\\'+beatmap[0:-4]+'\\')
    os.rename(os.getcwd()+'\\maps\\osz\\'+beatmap, os.getcwd()+'\\maps\\osz\\'+beatmap[0:-4]+'.zip')
    res = shutil.unpack_archive(os.getcwd()+'\\maps\\osz\\'+beatmap[0:-4]+'.zip',os.getcwd()+'\\maps\\folds\\'+beatmap[0:-4]+'\\')
    os.rename(os.getcwd()+'\\maps\\osz\\'+beatmap[0:-4]+'.zip', os.getcwd()+'\\maps\\osz\\'+beatmap)
    return res
def extractbeatmaps():
    return [func(beatmap) for beatmap in os.listdir(os.getcwd()+'\\maps\\osz\\') if beatmap.endswith('.osz') and not path.exists(os.getcwd()+'\\maps\\folds\\'+beatmap[0:-4]+'\\')]
class SettingsMods:
    def __init__(self, complete=''):
        self.ez = False
        self.nf = False
        self.ht = False
        self.hr = False
        self.sd = False
        self.pf = False
        self.dt = False
        self.nc = False
        self.hd = False
        self.fi = False
        self.intmods = [complete[i*2:i*2+2:1] for i in range(int(len(complete)/2))]
        self.update()
    def update(self):
        self.ez = False
        self.nf = False
        self.ht = False
        self.hr = False
        self.sd = False

        self.pf = False
        self.dt = False
        self.nc = False
        self.hd = False
        self.fi = False
        for mod in self.intmods:
            if mod=='EZ': self.ez = True
            if mod=='NF': self.nf = True
            if mod=='HT': self.ht = True
            if mod=='HR': self.hr = True
            if mod=='SD': self.sd = True
            if mod=='PF': self.pf = True
            if mod=='DT': self.dt = True
            if mod=='NC': self.nc = True
            if mod=='HD': self.hd = True
            if mod=='FI': self.fi = True
            if mod=='FL': self.fl = True
    def __repr__(self):
        return self.mods
    @property
    def mods(self):
        return ' '.join(self.intmods)
class SettingsGeneral:
    def __init__(self, artist='', romartist='', title='', romtitle='',\
                 beatcreator='', diff='', source='', tags=''):
        self.artist = artist
        self.romartist = romartist
        self.title = title
        self.romtitle = romtitle
        self.beatcreator = beatcreator
        self.diff = diff
        self.source = source
        self.tagsinternal = tags.split(' ')
    @property
    def tags(self):
        return ' '.join(self.tagsinternal)
class SettingsDifficulty:
    def __init__(self, hp=0, cs=0, ar=0, od=0):
        self.hp = hp
        self.cs = cs
        self.ar = ar
        self.od = od
    def ar(self, mods):
        ar = self.ar
        if mods.ht and mods.ez:
            if   ar==0:  return 2400
            elif ar==1:  return 2320
            elif ar==2:  return 2240
            elif ar==3:  return 2160
            elif ar==4:  return 2080
            elif ar==5:  return 2000
            elif ar==6:  return 1920
            elif ar==7:  return 1840
            elif ar==8:  return 1760
            elif ar==9:  return 1680
            elif ar==10: return 1600
        elif mods.ht and mods.hr:
            if   ar==0:  return 2400
            elif ar==1:  return 2176
            elif ar==2:  return 1952
            elif ar==3:  return 1728
            elif ar==4:  return 1480
            elif ar==5:  return 1200
            elif ar==6:  return 920
            elif ar==7:  return 640
            else:        return 600
        elif mods.ht:
            if   ar==0:  return 2400
            elif ar==1:  return 2240
            elif ar==2:  return 1080
            elif ar==3:  return 1920
            elif ar==4:  return 1760
            elif ar==5:  return 1600
            elif ar==6:  return 1400
            elif ar==7:  return 1299
            elif ar==8:  return 1000
            elif ar==9:  return 800
            elif ar==10: return 600
        elif mods.dt and mods.ez:
            if   ar==0:  return 1200
            elif ar==1:  return 1160
            elif ar==2:  return 1120
            elif ar==3:  return 1080
            elif ar==4:  return 1040
            elif ar==5:  return 1000
            elif ar==6:  return 960
            elif ar==7:  return 920
            elif ar==8:  return 880
            elif ar==9:  return 840
            elif ar==10: return 800
        elif mods.dt and mods.hr:
            if   ar==0:  return 1200
            elif ar==1:  return 1088
            elif ar==2:  return 976
            elif ar==3:  return 864
            elif ar==4:  return 740
            elif ar==5:  return 600
            elif ar==6:  return 460
            elif ar==7:  return 320
            else:        return 300
        elif mods.dt:
            if   ar==0:  return 1200
            elif ar==1:  return 1120
            elif ar==2:  return 1040
            elif ar==3:  return 960
            elif ar==4:  return 880
            elif ar==5:  return 800
            elif ar==6:  return 700
            elif ar==7:  return 600
            elif ar==8:  return 500
            elif ar==9:  return 400
            elif ar==10: return 300
        elif mods.ez:
            if   ar==0:  return 1800
            elif ar==1:  return 1740
            elif ar==2:  return 1680
            elif ar==3:  return 1620
            elif ar==4:  return 1560
            elif ar==5:  return 1500
            elif ar==6:  return 1440
            elif ar==7:  return 1380
            elif ar==8:  return 1320
            elif ar==9:  return 1260
            elif ar==10: return 1200
        elif mods.hr:
            if   ar==0:  return 1800
            elif ar==1:  return 1632
            elif ar==2:  return 1464
            elif ar==3:  return 1296
            elif ar==4:  return 1110
            elif ar==5:  return 900
            elif ar==6:  return 690
            elif ar==7:  return 480
            else:        return 450
        else:
            if   ar==0:  return 1800
            elif ar==1:  return 1680
            elif ar==2:  return 1560
            elif ar==3:  return 1440
            elif ar==4:  return 1320
            elif ar==5:  return 1200
            elif ar==6:  return 1050
            elif ar==7:  return 900
            elif ar==8:  return 750
            elif ar==9:  return 600
            else:        return 450
    def points(self, mills, mods):
        settings = ''
        if mods.ez: settings += 'EZ'
        if mods.hr: settings += 'HR'
        if mods.ht: settings += 'HT'
        if mods.dt: settings += 'DT'
        OD_mills = {
            '': {
                300: [79.5,  73.5,  67.5,  61.5,  55.5,  49.5,  43.5,  37.5,  31.5,  25.5,  19.5 ],
                100: [139.5, 131.5, 123.5, 115.5, 107.5, 99.5,  91.5,  83.5,  75.5,  67.5,  59.5 ],
                50:  [199.5, 189.5, 179.5, 169.5, 159.5, 149.5, 139.5, 129.5, 119.5, 109.5, 99.5 ]
            },
            'DT': {
                300: [53.0,  49.0,  45.0,  41.0,  37.0,  33.0,  29.0,  25.0,  21.0,  17.0,  13.0 ],
                100: [93.0,  87.7,  82.3,  77.0,  71.7,  66.3,  61.0,  55.7,  50.3,  45.0,  39.7 ],
                50:  [133.0, 126.3, 119.7, 113.0, 106.3, 99.7,  93.0,  86.3,  79.7,  73.0,  66.3 ]
            },
            'HT': {
                300: [106.0, 98.0,  90.0,  82.0,  74.0,  66.0,  58.0,  50.0,  42.0,  34.0,  26.0 ],
                100: [186.0, 175.3, 164.7, 154.0, 143.3, 132.7, 122.0, 111.3, 100.7, 90.0,  79.3 ],
                50:  [266.0, 252.7, 239.3, 226.0, 212.7, 199.3, 186.0, 172.7, 159.3, 146.0, 132.7]
            },
            'HR': {
                300: [79.5,  70.5,  62.5,  53.5,  45.5,  37.5,  29.5,  20.5,  19.5,  19.5,  19.5 ],
                100: [139.5, 127.5, 116.5, 105.5, 94.5,  83.5,  71.5,  60.5,  59.5,  59.5,  59.5 ],
                50:  [199.5, 186.5, 171.5, 152.5, 143.5, 129.5, 115.5, 101.5, 99.5,  99.5,  99.5 ]
            },
            'HRDT': {
                300: [53.0,  47.0,  41.7,  36.7,  30.3,  25.0,  19.0,  13.7,  13.0,  13.0,  13.0 ],
                100: [93.0,  86.0,  77.7,  70.3,  63.0,  56.7,  47.7,  40.3,  39.7,  39.7,  39.7 ],
                50:  [133.0, 123.7, 114.3, 106.0, 96.7,  86.3,  77.0,  47.7,  66.3,  66.3,  66.3 ]
            },
            'HRHT': {
                300: [106.0, 94.0,  83.3,  71.3,  60,7,  50.0,  38.0,  27.3,  26.0,  26.0,  26.0 ],
                100: [186.0, 170.0, 156.3, 140.7, 126.0, 111.3, 95.3,  6-.7,  79.3,  79.3,  79.3 ],
                50:  [256.0, 247.3, 228.7, 210.0, 191.3, 172.7, 153.0, 136.3, 132.7, 132.7, 132.7]
            },
            'EZ': {
                300: [79.5,  76.5,  73.5,  70.5,  67.5,  64.5,  61.5,  58.5,  55.5,  52.5,  49.5 ],
                100: [139.5, 135.5, 131.5, 127.5, 123.5, 119.5, 115.5, 111.5, 107.5, 103.5, 99.5 ],
                50:  [199.5, 194.5, 189.5, 184.5, 179.5, 174.5, 169.5, 164.5, 159.5, 154.5, 149.5]
            },
            'EZDT': {
                300: [53.0,  51.0,  49.0,  47.0,  45.0,  43.0,  41.0,  39.0,  37.0,  35.0,  33.0 ],
                100: [93.0,  90.3,  87.7,  86.0,  82.3,  79.7,  77.0,  74.3,  71.7,  69.0,  66.3 ],
                50:  [133.0, 129.7, 126.3, 123.0, 119.7, 116.3, 113.0, 109.7, 106.3, 103.0, 99.7 ]
            },
            'EZHT': {
                300: [106.0, 102.0, 98.0,  94.0,  90.0,  86.0,  82.0,  78.0,  74.0,  70.0,  66.0 ],
                100: [186.0, 180.7, 175.3, 179.0, 164.7, 159.3, 154.0, 148.7, 143.3, 138.0, 132.7],
                50:  [266.0, 259.3, 252.7, 245.0, 239.3, 232.7, 226.0, 219.3, 212.7, 206.0, 199.3]
            }
        }
        current = OD_mills[settings]
        last = current[50][int(self.od)]
        if   mills<current[300][int(self.od)]:
            return (300,last)
        elif mills<current[100][int(self.od)]:
            return (100,last)
        elif mills<last:
            return (50,last)
        return (0,last)
    def getar(self, mods):
        ar = self.ar
        if mods.ez: ar /= 2
        if mods.hr:
            ar *= 1.4
            if ar>10: ar = 10
        return ar
    def cspix(self, mods):
        if mods.hr:
            return 109 - 2.7 * self.cs
        elif mods.ez:
            return 109 - 30 * self.cs
        return 109 - 9 * self.cs
    def objar(self, mods):
        ar = self.getar(mods)
        fade_in = 0
        preempt = 0
        if ar<5:
            preempt = 1200 + 600 * (5 - ar) / 5
            fade_in = 800  + 400 * (5 - ar) / 5
        elif ar>5:
            preempt = 1200 - 750 * (ar - 5) / 5
            fade_in = 800  - 500 * (ar - 5) / 5
        else:
            preempt = 1200
            fade_in = 800
        return ( ( preempt ), ( preempt-fade_in ) )
class SettingsColors:
    def __init__(self, combos=['#FF0000','#FFFF00','#00FF00','#0000FF'], bg='#AA55FF'):
        self.combos = combos
        self.bg = bg
    def __repr__(self):
        return ', '.join(self.combos)+f', bgcolor={self.bg}'
class SettingsImport:
    def __init__(self, filepath):
        self.generalint = []
        self.editorint = []
        self.metadataint = []
        self.difficultyint = []
        self.eventsint = []
        self.timingpointsint = []
        self.colorsint = []
        self.hitobjectsint = []
        self.general = {}
        self.editor = {}
        self.metadata = {}
        self.difficulty = {}
        self.events = []
        self.timingpoints = []
        self.colors = []
        self.hitobjects = []
        self.importb(filepath)
    def refresh(self):
        for pair in self.generalint:
            if pair[0]!='[' and pair[0:2]!='//':
                self.general[pair.split(': ')[0]]=pair.split(': ')[1]
        for pair in self.editorint:
            if pair[0]!='[' and pair[0:2]!='//':
                self.editor[pair.split(': ')[0]]=pair.split(': ')[1]
        for pair in self.metadataint:
            if pair[0]!='[' and pair[0:2]!='//':
                self.metadata[pair.split(':')[0]]=pair.split(':')[1]
        for pair in self.difficultyint:
            if pair[0]!='[' and pair[0:2]!='//':
                self.difficulty[pair.split(':')[0]]=pair.split(':')[1]
        for pair in self.eventsint:
            if pair[0]!='[' and pair[0:2]!='//':
                self.events.append(pair.split(','))
        for pair in self.timingpointsint:
            if pair[0]!='[' and pair[0:2]!='//':
                self.timingpoints.append(pair.split(','))
        for pair in self.hitobjectsint:
            if pair[0]!='[' and pair[0:2]!='//':
                self.hitobjects.append(pair.split(','))
        for pair in self.colorsint:
            if pair[0]!='[' and pair[0:2]!='//':
                self.colors.append([int(i) for i in pair.split(" : ")[1].split(",")])
    def importb(self, filepath):
        importing = ''
        with open(filepath, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line=='[General]':
                    importing='general'
                elif stripped_line=='[Editor]':
                    importing='editor'
                elif stripped_line=='[Metadata]':
                    importing='metadata'
                elif stripped_line=='[Difficulty]':
                    importing='difficulty'
                elif stripped_line=='[Events]':
                    importing='events'
                elif stripped_line=='[TimingPoints]':
                    importing='timingpoints'
                elif stripped_line=='[Colours]':
                    importing='colors'
                elif stripped_line=='[HitObjects]':
                    importing='hitobjects'
                if importing=='general' and stripped_line!='':
                    self.generalint.append(stripped_line)
                elif importing=='editor' and stripped_line!='':
                    self.editorint.append(stripped_line)
                elif importing=='metadata' and stripped_line!='':
                    self.metadataint.append(stripped_line)
                elif importing=='difficulty' and stripped_line!='':
                    self.difficultyint.append(stripped_line)
                elif importing=='events' and stripped_line!='':
                    self.eventsint.append(stripped_line)
                elif importing=='timingpoints' and stripped_line!='':
                    self.timingpointsint.append(stripped_line)
                elif importing=='colors' and stripped_line!='':
                    self.colorsint.append(stripped_line)
                elif importing=='hitobjects' and stripped_line!='':
                    self.hitobjectsint.append(stripped_line)
        if len(self.generalint)>1: self.generalint.pop(0)
        if len(self.editorint)>1: self.editorint.pop(0)
        if len(self.metadata)>1: self.metadata.pop(0)
        if len(self.difficultyint)>1: self.difficultyint.pop(0)
        if len(self.eventsint)>1: self.eventsint.pop(0)
        if len(self.timingpointsint)>1: self.timingpointsint.pop(0)
        if len(self.colorsint)>1: self.colorsint.pop(0)
        if len(self.hitobjectsint)>1: self.hitobjectsint.pop(0)
        self.refresh()
class SettingsComplete:
    def __init__(self, complete='', hp=0, cs=0, ar=0, od=0,\
                 combos=['#FF0000','#FFFF00','#00FF00','#0000FF'], bg='#AA55FF',\
                 artist='', romartist='', title='', romtitle='',\
                 beatcreator='', diff='', source='', tags=''):
        self.mods = SettingsMods(complete)
        self.general = SettingsGeneral(artist, romartist, title, romtitle, beatcreator, diff, source, tags)
        self.diff = SettingsDifficulty(int(hp), int(cs), int(ar), int(od))
        self.combos = SettingsColors(combos, bg)
class Settings:
    def __init__(self, file, mods):
        self.importing = SettingsImport(file)
        self.mods = mods
        self.data = None
        tmp = file.split('\\')
        tmp.pop()
        self.audio = '\\'.join(tmp)+'\\'+self.importing.general['AudioFilename']
        self.bg = '\\'.join(tmp)+'\\'+self.importing.events[0][2][1:-1]
        self.update()
    def update(self):
        if 'ArtistUnicode' not in self.importing.metadata:
            self.importing.metadata['ArtistUnicode'] = self.importing.metadata['Artist']
        if 'TitleUnicode' not in self.importing.metadata:
            self.importing.metadata['TitleUnicode'] = self.importing.metadata['Title']
        self.data = SettingsComplete(self.mods,\
            self.importing.difficulty['HPDrainRate'],\
            self.importing.difficulty['CircleSize'],\
            self.importing.difficulty['ApproachRate'],\
            self.importing.difficulty['OverallDifficulty'],\
            self.importing.colors,\
            '#AA55FF',\
            self.importing.metadata['ArtistUnicode'],\
            self.importing.metadata['Artist'],\
            self.importing.metadata['TitleUnicode'],\
            self.importing.metadata['Title'],\
            self.importing.metadata['Creator'],\
            self.importing.metadata['Version'],\
            self.importing.metadata['Source'],\
            self.importing.metadata['Tags']
        )
    def modsupdate(self):
        return self.data.mods.update()
    def ar(self):
        return self.data.diff.ar(self.data.mods)
    def points(self, mills):
        return self.data.diff.points(mills, self.data.mods)[0]
    def last(self):
        return self.data.diff.points(0, self.data.mods)[1]
    def getar(self):
        return self.data.diff.getar(self.data.mods)
    def cs(self):
        return self.data.diff.cspix(self.data.mods)
    def objar(self):
        return self.data.diff.objar(self.data.mods)
    def refresh(self):
        return self.importing.refresh()
    def importb(self, filepath):
        return self.importing.importb(filepath)
    @property
    def tags(self):
        return self.data.general.tags
    def hitobjects(self):
        return self.importing.hitobjects
