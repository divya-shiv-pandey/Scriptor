import cv2
MIN_CONTOUR_AREA = 10   
img = cv2.imread("image_name.jpg")     
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
blured = cv2.blur(gray, (5,5), 0)    
img_thresh = cv2.adaptiveThreshold(blured, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 10))
threshed = cv2.morphologyEx(img_thresh, cv2.MORPH_CLOSE, rect_kernel)
Contours, Hierarchy = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for contour in Contours:
    if cv2.contourArea(contour) > MIN_CONTOUR_AREA:
        [X, Y, W, H] = cv2.boundingRect(contour)
        #cv2.rectangle(img, (X, Y), (X + W, Y + H), (0,0,255), 2)

        sub_face = img[Y:Y+H, X:X+W]
        gray = cv2.cvtColor(sub_face, cv2.COLOR_BGR2GRAY)
        face_file_name = "output/img_" + str(Y) + ".jpg"
        cv2.imwrite(face_file_name, gray)
cv2.imshow('contour', img)
