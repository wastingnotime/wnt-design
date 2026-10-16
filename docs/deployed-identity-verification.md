# Deployed WNT identity verification

Tracking: [WNT-166](https://linear.app/wastingnotime/issue/WNT-166).
Review: **2026-10-16 UTC**. Kit: **Forward W v1.0.0**.
Result: **deployed identity review passed, with the evidence limitations below**.
WNT-160–165 were independently confirmed Done in Linear before this review.

## Deployed comparison

37 anonymous Chromium scenarios cover 1440 × 1000 and 390 × 1000 on all five
surfaces, plus 320 × 1000 on the three owned websites. Every navigation returned
200, every inspected identity image loaded, and none had horizontal overflow.
These are responsive browser checks, not physical-device tests. Desktop and
mobile compositions were visually inspected together; Sliding Tasks retains its
cream/rust palette, arrow, typography and product-first presentation. WNT stays
in its small footer signature.

Raw [browser results](identity/wnt-166/browser-results.json) record final URLs,
locale, metadata, loaded marks, header/footer links and keyboard outlines. The
[evidence index](identity/wnt-166/README.md) links captures and supporting results.
No live product or channel settings were changed during this audit.

| Surface | Final public routes / state | Result |
| --- | --- | --- |
| Community Lab | <https://wastingnotime.org/>, `/login`, `/agents` | Approved green mark + Community Lab descriptor; consistent favicon/social kit; Blog/GitHub/YouTube/Wishlist footer destinations. `/agents` presents the anonymous login gate. |
| Sliding Tasks | <https://wastingnotime.org/sliding-tasks/?lang=en>, `/sliding-tasks/privacy/`, `/sliding-tasks/pt-br/`, `/sliding-tasks/pt-br/privacy/` | EN and PT-BR landing/privacy checked explicitly. Localized secondary signature, decorative mark, parent-home link and privacy/contact links fit down to 320px. Product favicon unchanged. |
| Wishlist | <https://wastingnotime.org/wishlist> and trailing-slash form both settle at `/wishlist?view=voting&app=sliding-tasks`; `/wishlist/privacy`, `/wishlist/admin` | Shared mark, Wishlist descriptor, parent-home link, board/tabs and anonymous admin entry fit. All assets stay below `/wishlist/identity/v1.0.0/`; no HTML fallback mistaken for an image. |
| GitHub | <https://github.com/wastingnotime> | Forward W avatar and current product/foundation README are public. Six pins: wnt-design, wishlist, sliding-tasks, wnt-web, wnt-go, wnt-contracts. Website/product/YouTube links present. Light and dark captures inspected. |
| YouTube | <https://www.youtube.com/@wastingnotime>; metadata canonical channel `UCkKJr0sXMpLxniMR_C5_yow` | Approved avatar/banner visible at desktop and narrow widths. Current description names WNT; website and GitHub destinations preserved. Product thumbnails remain primary. |

## Geometry, versions and delivery provenance

[Asset results](identity/wnt-166/asset-results.json) contain status, content type,
bytes, SHA-256, ETag and Last-Modified for two requests to each of 13 deployed
assets. **All match their consumer's recorded files byte-for-byte**. Community
Lab and Wishlist marks/icons are unchanged v1.0.0 exports. Their distinct social
cards are consumer compositions. Sliding Tasks' muted mark preserves the geometry
with the documented `#645f5a` fill; its own favicon remains the product arrow.
GitHub/YouTube reencode uploaded images, so their match uses upload provenance
and visible geometry, not an assertion of byte identity.

| Owner | Implementation / settings record | Production desired-state revision |
| --- | --- | --- |
| Community Lab | [3386b6b](https://github.com/wastingnotime/community-lab/commit/3386b6b), maintenance follow-up `2e18625` | [infra-platform fac0227](https://github.com/wastingnotime/infra-platform/commit/fac0227fb76a9b17c2fd484d507f55d767c8fe63), web digest `sha256:47054adfbf9fe66a8e0c95d0df44a8e1df6a203ffbb0a30b728bf3e8dfc27275` |
| Sliding Tasks | [a179b1c](https://github.com/wastingnotime/sliding-tasks/commit/a179b1c), WNT-162 implementation record | [infra-platform cea5c3e](https://github.com/wastingnotime/infra-platform/commit/cea5c3e425eddb8476e8ace2a2bdd454aeea57b5), site digest `sha256:2646c8dce709af22775a6d942eca0c5aabce48008e50866a95ae01a4764c2321` |
| Wishlist | [PR #23](https://github.com/wastingnotime/wishlist/pull/23), `26304df`, CI follow-up `d207dfc` | [infra-platform 13ee399](https://github.com/wastingnotime/infra-platform/commit/13ee399e52a2d8dfd8508ef35e7a85daf8af987a), web digest `sha256:a55694db07f09168026a074c1389d2098d5e9523a7473ef19d7bb30e9613ccf0` |
| GitHub | [Profile PR #2](https://github.com/wastingnotime/.github/pull/2); avatar/bio/links/pins are separate organization settings, as recorded in WNT-164 | Current public profile freshly captured; approved `avatar.png` upload provenance from WNT-164 |
| YouTube | [WNT-165 settings and hashes](identity/wnt-165/README.md), published and reloaded in Studio | Fresh public desktop/mobile captures confirm visible rollout; Studio record confirms link destinations and watermark configuration |

Digests above are read from infra-platform's production stack manifests at
`fac0227`. Fresh public asset hashes prove deployed identity content. No Swarm
runtime inspection was performed, so this audit does not independently attest
that every runtime service is running those digests.

## Accessibility and small-size review

[Accessibility results](identity/wnt-166/accessibility-results.json) record
rendered colors, target bounds and parent-link activation. Normal text/link
contrast exceeds 4.5:1: Sliding Tasks maker/copyright **6.00:1** on `#fff8f3`;
Community Lab/Wishlist muted text **7.13:1** and green **16.64:1** on `#050706`.
Header background is translucent; these reported dark-site ratios use its base
near-black color. The footer measurements use opaque rendered backgrounds.
This scoped review is not a whole-product WCAG certification.

Tab reaches changed brand/footer links with visible 2px outlines. EN/PT-BR
Sliding Tasks and Wishlist maker links passed Shift+Tab/Tab return and Enter
activation to `https://wastingnotime.org/` in the same tab. Accessible names
retain “made by WNT” / “feito por WNT” and localized parent-home descriptions;
adjacent image alt is empty. Target heights meet the 24px minimum. The four
Sliding Tasks page variants all expose the appropriate localized name and focus.
No manual screen-reader session was performed.

[16/32px favicon inspection](identity/wnt-166/favicon-actual-sizes.png) confirms
the W silhouette at 16px and separated panels at 32px; the fetched ICO matches
the approved multi-size export. GitHub's square avatar and YouTube's circular
avatar retain all panels. See the [original circular crop preview](identity/wnt-165/avatar-studio-crop.jpg)
and [Studio desktop/mobile/TV crop proof](identity/wnt-165/banner-studio-crops.jpg).
The current narrow YouTube capture also retains the banner mark/name. GitHub
was captured in light/dark modes; owned sites retain their supported fixed dark
or cream palettes, with approved monochrome variants documented in the kit.

## Metadata, caching and channel history

Community Lab and Wishlist expose distinct OG/Twitter cards; every declared OG
image in the reviewed set returned 200 with an image content type, including
GitHub and YouTube platform-generated previews. See [social image responses](identity/wnt-166/social-image-results.json).
Sliding Tasks retains localized product title/description/canonical metadata
and its product favicon; it has no explicit OG image or Twitter card. This is
existing product metadata, not replaced by WNT artwork. Wishlist has no explicit
canonical or OG URL in the inspected head; its title/card assets are product-specific.
These omissions are recorded rather than claimed as successful rich-card checks.

Repeat asset requests returned identical hashes and validators; fresh browser
contexts and ordinary reloads showed the current identity. No Cache-Control was
present on the 13 inspected asset responses. Versioned paths and validators are
present, but this is not proof of refreshed third-party preview caches. No
Facebook/LinkedIn/X preview debugger or physical browser favicon-cache session
was run.

YouTube requirements rechecked on 2026-10-16 against
[YouTube Help](https://support.google.com/youtube/answer/10456525?hl=en): banner
minimum 2048 × 1152, recommended 2560 × 1440, safe content 1235 × 338 at minimum
size, maximum 6 MB; square watermark at least 150px and below 1 MB. The existing
kit and WNT-165 Studio crop evidence meet those requirements.

Historical purple thumbnails are **deliberately retained**, not rollout defects:
[Designing the First API](https://www.youtube.com/watch?v=H_7tcMsT6HY) and
[A Calm Approach to Software Architecture](https://www.youtube.com/watch?v=Raw9YeVapPk).
WNT-165 records the editorial rationale and future thumbnail/end-card guidance.
No videos need reuploading. Watermark playback and physical TV checks were not run.

## Evidence limitations and closure disposition

The deployed identity checks above pass. The following limitations remain visible
and are excluded from that pass; project completion records a delivered identity
rollout, not retroactive completion of unavailable historical evidence or a full
physical-device/accessibility certification:

- Before/after: recovered Community Lab desktop/320px baselines are copied into
  this evidence set; WNT-165 supplies the original YouTube desktop baseline.
  The initial review preserves written observations for all five surfaces.
  No pre-rollout mobile screenshots exist for YouTube/GitHub/Sliding Tasks/
  Wishlist in the available evidence, and no pre-rollout screenshots were
  recovered for the latter three. They cannot be recreated as historical facts.
- Mobile/TV: fresh responsive browser captures and existing Studio all-device
  crop previews cover layout/crop review. Physical devices, native YouTube app,
  TV rendering, watermark playback and manual assistive technology remain untested.
- Social previews: origin metadata/image delivery passes where declared;
  Sliding Tasks rich-image metadata and Wishlist canonical/OG URL omissions
  remain outside the identity-only rollout. External preview caches are unverified.
- Runtime: public rollout is observed; infrastructure desired-state digests are
  recorded without claiming an independent runtime digest attestation.

These are explicit scope/evidence exceptions owned by the corresponding surface
owners (WNT-161–165), not hidden failures or newly completed tests. All five
surface tasks and the final deployed identity review are delivered. The project
can be marked Completed with this qualified closure record attached.
