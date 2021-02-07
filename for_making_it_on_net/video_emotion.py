# import cv2

# cam = cv2.VideoCapture(0)

# cv2.namedWindow("test")

# img_counter = 0

# while True:
#     ret, frame = cam.read()
#     if not ret:
#         print("failed to grab frame")
#         break
#     cv2.imshow("test", frame)

#     k = cv2.waitKey(1)
#     if k%256 == 27:
#         # ESC pressed
#         print("Escape hit, closing...")
#         break
#     elif k%256 == 32:
#         # SPACE pressed
#         img_name = "opencv_frame_{}.png".format(img_counter)
#         cv2.imwrite(img_name, frame)
#         print("{} written!".format(img_name))
#         img_counter += 1

# cam.release()

# cv2.destroyAllWindows()




#------------------------------------------------------------------------------------------------------------



# import pygame.camera
# import pygame.image
# import sys

# pygame.camera.init()

# cameras = pygame.camera.list_cameras()

# print "Using camera %s ..." % cameras[0]

# webcam = pygame.camera.Camera(cameras[0])

# webcam.start()

# # grab first frame
# img = webcam.get_image()

# WIDTH = img.get_width()
# HEIGHT = img.get_height()

# screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
# pygame.display.set_caption("pyGame Camera View")

# while True :
#     for e in pygame.event.get() :
#         if e.type == pygame.QUIT :
#             sys.exit()



#     # draw frame
#     screen.blit(img, (0,0))
#     pygame.display.flip()
#     # grab next frame    
#     img = webcam.get_image()



#------------------------------------------------------------------------------------------------------------




# import cv2
# from fer import FER

# #Storing the key pressed by user 
# cam = cv2.VideoCapture(0)



# while(True):
#     #Check if user hits ‘c’ or ‘g’ key
#     print("Enter a key")
#     k = cv2.waitKey(1)
#     print("key entered")
#     if( k == ord('c') ):

#         ret, frame = cam.read()
#         detector = FER()
#         try:
#             print(detector.top_emotion(frame))
#         except:
#             print("Cannot process frame :(")


#     if( k == ord('g') ):
#         cv2.imwrite('gray.jpg', gray_img )
#         print("Image saved in grayscale")
        
# cv2.destroyAllWindows()        





#-----------------------------------------------------------------------------------------------------

# For checking value of the pressed keys

# import cv2
# img = cv2.imread('E://Projects//Pygame experiment//images_without_bg//ball.png') # load a dummy image
# while(1):
#     cv2.imshow('ball image',img)
#     k = cv2.waitKey(33)
#     if k==27:    # Esc key to stop
#         break
#     elif k==-1:  # normally -1 returned,so don't print it
#         continue
#     else:
#         print(k) # else print its value


#--------------------------------------------------Golden Code------------------------------------------------------------





# import cv2
# from fer import FER
# from pygame.locals import *
# import pygame
# import time





# #Just for deciding ball rect and making it move up n down:
# def for_ball_rect(h, flag, rect):
#     if flag == 0:
#         h=h+1
#         rect = ballrect.move((1080,h)) #550- lower limit,  
#         if h==height:
#             flag = 1
#     elif flag == 1:
#         h=h-1
#         rect = ballrect.move((1080,h)) #550- lower limit,
#         if h == width:
#             flag = 0

#     return[h, flag, rect]




# if __name__ == "__main__":

#     pygame.init()
#     #Storing the key pressed by user 
#     cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#     width=59
#     height=451
#     pygame.display.set_caption("Hope")
#     ball = pygame.image.load("E://Projects//Pygame experiment//images_without_bg//ball.png")
#     ball = pygame.transform.scale(ball, (200,200))
#     screen = pygame.display.set_mode((640,480), flags = pygame.RESIZABLE)
#     ballrect = ball.get_rect()
#     screen.fill(pygame.Color('white'))
#     h=60         
#     flag=0
#     white = pygame.Color(255,255,255)


#     capture=True
#     print("Loop start")
#     detector = FER()

#     while capture:
#         try:
#             ret, frame = cam.read()
#             # print("2")
#             print(detector.top_emotion(frame))
#             print("Done :)")
#             # capture = False
#             h, flag, rect = for_ball_rect(h,flag, ballrect)
#             ball = pygame.transform.rotate(ball, 90)

#             screen.blit(ball,ballrect)
#             pygame.display.update()
#             # time.sleep(5)
#         except:
#             print("Cannot process frame :(")
        


#     print("Loop end")        
#     cv2.destroyAllWindows()        


#-----------------------------------------------------Done(just run it) --------------------------------------------------------------------

# import cv2
# from fer import FER
# from pygame.locals import *
# import pygame 
# import time





# #Just for deciding ball rect and making it move up n down:
# def for_ball_rect(h, flag, rect):
#     if flag == 0:
#         h=h+1
#         rect = ballrect.move((1080,h)) #550- lower limit,  
#         if h==height:
#             flag = 1
#     elif flag == 1:
#         h=h-1
#         rect = ballrect.move((1080,h)) #550- lower limit,
#         if h == width:
#             flag = 0

#     return[h, flag, rect]




# if __name__ == "__main__":

#     pygame.init()
#     #Storing the key pressed by user 
#     cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#     width=59
#     height=451
#     pygame.display.set_caption("Hope")
#     img_directory = "E://Projects//Pygame experiment//images_without_bg//"

#     ball = pygame.image.load(img_directory + "ball.png")
#     happy_girl = pygame.image.load(img_directory + "happy_girl.png")
#     concerned_girl = pygame.image.load(img_directory + "concerned_girl.png")

#     ball = pygame.transform.scale(ball, (200,200))
#     screen = pygame.display.set_mode((1386,600), flags = pygame.RESIZABLE)
#     ballrect = ball.get_rect()
#     screen.fill(pygame.Color('white'))
#     h=60         
#     flag=0
#     white = pygame.Color(255,255,255)


#     capture=True
#     print("Loop start")
#     detector = FER()

#     while capture:
#         try:
#             ret, frame = cam.read()
#             # print("2")
#             print(detector.top_emotion(frame))
#             emotion = detector.top_emotion(frame)[0]
#             print("Done :)")
#             # capture = False
#             if emotion == 'happy':
#                 screen.fill(white)
#                 screen.blit(happy_girl, happy_girl.get_rect())
#                 # time.sleep(3)
#                 # pygame.display.update()
#             elif emotion == 'neutral':
#                 screen.fill(white)
#                 screen.blit(concerned_girl, concerned_girl.get_rect())  
#                 # time.sleep(3)
#                 # pygame.display.update()
#             elif emotion == 'surprise':
#                 screen.fill(white)
#                 screen.blit(ball, ballrect)  
#                 # time.sleep(3)
#             # elif emotion == 'happy':
#             #     screen.blit(happy_girl, happy_girl.get_rect())
#             # elif emotion == 'happy':
#             #     screen.blit(happy_girl, happy_girl.get_rect())
#             # elif emotion == 'happy':
#             #     screen.blit(happy_girl, happy_girl.get_rect())  

#             pygame.display.update()
#             # time.sleep(5)
#         except:
#             print("Cannot process frame :(")
        


#     print("Loop end")        
#     cv2.destroyAllWindows()        



#------------------------------------------------------------------------------------------------------------------------





# Link for full body images: (https://www.google.com/search?q=full%20body%20anime%20girl%20without%20face&tbm=isch&tbs=rimg:CfhJGGMPuztsYeZT3wf285Xu&hl=en-US&sa=X&ved=0CCIQuIIBahcKEwjA_eDm7JHuAhUAAAAAHQAAAAAQDA&biw=1349&bih=625)




import cv2
from fer import FER
from pygame.locals import *
import pygame 
import time





if __name__ == "__main__":

    pygame.init()
    #Storing the key pressed by user 
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    width=59
    height=451
    pygame.display.set_caption("Hope")
    img_directory = "E://Projects//Pygame experiment//images_without_bg//"

    ball = pygame.image.load(img_directory + "ball.png")
    concerned_girl = pygame.image.load(img_directory + "concerned_girl.png")
    happy_girl = pygame.image.load(img_directory + "happy_girl.png")

    happy_girl = pygame.transform.scale(happy_girl, (concerned_girl.get_width(), concerned_girl.get_height()))

    ball = pygame.transform.scale(ball, (200,200))
    screen = pygame.display.set_mode((0,0), flags = pygame.FULLSCREEN)
    ballrect = ball.get_rect()
    screen.fill(pygame.Color('white'))
    kybrd104 = [(1114.28,350),(1164.28,350),(1164.28,400),(1114.28,400),(1114.28,350)]
    white = pygame.Color(255,255,255)
    blue = pygame.Color(0,0,128)
    print("*******")
    print(happy_girl.get_size())
    print(concerned_girl.get_size())
    
    print("*******")
    
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

    while capture:
        try:
            ret, frame = cam.read()
            # print("2")
            print(detector.detect_emotions(frame))
            # print(detector.top_emotion(frame))
            emotion = detector.top_emotion(frame)[0]
            print("Done :)")
            # capture = False
            screen.fill(white)

            # pygame.draw.lines(screen, blue, False, [(300,200),(300,270)], 1)
            pygame.draw.lines(screen, blue, False, [(100,500),(900,500)], 5)
            pygame.draw.lines(screen, blue, False, [(100,550),(900,550)], 5)
            
            if emotion == 'happy':
                list = ["Hello Luv,", "How are you doing?"]
                # pos_x = happy_girl.get_rect().center[0]
                # pos_y = happy_girl.get_rect().center[1]

                y=0
                for i in list:
                    textsurface = myfont.render(i, False, (0, 0, 0))
                    screen.blit(textsurface,(pos_x + 300,pos_y+y))
                    y+=25
                
                tr = textsurface.get_rect()
                pygame.draw.ellipse(screen, blue,[550,110,650,230], 5)

                screen.blit(happy_girl, happy_girl.get_rect())
            elif emotion == 'neutral':
                screen.blit(concerned_girl, concerned_girl.get_rect())  
            elif emotion == 'surprise':
                screen.blit(ball, ballrect) 

            # elif emotion == 'happy':
            #     screen.blit(happy_girl, happy_girl.get_rect())
            # elif emotion == 'happy':
            #     screen.blit(happy_girl, happy_girl.get_rect())
            # elif emotion == 'happy':
            #     screen.blit(happy_girl, happy_girl.get_rect())  

            pygame.display.update()
            # time.sleep(5)
        except:
            print("Cannot process frame :(")

        # event = event in pygame.event.get()
        for event in pygame.event.get():
            if event.type == QUIT :
                capture = False

            elif event.type == KEYDOWN and event.key == K_q:
                capture = False            
            


            


    print("Loop end")        
    cv2.destroyAllWindows()        

































































# if __name__ == '__main__':
#     pg.init()
#     main()
#     pg.quit()