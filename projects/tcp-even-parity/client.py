import argparse
import socket


def append_even_parity_bit(bitstring: str) -> str:
    parity_bit = "0" if bitstring.count("1") % 2 == 0 else "1"
    return f"{bitstring}{parity_bit}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="TCP even parity client")
    parser.add_argument("--host", default="127.0.0.1", help="Server host")
    parser.add_argument("--port", type=int, default=12347, help="Server port")
    parser.add_argument("--data", help="Bitstring to send (if omitted, prompt interactively)")
    parser.add_argument(
        "--append-parity-bit",
        action="store_true",
        help="Append parity bit before sending",
    )
    return parser.parse_args()


def run_client(host: str, port: int, data: str, append_parity_bit: bool) -> None:
    payload = append_even_parity_bit(data) if append_parity_bit else data
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(payload.encode("utf-8"))
        response = client_socket.recv(1024).decode("utf-8", errors="replace")
    print(f"Sent: {payload}")
    print(f"Server response: {response}")


if __name__ == "__main__":
    args = parse_args()
    input_data = args.data if args.data is not None else input("Enter bitstring: ").strip()
    if not input_data or any(ch not in {"0", "1"} for ch in input_data):
        raise SystemExit("Input must be a non-empty bitstring with only 0/1.")
    run_client(args.host, args.port, input_data, args.append_parity_bit)
