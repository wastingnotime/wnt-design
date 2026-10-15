# WNT visual identity review

Initial review: 2026-10-15. The findings below describe the pre-rollout baseline.
Update: Henrique selected **B — Forward W**; the [v1.0.0 kit](identity/README.md)
is available with local validation. Consumer rollout remains open.

Coordination: [WNT — Visual Identity & Product Attribution](https://linear.app/wastingnotime/project/wnt-visual-identity-and-product-attribution-4019f7abeeb8), WastingNoTime team.

## Direction

Green is the current WNT direction. Purple belongs to the earlier identity.
The selected mark is **Forward W**, recorded in [WNT-160 selection](wnt-160-logo-selection.md).
The hourglass/arrow exploration and imported hourglass assets are historical references.
Imported artwork is cataloged in the [historical archive](../assets/archive/pre-forward-w/README.md).

WNT channels share the selected mark and identity. Products may keep their own colors, typography, logo and tone. A small linked “made by WNT” signature connects those products to the parent identity; a monochrome variant should fit the product palette. Localize the signature where appropriate. Product identity remains primary.

This repository owns editable master assets, identity guidance, export provenance and asset versions. Consumers implement their own platform-specific integration.

## Findings and handoffs

| Surface / owner | Observed | Planned work |
| --- | --- | --- |
| [Community Lab](https://wastingnotime.org/) / `community-lab` | Mint on near-black, monospace, framed `cl` badge and `wnt / community lab`. Green hourglass favicon differs from the header badge. Footer links Blog and GitHub. | Shared WNT mark plus Community Lab descriptor; aligned favicon/social assets; channel links. WNT-161. |
| [Sliding Tasks](https://wastingnotime.org/sliding-tasks/) / `sliding-tasks` | Cream, rust arrow icon, green accents, Outfit/DM Sans in source. EN/PT-BR landing/privacy pages have copyright attribution but no linked maker signature. | Add subtle localized WNT signature to the site; preserve product logo, favicon, palette and typography. WNT-162. |
| [Wishlist](https://wastingnotime.org/wishlist) / `wishlist` | Mint on near-black, framed `wl` badge, `wnt / wishlist`, WNT footer text without visible parent-home navigation. Local server entry has no explicit favicon/social-image declarations. | Shared WNT mark with Wishlist descriptor; parent link; verify deployed metadata and add base-path-safe assets. WNT-163. |
| [GitHub organization](https://github.com/wastingnotime) / organization settings and `.github` | Purple hourglass remains. Profile highlights archived projects; popular repositories are archived Contacts examples. | Approved avatar; current profile introduction and links; review featured public repositories. WNT-164. |
| [YouTube](https://www.youtube.com/@wastingnotime) / channel settings | Purple avatar, blue/teal circuit banner, historical purple thumbnails and newer product-specific thumbnails. | Approved green avatar/banner; channel links; reusable restrained signature for future videos. Decide explicitly how to treat historical thumbnails. WNT-165. |

The organization profile README is served from `wastingnotime/.github`; modifying `community-lab` alone cannot update it. Community Lab owns the main website.

## Source evidence

Live desktop browser inspection covered all five surfaces, including current GitHub and YouTube avatars. Sliding Tasks redirected to PT-BR in the review browser. Source inspection supplemented the live review:

- `community-lab/apps/web/src/components/site-header.tsx`, `site-footer.tsx`, `app.css`, and `entry-server.tsx`.
- `sliding-tasks/apps/site/sliding-tasks/index.html`, `pt-br/index.html`, both privacy pages, and `styles.css`.
- `wishlist/apps/web/src/routes/index.tsx`, `app.css`, and `entry-server.tsx`.

Local source evidence is not proof of deployed metadata. Mobile layouts, measured contrast, keyboard behavior, social previews and device-specific crops still require implementation verification. Muted text on the dark sites deserves particular contrast attention.

## Delivery sequence

1. WNT-160: select the concept with Henrique; publish SVG masters, wordmark, monochrome variants, export kit and maker-signature rules. Check 16/32px legibility and light/dark usage.
2. WNT-161–165: apply the approved kit to the five surfaces. Each task is blocked by WNT-160 and contains its repository/surface handoff and acceptance criteria.
3. WNT-166: review the deployed set together, including mobile, avatar/banner crops, localization, accessibility, metadata, cross-links and asset versions.

The [deployed verification record](deployed-identity-verification.md) tracks
WNT-166 readiness, evidence requirements and the final acceptance checklist.

The Linear project is the coordination record requested for this review. No live branding was changed during the review. Android app restyling and reuploading historical videos are outside this site's attribution rollout.
