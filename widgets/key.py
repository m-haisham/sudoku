from typing import Union

_number_map = {
    # 0-9 keys
    48: 0,
    49: 1,
    50: 2,
    51: 3,
    52: 4,
    53: 5,
    54: 6,
    55: 7,
    56: 8,
    57: 9,

    # numpad
    256: 0,
    257: 1,
    258: 2,
    259: 3,
    260: 4,
    261: 5,
    262: 6,
    263: 7,
    264: 8,
    265: 9,
}


class Number:
    @staticmethod
    def mapper(keycode: int) -> Union[int, None]:
        try:
            return _number_map[keycode]
        except KeyError:
            return None
