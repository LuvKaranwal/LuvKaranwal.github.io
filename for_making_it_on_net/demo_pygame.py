import pygame
from pygame.locals import *
from pygame import mixer
import time 
import cv2
from pygame import camera
from fer import FER
import matplotlib.pyplot as plt         
import numpy as np


def quit_handler():
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT or (
            event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit() 
            quit()
            # The pygame.quit() function will uninitialize all pygame modules, 
            # and the Python quit() function will exit the program.



#Just for deciding ball rect and making it move up n down:
def for_ball_rect(h, flag, rect):
    if flag == 0:
        h=h+1
        rect = ballrect.move((1080,h)) #550- lower limit,  
        if h==height:
            flag = 1
    elif flag == 1:
        h=h-1
        rect = ballrect.move((1080,h)) #550- lower limit,
        if h == width:
            flag = 0

    return[h, flag, rect]

#Live feeding of images(Video Proctoring)
def camstream(camera):
    camera.init()
    DEVICE = 0
    SIZE = (640, 480)
    FILENAME = 'capture.png'
    display = pygame.display.set_mode(SIZE, 0)
    camera = pygame.camera.Camera(DEVICE, SIZE)
    camera.start()
    screen = pygame.surface.Surface(SIZE, 0, display)
    capture = True
    while capture:
        # photo = camera.get_image(screen)
        display.blit(screen, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                capture = False
            elif event.type == KEYDOWN and event.key == K_s:
                photo = camera.get_image(screen)
                pygame.image.save(photo, "E://Projects//Pygame experiment//images_without_bg//img.jpg")
                img = plt.imread("E://Projects//Pygame experiment//images_without_bg//img.jpg")
                
                detector = FER()

                print("Started processing..")
                try:
                    print(detector.top_emotion(img))
                    print("Ended Processing result :)")
                except:
                    print("Couldn't generate emotion analysis :(")                    
                # plt.imshow(img)    

                # image = pygame.image.save(screen, FILENAME)
                # pygame.image.save(photo, "E://Projects//Pygame experiment//images_without_bg//img.jpg")
                # img = plt.imread("E://Projects//Pygame experiment//images_without_bg//img.jpg")
                # detector = FER(mtcnn=True)
                # print(detector.detect_emotions("E://Projects//Pygame experiment//images_without_bg//img.jpg"))
                # plt.imshow(img)
                
    camera.stop()
    # pygame.quit()
    return


def video():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.isOpened()

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0,  (640,480))

    while(True):
        ret, frame = cap.read()

        if ret == True:
            # frame = cv2.flip(frame, 0)
            # out.write(frame)
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


            detector = FER()
            print(detector.top_emotion(frame))



            # cv2.imshow('frame', frame)

            
            if 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":

    f = pygame.init()
    print(f) # 6 Successful setups with 0 failure.
    width=59
    height=451

    color = (120,120,100)
    speed = [4,4]
    pygame.display.set_caption('Hope')
    img_directory= "E://Projects//Pygame experiment//images_without_bg//"
    ball = pygame.image.load(img_directory + "ball.png" )
    # ball = pygame.image.load(img_directory + "balll.gif" )
    ball = pygame.transform.scale(ball, (200,200))
    # ball = pygame.transform.flip(ball, True, True) # Use the (True, False) parameters for adjusting the mirror image or vertical/Horizontal flip of the image.
            
    ballrect = ball.get_rect()
    print(ball.get_size())    
    # Play Music
    # mixer.init()

    # mixer.music.load("Jason_Derulo_-_Mamacita_talkglitz.tv.mp3")
    # mixer.music.set_volume(0.7)     # Setting the volume 
    # mixer.music.play()    # Start playing the song 

        
    h=60         
    flag=0
    white = pygame.Color(255,255,255)
    blue = pygame.Color(0,0,128)
  

    camstream(camera)
    # video()
    screen = pygame.display.set_mode( (0,0), flags = pygame.FULLSCREEN )
    # Take and save a image.
    # camera.init()
    # cam = pygame.camera.Camera(0,(640,480))
    # cam.start()
    # image = cam.get_image()
    # pygame.image.save(image, "E:/Projects/Pygame experiment/images_without_bg/img.png")
    # cam.stop()
  
  
    while True:

        screen.fill(pygame.Color("black"))

        h, flag, rect = for_ball_rect(h,flag, ballrect)
        ball = pygame.transform.rotate(ball, 90)
        time.sleep(0.001)
        screen.blit(ball, rect)
        pygame.draw.line(screen, white, (100, height+190), (1600, height+190), 2)
        pygame.display.update()
        quit_handler()

        