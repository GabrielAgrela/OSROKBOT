import cv2
import numpy as np
import pyautogui

def feature_matching(target_image_path, screenshot_path):
    # Load the images in grayscale
    img1 = cv2.imread(target_image_path, 0)          # target image
    img2 = cv2.imread(screenshot_path, 0)            # screenshot

    # Initialize ORB detector
    orb = cv2.ORB_create()

    # Find the keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # Use the BFMatcher (Brute Force Matcher) and Hamming distance. Set crossCheck to True for better results
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors
    matches = bf.match(des1, des2)

    # Sort them in ascending order of distance
    matches = sorted(matches, key=lambda x: x.distance)

    # If you have a decent number of good matches, then proceed
    if len(matches) > MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

        # Find homography matrix. While this step is for perspective transformation, it's also a good way to filter out wrong matches
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()

        # Get the top-left and bottom-right corners of the matched area
        h, w = img1.shape
        pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, M)

        center_x = int((dst[0][0][0] + dst[2][0][0]) / 2)
        center_y = int((dst[0][0][1] + dst[2][0][1]) / 2)

        pyautogui.click(center_x, center_y)

    else:
        print("Not enough matches found - %d/%d" % (len(matches), MIN_MATCH_COUNT))
        matchesMask = None

    # Optional: Draw matches (for visualization purposes)
    draw_params = dict(matchColor=(0, 255, 0),
                       singlePointColor=None,
                       matchesMask=matchesMask,
                       flags=2)

    result_img = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, **draw_params)
    cv2.imshow("Matches", result_img)
    cv2.waitKey(0)

MIN_MATCH_COUNT = 10
feature_matching("path_to_target_image.png", "path_to_screenshot.png")
