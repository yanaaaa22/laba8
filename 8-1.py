from PIL import Image
image = Image.open('1.jpg')
box = (50, 50, 950, 950)
crop_img = image.crop(box)
crop_img.save('new_1.jpg')