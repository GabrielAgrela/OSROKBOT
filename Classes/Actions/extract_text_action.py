from Actions.action import Action
import pytesseract
import time
from PIL import Image, ImageFilter, ImageEnhance,ImageOps
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"D:\eu\apps\tess\tesseract.exe"  # Windows



# You can now use the preprocessed image in your existing code

class ExtractTextAction(Action):
    def __init__(self, image_path="test.png", skip_check_first_time=False, description="", aggregate=False):
        super().__init__(skip_check_first_time)
        self.image_path = image_path
        self.description = description
        self.aggregate = aggregate

    def preprocess_image(self, image_path):
        # Open the image file
        img = Image.open(image_path)

        img = img.convert('L')

  

        #if description has "title" in it, then we need to crop the image
        if "Question" in self.description:
            img = img.point(lambda x: 0 if x < 140 else 255, '1')
        else:
            img = img.point(lambda x: 0 if x < 200 else 255, '1')
            # reverse colors
            img = ImageOps.invert(img)
        

        
        img.save("testprocessed.png")
        return img

    def execute(self):
        try:
            if not self.aggregate:
                with open('string.txt', 'w') as f:
                    f.write("")
                
            img = self.preprocess_image(self.image_path)
            text = pytesseract.image_to_string(img,lang='eng', config='--oem 1')
            text = self.description + text
            print("OCR : ", text) 
            with open('string.txt', 'a') as f:
                f.write(text)
            return True
        except Exception as e:
            print(f"Failed to extract text from image: {e}")
            return False