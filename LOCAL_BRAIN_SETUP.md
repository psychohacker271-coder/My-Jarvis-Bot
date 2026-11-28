# NEXORA Local Brain setup (Windows)

This helper connects NEXORA to a local Ollama model without a paid AI API key.

## 1. Requirements
- Windows laptop with Ollama installed and running.
- Python 3.10 or newer.
- A local Ollama model installed. The default is `qwen3.5:0.8b`; if yours has a different name, set `OLLAMA_MODEL` before starting.

## 2. Download the files
Download `nexora_local_brain.py` and `requirements-local-brain.txt` from this GitHub repository into the same folder.

## 3. Install and start
Open PowerShell in that folder and run:

```powershell
py -m pip install -r requirements-local-brain.txt
py nexora_local_brain.py
```

The terminal prints a one-time access token. Keep it private.

## 4. Connect NEXORA
In NEXORA → Settings:
- Local AI endpoint: `http://127.0.0.1:8765`
- Required laptop access token: paste the token printed in PowerShell.
- Tap **Test connection**.

Keep both Ollama and the Local Brain terminal running while chatting.

## 5. Android phone
The phone cannot use the laptop's `127.0.0.1` address. For phone access, configure a trusted HTTPS tunnel to the laptop's local port 8765, then paste that HTTPS address and the same token into NEXORA Settings. Do not expose port 8765 directly to the public internet.

## Troubleshooting
- If Ollama is not running, open Ollama first.
- If the model is missing, run `ollama list` and set `OLLAMA_MODEL` to an installed model name.
- If Windows Firewall asks, allow access only on private networks.
- If the connection test fails, check the endpoint, token, and that the terminal is still open.

The server binds to localhost only, checks the access token, allows the NEXORA app origin, and streams replies in the format expected by the NEXORA frontend.
