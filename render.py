"""Draw the 25 November 2026 world-news infographic (1024x1024 PNG).

Pure PIL drawing, no network, no clock, no randomness: the same input
always produces the same bytes. Run: python3 render.py [out_path]
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

# --- palette ---------------------------------------------------------------
PAPER = (244, 241, 234)
INK = (18, 28, 40)
NAVY = (15, 42, 67)
NAVY2 = (22, 58, 88)
GOLD = (212, 175, 55)
RED = (178, 34, 34)
TEAL = (14, 116, 110)
AMBER = (180, 110, 0)
SLATE = (90, 100, 112)
CARD = (255, 255, 255)
LINE = (214, 208, 196)
WHITE = (255, 255, 255)
BODY = (52, 64, 78)

FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
]


def font(name, size):
    for d in FONT_DIRS:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


BOLD = "DejaVuSans-Bold.ttf"
REG = "DejaVuSans.ttf"


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_globe(d, cx, cy, r, color):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=4)
    d.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r], outline=color, width=3)
    d.line([cx - r, cy, cx + r, cy], fill=color, width=3)
    d.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55], 0, 360, fill=color, width=3)


def draw_chip(d, x, y, s, color):
    d.rounded_rectangle([x, y, x + s, y + s], radius=8, outline=color, width=5)
    d.rounded_rectangle([x + s * 0.28, y + s * 0.28, x + s * 0.72, y + s * 0.72],
                        radius=4, outline=color, width=4)
    for i in range(3):
        off = s * (0.25 + i * 0.25)
        d.line([x + off, y - 10, x + off, y], fill=color, width=4)
        d.line([x + off, y + s, x + off, y + s + 10], fill=color, width=4)
        d.line([x - 10, y + off, x, y + off], fill=color, width=4)
        d.line([x + s, y + off, x + s + 10, y + off], fill=color, width=4)


def draw_chart_down(d, x, y, s, color):
    d.line([x, y + s, x + s, y + s], fill=color, width=4)
    d.line([x, y, x, y + s], fill=color, width=4)
    pts = [(x + 6, y + s * 0.25), (x + s * 0.35, y + s * 0.45),
           (x + s * 0.55, y + s * 0.30), (x + s - 6, y + s * 0.75)]
    d.line(pts, fill=color, width=5, joint="curve")
    d.polygon([(x + s - 14, y + s * 0.75), (x + s - 2, y + s * 0.75),
               (x + s - 6, y + s * 0.60)], fill=color)


def draw_shield(d, x, y, s, color):
    pts = [(x + s * 0.5, y), (x + s, y + s * 0.22), (x + s * 0.92, y + s * 0.62),
           (x + s * 0.5, y + s), (x + s * 0.08, y + s * 0.62),
           (x, y + s * 0.22)]
    d.polygon(pts, outline=color, width=5)
    d.line([x + s * 0.5, y + s * 0.30, x + s * 0.5, y + s * 0.68], fill=color, width=5)
    d.line([x + s * 0.32, y + s * 0.48, x + s * 0.68, y + s * 0.48], fill=color, width=5)


def draw_tally(d, x, y, s, color):
    for i in range(4):
        d.line([x + i * s * 0.22, y + s * 0.15, x + i * s * 0.22, y + s * 0.85],
               fill=color, width=5)
    d.line([x - 4, y + s * 0.80, x + s * 0.85, y + s * 0.20], fill=color, width=5)


def draw_smoke(d, x, y, s, color):
    d.rectangle([x, y + s * 0.45, x + s * 0.30, y + s], fill=color)
    d.rectangle([x + s * 0.38, y + s * 0.30, x + s * 0.62, y + s], fill=color)
    d.rectangle([x + s * 0.70, y + s * 0.55, x + s, y + s], fill=color)
    for cx, cy, r in [(x + s * 0.15, y + s * 0.25, 7), (x + s * 0.50, y + s * 0.12, 9),
                      (x + s * 0.82, y + s * 0.30, 6)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=4)


def draw_gauge(d, x, y, s, color):
    d.arc([x, y + s * 0.15, x + s, y + s * 1.05], 180, 360, fill=color, width=6)
    d.line([x + s * 0.5, y + s * 0.62, x + s * 0.82, y + s * 0.30], fill=color, width=5)
    d.ellipse([x + s * 0.42, y + s * 0.54, x + s * 0.58, y + s * 0.70], fill=color)
    d.line([x, y + s * 0.62, x + s, y + s * 0.62], fill=color, width=3)


ICONS = {
    "chip": draw_chip,
    "chart": draw_chart_down,
    "shield": draw_shield,
    "tally": draw_tally,
    "smoke": draw_smoke,
    "gauge": draw_gauge,
}

STORIES = [
    # lead story
    dict(tag="TECH  |  UNITED STATES - CHINA", accent=RED, icon="chip",
         head="Huawei convicted in US trial",
         body=("Brooklyn jury finds Huawei guilty on 10 of 12 counts: bank fraud, "
               "sanctions breaches, trade-secret theft over Iran business."),
         when="Verdict Tue 24 Nov (US) - reported worldwide Wed 25 Nov"),
    dict(tag="MARKETS  |  ASIA  -  WED 25 NOV", accent=AMBER, icon="chart",
         head="AI sell-off sweeps Asia",
         body=("SoftBank falls 11%+, Advantest -12%; Kospi -4.5%, Nikkei -2.5% as "
               "Nvidia's slide spreads.")),
    dict(tag="SECURITY  |  USA  -  WED 25 NOV", accent=NAVY2, icon="shield",
         head="CIA and ODNI breached",
         body=("NYT reports intruders hit an open-source intelligence network; "
               "some unclassified data exposed.")),
    dict(tag="WAR  |  UKRAINE  -  25 NOV", accent=TEAL, icon="tally",
         head="700,000 Russian troops killed",
         body=("A new analysis puts Russian military deaths past 700,000 in the "
               "nearly five-year war.")),
    dict(tag="MIDDLE EAST  |  GAZA  -  25 NOV", accent=RED, icon="smoke",
         head="Gaza 'a toxic wasteland'",
         body=("Oxfam warns of pollution risks across 99%+ of Gaza: heavy metals, "
               "asbestos, 61m tonnes of rubble.")),
    dict(tag="ECONOMY  |  AUSTRALIA & JAPAN  -  DATA OUT WED 25 NOV",
         accent=AMBER, icon=None,
         head="Inflation jumps in Australia and Japan",
         body=("Australia CPI hits 4.9%; Japan services prices +4.2%, fastest "
               "since 1990.")),
]

TICKER = ("ALSO TODAY  •  US blacklists Megaspeed over Nvidia chip diversion  •  "
          "Sanofi to buy Insmed for $41bn  •  Trump pardons turkeys Freedom & Feathers  •  "
          "Houthi drone hits Riyadh tower, 11 hurt  •  England beat Australia in 2nd T20I  •  "
          "BJP & SAD reunite")

FOOTER = ("Sources: Reuters  •  CNN  •  US DOJ  •  RFE/RL  •  CNBC  •  Oxfam  •  "
          "FinScans  •  Hindu BusinessLine    |    make.fun")


def story_card(d, x, y, w, h, s, lead=False):
    d.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=CARD,
                        outline=LINE, width=2)
    d.rounded_rectangle([x, y, x + 10, y + h], radius=5, fill=s["accent"])
    tx = x + 28
    # tag
    tag_f = font(BOLD, 19 if lead else 17)
    d.text((tx, y + 13), s["tag"], font=tag_f, fill=s["accent"])
    # icon (top right) if any
    isz = 88 if lead else 68
    ix = x + w - isz - 24
    iy = y + 20
    if s["icon"]:
        d.rounded_rectangle([ix - 12, iy - 12, ix + isz + 12, iy + isz + 12],
                            radius=12, fill=(238, 240, 243))
        ICONS[s["icon"]](d, ix, iy, isz, s["accent"])
    # headline
    head_f = font(BOLD, 38 if lead else 29)
    head_w = w - 28 - (isz + 48 if s["icon"] else 20)
    hlines = wrap(d, s["head"], head_f, head_w)[:2]
    hy = y + 40 if lead else y + 38
    lh = 40 if lead else 34
    for ln in hlines:
        d.text((tx, hy), ln, font=head_f, fill=INK)
        hy += lh
    # body, clipped to the space above the when-line (lead) or card bottom
    body_f = font(REG, 23 if lead else 20)
    body_w = w - 28 - (150 if lead else 20)
    blines = wrap(d, s["body"], body_f, body_w)
    blh = 26 if lead else 25
    limit_y = (y + h - 30) if lead else (y + h - 8)
    by = hy + 4
    max_lines = max(0, (limit_y - by) // blh)
    for ln in blines[:max_lines]:
        d.text((tx, by), ln, font=body_f, fill=BODY)
        by += blh
    # when line (lead only)
    if lead and s.get("when"):
        d.text((tx, y + h - 28), s["when"], font=font(BOLD, 18), fill=SLATE)


def build(out_path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- header ------------------------------------------------------------
    d.rectangle([0, 0, W, 136], fill=NAVY)
    d.rectangle([0, 136, W, 142], fill=GOLD)
    draw_globe(d, 72, 68, 40, GOLD)
    d.text((132, 16), "THE WORLD IN ONE DAY", font=font(BOLD, 48), fill=WHITE)
    d.text((132, 78), "WEDNESDAY  25  NOVEMBER  2026",
           font=font(BOLD, 30), fill=GOLD)
    d.text((W - 168, 24), "6 STORIES", font=font(BOLD, 24), fill=GOLD)
    d.text((W - 168, 58), "ONE DAY", font=font(BOLD, 20), fill=(170, 190, 210))
    d.text((W - 168, 84), "ONE IMAGE", font=font(BOLD, 20), fill=(170, 190, 210))

    # --- lead story --------------------------------------------------------
    story_card(d, 24, 152, 976, 168, STORIES[0], lead=True)

    # --- 2x2 grid ----------------------------------------------------------
    gx, gy = 24, 332
    cw, ch, gap = 480, 208, 16
    for i, s in enumerate(STORIES[1:5]):
        story_card(d, gx + (i % 2) * (cw + gap), gy + (i // 2) * (ch + gap),
                   cw, ch, s)

    # --- bottom wide story -------------------------------------------------
    story_card(d, 24, 772, 976, 112, STORIES[5], lead=False)

    # --- ticker ------------------------------------------------------------
    d.rectangle([0, 884, W, 960], fill=INK)
    tick_f = font(BOLD, 20)
    tlines = wrap(d, TICKER, tick_f, W - 48)
    ty = 890
    for ln in tlines[:3]:
        d.text((24, ty), ln, font=tick_f, fill=(232, 226, 200))
        ty += 23

    # --- footer ------------------------------------------------------------
    d.text((24, 970), FOOTER, font=font(REG, 15), fill=SLATE)

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    img.save(out_path, format="PNG")
    return out_path


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    build(out)
    print("wrote", out)
