import msvcrt

NEXT_CHARACTER_IS_KEYCODE = [b'\xe0', b'\xe0', b'0x00']


def get_key_press():
    while True:
        ch1 = msvcrt.getch()
        if ch1 in NEXT_CHARACTER_IS_KEYCODE:
            ch2 = msvcrt.getch()
            if ch2 == b'H':
                return 'Up'
            elif ch2 == b'K':
                return 'Left'
            elif ch2 == b'P':
                return 'Down'
            elif ch2 == b'M':
                return 'Right'
        elif ch1 == b'\r':
            return 'Return'
        else:
            return 'Wrong'
