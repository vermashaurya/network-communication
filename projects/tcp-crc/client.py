import argparse
import socket


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="TCP CRC client")
    parser.add_argument("--host", default="127.0.0.1", help="Server host")
    parser.add_argument("--port", type=int, default=12348, help="Server port")
    parser.add_argument("--message", help="Message payload (if omitted, prompt interactively)")
    return parser.parse_args()


def run_client(host: str, port: int, message: str) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(message.encode("utf-8"))
        response = sock.recv(1024).decode("utf-8", errors="replace")
    print(f"Sent payload: {message}")
    print(f"Server response: {response}")


if __name__ == "__main__":
    args = parse_args()
    payload = args.message if args.message is not None else input("Enter message: ")
    if not payload:
        raise SystemExit("Message cannot be empty.")
    run_client(args.host, args.port, payload)
