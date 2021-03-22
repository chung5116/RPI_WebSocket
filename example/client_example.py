import websockets
import asyncio

HOST = '192.168.50.2'
PORT = 8764        # The port used by the server


async def hello():
    uri = 'ws://192.168.50.2:8764'

    async with websockets.connect(uri) as websocket:
        name = input("what's your name?")
        
        await websocket.send(name)
        print(f"> {name}") 

        greeting = await websocket.recv()

        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())