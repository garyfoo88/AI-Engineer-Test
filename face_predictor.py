import cv2
import cvlib as cv


def coordinates(n):
    return n // 100


def face_predictor(image_path):
    image = cv2.imread(image_path)
    faces, confidences = cv.detect_face(image)
    face_tiles = []
    for face in faces:
        result = map(coordinates, face)
        face_tiles.append(list(result)[1:3])

    return face_tiles
