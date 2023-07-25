import asyncio, socket

async def handle_client(client):
    loop = asyncio.get_event_loop()
    request = None
    while request != 'quit':
        request = (await loop.sock_recv(client, 255)).decode('utf8')
        # response = str(eval(request)) + '\n'
        response = request[::-1]
        await loop.sock_sendall(client, response.encode('utf8'))
    client.close()

async def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(8)
    server.setblocking(False)

    loop = asyncio.get_event_loop()

    tasks = []
    while True:
        client, _ = await loop.sock_accept(server)
        tasks.append(loop.create_task(handle_client(client)))
        print(len(tasks))

asyncio.run(run_server())