# YouTube identity rollout — WNT-165

Channel: <https://www.youtube.com/@wastingnotime>  
Channel ID: `UCkKJr0sXMpLxniMR_C5_yow`  
Execution: 2026-10-15 America/Sao_Paulo (2026-10-16 UTC).  
Kit: Forward W **v1.0.0**, unchanged consumer adoption; no shared API or asset version change.

## Settings delivery

Uploaded the kit's `avatar.png`, `youtube-banner.png` and `video-watermark.png`
through YouTube Studio customization, accepted their full-image crops, and
published. Reloading Studio confirmed the saved assets, description, both links,
and **End of video** watermark setting (last 15 seconds). The watermark is a
secondary white mark; future video editors should preview contrast and choose
the dark variant for light footage when baking a signature into a video.

Upload provenance (SHA-256, relative to `assets/identity/v1.0.0/exports/`):

| File | Bytes | Dimensions | SHA-256 |
| --- | ---: | --- | --- |
| avatar.png | 20211 | 800 × 800 | f456db90c90c83d83aaaddd46d45a033f351374406db002660bf56b9ebf49350 |
| youtube-banner.png | 39597 | 2560 × 1440 | 8a41d5b24189923112fddc396f56d974154727f96b2d3f9fc9ba6d2c6542d3fd |
| video-watermark.png | 2579 | 150 × 150 | 85907f67f54c218dc58e3be114ec35c9f61220d56f069504ef301496c95191c8 |

The avatar uses the same export designated for GitHub; this task does not
certify the separate GitHub settings rollout.

Published description:

> Wasting No Time (WNT) — useful software, built in public.
>
> Product walkthroughs, software architecture, simulations, and AI applied to development. We share the reasoning, decisions, and working results behind what we build.
>
> Explore our products and experiments at https://wastingnotime.org/
> Find our open-source work at https://github.com/wastingnotime

Links, in order: **WNT Community Lab** → <https://wastingnotime.org/>;
**GitHub** → <https://github.com/wastingnotime>.

## Thumbnail and future-video decision

Retain the historical purple artwork for these videos as a record of the
channel's earlier identity. Replacing it would provide little product context;
the channel-level identity supplies the current maker branding. No videos were
reuploaded or edited solely for branding.

- [Designing the First API](https://www.youtube.com/watch?v=H_7tcMsT6HY)
- [A Calm Approach to Software Architecture](https://www.youtube.com/watch?v=Raw9YeVapPk)

Keep the existing Sliding Tasks thumbnails and Simulation Observatory screenshot.
Future thumbnails lead with the product and topic. Follow the
[video guidance](../README.md#channels-and-video): a 96–128px monochrome signature
on a 1280 × 720 thumbnail, at least 24px inset, away from platform overlays;
inspect at actual display size. Use `thumbnail-signature.svg` as the starting
asset. Use `end-card.png`/`.svg` for a secondary maker signature, leaving the
product title and calls to action primary and previewing YouTube end-screen
positions before publishing. Do not impose WNT green on product artwork.

## Verification and evidence

Browser: Brave, WNT profile, desktop web, dark theme, English UI. Screenshots
capture the browser's existing viewport; Studio previews are not physical-device
checks. Current requirements checked against
[YouTube Help](https://support.google.com/youtube/answer/10456525?hl=en)
on 2026-10-16 UTC: banner minimum 2048 × 1152, recommended 2560 × 1440,
maximum 6 MB; text/logo safe area 1235 × 338 at minimum size; square watermark
at least 150px and less than 1 MB. Studio recommends a profile PNG at least
98 × 98 and at most 4 MB (stricter than Help's 15 MB maximum); this upload meets
both.

- [Before channel](before-channel.jpg): purple avatar, circuit banner, five videos.
- [Studio banner crops](banner-studio-crops.jpg): pass; complete mark/name inside
  “Viewable on all devices”, desktop strip and full TV bounds at default crop.
- [Studio circular avatar](avatar-studio-crop.jpg): pass; all four panels retained.
- [Persisted Studio configuration](studio-published.jpg): pass after reload;
  approved images, description and destinations saved, Publish disabled.
- [Public desktop](after-channel-desktop.jpg): pass; new avatar, banner and
  description appeared after propagation and reload. Website link appears in
  the header; both destinations are preserved in Studio.
- Narrow viewport override did not change the captured desktop surface, so no
  mobile screenshot is claimed. Mobile banner safety is covered by Studio’s
  all-device crop preview.

Physical mobile and TV checks and watermark playback verification are not run;
WNT-166 owns the final cross-surface deployed audit. Preserve the historical
assets under `assets/archive/pre-forward-w/` for rollback. Restore prior
artwork through Studio if necessary; rollback does not require video reuploads.
