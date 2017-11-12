# -*- coding:utf-8 -*-

from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random

_letter_cases = "abcdefghijklmnopqrstuvwxyz"  # 小写字母，去除可能干扰的i，l，o，z
_upper_cases = _letter_cases.upper()  # 大写字母
_numbers = ''.join(map(str, range(1, 10)))  # 数字
init_chars = ''.join((_upper_cases, _numbers))


def strRandom(chars=init_chars, length=4):
    c_chars = random.sample(chars, length)
    return ''.join(c_chars)


def colorRandom1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机长生颜色2


def colorRandom2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 136
height = 40
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建font对象
font = ImageFont.truetype('Arial.ttf', 36)

# 创建draw对象
draw = ImageDraw.Draw(image)
rcol1 = colorRandom1()
rcol2 = colorRandom2()
# 填充每一个颜色
for x in range(width):
    for y in range(height):
        if x % 12 > 5 and x % 12 < 7 and y % 7 > 2 and y % 10 < 5:
            pass
        else:
            draw.point((x, y), fill=rcol1)

# 输出文字
strs = strRandom()
for t in range(4):
    a = random.randint(25, 30)
    draw.text((a * t + 10, 0), strs[t],
              font=font, fill=colorRandom2())
print strs
image.save('./image/' + strs + '.jpg', 'jpeg')
