#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 Q群6089740
# CreateDate: 2021-2-10
# douyin or dingding or wechat: pythontesting

#Import required Image library
from PIL import Image, ImageDraw, ImageFont

#Create an Image Object from an Image
im = Image.open('/home/andrew/Pictures/boy.png')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "support qq group 6089740"

font = ImageFont.truetype('freefont/FreeSans.ttf', 15)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin -10
y = height - textheight - margin -10

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
draw.text((x, 0), text, font=font)
draw.text((10, 0), text, font=font)
draw.text((10, y), text, font=font)
im.show()

#Save watermarked image
im.save('/home/andrew/Pictures/watermark.png')