# NEXORA AI

A voice-first personal AI companion project. The live web/PWA application is hosted on Hatchable; this repository branch records the project overview and current implementation status.

## Live app
https://nexora-ai-nv88.hatchable.site

## Companion characters
- **KAI** — warm, friendly male best-friend style.
- **RYAN** — lower, clear, confident male tech-friend style.
- **MAYA** — bright, cheerful female best-friend style.
- **ANGEL** — calm, gentle, caring female style.
- **RIYA** — warm, expressive, affectionate and playful female style.
- **NEXORA** — the central controller that routes voice commands to the requested companion.

Each companion has a separate speech profile (voice-gender preference, voice selection slot, rate and pitch). The browser build selects from voices installed on the user's device; the actual available voices and naturalness depend on Android/Windows/browser speech engines. This is a device-voice fallback, not a bundled premium neural voice pack.

## Current foundations
- Five selectable companion profiles: KAI, RYAN, MAYA, ANGEL and RIYA.
- Three.js avatar scene with model-loading and fallback paths.
- Browser speech recognition, wake phrase handling and clap-to-wake (browser/device support required).
- Companion-specific speech settings and voice selection from device-installed voices.
- Local-first chat and memory storage, JSON backup/restore.
- Optional connection to a laptop-hosted local AI service.
- Signed-in account sync endpoint for chats and memories.
- Installable PWA shell.

## Voice quality roadmap
For consistent, higher-quality offline neural voices across both Android and Windows, integrate a local TTS runtime such as Piper or Kokoro and bundle/download appropriately licensed voice models. This requires model downloads, storage, CPU/RAM testing and platform-specific packaging. No paid voice API is required for a local runtime, but model licenses and redistribution terms must be checked individually.

## Important limitations
- This repository branch is project documentation, not a compiled Android APK or Windows installer.
- Browser voice recognition may need internet and the app open; background wake is not guaranteed.
- Browser/device TTS voices vary by device. The five profiles apply distinct settings and choose different available voices where possible; guaranteed studio-quality unique voices require a bundled neural TTS runtime.
- YouTube and other app shortcuts open official sites; they do not yet automate uploads or control signed-in accounts.
- The local AI brain needs a separately installed local model/runtime. No paid API is required for that local mode.
- Sample character model licensing must be checked before redistribution.
- Android native source mentioned in project notes still needs a build and real-device verification.

## Development
The Hatchable project is the deployment source of truth. Review and test source changes there, then mirror approved changes into this repository.
