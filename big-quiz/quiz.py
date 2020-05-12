WIDTH = 1280
HEIGHT = 720

# interface
main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

# move_ip() moves each rectangle to the place you want it on the screen
main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10

q1 = ['What is the capital of France?',
      'London', 'Paris', 'Berlin', 'Tokyo', 2]
q2 = ["What is 5+7?",
      "12", "10", "14", "8", 1]
q3 = ["What is the seventh month of the year?",
      "April", "May", "June", "July", 4]
q4 = ["Which planet is closest to the Sun?",
      "Saturn", "Neptune", "Mercury", "Venus", 3]
q5 = ["Where are the pyramids?",
      "India", "Egypt", "Morocco", "Canada", 2]


def draw():
    screen.fill('dim gray')
    screen.draw.filled_rect(main_box, 'sky blue')
    screen.draw.filled_rect(timer_box, 'sky blue')

    for box in answer_boxes:
        screen.draw.filled_rect(box, 'orange')


def game_over():
    pass


def correct_answer():
    pass


def on_mouse_down(pos):
    pass


def update_time_left():
    pass
