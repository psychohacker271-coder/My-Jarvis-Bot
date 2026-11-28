# NEXORA Avatar Pipeline

## Goal
Replace the rejected toy-like MakeHuman/Ara3D bodies with full-body anime-human companions, inspired by high-quality shonen anime proportions and shading (not copied Demon Slayer characters).

## Live baseline after this avatar pass
- Hatchable project: `proj_LfgsvYRQRBpg`
- Live version: v59
- Live URL: https://nexora-ai-nv88.hatchable.site
- Renderer: `public/avatar3d.js`
- VRM runtime: `public/vendor/three-vrm.module.js` (@pixiv/three-vrm 3.5.5, MIT)
- Renderer uses MToon materials and VRM humanoid/expression support. It lazy-loads only the selected companion to limit mobile memory use.

## Five model assignments
All five model URLs returned HTTP 200 and have distinct file sizes. The runtime fetches the active model from the upstream public repository (not copied into the app bundle).

| Companion | Model | Source path | License notes |
|---|---|---|---|
| KAI | HairSample_Male | `vroid/beta/HairSample_Male.vrm` | VRoid sample CC0 |
| RYAN | AvatarSample_C | `vroid/stable/AvatarSample_C.vrm` | VRoidPreset A–Z terms permit use, alteration and redistribution; copyright remains with pixiv |
| MAYA | HairSample_Female | `vroid/beta/HairSample_Female.vrm` | VRoid sample CC0 |
| ANGEL | AvatarSample_A | `vroid/stable/AvatarSample_A.vrm` | VRoidPreset A–Z terms permit use, alteration and redistribution; copyright remains with pixiv |
| RIYA | AvatarSample_B | `vroid/stable/AvatarSample_B.vrm` | VRoidPreset A–Z terms permit use, alteration and redistribution; copyright remains with pixiv |

Sources:
- Models: https://github.com/madjin/vrm-samples
- Official VRoid sample-model license overview: https://vroid.pixiv.help/hc/en-us/articles/4402614652569-Do-VRoid-Studio-s-sample-models-come-with-conditions-of-use
- AvatarSample A–Z terms: https://vroid.pixiv.help/hc/en-us/articles/4402394424089-VRoidPreset-A-Z
- three-vrm: https://github.com/pixiv/three-vrm

## Implementation shipped in v59
- Replaced the previous MakeHuman GLB selection with five separate VRM models.
- Added VRMLoaderPlugin and VRMUtils integration from three-vrm.
- Preserves VRM MToon/anime materials, humanoid rig and facial expression system.
- Added blink, vowel-mouth expressions, subtle head/chest idle movement.
- Loads only the selected companion model.
- NEXORA blue central core and the existing companion switching interface remain in place.
- No automatic fallback to the old toy-like GLB models.

## Validation status
- [x] Rejected MakeHuman GLBs no longer used by the active renderer.
- [x] All five upstream model URLs verified with HTTP 200 and content lengths.
- [x] VRM loader added and deploy validators pass.
- [x] v59 deployed live.
- [ ] Browser visual test blocked by Hatchable browser-farm 504 timeout.
- [ ] Verify each character's actual appearance and full-body framing on Android.
- [ ] Optimize VRM textures/download sizes if Android performance needs it.
- [ ] User visually approves all five character appearances.

## Character art direction
- KAI: male best friend; warm, casual, friendly.
- RYAN: male tech-smart friend; distinct silhouette and techwear direction.
- MAYA: female best friend; cheerful and expressive.
- ANGEL: female affectionate companion; gentle, elegant styling.
- RIYA: female caring companion; confident, warm styling.
- All: complete full-body anatomy, visible natural hands/fingers, detailed anime face/hair/clothing, proportionate head/body, natural idle pose, no T-pose, no toy-like rounded limbs.

## Important next pass
The VRoid sample models are a substantial move toward actual anime-human bodies, but they are starter assets, not finished bespoke NEXORA character designs. After the five are visually checked on-device, customize hair, clothing, palettes and individual facial styling under the applicable model terms. Do not call the art direction complete until the user approves the actual Android screenshots.
