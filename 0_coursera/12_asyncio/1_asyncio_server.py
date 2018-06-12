import asyncio

# server

async def handler(reader, writer):
	data = await reader.read(1024)
	message = data.decode()
	addr = writer.get_extra_info("peername")
	print("received %r from %r" % (message, addr))
	writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handler, "127.0.0.1", 10001, loop=loop)
server = loop.run_until_complete(coro)
try:
	loop.run_forever()
except KeyboardInterrupt:
	pass


server.close()
loop.run_until_complete(server.wait_closed())
loop.close()



# tcp client
'''
import asyncio

async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection("127.0.0.1", 10001, loop=loop)

    print("send: %r" % message)
    writer.write(message.encode())
    writer.close()

loop = asyncio.get_event_loop()
message = "hello World!"
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()
'''
