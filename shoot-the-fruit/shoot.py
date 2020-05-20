from random import randint

apple = Actor("apple")
kiwi = Actor("kiwi")
score = 0


def draw():
    screen.clear()
    apple.draw()
    kiwi.draw()


def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)


def place_kiwi():
    kiwi.x = randint(10, 800)
    kiwi.y = randint(10, 600)


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print('Good shot!')
        score + 1
        place_apple()
    elif kiwi.collidepoint(pos):
        print('Good shot!')
        score + 1
        place_kiwi()
    else:
        print('You missed!')
        quit()


place_apple()
