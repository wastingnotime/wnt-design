# WNT-166 evidence — 2026-10-16 UTC

[Final report](../../deployed-identity-verification.md) contains results,
provenance and explicit limitations. Anonymous headless Chromium; English
browser locale; responsive viewports, not physical devices.

- [Browser results](browser-results.json): 37 routes/viewport scenarios, metadata,
  final destinations, identity image loading and keyboard focus records.
- [Asset responses and hashes](asset-results.json): 13 assets, twice each.
- [Accessibility and activation](accessibility-results.json).
- [Social-image responses](social-image-results.json).
- [Favicons at actual 16/32px](favicon-actual-sizes.png).

Screenshot names are `<surface>-<width>.jpg`, full page at 1000px viewport height:

| Surface | Desktop | Narrow |
| --- | --- | --- |
| Community Lab | [1440](community-1440.jpg) | [390](community-390.jpg), [320](community-320.jpg) |
| Sliding Tasks EN | [1440](sliding-en-1440.jpg) | [390](sliding-en-390.jpg), [320](sliding-en-320.jpg) |
| Sliding Tasks EN privacy | [1440](sliding-en-privacy-1440.jpg) | [390](sliding-en-privacy-390.jpg), [320](sliding-en-privacy-320.jpg) |
| Sliding Tasks PT-BR | [1440](sliding-pt-1440.jpg) | [390](sliding-pt-390.jpg), [320](sliding-pt-320.jpg) |
| Sliding Tasks PT-BR privacy | [1440](sliding-pt-privacy-1440.jpg) | [390](sliding-pt-privacy-390.jpg), [320](sliding-pt-privacy-320.jpg) |
| Wishlist | [1440](wishlist-1440.jpg) | [390](wishlist-390.jpg), [320](wishlist-320.jpg) |
| Wishlist trailing slash | [1440](wishlist-slash-1440.jpg) | [390](wishlist-slash-390.jpg), [320](wishlist-slash-320.jpg) |
| Wishlist privacy | [1440](wishlist-privacy-1440.jpg) | [390](wishlist-privacy-390.jpg), [320](wishlist-privacy-320.jpg) |
| Wishlist admin | [1440](wishlist-admin-1440.jpg) | [390](wishlist-admin-390.jpg), [320](wishlist-admin-320.jpg) |
| GitHub | [light](github-1440.jpg), [dark](github-dark-1440.jpg) | [390](github-390.jpg) |
| YouTube | [1440](youtube-1440.jpg) | [390](youtube-390.jpg) |

`community-login-*` and `community-agents-*` record anonymous secondary routes.
Recovered pre-rollout Community Lab [desktop](before-community-1440.png) and
[320px](before-community-320.png) captures come unchanged from community-lab's
`work/changes/wnt-161-identity/evidence/baseline-*-home.png`. Other available
historical channel/crop evidence remains under [WNT-165](../wnt-165/README.md).
