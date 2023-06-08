import cv2
import numpy as np
import pyautogui

class ImageFinder:
    def __init__(self, threshold=0.8):
        self.threshold = threshold

    def find_and_click_image(self, target_image_path, screenshot, win, y_offset):
        screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        target_image = cv2.imread(target_image_path)
        result = cv2.matchTemplate(screenshot_cv, target_image, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= self.threshold)

        if len(loc[0]) > 0:
            print(f"Found {len(loc[0])} matches for {target_image_path} in screenshot.")
            
            for pt in zip(*loc[::-1]):
                print(f"Top-left corner of match: {pt}")
                cv2.rectangle(screenshot_cv, pt, (pt[0] + target_image.shape[1], pt[1] + target_image.shape[0]), (0,0,255), 2)
                center_x = pt[0] + target_image.shape[1] // 2 + win.left
                center_y = pt[1] + target_image.shape[0] // 2 + win.top
                pyautogui.click(center_x, center_y+y_offset)
                break  # stop after the first match
            return True  # Image found and clicked
        else:
            print(f"No matches for {target_image_path} found in screenshot.")
            return False  # Image not found
