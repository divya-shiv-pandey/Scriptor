# Import the Images module from pillow
from PIL import Image
  
# Open the image by specifying the image path.
image_path = "inputimg.jpeg"
image_file = Image.open(image_path)
  
# the default
image_file.save("image_name.jpg", quality=95)
  
# Changing the image resolution using quality parameter
# Example-1
image_file.save("image_name2.jpg", quality=25)
  
# Example-2
image_file.save("image_name3.jpg", quality=1)
