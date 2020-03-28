from PIL import Image, ImageFilter

im = Image.open('2.jpg')

# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)


im2.save('blur.jpg', 'jpeg')
