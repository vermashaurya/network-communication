# UDP Echo

UDP request/response demo where server returns `ECHO: <message>`.

## Run

```bash
python projects/udp-echo/server.py
python projects/udp-echo/client.py
```

## Notes

- Server listens on `127.0.0.1:12000` by default.
- Client supports interactive loop with `quit`.
