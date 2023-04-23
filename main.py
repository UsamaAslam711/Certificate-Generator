from PIL import Image, ImageDraw, ImageFont

# Open the PNG image file
image = Image.open('image/Participation.png')

# Create a drawing object
draw = ImageDraw.Draw(image)

# Define the font and size for the text
font = ImageFont.truetype('GreatVibes-Regular.ttf', 400)

# Define the text to write on the image
text = input('Enter the name: ')

# Calculate the size of the text
text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]

# Calculate the position of the text
x = (image.width - text_width) / 2
y = 2300

# Define the color of the text
text_color = (26, 53, 95)

# Write the text on the image
draw.text((x, y), text, font=font, fill=text_color)

# Save the modified image as a new PNG file
image.save('image_with_name.png')
