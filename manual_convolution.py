from PIL import Image
im = Image.open('jcook.jpg')
print(im.format, im.size, im.mode)
im.show()