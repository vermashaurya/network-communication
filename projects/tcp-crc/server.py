import argparse
import socket


def crc8(data: bytes, polynomial: int = 0x07, init: int = 0x00) -> int:
    crc = init
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = ((crc << 1) ^ polynomial) & 0xFF
            else:
                crc = (crc << 1) & 0xFF
    return crc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="TCP CRC server")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host")
    parser.add_argument("--port", type=int, default=12348, help="Bind port")
    return parser.parse_args()


def run_server(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen(5)
        print(f"[tcp-crc/server] Listening on {host}:{port}")
        try:
            while True:
                conn, addr = sock.accept()
                with conn:
                    payload = conn.recv(1024)
                    checksum = crc8(payload)
                    response = f"CRC8={checksum}"
                    conn.sendall(response.encode("utf-8"))
                    print(f"[tcp-crc/server] {addr} payload={payload!r} crc={checksum}")
        except KeyboardInterrupt:
            print("\n[tcp-crc/server] Stopped.")


if __name__ == "__main__":
    args = parse_args()
    run_server(args.host, args.port)
