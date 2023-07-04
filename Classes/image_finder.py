import cv2
import numpy as np
import pyautogui
from termcolor import colored


class ImageFinder:
    def __init__(self, threshold=0.7):
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

        # find all matches above threshold
        locations = np.where(result >= self.threshold)
        matches = list(zip(*locations[::-1]))  # reverse x, y and make list of tuples
        
        # draw rectangles on all matched locations
        w, h = (resized_img.shape[1], resized_img.shape[0])
        for pt in matches:
            cv2.rectangle(screenshot_cv, pt, (int(pt[0] + w), int(pt[1] + h)), (255,0,255), 4)

        # save screenshot with rectangles
        cv2.imwrite("screenshot.png", screenshot_cv)
        # return the number of matches, screenshot with rectangles, and the highest matching value
        return scaling_factor, matches, len(matches), max(result.ravel()), target_image, screenshot_cv



    def find_and_click_image(self, target_image_path, screenshot, win, x_offset, y_offset, max_matches):
        
        best_scale, best_loc, num_matches, best_max_val, target_image, screenshot_cv = self._match_image(target_image_path, screenshot)
        
        if best_max_val >= self.threshold:
            # Store the current active window and mouse position
            prev_active_window = pyautogui.getActiveWindow()
            prev_mouse_x, prev_mouse_y = pyautogui.position()
            # Create an array of rectangles with format [[x1, y1, x2, y2], ...]
            rects = np.array([(pt[0], pt[1], pt[0] + target_image.shape[1] * best_scale[0], pt[1] + target_image.shape[0] * best_scale[1]) for pt in best_loc])

            # Apply non-maximum suppression to the rectangles
            pick = ImageFinder.non_max_suppression_fast(rects, 0.3)  # You may need to adjust the overlap threshold value

            for (startX, startY, endX, endY) in pick:
                # Draw the final bounding boxes

                # rbg value

                cv2.rectangle(screenshot_cv, (int(startX), int(startY)), (int(endX), int(endY)), (255,0,255), 2)

                center_x = int(startX + (endX - startX) // 2 + win.left)
                center_y = int(startY + (endY - startY) // 2 + win.top)

                # scale offsets according to the best scaling factor
                x_offset_scaled = int(x_offset * best_scale[0])
                y_offset_scaled = int(y_offset * best_scale[1])

            

            print(colored(f"found {target_image_path} {len(pick)}x at {best_max_val}%", "green"))
            if (len(pick) >= max_matches and max_matches != 0):
                return False
            if (len(pick) < max_matches and max_matches != 0):
                return True

            pyautogui.click(center_x + x_offset_scaled, center_y + y_offset_scaled)
            prev_active_window.activate()
            pyautogui.moveTo(prev_mouse_x, prev_mouse_y)

            return True
        else:
            print(colored(f"No matches for {target_image_path} found in screenshot.", "red"))
            if max_matches != 0:
                return True
            return False

    @staticmethod   
    def non_max_suppression_fast(boxes, overlapThresh):
        if len(boxes) == 0:
            return []

        pick = []

        x1 = boxes[:, 0]
        y1 = boxes[:, 1]
        x2 = boxes[:, 2]
        y2 = boxes[:, 3]

        area = (x2 - x1 + 1) * (y2 - y1 + 1)
        idxs = np.argsort(y2)

        while len(idxs) > 0:
            last = len(idxs) - 1
            i = idxs[last]
            pick.append(i)

            xx1 = np.maximum(x1[i], x1[idxs[:last]])
            yy1 = np.maximum(y1[i], y1[idxs[:last]])
            xx2 = np.minimum(x2[i], x2[idxs[:last]])
            yy2 = np.minimum(y2[i], y2[idxs[:last]])

            w = np.maximum(0, xx2 - xx1 + 1)
            h = np.maximum(0, yy2 - yy1 + 1)

            overlap = (w * h) / area[idxs[:last]]

            idxs = np.delete(idxs, np.concatenate(([last],
                np.where(overlap > overlapThresh)[0])))

        return boxes[pick]





        
    def find_image(self, target_image_path, screenshot):
        best_scale, best_loc, num_matches, best_max_val, target_image, screenshot_cv = self._match_image(target_image_path, screenshot)

        
        if best_max_val >= self.threshold:
            print(colored(f"found {target_image_path} {best_max_val}%", "green"))
            return True
        else:
            print(colored(f"No matches for {target_image_path} found in screenshot.", "red"))
            return False
