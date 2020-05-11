from random import randint


WIDTH = 400
HEIGHT = 400
score = 0
# to tell Pygame Zero if the game over or not
game_over = False

# add Actors in the game
fox = Actor('fox')
fox.pos = 100, 100

coin = Actor('coin')
coin.pos = 200, 200

def draw():
    # set background color
    screen.fill('green')
    # draw fox and coin on the screen
    fox.draw()
    coin.draw()
    # This line will display the score in the top-left corner of the screen
    screen.draw.text('Score: ' + str(score), color='black', topleft=(10, 10))

    # Ending the game. Show the final Score
    if game_over:
        screen.fill('pink')
        screen.draw.text('Final Score: ' + str(score), topleft=(10, 10), fontsize=60)

# Set random place of coin
def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (WIDTH - 20))

# If time has left - GAME OVER!!!
def time_up():
    global game_over
    game_over = True

# It MOVING!!!
def update():
    global score

    if keyboard.left:
        fox.x = fox.x - 2
    elif keyboard.right:
        fox.x = fox.x + 2
    elif keyboard.up:
        fox.y = fox.y - 2
    elif keyboard.down:
        fox.y = fox.y + 2

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 10
        place_coin()

clock.schedule(time_up, 7.0)
place_coin()