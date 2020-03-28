from PIL import Image
im = Image.open('1.png')

w, h = im.size

print('image size: %sx%s' % (w, h))

im.thumbnail((w//2, h//2))

print('Resize image to: %sx%s' % (w//2, h//2))

im.save('2.jpg', 'jpeg')