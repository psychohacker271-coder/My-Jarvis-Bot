# NEXORA Local Brain setup (Windows)

This helper connects NEXORA to a local Ollama model without a paid AI API key and can optionally provide distinct online neural voices per character.

## 1. Requirements
- Windows laptop with Ollama installed and running.
- Python 3.10 or newer.
- A local Ollama model installed. The default is `qwen3.5:0.8b`; if yours has a different name, set `OLLAMA_MODEL` before starting.

## 2. Download the files
Download these four files from this GitHub repository into the same folder: `nexora_local_brain.py`, `nexora_agents.py`, `requirements-local-brain.txt` and `START_NEXORA_BRAIN.bat`. The `nexora_agents.py` module is required by the brain server.

## 3. Install and start
For one-click startup on Windows, double-click `START_NEXORA_BRAIN.bat`. It checks Ollama, starts its local service if needed, installs the Python dependencies, and launches the brain server. Keep the terminal window open.

Or open PowerShell in that folder and run:

```powershell
py -m pip install -r requirements-local-brain.txt
py nexora_local_brain.py
```

The terminal prints a one-time access token. Keep it private. The requirements file installs the free Edge TTS fallback.

## 4. Connect NEXORA
In NEXORA → Settings:
- Local AI endpoint: `http://127.0.0.1:8765`
- Required laptop access token: paste the token printed in PowerShell.
- Tap **Test connection**.

Keep both Ollama and the Local Brain terminal running while chatting. NEXORA has six distinct character voice profiles. By default it uses free Edge TTS voices. For ElevenLabs-quality multilingual voices, you can optionally configure an ElevenLabs API key as a Windows environment variable **on your own laptop** before starting the server:

```powershell
$env:ELEVENLABS_API_KEY="YOUR_KEY"
py nexora_local_brain.py
```

Do not paste the key into NEXORA chat, browser code, GitHub, or a screenshot. ElevenLabs synthesis uses your account's plan credits and may incur usage limits or charges; check your plan before enabling it. When configured, the server uses the selected ElevenLabs voice for Hindi, Hinglish and English with `eleven_multilingual_v2`. If the key is missing, invalid, or the service is temporarily unavailable, the server falls back to free Edge TTS so speech can continue.

## 5. What the agents can do
The local runtime exposes NEXORA, KAI, RYAN, MAYA, ANGEL and RIYA as separate role-configured agents. NEXORA can consult up to two specialists in one turn. Safe local tools include arithmetic, local date/time, agent roster and installed Ollama model status. Tool use depends on the selected Ollama model supporting tool calling; if it does not, normal local chat still works.

## 6. Android phone
The phone cannot use the laptop's `127.0.0.1` address. For phone access, configure a trusted HTTPS tunnel to the laptop's local port 8765, then paste that HTTPS address and the same token into NEXORA Settings. Do not expose port 8765 directly to the public internet.

## Troubleshooting
- If Ollama is not running, open Ollama first.
- If the model is missing, run `ollama list` and set `OLLAMA_MODEL` to an installed model name.
- If Windows Firewall asks, allow access only on private networks.
- If the connection test fails, check the endpoint, token, and that the terminal is still open.

The server binds to localhost only, checks the access token, allows the NEXORA app origin, and streams replies in the format expected by the NEXORA frontend.
