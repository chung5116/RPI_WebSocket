import socket
import websockets
import asyncio
# WS server example

HOST = '192.168.50.2'
PORT = 8764        # The port used by the server


async def hello(websocket,hello):
    
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")


start_server = websockets.serve(hello,HOST,PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
