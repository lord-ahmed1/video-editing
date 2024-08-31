import cv2 as cv
import numpy as np
from random import randint
terminate=0
text_color=int(input('apply text color ?'))
use_board_color=int(input('apply board color ?'))
use_border=int(input("apply border ?"))

#colours to use  border alone 255,240,31   writing 100,100,0   use 187,255,255

video=cv.VideoCapture('Test.mp4')

width=int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height=int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
rate=int(video.get(cv.CAP_PROP_FPS))
print(f'width {width} height {height} rate {rate}')

fourcc=cv.VideoWriter_fourcc(*'MJPG')
out=cv.VideoWriter('output.mp4',fourcc,rate,(width,height))

hl,sl,vl,hu,su,vu=36,0,146,131,255,255

# i=10
kernel=np.array((10,10),np.uint8)

while terminate==0:
    upper=np.array([hu,su,vu])
    lower=np.array([hl,sl,vl])
    _,frame=video.read()
    
    if _:
        #######                               text color 
        neon=np.zeros(frame.shape,np.uint8)
        if text_color:
            neon[:,:]=187,255,255

        
        border_color=np.zeros(frame.shape,np.uint8)
        if use_border :
            border_color[:,:]=255,240,31
        hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)


        mask=cv.inRange(hsv,lower,upper)


        ###########                          isolate board
        if use_board_color:
            board=cv.inRange(hsv,np.array([34,0,0]),np.array([86,255,255]))
            board=cv.bitwise_not(board)
            frame=cv.bitwise_and(frame,frame,mask=board)
            board=cv.bitwise_not(board)
            

            board_color=np.zeros(frame.shape,np.uint8)
            board_color[:,:]=0,0,0
            board=cv.bitwise_and(board_color,board_color,mask=board)
            frame=cv.add(frame,board)
    
        
                                      ####       apply mask
        mask=cv.dilate(mask,kernel,iterations=6)
        mask=cv.erode(mask,kernel,iterations=3)
        mask=cv.blur(mask,(3,3))
        
        border=cv.Canny(mask,100,255)
        border=cv.GaussianBlur(border,(3,3),3)
        border=cv.bitwise_and(border_color,border_color,mask=border)



        mask=cv.bitwise_and(neon,neon,mask=mask)
        show=cv.add(mask,frame)
        show=cv.add(show,border)
        out.write(show)




        cv.imshow("video",frame)
        cv.imshow("video2",show)
    else:
        terminate=1



    key=cv.waitKey(1)

    if key!=-1:
        cv.imwrite('image.png',border)
    if key==27:
        terminate=1  


    # if key==ord('1'):
    #     hl=hl+1
    #     print(hl,'h1')
    # if key==ord('2'):
    #     sl=sl+1
    #     print(sl)
    # if key==ord('3'):
    #     vl=vl+1
    #     print(vl)
    # if key==ord('4'):
    #     hu=hu+1
    #     print(hu)
    # if key==ord('5'):
    #     su=su+1
    #     print(su)
    # if key==ord('6'):
    #     vu=vu+1
    #     print(vu)



    # if key==ord('7'):
    #     hl=hl-1
    #     print(hl,'h1')
    # if key==ord('8'):
    #     sl=sl-1
    #     print(sl)
    # if key==ord('9'):
    #     vl=vl-1
    #     print(vl)
    # if key==ord('0'):
    #     hu=hu-1
    #     print(hu)
    # if key==ord('-'):
    #     su=su-1
    #     print(su)
    # if key==ord('='):
    #     vu=vu-1
    #     print(vu)
#print(f'bl {hl}  gl {sl}  rl {vl}  bu {hu}  gu {su}  vu  {vu}')  
video.release()
cv.destroyAllWindows()
out.release()
print('done')
# img=cv.imread('image.png')
# cropped_img=img
# blur=cv.blur(cropped_img,(1,1))
# hl,sl,vl,hu,su,vu=1,1,8,190,135,115
# kernel=np.array((10,10),np.uint8)
# neon=np.zeros(cropped_img.shape,np.uint8)
# neon[:,:]=57,255,20
# while terminate==0:

#     upper=np.array([hu,su,vu])
#     lower=np.array([hl,sl,vl])
#     hsv=cv.cvtColor(blur,cv.COLOR_BGR2HSV)
#     mask=cv.inRange(hsv,lower,upper)
#     mask=cv.bitwise_not(mask)
#     mask=cv.dilate(mask,kernel,iterations=6)
#     mask=cv.erode(mask,kernel,iterations=3)
#     mask=cv.bitwise_and(neon,neon,mask=mask)
#     show=cv.add(mask,cropped_img)


#     cv.imshow("video",img)
#     cv.imshow("video2",show)



#     key=cv.waitKey(1)

#     if key==27:
#         terminate=1  

#     if key==ord('1'):
#         hl=hl+1
#         print(hl,'h1')
#     if key==ord('2'):
#         sl=sl+1
#         print(sl)
#     if key==ord('3'):
#         vl=vl+1
#         print(vl)
#     if key==ord('4'):
#         hu=hu+1
#         print(hu)
#     if key==ord('5'):
#         su=su+1
#         print(su)
#     if key==ord('6'):
#         vu=vu+1
#         print(vu)
# print(f'bl {hl}  gl {sl}  rl {vl}  bu {hu}  gu {su}  vu  {vu}')

# #bl 1  gl -4  rl 8  bu 96  gu 135  vu  110