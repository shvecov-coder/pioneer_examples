from pioneer_sdk import VideoStream


def main():
    stream = VideoStream()
    while True:
        cmd = input()
        if cmd == 'start':
            stream.start()
        elif cmd == 'stop':
            stream.stop()
        else:
            print('Invalid command')


if __name__ == '__main__':
    main()
