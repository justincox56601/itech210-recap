'''
This is going to be a small flash card game used to review for an upcoming test
I will create a set of flashcards, and then students will be rquired to 
create their own set of flash cards and use this game as a study tool.
'''
import pygame
import random
from questions import questions


#setup
pygame.init()
WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ITECH 210 RECAP")
clock = pygame.time.Clock()
dt = 0

#Font Set UP
LARGE_FONT = pygame.font.SysFont("arial", 40)
MEDIUM_FONT = pygame.font.SysFont("arial", 30)
SMALL_FONT = pygame.font.SysFont("arial", 20)

#Color Set Up
DARK_GREY = "#171717"
MEDIUM_GREY = "#444444"
LIGHT_GREY = "#EDEDED"
GREEN = "#08CB00"

#game settings
score = 0
question_index = 0
mouse_pos =None
clicked = False

#load music
pygame.mixer.music.load("bg_music.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.025)
click_sound = pygame.mixer.Sound("click.wav")
click_sound.set_volume(0.5)
correct_sound = pygame.mixer.Sound("correct.wav")
correct_sound.set_volume(0.25)

#shuffle questions
random.shuffle(questions)

#question label
num_questions = len(questions)
question_num = MEDIUM_FONT.render(f"Question {question_index+1} / {num_questions}", True, LIGHT_GREY)
question_num_rect = question_num.get_rect(topleft=(10,10))

#score label
score_text = MEDIUM_FONT.render(f"Score {score} / {num_questions}", True, LIGHT_GREY)
score_rect = score_text.get_rect(topright=(WIDTH-10,10))

#question text
question_text = MEDIUM_FONT.render(questions[question_index].get('question'), True, LIGHT_GREY)
question_rect = question_text.get_rect(center=(WIDTH/2, HEIGHT/2))

#answers
answers = []
for index, answer in enumerate(questions[question_index].get('options')):
    text = SMALL_FONT.render(answer, True, LIGHT_GREY)
    rect = text.get_rect(midleft=(WIDTH*0.1, HEIGHT/2 + (index + 1) * 30))
    answers.append([text,rect])


def update_font_color():
    for index, answer in enumerate(answers):
        if mouse_pos == None:
            continue

        if answer[1].collidepoint(mouse_pos):
            answer[0] = SMALL_FONT.render(questions[question_index].get('options')[index], True, GREEN)
        else:
            answer[0] = SMALL_FONT.render(questions[question_index].get('options')[index], True, LIGHT_GREY)

def check_answer():
    for index, answer in enumerate(answers):
        if mouse_pos == None:
            continue

        if answer[1].collidepoint(mouse_pos):
            answer = questions[question_index].get('answer')
            if answer == index:
                correct_sound.play(maxtime=500)
                correct_sound.fadeout(500)
                update_score()
    
    update_question()

def update_score():
    global score
    global score_text
    global score_rect

    score += 1
    score_text = MEDIUM_FONT.render(f"Score {score} / {num_questions}", True, LIGHT_GREY)
    score_rect = score_text.get_rect(topright=(WIDTH-10,10))         

def update_question():
    global questions
    global question_index
    global question_num
    global question_text
    global question_rect
    global answers
    global score

    #update question
    question_index += 1

    if(question_index >= len(questions)):
        question_text = MEDIUM_FONT.render(f"You got {score} out of {len(questions)} questions correct!", True, LIGHT_GREY)
        question_rect = question_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        answers = []
    else:
        question_num = MEDIUM_FONT.render(f"Question {question_index+1} / {num_questions}", True, LIGHT_GREY)
        question_text = MEDIUM_FONT.render(questions[question_index].get('question'), True, LIGHT_GREY)
        question_rect = question_text.get_rect(center=(WIDTH/2, HEIGHT/2))

        #update answers
        answers = []
        for index, answer in enumerate(questions[question_index].get('options')):
            text = SMALL_FONT.render(answer, True, LIGHT_GREY)
            rect = text.get_rect(midleft=(WIDTH*0.1, HEIGHT/2 + (index + 1) * 30))
            answers.append([text,rect])


#main loop
running = True
while running:
    #check for pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos 

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_sound.play()
            check_answer()
        
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        


    screen.fill(DARK_GREY)
    
    #highlight answer text if mouse is hovering over it
    update_font_color()
    

    #draw
    screen.blit(question_num, question_num_rect)
    screen.blit(score_text, score_rect)
    screen.blit(question_text, question_rect)
    #draw answers
    for answer in answers:
        screen.blit(answer[0], answer[1])



    pygame.display.flip()
    dt = clock.tick(60)/1000


pygame.quit()