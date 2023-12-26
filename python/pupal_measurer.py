from turtle import circle
import cv2
import csv
import numpy as np
import numpy as np


def main_video(csv_file_path, video_file_path):
    cap = cv2.VideoCapture(video_file_path)
    csv_file = open(csv_file_path, "w")
    csv_writer = csv.writer(csv_file)
    counter = 0
    list_of_radiuses = []
    while True:
        counter += 1
        ret, frame = cap.read()
        print(ret, frame)

        # Check if the frame was successfully captured
        if not ret:
            break
        circles = detect_iris(frame)
        if circles.any() is not None and not circles.any() == -1:
            for c in circles:  
                list_of_radiuses.append(c)
        elif circles == -1: print("more than one circle detected or no circle detected. Please try again.")
        else: print("No circle detected. Please try again.")
        if len(list_of_radiuses) == 5:
            radius = np.mean(list_of_radiuses)
            # csv_writer.writerow([counter, radius])
            print(radius)
        # Check if the user wants to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        output = draw_circles(circles, frame)
        cv2.imshow('frame', output)


    cv2.destroyAllWindows()
    cap.release()
    csv_file.close()
    
def main_photo(image_path):
    image = cv2.imread(image_path)

    circles = detect_iris(image)
    # Display the image
    # cv2.imshow('image', image)
    if circles.any() !=None and not circles.any() == -1:
        print("good")
    elif circle == -1: print("more than one circle detected or no circle detected. Please try again.")
    else: print("No circle detected. Please try again.")

    output = draw_circles(circles, image)

    cv2.imshow("image with iris detected", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_iris(frame):
    if frame is None:
        print("Error: Frame is empty")
        return None

    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray', grayscale_image)
    processed_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
    # cv2.imshow('processed', processed_image)
    _, thresholded_image = cv2.threshold(grayscale_image, 33, 255, cv2.THRESH_BINARY)
    # cv2.imshow('thresholded', thresholded_image)

    min_radius = 100
    max_radius = 250
    param1 = 1000
    param2 = 10

    circles = cv2.HoughCircles(
        thresholded_image,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=20,
        param1=param1,
        param2=param2,
        minRadius=min_radius,
        maxRadius=max_radius
    )

    if circles is not None:
        if len(circles) > 1:
            return -1  # -1 means that there are many circles
        elif len(circles) == 1:
            return circles[0][2]
    else:
        return None

def draw_circles(circles, frame):
    if circles is not None:
        if circles.ndim == 2:  # 2D array
            circles = np.uint16(np.around(circles))
            for circle in circles:
                center = (int(circle[0]), int(circle[1]))  # Convert to integers
                radius = int(circle[2])  # Convert to an integer
                # Draw the circle
                cv2.circle(frame, center, radius, (0, 255, 0), 1)
        elif circles.ndim == 1:  # 1D array
            center = (int(circles[0]), int(circles[1]))  # Convert to integers
            radius = int(circles[2])  # Convert to an integer
            # Draw the circle
            cv2.circle(frame, center, radius, (0, 255, 0), 1)
    return frame

main_video(csv_file_path= 'data_avg.csv', video_file_path= 'data/1.mp4')
# main_photo(image_path= 'test_image.png')