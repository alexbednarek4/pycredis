from dataclasses import dataclass


MSG_SEPARATOR = b"\r\n"


@dataclass
class SimpleString:
    data: str


def extract_msg_from_buffer(buffer):
    match chr(buffer[0]):
        case "+":
            separator = buffer.find(MSG_SEPARATOR)
            if separator != -1:
                return SimpleString(buffer[1:separator].decode()), \
                    separator + 2
    return None, 0


def test_read_frame_simple_string_incomplete():
    buff = b"+Incomple"
    frame, frame_size = extract_msg_from_buffer(buff)
    assert frame == None
    assert frame_size == 0


def test_read_frame_simple_string_complete():
    buff = b"+OK\r\n"
    frame, frame_size = extract_msg_from_buffer(buff)
    assert frame == SimpleString("OK")
    assert frame_size == 5


def test_read_frame_simple_string_extra_data():
    buff = b"+OK\r\n+Next"
    frame, frame_size = extract_msg_from_buffer(buff)
    assert frame == SimpleString("OK")
    assert frame_size == 5
