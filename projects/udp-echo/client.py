import argparse
import socket


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="UDP echo client")
    parser.add_argument("--host", default="127.0.0.1", help="Server host")
    parser.add_argument("--port", type=int, default=12000, help="Server port")
    parser.add_argument("--timeout", type=float, default=5.0, help="Receive timeout seconds")
    return parser.parse_args()


def run_client(host: str, port: int, timeout: float) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    target = (host, port)
    print("[udp-echo/client] Type 'quit' to exit.")
    try:
        while True:
            message = input("Message: ").strip()
            if message.lower() in {"quit", "exit"}:
                break
            if not message:
                continue
            sock.sendto(message.encode("utf-8"), target)
            response, server_addr = sock.recvfrom(1024)
            print(f"Response from {server_addr}: {response.decode('utf-8', errors='replace')}")
    except socket.timeout:
        print("[udp-echo/client] Timeout waiting for response.")
    except KeyboardInterrupt:
        print("\n[udp-echo/client] Stopped.")
    finally:
        sock.close()


if __name__ == "__main__":
    args = parse_args()
    run_client(args.host, args.port, args.timeout)
