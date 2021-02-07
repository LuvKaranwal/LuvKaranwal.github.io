import cv2
from fer import FER
from pygame.locals import *
import pygame 
import time
from pygame import mixer


def image_display(emo) :
    screen.blit(emotions[emo], emotions_rect[emo])
    Emotion = emo[0].upper()+emo[1:]
    textsurface = myfont.render(Emotion, False, (0, 0, 0))
    screen.blit(textsurface,(pos_x + 20,pos_y))
    pygame.draw.ellipse(screen, blue,[300,110,400,230], 5)


if __name__ == "__main__":

    pygame.init()
    #Storing the key pressed by user 
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    width=59
    height=451
    pygame.display.set_caption("Hope")
    img_directory = "E://Projects//Pygame experiment//for_making_it_on_net//images_with_bg//face expressions//merge//new_set3//"

    happy = pygame.image.load(img_directory + "Happy.png")
    angry = pygame.image.load(img_directory + "angry.png")
    neutral = pygame.image.load(img_directory + "neutral.png")
    sad = pygame.image.load(img_directory + "sad.png")            
    surprise = pygame.image.load(img_directory + "surprise.png")
    disgust = pygame.image.load(img_directory + "disgust.png")
    fear = pygame.image.load(img_directory + "fear.png")  
    


    # mixer.init()

    # mixer.music.load("Jason_Derulo_-_Mamacita_talkglitz.tv.mp3")
    # mixer.music.set_volume(0.7)     # Setting the volume 
    # mixer.music.play()    # Start playing the song 


    emotions = {'happy': happy, 'angry': angry, 'neutral': neutral, 'sad': sad, 'surprise': surprise, 'disgust': disgust, 'fear': fear}
    
    for key in emotions:
        emotions[key] = pygame.transform.scale(emotions[key], (480,800))

    emotions_rect = {}

    for key in emotions:
        emotions_rect[key] = emotions[key].get_rect().move(750,20)


    screen = pygame.display.set_mode((0,0), flags = pygame.FULLSCREEN)
    screen.fill(pygame.Color('white'))
    # kybrd104 = [(1114.28,350),(1164.28,350),(1164.28,400),(1114.28,400),(1114.28,350)]
    white = pygame.Color(255,255,255)
    blue = pygame.Color(0,0,128)
    bg_color = pygame.Color(222, 239, 232)    
    # For text beside images
    pygame.font.init() # you have to call this at the start, 
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    
    h=60         
    flag=0

    # Variable for deciding placement of text in images
    pos_x , pos_y = (450, 184) 
    capture=True
    print("Loop start")
    detector = FER()
    counter=0
    while capture:
        counter += 1
        print(counter)
        pygame.time.Clock().tick(10)
        try:
            ret, frame = cam.read()
            print(detector.detect_emotions(frame))
            # print(detector.top_emotion(frame))
            emotion = detector.top_emotion(frame)[0]
            print("Done :)")
            screen.fill(bg_color)
            
            if emotion == 'happy':
                # For image
                image_display(emotion)

            elif emotion == 'neutral':
                # For image
                image_display(emotion)                

            elif emotion == 'sad':
                # For image
                image_display(emotion)

            elif emotion == 'angry':
                # For image
                image_display(emotion)

            elif emotion == 'surprise':
                # For image
                image_display(emotion)

            elif emotion == 'fear':
                # For image
                image_display(emotion)

            elif emotion == 'disgust':
                # For image
                image_display(emotion)                


            pygame.display.update()

        except:
            screen.fill(bg_color)
            textsurface = myfont.render('No Clue', False, (0, 0, 0))
            screen.blit(textsurface,(pos_x + 20,pos_y))
            pygame.draw.ellipse(screen, blue,[300,110,400,230], 5)
                

            pygame.display.update()
            print("Cannot process frame :(")
            screen.fill(bg_color)

        for event in pygame.event.get():
            if event.type == QUIT :
                capture = False

            elif event.type == KEYDOWN and event.key == K_q:
                capture = False            
            


            


    print("Loop end")        
    
    cv2.destroyAllWindows()        
    