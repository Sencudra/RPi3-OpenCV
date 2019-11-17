
import cv2

import config as cfg


class Recognizer:

    def filter_frame(self, frame):

        def hsv_normilize(h, s, v):
            hue = (h / 360) * 180
            saturation = (s / 100) * 255
            value = (v / 100) * 255
            return hue, saturation, value

        def filter_color(frame, lower_threshold, upper_threshold):
            clone = frame.copy()
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            hsv_lower_norm = hsv_normilize(*cfg.THRESHOLD_LOWER_BLUE)
            hsv_upper_norm = hsv_normilize(*cfg.THRESHOLD_UPPER_BLUE)
            mask = cv2.inRange(hsv_frame,
                               hsv_lower_norm,
                               hsv_upper_norm)
            return cv2.bitwise_and(clone, clone, mask=mask)

        filtered_frame = filter_color(frame,
                                      cfg.THRESHOLD_LOWER_BLUE,
                                      cfg.THRESHOLD_UPPER_BLUE)

        gray_image = cv2.cvtColor(filtered_frame, cv2.COLOR_BGR2GRAY)

        _, thresholded_image = cv2.threshold(gray_image,
                                             cfg.THRESHOLD_VALUE,
                                             cfg.THRESHOLD_MAXVALUE,
                                             cv2.THRESH_BINARY)

        filtered_image = cv2.bilateralFilter(thresholded_image,
                                             cfg.FILTER_DIAMETER,
                                             cfg.FILTER_SIGMA_COLOR,
                                             cfg.FILTER_SIGMA_SPACE)

        image_with_edges = cv2.Canny(filtered_image,
                                     cfg.CANNY_THRESHOLD_FIRST,
                                     cfg.CANNY_THRESHOLD_SECOND)
        return image_with_edges

    def detect(self, image):

        def aproximate_cotours(contours):
            center_list = set()
            contour_list = []
            for contour in contours:

                is_curve_closed = True
                epsilon = 0.01 * cv2.arcLength(contour, is_curve_closed)

                approximation = cv2.approxPolyDP(contour,
                                                 epsilon,
                                                 is_curve_closed)

                area = cv2.contourArea(contour)

                # Main magic
                if ((len(approximation) > cfg.AREA_APROXIMATION) &
                        (cfg.AREA_UPPER_BOUND > area > cfg.AREA_LOWER_BOUND)):
                    contour_list.append(contour)
                    center_list.add(get_contour_center(contour))

            return contour_list, list(center_list)

        def get_contour_center(contour):
            moments = cv2.moments(contour)
            center_x = int(moments["m10"] / moments["m00"])
            center_y = int(moments["m01"] / moments["m00"])
            return center_x, center_y

        clone = image.copy()

        grayed_image = self.filter_frame(clone)

        contours, _ = cv2.findContours(grayed_image,
                                       cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)

        contour_list, center_list = aproximate_cotours(contours)

        cv2.drawContours(clone,
                         contour_list,
                         cfg.DRAW_CONTOUR,
                         cfg.DRAW_COLOR_BLUE,
                         cfg.DRAW_THICKNESS)

        for center_x, center_y in center_list:
            cv2.circle(clone,
                       (center_x, center_y),
                       cfg.DRAW_RADIUS,
                       cfg.DRAW_COLOR_RED,
                       cfg.DRAW_CIRCLE_THICKNESS)

        # Draw screen center
        cv2.circle(clone,
                   (clone.shape[1] // 2, clone.shape[0] // 2),
                   cfg.DRAW_CENTER_RADIUS,
                   cfg.DRAW_COLOR_GREEN,
                   cfg.DRAW_CIRCLE_THICKNESS)

        return clone, center_list
