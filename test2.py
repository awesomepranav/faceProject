import io
import os
#def detect_faces(path):
    #"""Detects faces in an image."""
from google.cloud import vision
from google.cloud.vision import types
    
client = vision.ImageAnnotatorClient()
# The name of the image file to annotate
file_name = os.path.join('.','Surprised.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

print('file opened')
image = vision.types.Image(content=content)
response = client.face_detection(image=image)
faces = response.face_annotations
# Names of likelihood from google.cloud.vision.enum
likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                    'LIKELY', 'VERY_LIKELY')
print('Faces:')
for face in faces:
    print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
    print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
    print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in face.bounding_poly.vertices])

    print('face bounds: {}'.format(','.join(vertices)))

