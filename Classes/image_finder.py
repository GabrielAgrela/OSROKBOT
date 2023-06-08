import cv2
import numpy as np
import pyautogui

class ImageFinder:
    def __init__(self, threshold=0.65):
        self.threshold = threshold

    def _match_image(self, target_image_path, screenshot):
        screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        target_image = cv2.imread(target_image_path)

        scales = np.linspace(0.8, 2.0, 20)[::-1]

        best_scale = None
        best_loc = None
        best_max_val = -1

        for scale in scales:
            resized_img = cv2.resize(target_image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
            
            if resized_img.shape[0] > screenshot_cv.shape[0] or resized_img.shape[1] > screenshot_cv.shape[1]:
                continue
            
            result = cv2.matchTemplate(screenshot_cv, resized_img, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)
            
            if max_val > best_max_val:
                best_scale = scale
                best_loc = max_loc
                best_max_val = max_val

        return best_scale, best_loc, best_max_val, target_image, screenshot_cv

    def find_image(self, target_image_path, screenshot, win, y_offset):
        best_scale, best_loc, best_max_val, target_image, screenshot_cv = self._match_image(target_image_path, screenshot)

        if best_max_val >= self.threshold:
            print(f"Found a match for {target_image_path} in screenshot at scale {best_scale} with confidence {best_max_val}.")
            pt = best_loc
            w, h = (target_image.shape[1] * best_scale, target_image.shape[0] * best_scale)
            cv2.rectangle(screenshot_cv, pt, (int(pt[0] + w), int(pt[1] + h)), (0,0,255), 2)
            return True
        else:
            print(f"No matches for {target_image_path} found in screenshot.")
            return False

    def find_and_click_image(self, target_image_path, screenshot, win, y_offset):
        best_scale, best_loc, best_max_val, target_image, screenshot_cv = self._match_image(target_image_path, screenshot)

        if best_max_val >= self.threshold:
            print(f"Found a match for {target_image_path} in screenshot at scale {best_scale} with confidence {best_max_val}.")
            pt = best_loc
            w, h = (target_image.shape[1] * best_scale, target_image.shape[0] * best_scale)
            cv2.rectangle(screenshot_cv, pt, (int(pt[0] + w), int(pt[1] + h)), (0,0,255), 2)
            center_x = int(pt[0] + w // 2 + win.left)
            center_y = int(pt[1] + h // 2 + win.top)
            pyautogui.click(center_x, center_y+y_offset)
            return True
        else:
            print(f"No matches for {target_image_path} found in screenshot.")
            return False
