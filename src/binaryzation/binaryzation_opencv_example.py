import cv2
from pioneer_sdk import Pioneer
from pioneer_sdk import Camera


def nothing():
    pass


def main():
    cam = Camera()

    cv2.namedWindow('Trackbar')

    cv2.createTrackbar('min H', 'Trackbar', 0, 255, nothing)
    cv2.createTrackbar('min S', 'Trackbar', 0, 255, nothing)
    cv2.createTrackbar('min V', 'Trackbar', 0, 255, nothing)
    cv2.createTrackbar('max H', 'Trackbar', 0, 255, nothing)
    cv2.createTrackbar('max S', 'Trackbar', 0, 255, nothing)
    cv2.createTrackbar('max V', 'Trackbar', 0, 255, nothing)

    while True:
        frame = cam.get_cv_frame()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        minH = cv2.getTrackbarPos('min H', 'Trackbar')
        minS = cv2.getTrackbarPos('min S', 'Trackbar')
        minV = cv2.getTrackbarPos('min V', 'Trackbar')

        maxH = cv2.getTrackbarPos('max H', 'Trackbar')
        maxS = cv2.getTrackbarPos('max S', 'Trackbar')
        maxV = cv2.getTrackbarPos('max V', 'Trackbar')

        min_p = (minH, minS, minV)
        max_p = (maxH, maxS, maxV)

        mask_frame = cv2.inRange(hsv_frame, min_p, max_p)
        result_frame = cv2.bitwise_and(frame, frame, mask=mask_frame)
        cv2.imshow('Binarization', result_frame)
        cv2.imshow('Original frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
