import cv2
from pioneer_sdk import Camera
from pioneer_sdk import Pioneer


def main():
    led_is_off = True
    cam = Camera()
    last_color_led = ''
    pioneer = Pioneer()
    detect_colors = {'red': ((0, 80, 158), (23, 255, 255))}
    leds_colors = {'red': (255, 0, 0)}

    while True:
        frame = cam.get_cv_frame()

        for color_name, color_component in detect_colors.items():
            min_color = color_component[0]
            max_color = color_component[1]
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask_color = cv2.inRange(hsv_frame, min_color, max_color)

            contours, _ = cv2.findContours(mask_color, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

            if len(contours) != 0:
                max_contour = max(contours, key=cv2.contourArea)
                if cv2.contourArea(max_contour) > 2000:
                    x, y, w, h = cv2.boundingRect(max_contour)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    if last_color_led != color_name:
                        r = leds_colors[color_name][0]
                        g = leds_colors[color_name][1]
                        b = leds_colors[color_name][2]
                        pioneer.led_control(255, r, g, b)
                        led_is_off = False
                        last_color_led = color_name
                else:
                    if not led_is_off:
                        pioneer.led_control(255, 0, 0, 0)
                        led_is_off = True
                        last_color_led = ''

            cv2.imshow('Frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break


if __name__ == '__main__':
    main()
