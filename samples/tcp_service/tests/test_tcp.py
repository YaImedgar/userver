# /// [Functional test]
import socket


async def test_basic(service_client, loop):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8180))

    await loop.sock_sendall(sock, b'hi')
    hello = await loop.sock_recv(sock, 5)
    assert hello == b'hello'

    await loop.sock_sendall(sock, b'whats up?')
    try:
        await loop.sock_recv(sock, 1)
        assert False
    except ConnectionResetError:
        pass
    # /// [Functional test]
