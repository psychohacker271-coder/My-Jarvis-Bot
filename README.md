# NEXORA AI

A voice-first personal AI companion project. The live web/PWA application is hosted on Hatchable; this repository branch records the project overview and implementation notes.

## Live app
https://nexora-ai-nv88.hatchable.site

- Current live Hatchable version: **v66**
- Hatchable project: `proj_LfgsvYRQRBpg`
- Hatchable is the deployment source of truth. This GitHub branch is project documentation, not the live application source or an APK.

## Companion characters
- **KAI** — warm, friendly male best-friend style.
- **RYAN** — clear, confident male tech-friend and coding helper.
- **MAYA** — same-age anime-style study-mentor friend; explains school topics patiently and playfully.
- **ANGEL** — same-age anime-style classmate friend; sweet, caring, playful and gently teasing.
- **RIYA** — extra-caring, warm anime-style AI companion friend; supportive, expressive and occasionally playfully grumpy, without romantic-partner framing.
- **NEXORA** — central controller that routes voice commands to the requested companion.

All characters are AI companions, not real people. Character conversations should remain age-appropriate, respectful and non-possessive.

Each companion has a separate speech profile (voice preference, voice selection slot, rate and pitch). The browser build selects from voices installed on the user's device; availability and naturalness depend on Android/Windows/browser speech engines. This is a device-voice fallback, not a bundled premium neural voice pack.

## Current foundations
- Five selectable companion profiles: KAI, RYAN, MAYA, ANGEL and RIYA.
- Three.js avatar scene with VRM loading, humanoid expressions and MToon-compatible rendering.
- Five documented VRoid sample model assignments; only the selected companion model is loaded at a time.
- Browser speech recognition, wake phrase handling and device-dependent speech synthesis.
- Companion-specific speech settings and voice selection from device-installed voices.
- Local-first chat and memory storage, JSON backup/restore.
- Optional connection to a laptop-hosted local AI service.
- Signed-in account sync endpoint for chats and memories.
- Installable PWA shell.
- Safe Automation Command Center currently records and classifies tasks; it does not yet execute OS or third-party account actions.

## Voice quality roadmap
For consistent, higher-quality offline neural voices across Android and Windows, integrate a local TTS runtime such as Piper or Kokoro and bundle/download appropriately licensed voice models. This requires model downloads, storage, CPU/RAM testing and platform-specific packaging. No paid voice API is required for a local runtime, but model licenses and redistribution terms must be checked individually.

## Important limitations
- This repository branch is project documentation, not a compiled Android APK or Windows installer.
- Browser voice recognition may need internet and the app open; background wake is not guaranteed.
- Browser/device TTS voices vary by device. The five profiles apply distinct settings and choose different available voices where possible; guaranteed studio-quality unique voices require a bundled neural TTS runtime.
- The anime VRM assets are starter models, not bespoke final designs. The v66 renderer deployment has not yet been visually verified on the user's Android device.
- YouTube and other app shortcuts open official sites; they do not yet automate uploads or control signed-in accounts.
- The local AI brain needs a separately installed local model/runtime. No paid API is required for that local mode.
- Sample character model licensing must be checked before redistribution.
- Android native source mentioned in project notes still needs a build and real-device verification.

## Development
Use Hatchable to inspect, test and deploy app source. Use GitHub for project documentation, history, issue tracking and code review. Mirror verified implementation status into this documentation branch without treating it as the app's source of truth.
