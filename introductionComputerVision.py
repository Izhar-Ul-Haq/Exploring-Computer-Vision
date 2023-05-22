from PIL import Image
with Image.open("duckTheNature.jpg") as im:
    angle45 = im.rotate(45)
    angle90 = im.rotate(90)
    angle180 = im.rotate(180)
    angle360 = im.rotate(360)
    angle45.show()
    angle90.show()
    angle180.show()
    angle360.show()
    im.show()