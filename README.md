# Network Communication Projects

A curated multi-project repository focused on socket programming fundamentals and error-checking algorithms.

## What This Repository Contains

- `projects/udp-chat`: two-way UDP chat flow.
- `projects/udp-echo`: UDP request/response echo service.
- `projects/tcp-even-parity`: TCP parity checker for bitstrings.
- `projects/tcp-crc`: TCP service that returns CRC8 for payloads.
- `projects/checksum-lab`: checksum utility for 1's complement addition.
- `demos/` and `site/`: browser-facing showcase for GitHub Pages.

## Quick Start

1. Create a Python 3.10+ environment.
2. Run a server script in one terminal.
3. Run its matching client script in another terminal.

Example:

```bash
python projects/udp-echo/server.py
python projects/udp-echo/client.py
```

## Why GitHub Pages Still Works

Raw socket servers cannot run on GitHub Pages. This repository solves that by:
- keeping real socket projects runnable locally;
- exposing documentation, architecture, and algorithm demos on a static Pages site.

## Project Structure

- `projects/`: implementation code
- `tests/`: unit tests
- `docs/`: technical notes and migration map
- `assets/`: media and diagrams
- `site/`: static showcase site

## Roadmap

- Add demo GIFs under `assets/`.
- Expand protocol notes in `docs/`.
- Add more integration tests.

## License

This project is licensed under the [MIT License](LICENSE). 
<br><br> Copyright (c) 2026 <br>
<img src="name-geo4.avif" alt="Logo" width="600"/>  <br> <br>
[![License](https://img.shields.io/github/license/vermashaurya/network-communication)](LICENSE) <br>
Feel free to take inspiration. <br>Happy Coding!   
