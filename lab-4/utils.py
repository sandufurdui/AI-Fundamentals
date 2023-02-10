import cv2
import numpy as np
import matplotlib.pyplot as plt 


def blur_image(image_path, ksize=(10, 10)): 
    image = cv2.imread(image_path)

    # Using cv2.blur() method
    blurred_image = cv2.blur(image, ksize)
    # Plot both images using subplots
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[0].set_title('Original image')
    axs[1].imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
    axs[1].set_title('Blurred image')
    plt.show()
    
# https://www.geeksforgeeks.org/python-opencv-cv2-blur-method/



def sharpen_image(image_path): 
    image = cv2.imread(image_path)

    sharpen_filter = np.array([[-1,-1,-1],
                              [-1,9,-1],
                              [-1,-1,-1]])
    
    #apply the filter to the original photo
    sharp_image = cv2.filter2D(image, -1, sharpen_filter)
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[0].set_title('Original image')
    axs[1].imshow(cv2.cvtColor(sharp_image, cv2.COLOR_BGR2RGB))
    axs[1].set_title('Blurred image')
    plt.show()
# https://www.codespeedy.com/how-to-sharpen-an-image-in-python-using-opencv/


# https://www.geeksforgeeks.org/face-detection-using-cascade-classifier-using-opencv-python/



def detect_face(image_path):
    cascade_path='haarcascade_frontalface_default.xml' 
    face_cascade = cv2.CascadeClassifier(cascade_path)
     
    image = cv2.imread(image_path)
    
    #convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    #if faces are detected, return the face coordinates
    if len(faces) > 0:
        return faces.tolist()
    else:
        return None

def is_gray(imgpath):
    img = cv2.imread(imgpath)
    if len(img.shape) < 3: return True
    if img.shape[2]  == 1: return True
    b,g,r = img[:,:,0], img[:,:,1], img[:,:,2]
    if (b==g).all() and (b==r).all(): return True
    return False

# https://stackoverflow.com/questions/23660929/how-to-check-whether-a-jpeg-image-is-color-or-gray-scale-using-only-python-stdli

def detect_eyes(imgpath):
    cascade_path='haarcascade_eye.xml'
    eyes_cascade = cv2.CascadeClassifier(cascade_path)
    image = cv2.imread(imgpath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eyes = eyes_cascade.detectMultiScale(gray, 1.1, 4)

    if len(eyes) >= 2:
        return abs(eyes[0][1] - eyes[1][1]) <= 5
    return False
# https://itsourcecode.com/free-projects/opencv/eye-detection-opencv-python-with-source-code/

def has_one_face(image_path):
    cascade_path='haarcascade_frontalface_default.xml' 
    face_cascade = cv2.CascadeClassifier(cascade_path)
     
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 1:
        return True
    else:
        return False

def calculate_face_area(image_path):
    cascade_path='haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    total_image_area = image.shape[0] * image.shape[1]
    for (x, y, w, h) in faces:
        face_area = w * h
        if face_area >= 0.2 * total_image_area and face_area <= 0.5 * total_image_area:
            return True
    return False

def calculate_result(img_path):
  if calculate_face_area(img_path) and has_one_face(img_path) and detect_eyes(img_path) and not is_gray(img_path):
    return True
  else:
    return False


blur_image("test_images/0AA0A2.jpg")
sharpen_image("test_images/0AA0A2.jpg")