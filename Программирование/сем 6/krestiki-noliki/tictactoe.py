import pyglet
from pyglet.window import mouse
window = pyglet.window.Window(width = 470, height = 550)

#batch = pyglet.graphics.Batch()

cross_img = pyglet.image.load('Artboard 3 copy 6-min.png')
circle_img = pyglet.image.load('Artboard 3 copy 10-min.png')
background_img = pyglet.image.load('background.png')
background_sprite = pyglet.sprite.Sprite(background_img, x=0, y=0,)
circle_texture = circle_img.get_texture()
cross_texture = cross_img.get_texture()
cross_texture.width = 140
cross_texture.height = 140
circle_texture.width = 140
circle_texture.height = 140
background_sprite.scale = 0.5
label = pyglet.text.Label('Крестики-нолики', font_name='Roboto-mono',
                          font_size=20,
                          x=window.width//2, y=window.height - 30,
                          anchor_x='center', anchor_y='top')

label_start = pyglet.text.Label('Играть!', font_name='Roboto-mono',
                          font_size=25,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
label_cross_win = pyglet.text.Label('Крестики выиграли! Начать заново.', font_name='Roboto-mono',
                          font_size=20,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
label_circle_win = pyglet.text.Label('Нолики выиграли! Начать заново.', font_name='Roboto-mono',
                          font_size=20,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
label_draw = pyglet.text.Label('Ничья! Начать заново.', font_name='Roboto-mono',
                          font_size=20,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

class game:
    def __init__(self):
        self.a = [[0]*3,[0]*3,[0]*3]
        self.turn = True
        self.start = True
        self.restart = False
        self.victory = 0

    def click(self,x,y):
        if self.turn == True:
            self.a[x][y] = 1
        else:
            self.a[x][y] = 2
        self.turn = not self.turn


mygame = game()


def victory(i):
    mygame.victory = i
    mygame.restart = True


def check():
    for x in range(3):
        for y in range(3):
            if mygame.a[x][y] == 1:
                cross_texture.blit(x*155+10, y*155+10)
            elif mygame.a[x][y] == 2:
                circle_texture.blit(x*155+10, y*155+10)
    for x in range(3):
        if mygame.a[x][0] == mygame.a[x][1] and mygame.a[x][0] == mygame.a[x][2] and mygame.a[x][0] != 0:
            victory(mygame.a[x][0])
            return 0
        if mygame.a[0][x] == mygame.a[1][x] and mygame.a[0][x] == mygame.a[2][x] and mygame.a[0][x] != 0:
            victory(mygame.a[0][x])
            return 0
    if mygame.a[0][0] == mygame.a[1][1] and mygame.a[0][0] == mygame.a[2][2] and mygame.a[0][0] != 0:
        victory(mygame.a[0][0])
        return 0
    if mygame.a[2][0] == mygame.a[1][1] and mygame.a[1][1] == mygame.a[0][2] and mygame.a[1][1] != 0:
        victory(mygame.a[1][1])
        return 0
    for x in range(3):
        for y in range(3):
            if mygame.a[x][y] == 0:
                return 0
    victory(0)


@window.event
def on_draw():
    window.clear()
    pyglet.gl.glClearColor(0.5,0,0,1)
    label.draw()
    background_sprite.draw()
    check()
    if mygame.start == True:
        window.clear()
        label_start.draw()
        return 0
    elif mygame.restart == True:
        mygame.a = [[0] * 3, [0] * 3, [0] * 3]
        if mygame.victory == 0:
            window.clear()
            label_draw.draw()
        elif mygame.victory == 1:
            window.clear()
            label_cross_win.draw()
            anim_cross_win.draw()
        elif mygame.victory == 2:
            window.clear()
            label_circle_win.draw()
            anim_circle_win.draw()
        return 0


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        if mygame.start == True:
            mygame.start = False
            return 0
        elif mygame.restart == True:
            mygame.restart = False
            return 0
        else:
            x = int(x//155)
            y = int(y//155)
            print ("%d , %d" % (x, y))
            if mygame.a[x][y] == 0:
                mygame.click(x,y)
            print (mygame.a)

song = pyglet.media.load('music.mp3')
song.play()

image_frames = ('Xwin/1.png',
                'Xwin/2.png',
                'Xwin/3.png',
                'Xwin/4.png',
                'Xwin/5.png',
                'Xwin/6.png',
                'Xwin/7.png')

images = map(lambda img: pyglet.image.load(img), image_frames)
animation = pyglet.image.Animation.from_image_sequence(images, 0.33)

anim_cross_win = pyglet.sprite.Sprite(animation)

image_frames = ('0win/1.png',
                '0win/2.png',
                '0win/3.png',
                '0win/4.png',
                '0win/5.png',
                '0win/6.png',
                '0win/7.png',
                '0win/8.png')

images = map(lambda img: pyglet.image.load(img), image_frames)
animation = pyglet.image.Animation.from_image_sequence(images, 0.33)

anim_circle_win = pyglet.sprite.Sprite(animation)

pyglet.app.run()