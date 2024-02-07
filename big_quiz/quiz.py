import pgzrun
import random

WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40) 
timer_box.move_ip(990, 40) 
answer_box1.move_ip(50, 358) 
answer_box2.move_ip(735, 358) 
answer_box3.move_ip(50, 538) 
answer_box4.move_ip(735, 538)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10

q1 = ["What is the capital of Greece?","London","Rome","Barcelona","Athens",4]
q2 = ["Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", 3]
q3 = ["Who wrote 'To Kill a Mockingbird'?", "Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway", 3]
q4 = ["What is the chemical symbol for water?", "H", "O", "He", "W", 3]
q5 = ["What is the tallest mammal on Earth?", "Elephant", "Giraffe", "Kangaroo", "Lion", 3]
questions = [q1, q2, q3, q4, q5 ]
#get first question
question = questions.pop(0)


def draw():
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.textbox(question[0], main_box, color=("black"))
    
    screen.draw.filled_rect(timer_box, "sky blue")
    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    index = 1
    
    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")
        screen.draw.textbox(question[index], box, color=("black"))
        # no need to declare question as global because its only accessed but not modified 
        index = index + 1
        
def game_over():
    global question, time_left
    message = "Game Over. You got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

def correct_answer():
    global score, question, time_left
    score += 1
    
    if questions:
        # get next question
        question = questions.pop(0)
        time_left = 10
    else:
        print("End of questions.")
        game_over()

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print("Correct!")
                correct_answer()
            else:
                game_over()
        index += 1

def update_time_left():
    global time_left
    
    if time_left:
        time_left = time_left - 1
    else:
        game_over()
        
clock.schedule_interval(update_time_left, 1.0)

pgzrun.go()