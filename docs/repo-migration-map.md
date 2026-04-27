# Repository Migration Map

This document records how the original flat scripts were normalized into a multi-project layout.

## Source to Destination

- `client.py` -> `projects/udp-chat/client.py`
- `server.py` -> `projects/udp-chat/server.py`
- `1spclient.py` -> `projects/udp-echo/client.py`
- `1spserver.py` -> `projects/udp-echo/server.py`
- `eparityclient.py` -> `projects/tcp-even-parity/client.py`
- `eparityserver.py` -> `projects/tcp-even-parity/server.py`
- `labfatclient.py` -> `projects/tcp-crc/client.py`
- `labfatserver.py` -> `projects/tcp-crc/server.py`
- `crash1.py` and `digital1.py` -> `projects/checksum-lab/cli.py`

## Layout Rationale

- `projects/`: runnable Python networking projects.
- `demos/`: browser demos for algorithmic logic that can run on GitHub Pages.
- `site/`: static showcase site for GitHub Pages.
- `docs/`: architecture and protocol notes.
- `assets/`: screenshots, diagrams, and media artifacts.
- `tests/`: test suite for core logic.
