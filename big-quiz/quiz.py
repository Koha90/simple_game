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
answer_box3.move_ip(50, 358)
answer_box4.move_ip(735, 358)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]


def game_over():
    pass


def correct_answer():
    pass


def on_mouse_down(pos):
    pass


def update_time_left():
    pass
