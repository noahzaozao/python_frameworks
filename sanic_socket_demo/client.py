import datetime

import websocket

now = datetime.datetime.now()
print(now)


def send_query_websocket():
    ws = websocket.WebSocket()
    ws.connect("ws://127.0.0.1:9000/feed")
    result_1 = ws.recv()
    print(result_1)

    ws.send("I am test msg!")
    ws.close()
    return True


if __name__ == '__main__':
    send_query_websocket()
