import cv2
from imutils import face_utils
import numpy as np
import imutils
import dlib
import math

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:\Users\homer\image\shape_predictor_68_face_landmarks.dat")
while True:
    ret, frame = cap.read()
    #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    frame = imutils.resize(frame, width=1000)
    size = frame.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    rects = detector(gray, 0)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #cv2.circle(frame, (x,y), 3, (0,255,0), 2)
        #for (x,y) in shape:
        #    cv2.circle(frame, (x,y), 1, (0,0,255), 2)
    
        #2D image points. If you change the image, you need to change vector
        image_points = np.array([
                                    (shape[30][0], shape[30][1]),     # Nose tip
                                    (shape[8][0], shape[8][1]),       # Chin
                                    (shape[45][0], shape[45][1]),     # Left eye left corner
                                    (shape[36][0], shape[36][1]),     # Right eye right corner
                                    (shape[54][0], shape[54][1]),     # Left Mouth corner
                                    (shape[48][0], shape[48][1])      # Right mouth corner
                                ], dtype="double")
 
        # 3D model points.
        model_points = np.array([
                                    (0.0, 0.0, 0.0),             # Nose tip
                                    (0.0, -330.0, -65.0),        # Chin
                                    (-225.0, 170.0, -135.0),     # Left eye left corner
                                    (225.0, 170.0, -135.0),      # Right eye right corner
                                    (-150.0, -150.0, -125.0),    # Left Mouth corner
                                    (150.0, -150.0, -125.0)      # Right mouth corner
                                 ])
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

        focal_length = size[1]
        center = (size[1]/2, size[0]/2)
        camera_matrix = np.array(
                                    [[focal_length, 0, center[0]],
                                    [0, focal_length, center[1]],
                                    [0, 0, 1]], dtype = "double"
                                )
        print ("Camera Matrix :")
        print (np.matrix(camera_matrix))
 
        dist_coeffs = np.zeros((4,1)) # Assuming no lens distortion
        (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix, dist_coeffs, flags=cv2.cv2.SOLVEPNP_ITERATIVE)
 
        print ("Rotation Vector:")
        print (np.matrix(rotation_vector))
        print ("Translation Vector:")
        print (np.matrix(translation_vector))

        angle=math.fabs(rotation_vector[1]*57.3)
        cv2.putText(frame, str("ANGLE: %.1f")%angle, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Project a 3D point (0, 0, 1000.0) onto the image plane.
        # We use this to draw a line sticking out of the nose
        (nose_end_point2D, jacobian) = cv2.projectPoints(np.array([(0.0, 0.0, 300.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)
 
        for p in image_points:
            cv2.circle(frame, (int(p[0]), int(p[1])), 3, (0,0,255), -1)
 
        p1 = ( int(image_points[0][0]), int(image_points[0][1]))
        p2 = ( int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))
        cv2.line(frame, p1, p2, (255,0,0), 2)

    cv2.namedWindow("Video")
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
