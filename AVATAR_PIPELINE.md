# NEXORA Avatar Pipeline

## Goal
Use five full-body 3D companions with distinct role-themed models, natural idle animation and speech movement. Load only the selected companion to reduce mobile memory use.

## Live baseline
- Hatchable project: `proj_LfgsvYRQRBpg`
- Live URL: https://nexora-ai-nv88.hatchable.site
- Current source of truth: Hatchable project files
- Renderer: `public/avatar3d.js`
- Runtime: Three.js + GLTFLoader + three-vrm (VRM files remain supported).

## Five local full-body models
The Hatchable project stores these files under `public/models/`:

| Companion | Local asset | Role direction |
|---|---|---|
| KAI | `/models/kai-human.glb` | Male gamer / warm best friend |
| RYAN | `/models/ryan-human.glb` | Male cyberpunk-tech / coding friend |
| MAYA | `/models/maya-human.glb` | Female study-mentor friend |
| ANGEL | `/models/angel-human.glb` | Female classmate friend |
| RIYA | `/models/riya-human.glb` | Female gentle, supportive companion |

### Structural validation
All five files returned HTTP 200 and passed GLB header/length checks:
- GLB magic: `glTF`
- GLB version: 2
- Each has a skinned mesh, skeleton nodes and one animation named `Idle`.
- Files are approximately 3.99–5.97 MB each.
- The renderer update uses same-origin local paths, so it no longer depends on external GitHub raw-file availability.

### Important review items
- Structural validation does not prove the rendered model looks correct.
- Check framing, face, clothing, model-to-role fit, idle animation and performance on Android.
- The existing files' original creator/license provenance still needs confirmation before redistribution.
- Do not mark character art direction complete until the user approves the visible models.

## Renderer behavior
- Loads only the selected model.
- Supports GLB through GLTFLoader and VRM through VRMLoaderPlugin.
- Fits model bounds to configured character height.
- Plays the GLB `Idle` animation where present.
- Attempts blink and viseme/mouth movement when the model exposes suitable morph targets.
- Shows a fallback status message if a model fails to load.

## GitHub research
- Open-source avatar registry: https://github.com/ToxSam/open-source-avatars
- VRM runtime: https://github.com/pixiv/three-vrm
- The registry documents individual collection licenses; verify the exact model license before copying or redistributing external assets.

## Next pass
1. Verify all five models visually in the live Android browser.
2. Confirm each model's outfit and silhouette fit its assigned role and remain age-appropriate.
3. Get user approval before declaring the art direction final.
