# Identity v1.0.0 validation

Date: 2026-10-15. Scope: local production assets for WNT-160, selected direction B.
This is not WNT-166 deployed verification.

## Results

| Check | Result / evidence |
| --- | --- |
| Editable geometry | Four Bézier paths in `masters/mark.svg`; all 17 production SVG exports contain the exact same path data |
| Production independence | Export SVGs have no text nodes, raster embeds, scripts, foreign objects or external references; lettering is outlined |
| Light/dark and monochrome | [Specimen](v1.0.0-specimen.png) inspected: flat mint on dark, dark on cream, white on dark |
| Favicon sizes | Native 16/32/48px renders inspected in the specimen; W silhouette and ascending terminal remain readable. Fold gaps become antialiased at 16px; the silhouette does not depend on seeing every gap |
| ICO integrity | ICO has precisely 16/32/48px frames; decoded pixels match the respective native PNG renders |
| Avatar crops | Square and circular construction inspected in the specimen; all four panels remain inside the crop |
| Maker hierarchy | 24px-wide monochrome mark beside 14px EN/PT-BR text in specimen; product name remains prominent. This is a static specimen, not live Sliding Tasks |
| Banner crops | [Crop proof](v1.0.0-banner-crops.png) inspected at full TV canvas, illustrative desktop strip, proportionally scaled minimum safe region and conservative inner region; no essential artwork cut off |
| Channel file limits | Banner PNG below 6 MB; both watermark PNGs are transparent RGBA, 150 × 150 and below 1 MB |
| Integrity / repeatability | All 32 manifest entries matched SHA-256; rebuilding a second time with the recorded tool versions produced a byte-identical manifest |

The specimen's “actual size” icon row refers to native pixels in the 1400px-wide
artifact. A chat or document viewer may scale the overall sheet; inspect the
individual PNGs at 100% for a device-pixel comparison. Circle/banner proofs are
constructed from the exact vector export geometry, not platform screenshots.

## Measured contrast

Computed from sRGB linearization and relative luminance `(lighter + .05) /
(darker + .05)` in the export script; full precision is used before reporting.

| Foreground / background | Ratio | Decision |
| --- | --- | --- |
| `#9cffaa` / `#101813` | 14.8853:1 | Approved dark-context pair |
| `#101813` / `#fff8f3` | 17.1873:1 | Approved light-context pair |
| `#ffffff` / `#101813` | 18.0709:1 | Approved reversed monochrome pair |
| Sliding Tasks `#645f5a` / `#fff8f3` | 6.0045:1 | Suitable existing footer colors for normal attribution text |
| `#9cffaa` / `#fff8f3` | 1.1546:1 | Do not use for maker attribution or text |

Criteria: [WCAG text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
YouTube upload dimensions and limits were checked against
[YouTube Help](https://support.google.com/youtube/answer/10456525?hl=en) on this date.

## Reproduction and remaining consumer work

Run `python3 scripts/export-identity.py` from the repository root with Pillow and
`rsvg-convert` available. Exact versions, pixel sizes and hashes are in the
[manifest](../../assets/identity/v1.0.0/manifest.json). Masters are committed, so no
image-generation service or font installation is required for export.

WNT-161–165 must still verify rendered focus, accessible names, responsive footer
wrapping, platform upload crop previews, asset paths, social metadata and caching.
No production site or organization/channel settings were changed. Historical
thumbnail treatment remains a WNT-165 editorial decision. WNT-166 remains the
completion gate for deployed consistency.
