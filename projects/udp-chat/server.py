import argparse
import socket


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="UDP chat server")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host")
    parser.add_argument("--port", type=int, default=12346, help="Bind port")
    parser.add_argument(
        "--reply-prefix",
        default="Server reply:",
        help="Prefix applied to each response",
    )
    return parser.parse_args()


def run_server(host: str, port: int, reply_prefix: str) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f"[udp-chat/server] Listening on {host}:{port}")
    try:
        while True:
            data, addr = sock.recvfrom(4096)
            message = data.decode("utf-8", errors="replace")
            print(f"[udp-chat/server] {addr} -> {message}")
            reply = f"{reply_prefix} {message}"
            sock.sendto(reply.encode("utf-8"), addr)
    except KeyboardInterrupt:
        print("\n[udp-chat/server] Stopped.")
    finally:
        sock.close()


if __name__ == "__main__":
    args = parse_args()
    run_server(args.host, args.port, args.reply_prefix)
