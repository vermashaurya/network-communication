import argparse
import socket


def has_even_parity(bitstring: str) -> bool:
    return bitstring.count("1") % 2 == 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="TCP even parity server")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host")
    parser.add_argument("--port", type=int, default=12347, help="Bind port")
    return parser.parse_args()


def run_server(host: str, port: int) -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[tcp-even-parity/server] Listening on {host}:{port}")
    try:
        while True:
            connection, client_address = server_socket.accept()
            with connection:
                data = connection.recv(1024).decode("utf-8", errors="replace").strip()
                print(f"[tcp-even-parity/server] {client_address} -> {data}")
                if not data or any(ch not in {"0", "1"} for ch in data):
                    response = "Invalid bitstring. Use only 0 and 1."
                elif has_even_parity(data):
                    response = "Even parity check passed."
                else:
                    response = "Even parity check failed."
                connection.sendall(response.encode("utf-8"))
    except KeyboardInterrupt:
        print("\n[tcp-even-parity/server] Stopped.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    args = parse_args()
    run_server(args.host, args.port)
