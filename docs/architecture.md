# Architecture Overview

```mermaid
flowchart LR
  user[UserTerminal] --> clientPy[PythonClient]
  clientPy -->|"UDP/TCP localhost"| serverPy[PythonServer]
  serverPy --> clientPy
  user --> pages[GitHubPagesSite]
  pages --> jsDemo[BrowserAlgorithmDemos]
  jsDemo --> user
```

## Design Principles

- Keep networking behavior authentic in Python socket modules.
- Keep GitHub Pages browser-native and algorithm focused.
- Provide one-click discoverability from root README and site landing.
