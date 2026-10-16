# WNT identity and maker signature

Current kit: [v1.0.0 — Forward W](../../assets/identity/v1.0.0/README.md).
Direction B was selected by Henrique on 2026-10-15 because it is distinguishable.
The [selection record](../wnt-160-logo-selection.md) preserves the exploration.
[Specimen](v1.0.0-specimen.png) · [banner crop proof](v1.0.0-banner-crops.png) ·
[validation](validation-v1.0.0.md).

## Mark, palette and sizes

Use the supplied four-panel geometry without redrawing, stretching, rotating,
adding gradients, adding outlines, or closing the fold separations. Use one solid
color. Use the full-name wordmark for parent-brand artwork, and live product
names/descriptors in the consumer's own typography. Keep asset aspect ratios.

| Role | Value | Use |
| --- | --- | --- |
| WNT green | `#9cffaa` | Mark/brand text on near-black |
| WNT ink | `#101813` | Dark background or monochrome mark on light backgrounds |
| Warm paper | `#fff8f3` | Optional light background and lettering on dark |
| White / black | `#ffffff` / `#000000` | Monochrome reproduction |

Green is optional for maker attribution. Do not put mint text or a mint maker
mark on a light background: mint/paper contrast is only 1.15:1. Approved green/ink
contrast is 14.89:1; ink/paper is 17.19:1. Other product colors require measurement.
Use at least 4.5:1 for normal-sized attribution text and a 3:1 minimum for its mark
as a WNT readability rule. Logo text has a WCAG exception, but attribution prose
still needs readable contrast. See [WCAG contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

The mark's source viewBox is 128 × 96. Reserve clear space of **16 source units**
(one eighth of the viewBox width) outside its painted silhouette; viewBox padding
alone does not provide all of that clear space. At 32px viewBox width this is 4px.
Exported avatar/lockup padding is intentional. Favicons are the sole tight-space
exception and use the supplied square tile. Do not crop individual panels.

- Normal standalone mark: minimum 24px viewBox width; prefer 32px in site headers.
- Maker signature: 24px mark viewBox width beside at least 14px readable live text.
- Full 640 × 128 lockup: minimum rendered width 240px; below that use mark + live
  text. Never shrink the complete lockup to make a favicon or avatar.
- Favicons: supplied 16/32/48px renders. At 16px, recognize the W silhouette; fine
  fold separation is secondary. Never derive these by downscaling the avatar.
- Avatar: upload the 800px square; retain the centered 70%-width mark placement.
  Display at least 32px where the consumer controls size. The circular crop must
  contain every panel; do not enlarge the mark inside a platform crop editor.

## Maker signature contract

Destination: **https://wastingnotime.org/**. Use a normal link in the same tab.
The parent mark identifies the maker; a product's logo, favicon, palette,
typography, hero, screenshots and navigation remain its own.

| Locale | Visible text | Accessible link name |
| --- | --- | --- |
| EN | `made by WNT` | `made by WNT — Wasting No Time home` |
| PT-BR | `feito por WNT` | `feito por WNT — página inicial da Wasting No Time` |

Keep the visible words in the accessible name. Treat the adjacent mark as
decorative when the link already contains the text: empty image alt or an
accessibility-hidden inline graphic. An icon-only parent link instead needs the
localized name “Wasting No Time home” / “página inicial da Wasting No Time”.
Do not rely on an SVG title to label an external image or link.

Place the signature in the footer, separated from the primary product identity.
Use the product's normal text style and an appropriate monochrome color; in
Sliding Tasks the existing muted `#645f5a` on cream measures 6.00:1. Keep the mark
and phrase together, with an 8px gap. Permit the footer's groups to wrap at narrow
widths without overlap, clipping, or displacement of privacy/contact links.
Do not turn the signature into a large badge, headline or primary action.

Use native link keyboard behavior. Provide an unclipped visible focus indicator;
a 2px solid outline with 3px offset is the baseline, in a color with at least 3:1
contrast against adjacent surfaces. Preserve a system-visible indicator in forced
colors. The link must remain discoverable without relying on color alone (for
example, underline the text) and have at least a 24 × 24 CSS-pixel target area.
Consumers must verify Tab/Shift+Tab, Enter activation, zoom and screen-reader name
in their rendered pages. This document defines behavior; it supplies no framework
component. See [WCAG focus guidance](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html).

## Channels and video

Use the same avatar export for GitHub and YouTube. Community Lab and Wishlist
pair the shared mark with their own descriptors. Sliding Tasks uses the maker
signature and retains its own product mark and favicon.

The supplied YouTube banner is 2560 × 1440. All essential content fits within a
centered **1235 × 338** rectangle on that full canvas, a deliberately conservative
inner region. YouTube documents that safe size at its smaller 2048 × 1152 minimum;
scaling it proportionally to this canvas gives 1543.75 × 422.5. The proof includes
both regions, the full image and an illustrative desktop strip. Check the actual
Studio preview during WNT-165; these constructions are not screenshots of devices.
The file is under the current 6 MB limit. Requirements were checked on 2026-10-15
against [YouTube Help](https://support.google.com/youtube/answer/10456525?hl=en).

For future product thumbnails, lead with the product's identity and content.
A monochrome WNT signature can sit in a quiet upper corner, clear of the topic and
platform overlays. At 1280 × 720, use a signature about 96–128px wide with at least
24px inset; inspect it at the actual thumbnail display size. Do not use green as a
mandatory product background. Place the signature on a calm contrasting region.
The supplied 320 × 96 transparent artwork is a starting asset, not a thumbnail.

The end-card provides a lower, secondary maker signature. Product title, next
video and calls to action belong in its open area; preview platform end-screen
overlays before publishing. The white/dark 150px transparent watermark variants
must be chosen for the video background and kept subordinate to content. YouTube
currently requires square watermarks at least 150px and below 1 MB; both qualify.

Historical purple thumbnails are retained as historical artwork. The
[WNT-165 rollout record](wnt-165/README.md) lists the affected URLs, rationale,
uploaded asset hashes and Studio crop evidence. Do not reupload historical
videos solely for branding.

## Ownership, compatibility and rollout

This is shared identity evolution owned by `wnt-design`: one recognizable WNT
geometry, export version and maker-link meaning across existing consumers.
Maintaining separate hand-drawn marks already produces inconsistent channel and
site identity. Centralizing the masters and export provenance removes that drift;
product behavior and framework implementation stay with consumers.

The public surface is the versioned kit path, manifest, geometry and usage rules.
Version 1.0.0 is the first selected kit. It supersedes the imported hourglass for
new WNT channel branding; imported files and exploration boards remain historical
reference, not current assets. A shape, palette or naming change requires a new
versioned directory. Do not overwrite a version already adopted by a consumer.
Regenerating with different rendering tools may change bytes; preserve an adopted
manifest, and publish a new version if outputs differ.

| Consumer | Current baseline | Migration / owner |
| --- | --- | --- |
| Community Lab | Framed `cl` header, hourglass favicon | WNT-161: first site adoption, descriptor, icons/social assets |
| Sliding Tasks site | Product logo/colors, plain copyright footer | WNT-162: localized EN/PT-BR landing/privacy maker links only |
| Wishlist | Framed `wl`, missing explicit local favicon/social declarations in initial review | WNT-163: shared mark, parent link, base-path-safe asset URLs |
| GitHub organization / `.github` | Historical purple avatar and profile | WNT-164: settings upload and separate profile changes |
| YouTube | Historical avatar/banner and mixed thumbnails | WNT-165: settings upload, previews and thumbnail decision |

Produce this kit first; migrate and validate Community Lab as the first consumer,
then deliver other consumers independently. Each records kit version, export
hashes, PR/deployed revision or settings change, final URL and screenshots. Serve
assets through the consumer's supported base path; don't hotlink local repository
paths. Use versioned URLs when caching; measure the deployed result. Product social
cards and metadata remain product-specific.

No consumer has been migrated by WNT-160. Keep prior deployed assets available for
rollback until each adoption passes. WNT-166 owns final deployed comparison and
project closure; local kit validation cannot replace that audit.
