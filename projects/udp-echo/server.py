import argparse
import socket


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="UDP echo server")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host")
    parser.add_argument("--port", type=int, default=12000, help="Bind port")
    return parser.parse_args()


def run_server(host: str, port: int) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f"[udp-echo/server] Listening on {host}:{port}")
    try:
        while True:
            payload, client_address = sock.recvfrom(1024)
            message = payload.decode("utf-8", errors="replace")
            print(f"[udp-echo/server] {client_address} -> {message}")
            reply = f"ECHO: {message}"
            sock.sendto(reply.encode("utf-8"), client_address)
    except KeyboardInterrupt:
        print("\n[udp-echo/server] Stopped.")
    finally:
        sock.close()


if __name__ == "__main__":
    args = parse_args()
    run_server(args.host, args.port)
