# TCP Even Parity

TCP client/server project that validates even parity for received bitstrings.

## Run

```bash
python projects/tcp-even-parity/server.py
python projects/tcp-even-parity/client.py --data 101010 --append-parity-bit
```

## Notes

- Server validates bitstrings (`0/1` only).
- Client can optionally append parity bit before send.
