import argparse


def ones_complement(bits: str) -> str:
    return "".join("1" if b == "0" else "0" for b in bits)


def binary_add(a: str, b: str) -> str:
    width = max(len(a), len(b))
    total = int(a, 2) + int(b, 2)
    carry = total >> width
    result = total & ((1 << width) - 1)
    if carry:
        result = (result + carry) & ((1 << width) - 1)
    return format(result, f"0{width}b")


def checksum(blocks: list[str]) -> str:
    if not blocks:
        raise ValueError("Provide at least one block.")
    width = len(blocks[0])
    if any(len(b) != width or any(ch not in {"0", "1"} for ch in b) for b in blocks):
        raise ValueError("All blocks must be equal-length bitstrings (0/1 only).")
    running = blocks[0]
    for block in blocks[1:]:
        running = binary_add(running, block)
    return ones_complement(running)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Checksum lab CLI")
    parser.add_argument(
        "blocks",
        nargs="+",
        help="Bitstring blocks, e.g. 1010 0101 1111",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    result = checksum(args.blocks)
    print(f"Checksum: {result}")
