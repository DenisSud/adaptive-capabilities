import cv2
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# def main_video(video_file_path):

def main_video(video_file_path):
    cap = cv2.VideoCapture(video_file_path)

    counter = 0
    data = {}

    while True:
        counter += 1
        ret, frame = cap.read()
        # Check if the frame was successfully captured

        if not ret:
            break

        radius = measure(frame)
        if counter <= 10:
            data[counter] = radius
        else:
            if (data[counter]) / data[counter - 1] > 2:
                data[counter] = data[counter - 1]
            else:
                data[counter] = radius

    cap.release()
    
    return data

def main_photo(image_path):
    image = cv2.imread(image_path)
    radius = measure(image)
    print(radius)
    cv2.waitKey(0)

def measure(frame):
    if frame is None:
        print("Error: Frame is empty")
        return None
    area = -1
    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray', grayscale_image)
    processed_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
    # cv2.imshow('processed', processed_image)
    _, thresholded_image = cv2.threshold(grayscale_image, 33, 255, cv2.THRESH_BINARY)
    # cv2.imshow('thresholded', thresholded_image)
    area = cv2.countNonZero(thresholded_image)
    radius = np.sqrt(area / np.pi)
    return radius


def save_data(list_of_areas):
    data = {}
    for i, area in enumerate(list_of_areas):
        data[i] = area
    return data

def plot_data(data):
    sns.lineplot(data=data)
    plt.show()

if __name__ == "__main__":
    video_file_path = "1.mp4"
    print("prossing video:", video_file_path)
    data = main_video(video_file_path)
    print("done")
    plot_data(data)
