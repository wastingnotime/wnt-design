# Deployed WNT identity verification

Tracking: [WNT-166](https://linear.app/wastingnotime/issue/WNT-166).

## Current readiness — 2026-10-15

WNT-160 has since produced the selected [Forward W v1.0.0 kit](identity/README.md)
and [local validation](identity/validation-v1.0.0.md). The original blocker snapshot
below is historical; identity selection and kit preparation are now resolved.
The [WNT-165 YouTube rollout](identity/wnt-165/README.md) has now published
Forward W v1.0.0, recorded Studio device-safe crops, and retained the two
historical purple thumbnails by explicit editorial decision. Physical-device
and final cross-surface checks remain with WNT-166. Other rollout statuses
require fresh verification.

## Initial readiness snapshot — 2026-10-15

**Blocked on identity selection and rollout. No final verification has passed.**

The Linear issues and their comments were checked on this date. WNT-160 through
WNT-165 are all in Backlog, with no comments recording selection, deployment or
acceptance evidence. The local [initial review](visual-identity-review.md) also
states that the logo is not selected. The repository contains imported image
assets, but no approved, versioned identity kit. These facts establish missing
review prerequisites; they do not constitute a fresh inspection of live sites.

| Prerequisite | Required handoff | Recorded status |
| --- | --- | --- |
| [WNT-160](https://linear.app/wastingnotime/issue/WNT-160) | Henrique's selection, approved masters, export version and usage rules | Backlog; blocks all rollout tasks |
| [WNT-161](https://linear.app/wastingnotime/issue/WNT-161) | Community Lab deployment, PR and asset version | Backlog |
| [WNT-162](https://linear.app/wastingnotime/issue/WNT-162) | Sliding Tasks EN/PT-BR landing/privacy deployment and asset version | Backlog |
| [WNT-163](https://linear.app/wastingnotime/issue/WNT-163) | Wishlist deployment, base-path metadata and asset version | Backlog |
| [WNT-164](https://linear.app/wastingnotime/issue/WNT-164) | GitHub profile PR, organization settings change and asset version | Backlog |
| [WNT-165](https://linear.app/wastingnotime/issue/WNT-165) | YouTube settings change, asset version and historical-thumbnail decision | Backlog |

## Evidence record

Capture a baseline before each rollout while the old surface is still available.
The initial review is desktop/source observation only; it supplies neither mobile
nor accessibility evidence. If a baseline cannot be recovered, record the missing
evidence explicitly rather than reconstructing it as a historical screenshot.

For each check, record the date, requested and final URL, browser, viewport,
theme, locale, before/after capture paths, deployed revision or settings-change
record, approved kit version, observed result and any exception's owner and issue.
Use `not run`, `pass`, `fail` or `blocked`; a checklist entry alone is not evidence.
Record actual mobile-device checks separately from browser viewport emulation.
Keep public captures free of account information and private repositories.

## Surface coverage

All checks below are **not run**. URLs are review entry points from the rollout
issues, not verified final destinations. Discover secondary routes from the live
navigation and record redirects and final URLs during execution.

| Surface | Entry point | Required review |
| --- | --- | --- |
| Community Lab | <https://wastingnotime.org/> | Desktop/mobile header, footer and relevant secondary routes; shared mark and descriptor; favicon, Apple icon and social image; product/channel links |
| Sliding Tasks | <https://wastingnotime.org/sliding-tasks/> | Explicit EN and PT-BR landing and privacy routes; localized secondary maker link; narrow footer wrapping; privacy/contact links; product logo, favicon, colors, typography and thumbnails remain primary |
| Wishlist | <https://wastingnotime.org/wishlist> and <https://wastingnotime.org/wishlist/> | Both entry forms and redirects; privacy/admin headers where accessible; parent-home link; assets resolve under deployment base; Wishlist metadata is distinct from Community Lab; board, tabs and auth entry layout |
| GitHub organization | <https://github.com/wastingnotime> | Public avatar in square/circular contexts, profile in light/dark themes, current introduction, featured public repositories and website/product/YouTube links; distinguish `.github` PR from settings changes |
| YouTube | <https://www.youtube.com/@wastingnotime> | Avatar matches approved kit/GitHub; banner desktop/mobile/TV crops; description and website/GitHub links; restrained future-video signature and explicit historical-thumbnail treatment |

## Acceptance checks

- [ ] Capture before/after desktop and mobile views of all five surfaces. Include
  header/footer detail and enough context to assess the product/parent hierarchy.
- [ ] Compare each WNT mark with the approved SVG geometry and export manifest.
  Record the kit version and deployed asset URLs or uploaded export filenames.
  Byte-identical assets can be matched by hash; platform-reencoded images need
  upload provenance and visual comparison. Sliding Tasks keeps its own favicon.
- [ ] Inspect approved favicons at actual 16px and 32px sizes, avatars in square
  and circular crops, and marks against supported light/dark backgrounds.
- [ ] Measure rendered text/link contrast, including muted footer attribution,
  using actual foreground/background colors. Record ratios and the applicable
  accessibility criteria; screenshots alone do not prove contrast compliance.
- [ ] Navigate changed headers, footers and attribution links by keyboard. Record
  focus visibility, order, activation target and accessible names. Inspect icon
  links in the accessibility tree and check localized attribution wording.
- [ ] Verify all four Sliding Tasks locale/page combinations explicitly instead
  of relying on browser-language redirects. Check narrow-screen wrapping and that
  WNT endorsement remains visually secondary.
- [ ] Resolve Wishlist asset URLs from both entry forms and secondary routes;
  verify status, content type and content, since a successful HTML fallback is
  not a successfully loaded image. Check parent-home and channel cross-links.
- [ ] Inspect deployed HTML social metadata and fetch its image URLs. Record
  canonical URL, title, description, Open Graph/Twitter values, image identity
  and response headers. Distinguish metadata verification from an actual social
  platform preview; record unavailable preview checks as exceptions.
- [ ] Compare fresh and repeat requests after rollout. Record cache headers,
  redirects, validators and asset identity; check ordinary browser reload and a
  fresh browser context for stale favicon/social assets. Record external preview
  cache limitations rather than treating origin freshness as proof of refresh.
- [ ] Verify YouTube's current upload requirements at execution time and record
  the source and date. Capture the banner's desktop, mobile and TV crop previews;
  critical content must remain readable inside the approved safe area.
- [ ] Record WNT-165's explicit decision to retain or update historical purple
  thumbnails, with affected video URLs and rationale. A decision is still pending;
  do not infer it from their continued presence. Branding does not require video
  reuploads.
- [ ] Record final URLs, PRs, deployed revisions, settings changes and remaining
  exceptions with evidence links. Resolve failures with the owning surface task
  and repeat affected checks after deployment.

## Completion gate

WNT-166 and the project remain open until the approved kit is recorded, all five
surface tasks are complete, and this review passes. An unresolved exception must
remain visible and cannot silently count as a pass. Attach completed evidence to
this record when execution becomes possible; this preparation does not certify
the deployed identity or accessibility of any surface.
