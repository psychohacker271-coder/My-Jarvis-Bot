# NEXORA AI

A voice-first personal AI companion project. The live web/PWA application is hosted on Hatchable; this repository branch records the project overview and current implementation status.

## Live app
https://nexora-ai-nv88.hatchable.site

## Current foundations
- Five selectable companion profiles: KAI, RYAN, MAYA, ANGEL and RIYA.
- Three.js full-body avatar scene with model-loading and fallback paths.
- Browser speech recognition, wake phrase handling and clap-to-wake (browser/device support required).
- Local-first chat and memory storage, JSON backup/restore.
- Optional connection to a laptop-hosted local AI service.
- Signed-in account sync endpoint for chats and memories.
- Installable PWA shell.

## Important limitations
- This repository branch is project documentation, not a compiled Android APK or Windows installer.
- Browser voice recognition may need internet and the app open; background wake is not guaranteed.
- YouTube and other app shortcuts open official sites; they do not yet automate uploads or control signed-in accounts.
- The local AI brain needs a separately installed local model/runtime. No paid API is required for that local mode.
- Sample character model licensing must be checked before redistribution.
- Android native source mentioned in project notes still needs a build and real-device verification.

## Development
The Hatchable project is the deployment source of truth. Review and test source changes there, then mirror approved changes into this repository.