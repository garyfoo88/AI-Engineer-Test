import cv2
import cvlib as cv


# function to convert the coordinates to columns and rows
def coordinates(n):
    return n // 100


def face_predictor(image_path):
    image = cv2.imread(image_path)
    faces, confidences = cv.detect_face(image)
    face_tiles = []
    # loop through the detected faces
    for face in faces:
        result = map(coordinates, face)
        # result will have an output of [y1, x1, y2, x2]
        # append the 2nd and 3rd element of result giving us [row, column]
        face_tiles.append(list(result)[1:3])

    return face_tiles
