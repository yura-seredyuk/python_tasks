import asyncio
import time
import itertools
 
 
async def tcp_echo_client(message,id):
    reader, writer = await asyncio.open_connection('127.0.0.1', 5000)
 
    print('Send: %r' % message)
    writer.write(message.encode())
    
    time.sleep(5)

    data = await reader.read(100)
    print('Received: %r' % data.decode())
 
    print('Close the socket')
    writer.close()
 
responses = [['A', 8], ['B', 10], ['C', 7], ['D', 9], ['E', 8], ['F', 4], ['G', 7], ['H', 10], ['I', 8], ['J', 5], ['K', 9], ['L', 7], ['M', 7], ['N', 8], ['O', 2], ['P', 2], ['Q', 2], ['R', 9], ['S', 10], ['T', 7], ['U', 3], ['V', 9], ['W', 4], ['X', 4], ['Y', 10], ['Z', 9]]


loop = asyncio.get_event_loop()
# for i in range(1):
#     message = f'Message from client {i}!'
#     loop.run_until_complete(tcp_echo_client(message))

tasks = itertools.starmap(tcp_echo_client, responses)
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()