# WNT identity v1.0.0 — Forward W

Selected direction: **B**, by Henrique on 2026-10-15: “i prefer B, is very
distinguishable.” The vector production rendition retains the four folded panels
and rising right terminal, uses flat fills, and opens the separations for small
sizes. This directory is the versioned consumer kit, not proof of deployment.

- `masters/mark.svg`: editable four-path geometry; inherits `currentColor` when
  inlined. Its viewBox is 128 × 96. External image usage defaults to black; use
  an explicit-color export for external images.
- `masters/wordmark.svg`, `masters/initials.svg`: editable outlined lettering.
- `exports/mark-{green,dark,white,black}.svg`: transparent single-color marks.
- `exports/lockup-{dark,light,mono-dark,mono-white}.svg`: full-name lockups;
  `dark`/`light` include a background, `mono-*` are transparent.
- `exports/avatar.{svg,png}`: 800 × 800; square upload, safe for a circular crop.
- `exports/favicon.svg`, `favicon-{16,32,48}.png`, `favicon.ico`: opaque dark tile;
  native renders at each ICO size, same mark geometry.
- `exports/apple-touch-icon.{svg,png}`: opaque 180 × 180.
- `exports/social.{svg,png}`: 1200 × 630 parent-brand social card. Products should
  compose their own metadata imagery; this card is not a universal product card.
- `exports/youtube-banner.{svg,png}`: 2560 × 1440, centered content.
- `exports/video-watermark{,-dark}.{svg,png}`: transparent 150 × 150, white/dark.
- `exports/thumbnail-signature.svg`: transparent white mark + WNT initials.
- `exports/end-card.{svg,png}`: 1920 × 1080 with a restrained lower signature and
  open space for the video's product content.
- `manifest.json`: file hashes, dimensions, source pointers, palette, contrast
  measurements and rendering-tool versions. The manifest excludes itself.

Read [usage and adoption](../../../docs/identity/README.md) and
[validation](../../../docs/identity/validation-v1.0.0.md) before integration.
Rebuild exports from the repository root with `python3 scripts/export-identity.py`.
Requires Python 3, Pillow and `rsvg-convert`; production masters need no fonts.
Use the renderer versions recorded in the manifest for byte-identical output.

Provenance: the concept board was generated with the built-in image generation
service, then the selected mark was reconstructed as four editable Bézier paths.
The production vector is not an automatic trace or an embedded raster. Its full
geometry is in `masters/mark.svg`. Lettering is Lato Bold, outlined using fontTools
from `/usr/share/fonts/truetype/lato/Lato-Bold.ttf`, SHA-256
`e0b1c4de011de8dd077cf21f97919fc31158eb290ee1176cbae06d500a6304bc`.
The text is “Wasting No Time” / “WNT”, 64-unit size, glyph advances without kerning,
baseline 66 on an 88-unit-high canvas. Lato is by Łukasz Dziedzic, licensed under
SIL OFL 1.1; no font binary is distributed. Outlined artwork has no runtime font
dependency. Consumers keep their own typography for surrounding live text.
