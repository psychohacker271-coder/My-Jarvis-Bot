# NEXORA Avatar Pipeline

## Goal
Use five full-body 3D companions with role-themed models, natural idle animation and facial speech movement. Load only the selected companion to reduce mobile memory use.

## Live baseline
- Hatchable project: `proj_LfgsvYRQRBpg`
- Live URL: https://nexora-ai-nv88.hatchable.site
- Live version: **v70**
- Renderer: `public/avatar3d.js`
- Runtime: Three.js + GLTFLoader + three-vrm (VRM files remain supported).

## Five local full-body models
The Hatchable project stores these files under `public/models/`:

| Companion | Local asset | GLB scene/mesh name | Role direction |
|---|---|---|---|
| KAI | `/models/kai-human.glb` | `The_Gamer` | Male gamer / warm best friend |
| RYAN | `/models/ryan-human.glb` | `The_Cyberpunk_Hacker` | Male tech / coding friend |
| MAYA | `/models/maya-human.glb` | `The_Female_Executive` | Female study-mentor friend; visual role fit needs review |
| ANGEL | `/models/angel-human.glb` | `The_Flight_Attendant` | Female classmate friend; visual role fit needs review |
| RIYA | `/models/riya-human.glb` | `RIYA` | Female gentle, supportive companion |

### Structural validation (v68)
All five files returned HTTP 200 after v69 deployment and passed GLB header/length checks:
- GLB magic: `glTF`; version: 2.
- Each has a skinned mesh, skeleton nodes and one animation named `Idle`.
- Each has 34 facial morph targets, including eye blinks and visemes.
- Files are approximately 3.99–5.97 MB each.
- Renderer uses same-origin local paths and loads only the selected character.

### Important review items
- Structural validation does not prove that the rendered model looks correct.
- Check framing, face, clothing, model-to-role fit, age-appropriate styling, idle animation and performance on Android.
- Maya and Angel's scene names indicate executive/flight-attendant themed starter models; confirm whether their visible appearance fits their established same-age study-mentor/classmate roles. Replace them with better-fitting licensed assets if not.
- Existing files' original creator/license provenance still needs confirmation before redistribution.
- Do not mark character art direction complete until the user approves the visible models.

## Renderer behavior
- Loads only the selected model.
- Supports GLB through GLTFLoader and VRM through VRMLoaderPlugin.
- Fits model bounds to configured character height.
- Plays the GLB `Idle` animation where present.
- Uses facial morph targets for blink and vowel/viseme mouth movement where available.
- Shows a fallback status message if a model fails to load.

## GitHub research
- Open-source avatar registry: https://github.com/ToxSam/open-source-avatars
- VRM runtime: https://github.com/pixiv/three-vrm
- The registry documents individual collection licenses; verify the exact model license before copying or redistributing external assets.

## Next pass
1. Visually verify all five models in the live Android browser.
2. Confirm each outfit and silhouette fit the assigned role and remain age-appropriate.
3. Replace Maya/Angel models if their actual appearance does not fit their established roles.
4. Get user approval before declaring the art direction final.
