from Actions.action import Action
import pytesseract
import time
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"D:\eu\apps\tess\tesseract.exe"  # Windows

class ExtractTextAction(Action):
    def __init__(self, image_path="test.png", skip_check_first_time=False, description="", aggregate=False):
        super().__init__(skip_check_first_time)
        self.image_path = image_path
        self.description = description
        self.aggregate = aggregate

    def execute(self):
        try:
            # If it's the first run or not aggregating, clear the file
            if not self.aggregate:
                with open('string.txt', 'w') as f:
                    f.write("")
                
            img = Image.open(self.image_path)
            text = pytesseract.image_to_string(img)
            # concatenate description and text
            text = self.description + text
            print("OCR : ", text) 
            with open('string.txt', 'a') as f:
                f.write(text)
            return True
        except Exception as e:
            print(f"Failed to extract text from image: {e}")
            return False
