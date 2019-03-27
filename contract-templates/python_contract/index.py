import sys
import json
from contract import handler

def read_data():
    buffer = ''
    for line in sys.stdin:
        buffer += line
    return buffer


if __name__ == "__main__":
    data = read_data()
    parsed = json.loads(data)
    ret = handler.main(parsed)
    if ret is not None:
        serialized = json.dumps(ret)
        sys.stdout.buffer.write(serialized.encode('utf-8'))
