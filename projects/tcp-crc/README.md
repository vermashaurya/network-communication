# TCP CRC

TCP project where client sends payload and server responds with CRC8 checksum.

## Run

```bash
python projects/tcp-crc/server.py
python projects/tcp-crc/client.py --message "hello"
```

## Notes

- Uses CRC8 polynomial `0x07`.
- Intended for error-detection concept demonstration.
