import cv2
import numpy as np
import pyautogui

class ImageFinder:
    def __init__(self, threshold=0.75):
        self.threshold = threshold
        self.template_resolution = (1086, 637)  # original resolution at which the template was taken

    def _get_scaling_factor(self, screenshot):
        screen_resolution = (screenshot.shape[1], screenshot.shape[0])  # (width, height)
        scaling_factor = (screen_resolution[0] / self.template_resolution[0], screen_resolution[1] / self.template_resolution[1])  # (scale_x, scale_y)
        return scaling_factor

    def _match_image(self, target_image_path, screenshot):
        screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        target_image = cv2.imread(target_image_path)

        scaling_factor = self._get_scaling_factor(screenshot_cv)
        resized_img = cv2.resize(target_image, None, fx=scaling_factor[0], fy=scaling_factor[1], interpolation=cv2.INTER_AREA)

        result = cv2.matchTemplate(screenshot_cv, resized_img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
            
        return scaling_factor, max_loc, max_val, target_image, screenshot_cv

    def find_and_click_image(self, target_image_path, screenshot, win, y_offset):
        best_scale, best_loc, best_max_val, target_image, screenshot_cv = self._match_image(target_image_path, screenshot)

        if best_max_val >= self.threshold:
            print(f"Found a match for {target_image_path} in screenshot at scale {best_scale} with confidence {best_max_val}.")
            pt = best_loc
            w, h = (target_image.shape[1] * best_scale[0], target_image.shape[0] * best_scale[1])
            cv2.rectangle(screenshot_cv, pt, (int(pt[0] + w), int(pt[1] + h)), (0,0,255), 2)
            center_x = int(pt[0] + w // 2 + win.left)
            center_y = int(pt[1] + h // 2 + win.top)
            pyautogui.click(center_x, center_y+y_offset)
            return True
        else:
            print(f"No matches for {target_image_path} found in screenshot.")
            return False
        
    def find_image(self, target_image_path, screenshot, win, y_offset):
        best_scale, best_loc, best_max_val, target_image, screenshot_cv = self._match_image(target_image_path, screenshot)

        if best_max_val >= self.threshold:
            print(f"Found a match for {target_image_path} in screenshot at scale {best_scale} with confidence {best_max_val}.")
            pt = best_loc
            w, h = (target_image.shape[1] * best_scale[0], target_image.shape[0] * best_scale[1])
            return True
        else:
            print(f"No matches for {target_image_path} found in screenshot.")
            return False
