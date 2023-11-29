import pytesseract
from PIL import Image

def recognize_text(image_path):
    # Open the image
    image = Image.open(image_path)

    # Perform text recognition
    text = pytesseract.image_to_string(image)

    return text

# Example of usage
image_path = 'path/to/your/image.jpg'
recognized_text = recognize_text(image_path)

print("Recognized text:")
print(recognized_text)