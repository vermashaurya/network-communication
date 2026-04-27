from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load_module(relative_path: str, module_name: str):
    root = Path(__file__).resolve().parents[1]
    path = root / relative_path
    spec = spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module: {relative_path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_append_even_parity_bit():
    mod = load_module("projects/tcp-even-parity/client.py", "tcp_even_parity_client")
    assert mod.append_even_parity_bit("1010") == "10100"
    assert mod.append_even_parity_bit("1110") == "11101"


def test_has_even_parity():
    mod = load_module("projects/tcp-even-parity/server.py", "tcp_even_parity_server")
    assert mod.has_even_parity("1010") is True
    assert mod.has_even_parity("1110") is False


def test_checksum():
    mod = load_module("projects/checksum-lab/cli.py", "checksum_lab_cli")
    assert mod.checksum(["1010", "0101"]) == "0000"


def test_crc8():
    mod = load_module("projects/tcp-crc/server.py", "tcp_crc_server")
    # Known CRC8(0x07) test vector for ASCII "123456789"
    assert mod.crc8(b"123456789") == 0xF4
