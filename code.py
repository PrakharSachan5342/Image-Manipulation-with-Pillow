from PIL import Image, ImageFilter

# Open an image file
image = Image.open('image.jpg')

# Convert the image to grayscale
grayscale_image = image.convert('L')

# Apply a blur filter to the image
blurred_image = image.filter(ImageFilter.BLUR)

# Save the modified images
grayscale_image.save('grayscale_image.jpg')
blurred_image.save('blurred_image.jpg')
