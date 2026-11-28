# NEXORA AI

A voice-first personal AI companion project. The live web/PWA application is hosted on Hatchable; this repository branch records project documentation and the local Windows brain helper.

## Live app
https://nexora-ai-nv88.hatchable.site

- Current live Hatchable version: **v70**
- Hatchable project: `proj_LfgsvYRQRBpg`
- Hatchable is the deployment source of truth. This GitHub branch is project documentation and local helper code, not the live app source or an APK.

## Companion characters
- **KAI** — warm, friendly male best-friend style; gamer-themed full-body model.
- **RYAN** — analytical male tech friend; cyberpunk/hacker-themed full-body model.
- **MAYA** — same-age study-mentor friend; patient, cheerful, clear explanations.
- **ANGEL** — same-age classmate friend; playful, kind and curious.
- **RIYA** — extra-caring AI companion friend; gentle, thoughtful and supportive.
- **NEXORA** — central controller that routes voice commands to the requested companion.

All characters are AI companions, not real people. Character conversations should remain age-appropriate, respectful and non-possessive.

## Full-body model assets
The Hatchable project contains five local GLB 2.0 files under `public/models/`: `kai-human.glb`, `ryan-human.glb`, `maya-human.glb`, `angel-human.glb` and `riya-human.glb`. All five returned HTTP 200 after the v68 deployment and passed GLB 2.0 header/length checks. Each has a skinned mesh, 34 facial morph targets and an `Idle` animation. The renderer now points to these same-origin local assets instead of remote GitHub raw URLs. Visual appearance/framing still needs user review on Android. Original asset provenance/license must be confirmed before redistribution.

## Voice profiles
NEXORA and each companion have separate pitch/rate profiles. The browser selects from voices installed on the device and uses gender-aware voice selection where possible. Actual voice names and quality depend on Android/Windows speech engines; if a device exposes only one suitable voice, pitch/rate can differ but the underlying voice may remain the same. Guaranteed unique neural voices require a bundled local TTS runtime and individually licensed voice models.

## Free local AI brain
This branch includes `nexora_local_brain.py`, `requirements-local-brain.txt`, `START_NEXORA_BRAIN.bat` and `LOCAL_BRAIN_SETUP.md`. The FastAPI bridge streams replies from a local Ollama model in the NDJSON format expected by the NEXORA frontend. It also offers optional per-character Microsoft Edge neural TTS voices through the same token-protected laptop bridge. Neural TTS is OFF by default because spoken reply text is sent to an online speech service; the user must enable it in NEXORA Settings. No paid AI API key is required. The laptop must run Ollama and the bridge; Android access additionally needs a trusted HTTPS tunnel. The Windows launcher checks/starts Ollama, installs dependencies and starts the local server. The brain is not connected until the user starts it and NEXORA's connection test succeeds.

## Current foundations
- Five selectable companion profiles and local full-body GLB models.
- Three.js renderer with GLTF/VRM loader support, skeletons, idle animation and speech facial morphs.
- Browser speech recognition, wake phrase handling and device-dependent speech synthesis.
- Local-first chat and memory storage, JSON backup/restore.
- Optional laptop-hosted Ollama brain bridge.
- Signed-in account sync endpoint for chats and memories.
- Installable PWA shell.
- Safe Automation Command Center currently records and classifies tasks; it does not yet execute OS or third-party account actions.

## Important limitations
- This repository branch is not a compiled Android APK or Windows installer.
- Browser voice recognition may need internet and the app open; background wake is not guaranteed.
- Device TTS voice availability varies. Current profiles are distinct settings, not five bundled neural voices.
- Full-body GLB assets are structurally verified and served successfully, but each character still needs visual approval on Android.
- Local AI requires Ollama and the separate bridge to be running. The app reports a disconnected brain rather than presenting a scripted fallback as an AI answer.
- The free hosting account has a daily bandwidth cap; after it is reached, public asset/API requests pause until the quota resets.
- YouTube and other app shortcuts open official sites; they do not yet automate uploads or control signed-in accounts.
- Local GLB asset provenance/license must be confirmed before redistribution.

## Development
Use Hatchable to inspect, test and deploy app source. Use GitHub for project documentation, the local brain helper, history and code review. This branch is not the live app's source of truth.
