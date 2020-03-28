from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母
def randChar():
    return chr(random.randint(65, 90))

# 随机颜色
def randColor():
    return (random.randint(32, 127), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2
def randClolr2():
    return (random.randint(1,255), random.randint(0, 255), random.randint(0, 255))

width = 60 * 4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建font对象
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)

# 创建draw对象
draw = ImageDraw.Draw(image)

# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill = randColor())

# 输出文字
for t in range(4):
    draw.text((60 * t + 15, 10), randChar(), font=font, fill=randClolr2())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('verify_code.jpg', 'jpeg')
