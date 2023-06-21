import time as tm
from pioneer_sdk import Pioneer


def main():
    pioneer = Pioneer()
    colors = [[255, 0, 0],
              [0, 255, 0],
              [0, 0, 255]]

    for color in colors:
        for idx_led in range(4):
            pioneer.led_control(idx_led, color[0], color[1], color[2])
            tm.sleep(0.5)
            pioneer.led_control(idx_led, 0, 0, 0)
            tm.sleep(0.5)

    for color in colors:
        for i in range(3):
            pioneer.led_control(255, color[0], color[1], color[2])
            tm.sleep(0.5)
            pioneer.led_control(255, 0, 0, 0)
            tm.sleep(0.5)


if __name__ == '__main__':
    main()
