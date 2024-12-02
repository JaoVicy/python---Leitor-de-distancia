import cv2
import numpy as np

def calculate_distance(know_width, focal_length, perceived_width):

    return (know_width * focal_length / perceived_width)

def find_object(frame):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea, default=None)

    if largest_contour is not None:
        x, y, w, h = cv2.boundingRect(largest_contour)
        return (x, y, w, h)
    return None