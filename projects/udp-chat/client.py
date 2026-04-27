import argparse
import socket


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="UDP chat client")
    parser.add_argument("--host", default="127.0.0.1", help="Server host")
    parser.add_argument("--port", type=int, default=12346, help="Server port")
    parser.add_argument("--timeout", type=float, default=5.0, help="Receive timeout seconds")
    return parser.parse_args()


def run_client(host: str, port: int, timeout: float) -> None:
    server_address = (host, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    print("[udp-chat/client] Type 'quit' to exit.")
    try:
        while True:
            message = input("You: ").strip()
            if message.lower() in {"quit", "exit"}:
                break
            if not message:
                continue
            sock.sendto(message.encode("utf-8"), server_address)
            data, _ = sock.recvfrom(4096)
            print(f"Server: {data.decode('utf-8', errors='replace')}")
    except socket.timeout:
        print("[udp-chat/client] Timeout waiting for server response.")
    except KeyboardInterrupt:
        print("\n[udp-chat/client] Stopped.")
    finally:
        sock.close()


if __name__ == "__main__":
    args = parse_args()
    run_client(args.host, args.port, args.timeout)
