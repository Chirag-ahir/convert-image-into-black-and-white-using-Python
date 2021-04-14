------pip install pillow------

from PIL import Image
img=Image.open("colourful image.jpg")
blackAndWhite=img.convert("L")
blackAndWhite.save('bw_image.jpg')
blackAndWhite.show()
