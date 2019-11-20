import cv2
import cvlib as cv
import requests
import json
from urllib.request import urlopen
from PIL import Image


# function to convert the coordinates to columns and rows
def coordinates(n):
    return n // 100


def face_predictor(token):
    # get url from 'url_image'
    web_url = 'https://hackattic.com/challenges/basic_face_detection/problem?access_token='
    get_problem = requests.get(web_url + token).json()
    image_url = get_problem['image_url']
    # save the image to PNG
    img = Image.open(urlopen(image_url))
    img.save('image.png', 'PNG')
    # read the image
    image = cv2.imread('image.png')
    faces, confidences = cv.detect_face(image)
    face_tiles = []
    # loop through the detected faces
    for face in faces:
        result = map(coordinates, face)
        # result will have an output of [y1, x1, y2, x2]
        # append the 2nd and 3rd element of result giving us [row, column]
        face_tiles.append(list(result)[1:3])

    return face_tiles
    # tried converting to JSON structure using 'json.dumps(face_tiles).json()' but failed =(

