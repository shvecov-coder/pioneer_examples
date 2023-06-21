import time as tm
from pioneer_sdk import Pioneer


def main():
    cnt = 6
    is_arm = False
    timer = tm.time()
    pioneer = Pioneer()

    while cnt:
        if tm.time() - timer > 3:
            if is_arm:
                pioneer.disarm()
            else:
                pioneer.arm()
            cnt -= 1
            timer = tm.time()
            is_arm = not is_arm


if __name__ == '__main__':
    main()
