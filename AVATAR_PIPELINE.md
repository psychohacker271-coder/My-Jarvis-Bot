# NEXORA Avatar Pipeline

## Goal
Use full-body anime-human companions with anime facial styling, hair and clothing, humanoid movement and expressions. The VRoid sample models are starter assets, not finished bespoke character designs.

## Live baseline
- Hatchable project: `proj_LfgsvYRQRBpg`
- Live version: **v66**
- Live URL: https://nexora-ai-nv88.hatchable.site
- Renderer: `public/avatar3d.js`
- VRM runtime: `public/vendor/three-vrm.module.js` (@pixiv/three-vrm 3.5.5, MIT)
- Renderer uses the VRM loader, humanoid/expression support and MToon-compatible material path.
- Only the selected companion model is loaded at a time to limit mobile memory use.

## Five model assignments
The current renderer uses these upstream model URLs. Earlier project validation recorded HTTP 200 responses; recheck availability during future asset updates.

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

## v66 implementation
- Restored the documented five VRM model assignments after the interim GLB switch.
- Uses VRMLoaderPlugin and VRMUtils from the existing three-vrm runtime.
- Preserves the VRM humanoid rig and expression manager path, including blink and vowel-mouth expressions.
- Keeps the existing idle head/chest movement and lazy-loads only the active companion.
- Updated avatar cache version to `avatar3d.js?v=27`.
- Character personality profiles were updated separately in v65: MAYA is a same-age study-mentor friend, ANGEL a same-age classmate friend, and RIYA an extra-caring non-romantic AI companion friend.

## Validation status
- [x] VRM loader and runtime are present in the Hatchable project.
- [x] All five renderer assignments point to the documented VRM sample URLs in the v66 source.
- [x] Hatchable dry-run passed with no errors or warnings.
- [x] v66 deployed live.
- [ ] Recheck live browser loading of each external VRM URL.
- [ ] Visually verify full-body framing and appearance on Android.
- [ ] Check mobile memory/performance for each model.
- [ ] User visually approves all five character appearances.

## Character art direction
- KAI: male best friend; warm, casual, friendly.
- RYAN: male tech-smart friend; distinct silhouette and techwear direction.
- MAYA: same-age study mentor friend; cheerful and expressive.
- ANGEL: same-age classmate friend; gentle, playful and caring.
- RIYA: extra-caring supportive friend; warm and expressive.
- All: age-appropriate anime styling, detailed face/hair/clothing, natural full-body proportions, hands/fingers, expressive face, natural idle pose and no sexualized presentation.

## Next pass
After the five models are visually checked on-device, customize hair, clothing, palettes and individual facial styling under the applicable model terms. Do not call the art direction complete until the user approves the actual Android appearance.
