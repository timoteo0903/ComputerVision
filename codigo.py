import cv2
cap = cv2.VideoCapture(f'video_cV.mp4')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

backSub = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
while(1):
    ret, frame = cap.read()        
    fgMask = backSub.apply(frame)
        
    cv2.imshow('original',frame)    
    cv2.imshow('foregroundMask',fgMask)