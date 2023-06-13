from Actions.action import Action
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"D:\eu\apps\tess\tesseract.exe"  # Windows

class ExtractTextAction(Action):
    def __init__(self, image_path, skip_check_first_time=False):
        super().__init__(skip_check_first_time)
        self.image_path = image_path

    def execute(self):
        try:
            img = Image.open(self.image_path)
            text = pytesseract.image_to_string(img)
            print("sdas ",text) 
            return False
        except Exception as e:
            print(f"Failed to extract text from image: {e}")
            return False
