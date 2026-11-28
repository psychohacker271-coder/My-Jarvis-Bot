# NEXORA Avatar Pipeline

## Goal
Replace the current MakeHuman/Ara3D humanoid GLBs. The live KAI model shown in the user's Android screenshot is toy-like and does not meet the requested realistic-anime human style.

## Current live baseline
- Hatchable project: `proj_LfgsvYRQRBpg`
- Live version: v57
- Renderer: `public/avatar3d.js`
- Current assets: `public/models/{kai,ryan,maya,angel,riya}-human.glb`
- User screenshot confirms the current KAI result is unacceptable (rounded toy-like face/body, mitten-like hands, simplified clothing).

## Candidate asset source
- Repository: https://github.com/madjin/vrm-samples
- README identifies the CC0 sample collection separately from AvatarSample A/B/C, which have additional usage conditions.
- Candidate imported for evaluation only: `Avatar_Orion.vrm` (6,148,340 bytes), sourced from the repository's master branch.
- Source license notes: https://vroid.pixiv.help/hc/en-us/articles/4402614652569-Do-VRoid-Studio-s-sample-models-come-with-conditions-of-use
- Do not treat all VRoid sample files as CC0. Check each model's metadata and the source's license notes before bundling or redistributing.

## Integration requirements
1. Inspect candidate model appearance and VRM metadata before selecting it.
2. Use a VRM-aware Three.js loader (for example, `@pixiv/three-vrm`) rather than assuming a VRM file is an ordinary GLB.
3. Preserve MToon materials, humanoid bone mapping, expressions, blink, visemes, and spring-bone hair physics where supported.
4. Select five distinct character assets or create five genuinely distinct derivatives with permitted edits. Do not merely recolor one model.
5. Keep each model mobile-friendly: lazy-load selected avatar, compress textures, measure download size and frame rate on Android.
6. Test all five names individually on mobile viewport and obtain user visual approval before calling the art direction complete.

## Character art direction
- KAI: male, friendly best-friend energy; casual modern outfit.
- RYAN: male, tech-smart; distinct hairstyle and techwear outfit.
- MAYA: female, cheerful best friend; distinct hairstyle and casual outfit.
- ANGEL: female, gentle and affectionate; elegant modern outfit.
- RIYA: female, caring and confident; distinct hairstyle and outfit.
- All: complete full-body anatomy, natural hands/fingers, proportionate head/body, detailed hair/clothes, natural A-pose/idle, no T-pose, no toy-like rounded limbs.

## Status
- [x] User screenshot reviewed; current look rejected.
- [x] Candidate CC0 VRM sample imported into Hatchable for evaluation (not yet deployed).
- [ ] Inspect candidate appearance and metadata.
- [ ] Integrate VRM loader and validate candidate.
- [ ] Source/author five distinct licensed character models.
- [ ] Optimize and test Android performance.
- [ ] User approves all five appearances.
