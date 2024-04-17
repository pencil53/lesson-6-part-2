import cv2
import os
import PIL
from PIL import Image

#pillow = image processing library

path = "images"
meanwidth = 0
meanheight = 0
files = os.listdir(path)
print(files)
num_of_images = len(files)
print(num_of_images)

for file in files:
    image = Image.open(os.path.join(path,file))
    width,height = image.size
    print(image.size)
    meanwidth = meanwidth + width
    meanheight = meanheight + height

meanwidth = meanwidth//num_of_images
meanheight = meanheight//num_of_images
print(meanheight)
print(meanwidth)

for file in files:
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        image = Image.open(os.path.join(path,file))
        imageresized = image.resize((meanwidth,meanheight), PIL.Image.Resampling.LANCZOS)
        imageresized.save(file, "JPEG", quality = 95)
        print("image resized")

def videogenerator():
    videoname = "MyFirstVideo.avi"
    images = []
    for img in os.listdir(path):
        if img.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            images.append(img)
    frame = cv2.imread(os.path.join(path,images[0]))
    height,width,layers = frame.shape
    video_writer = cv2.VideoWriter(videoname,0,1,(width,height))
    for img in images:
        video_writer.write(cv2.imread(os.path.join(path,img)))
    cv2.destroyAllWindows()
    video_writer.release()
videogenerator()