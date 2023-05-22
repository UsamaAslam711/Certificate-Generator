from PIL import Image, ImageDraw, ImageFont
import os

# Open the PNG image file
image = Image.open('image/Participation.png')

# Create a drawing object
draw = ImageDraw.Draw(image)

# Define the font and size for the text
font = ImageFont.truetype('GreatVibes-Regular.ttf', 400)

