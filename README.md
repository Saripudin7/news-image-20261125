# news-image-20261125 — The World in One Day

[![make.fun bounty](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![Rank](https://make.fun/badge/news-image-20261125/Saripudin7/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![Reward](https://make.fun/badge/news-image-20261125/Saripudin7/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

One 1024×1024 infographic summing up the world's news of **Wednesday 25 November 2026**,
as reported on that day. Six stories, six regions and fields:

1. **US–China · Tech (verdict 24 Nov, reported worldwide 25 Nov)** — A Brooklyn jury
   convicts Huawei on 10 of 12 counts: bank fraud, sanctions breaches and trade-secret
   theft over its Iran business; acquitted of racketeering. *Reuters, CNN, US DOJ*
2. **Asia · Markets (25 Nov)** — AI sell-off sweeps Asia: SoftBank −11%+, Advantest −12%,
   Kospi −4.5%, Nikkei −2.5% as Nvidia's slide spreads. *CNBC, Reuters*
3. **USA · Security (25 Nov)** — The CIA and the ODNI suffer a breach of some unclassified
   information on an open-source intelligence network, first reported by the NYT. *Reuters*
4. **Ukraine · War (analysis published 25 Nov)** — A new analysis puts Russian military
   deaths past 700,000 in the nearly five-year war. *RFE/RL*
5. **Gaza · Middle East (report out 25 Nov)** — Oxfam warns Gaza has become "a toxic
   wasteland": pollution risks across 99%+ of the territory, 61m tonnes of rubble. *Oxfam*
6. **Australia & Japan · Economy (data out 25 Nov)** — Australia's CPI hits 4.9%; Japan's
   services prices rise 4.2%, the fastest since 1990. *FinScans*

Plus an "Also today" ticker: the US blacklists Megaspeed over Nvidia chip diversion,
Sanofi's $41bn bid for Insmed, Trump's turkey pardon, the Houthi drone hit on a Riyadh
tower, England's T20I win over Australia, and the BJP–SAD reunion.

Each panel shows the date its event happened or was first reported. Bounty and
leaderboard: https://make.fun/bounty/news-image-20261125

## How to run

```sh
python3 render.py          # redraw entry.png with Pillow (reference only)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # draws entry.png to out/entry.png
```

`main.py` draws the image with `render.py` (Pillow, no network). Both runs write
identical bytes (verified: same sha256 across two runs).
