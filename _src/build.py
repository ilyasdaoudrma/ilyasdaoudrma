"""Generates the SVG artwork for the GitHub profile README.

Run from the repo root:  python _src/build.py
Fonts are subset woff2 files embedded as data URIs so the SVGs render the
same everywhere (GitHub serves README images through a proxy that blocks
external font loading).
"""
import base64
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
FONTS = Path(__file__).resolve().parent / "fonts"

DARK = dict(bg="#0E0C0A", ink="#F3EDE2", muted="#9A8F80", accent="#E9A23B",
            line="#2E2821", live="#3DBF9F", page="#0d1117")
LIGHT = dict(bg="none", ink="#1A1613", muted="#6B6257", accent="#B8741A",
             line="#D9D0C3", live="#1F8A70", page="#ffffff")


def font_face(name: str, file: str, weight: str = "400") -> str:
    data = base64.b64encode((FONTS / file).read_bytes()).decode()
    return (f"@font-face{{font-family:'{name}';font-weight:{weight};"
            f"src:url(data:font/woff2;base64,{data}) format('woff2')}}")


SERIF = font_face("Fr", "fraunces-var.woff2", "100 900")
MONO = font_face("Mono", "plexmono-400.woff2", "400") + font_face("Mono", "plexmono-500.woff2", "500")


def star_path(cx: float, cy: float, r_out: float) -> str:
    """Classic zellige 8-point star (two overlapping squares) as one outline."""
    r_in = r_out * math.cos(math.radians(45)) / math.cos(math.radians(22.5))
    pts = []
    for k in range(16):
        r = r_out if k % 2 == 0 else r_in
        a = math.radians(k * 22.5 - 90)
        pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
    return "M" + " L".join(pts) + " Z"


def zellige_field(cx: float, cy: float, radius: float, step: float) -> str:
    stars, diamonds = [], []
    n = int(radius // step) + 2
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            x, y = cx + i * step, cy + j * step
            if math.hypot(x - cx, y - cy) > radius + step:
                continue
            stars.append(star_path(x, y, step * 0.42))
            hx, hy, d = x + step / 2, y + step / 2, step * 0.16
            diamonds.append(f"M{hx:.1f},{hy - d:.1f} L{hx + d:.1f},{hy:.1f} L{hx:.1f},{hy + d:.1f} L{hx - d:.1f},{hy:.1f} Z")
    return " ".join(stars), " ".join(diamonds)


def header() -> str:
    c = DARK
    w, h = 1280, 470
    cx, cy = 1045, 235
    stars, diamonds = zellige_field(cx, cy, 300, 118)
    rosette = star_path(cx, cy, 84)
    rosette_in = star_path(cx, cy, 52)
    roles = [
        "fine-tunes LLMs that speak Moroccan Darija",
        "builds RAG pipelines and AI agents",
        "ships full-stack AI products end to end",
    ]
    role_nodes = "\n".join(
        f'<text class="role r{i}" x="64" y="408">{r}</text>' for i, r in enumerate(roles)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Ilyas Daoud El Asmi — AI Engineer (LLM fine-tuning, RAG, AI agents) building full-stack AI products, Oujda, Morocco">
<style>
{SERIF}{MONO}
.mono{{font-family:'Mono',ui-monospace,monospace}}
.serif{{font-family:'Fr',Georgia,serif}}
.spin{{transform-origin:{cx}px {cy}px;animation:spin 160s linear infinite}}
.draw{{stroke-dasharray:1;animation:draw 2.8s cubic-bezier(.16,1,.3,1) .3s backwards}}
.draw2{{animation-delay:.9s}}
.role{{font-family:'Mono',ui-monospace,monospace;font-size:22px;fill:{c["ink"]};opacity:0;animation:cyc 10.5s infinite}}
.r0{{opacity:1}}
.r1{{animation-delay:3.5s}} .r2{{animation-delay:7s}}
.caret{{animation:blink 1s steps(1) infinite}}
.fade{{animation:up 1s cubic-bezier(.16,1,.3,1) backwards}}
.d1{{animation-delay:.15s}} .d2{{animation-delay:.35s}} .d3{{animation-delay:.55s}} .d4{{animation-delay:.8s}}
.pulse{{transform-box:fill-box;transform-origin:center;animation:pulse 2.4s ease-out infinite}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
@keyframes draw{{from{{stroke-dashoffset:1}}to{{stroke-dashoffset:0}}}}
@keyframes cyc{{0%{{opacity:0;transform:translateY(10px)}}5%,29%{{opacity:1;transform:none}}33%,100%{{opacity:0;transform:translateY(-6px)}}}}
@keyframes blink{{50%{{opacity:0}}}}
@keyframes up{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:none}}}}
@keyframes pulse{{0%{{transform:scale(1);opacity:.7}}100%{{transform:scale(3.2);opacity:0}}}}
@media (prefers-reduced-motion:reduce){{.spin,.draw,.fade,.pulse,.caret{{animation:none;opacity:1;stroke-dashoffset:0}}.role{{animation:none}}.r0{{opacity:1}}}}
</style>
<defs>
  <clipPath id="card"><rect width="{w}" height="{h}" rx="22"/></clipPath>
  <radialGradient id="fadeMask" cx="{cx}" cy="{cy}" r="330" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#fff"/><stop offset=".55" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </radialGradient>
  <mask id="fm"><rect width="{w}" height="{h}" fill="url(#fadeMask)"/></mask>
  <radialGradient id="glow" cx="{cx}" cy="{cy}" r="260" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="{c["accent"]}" stop-opacity=".22"/><stop offset="1" stop-color="{c["accent"]}" stop-opacity="0"/>
  </radialGradient>
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .05 0"/></filter>
</defs>
<g clip-path="url(#card)">
  <rect width="{w}" height="{h}" fill="{c["bg"]}"/>
  <rect width="{w}" height="{h}" fill="url(#glow)"/>
  <g mask="url(#fm)">
    <g class="spin" fill="none" stroke="{c["accent"]}" stroke-width="1.1">
      <path d="{stars}" stroke-opacity=".32"/>
      <path d="{diamonds}" stroke-opacity=".22"/>
    </g>
  </g>
  <path class="draw" pathLength="1" d="{rosette}" fill="none" stroke="{c["accent"]}" stroke-width="2.2"/>
  <path class="draw draw2" pathLength="1" d="{rosette_in}" fill="none" stroke="{c["ink"]}" stroke-width="1.4" stroke-opacity=".8"/>
  <circle cx="{cx}" cy="{cy}" r="5" fill="{c["accent"]}"/>
  <rect width="{w}" height="{h}" filter="url(#grain)"/>

  <g class="fade d1">
    <text class="mono" x="64" y="84" font-size="15" letter-spacing="3.5" fill="{c["accent"]}">OUJDA, MOROCCO  ·  34.68°N  1.91°W</text>
    <text x="64" y="120" font-size="19" fill="{c["muted"]}" font-family="'Segoe UI','Noto Sans','Noto Sans Arabic',Tahoma,sans-serif">Hello · Bonjour · مرحبا</text>
  </g>
  <text class="serif fade d2" x="58" y="238" font-size="118" font-weight="620" letter-spacing="-3" fill="{c["ink"]}" style="font-variation-settings:'opsz' 144">Ilyas Daoud</text>
  <text class="serif fade d3" x="60" y="342" font-size="118" font-weight="420" letter-spacing="-2" fill="none" stroke="{c["ink"]}" stroke-width="1.4" style="font-variation-settings:'opsz' 144">El Asmi<tspan fill="{c["accent"]}" stroke="none">.</tspan></text>
  <g class="fade d4">
    <text class="mono" x="64" y="408" font-size="22" fill="{c["accent"]}">›</text>
    <g transform="translate(24 0)">{role_nodes}</g>
  </g>

  <g class="mono" font-size="13" letter-spacing="2.5" fill="{c["muted"]}">
    <circle class="pulse" cx="{w - 500}" cy="437" r="4" fill="{c["live"]}"/>
    <circle cx="{w - 500}" cy="437" r="4" fill="{c["live"]}"/>
    <text x="{w - 48}" y="442" text-anchor="end">AI ENGINEER  ·  LLM · RAG · AGENTS  ·  FULL-STACK</text>
  </g>
</g>
</svg>'''


def section(num: str, title: str, caption: str, c: dict) -> str:
    w, h = 1280, 128
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}">
<style>{SERIF}{MONO}
.mono{{font-family:'Mono',ui-monospace,monospace}}.serif{{font-family:'Fr',Georgia,serif}}
.rule{{stroke-dasharray:1;animation:draw 1.6s cubic-bezier(.16,1,.3,1) .2s backwards}}
@keyframes draw{{from{{stroke-dashoffset:1}}to{{stroke-dashoffset:0}}}}
@media (prefers-reduced-motion:reduce){{.rule{{animation:none;stroke-dashoffset:0}}}}
</style>
<text class="mono" x="4" y="36" font-size="17" letter-spacing="3" fill="{c["accent"]}">{num}</text>
<path d="{star_path(58, 30, 9)}" fill="none" stroke="{c["accent"]}" stroke-width="1.5"/>
<text class="serif" x="0" y="100" font-size="60" font-weight="560" letter-spacing="-1.5" fill="{c["ink"]}" style="font-variation-settings:'opsz' 144">{title}</text>
<line class="rule" pathLength="1" x1="92" y1="30" x2="{w}" y2="30" stroke="{c["line"]}" stroke-width="1.5"/>
<text class="mono" x="{w}" y="100" text-anchor="end" font-size="15" letter-spacing="3" fill="{c["muted"]}">{caption}</text>
</svg>'''


TIMELINE = [
    ("WORK", "2025 — NOW", "Founder, freelance web developer", "WEBZI1 STUDIO · RABAT",
     "Websites for cafés, restaurants &amp; shops — FR/EN/AR, SEO, deployed.", True),
    ("WORK", "APR — JUN 2026", "AI Intern", "LEADZ TECH SERVICES · RABAT",
     "Fine-tuned a conversational LLM for Moroccan Darija; RAG + OCR.", False),
    ("WORK", "APR — MAY 2025", "Machine Learning Intern", "CHU MOHAMMED VI · OUJDA",
     "Deep learning to help detect breast anomalies on mammograms.", False),
    ("WORK", "JUL 2024", "Web Development Intern", "REGIONAL HEALTH DIRECTORATE · OUJDA",
     "A responsive, accessible institutional website.", False),
    ("STUDY", "2025 — 2026", "B.Sc. Data Analytics &amp; Business Intelligence", "EST OUJDA",
     "", False),
    ("STUDY", "2023 — 2025", "DUT, Business Intelligence &amp; Machine Learning", "EST OUJDA",
     "", False),
]


def timeline(c: dict) -> str:
    w = 1280
    x_date, x_line, x_body = 0, 290, 340
    y, rows, prev_group = 20, [], None
    for group, date, role, org, desc, live in TIMELINE:
        if group != prev_group:
            if prev_group is not None:
                y += 26
            rows.append(f'<text class="mono" x="{x_date}" y="{y + 18}" font-size="15" letter-spacing="4" fill="{c["accent"]}">{group}</text>')
            y += 52
            prev_group = group
        node_y = y + 22
        hollow = group == "STUDY"
        node = (f'<circle cx="{x_line}" cy="{node_y}" r="8" fill="{c["page"]}" stroke="{c["accent"]}" stroke-width="2.5"/>'
                if hollow else f'<circle cx="{x_line}" cy="{node_y}" r="8" fill="{c["live"] if live else c["accent"]}"/>')
        if live:
            node += f'<circle class="pulse" cx="{x_line}" cy="{node_y}" r="8" fill="{c["live"]}"/>'
        rows.append(node)
        rows.append(f'<text class="mono" x="{x_date}" y="{node_y + 7}" font-size="19" letter-spacing="1.5" fill="{c["muted"]}">{date}</text>')
        rows.append(f'<text class="serif" x="{x_body}" y="{y + 34}" font-size="38" font-weight="560" letter-spacing="-.6" fill="{c["ink"]}" style="font-variation-settings:\'opsz\' 72">{role}</text>')
        rows.append(f'<text class="mono" x="{x_body}" y="{y + 70}" font-size="17" letter-spacing="2.5" fill="{c["accent"]}">{org}</text>')
        if desc:
            rows.append(f'<text class="serif" x="{x_body}" y="{y + 108}" font-size="26" font-weight="380" fill="{c["muted"]}" style="font-variation-settings:\'opsz\' 24">{desc}</text>')
            y += 150
        else:
            y += 110
    h = y + 10
    line = f'<line x1="{x_line}" y1="60" x2="{x_line}" y2="{h - 60}" stroke="{c["line"]}" stroke-width="2"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Experience and education timeline">
<style>{SERIF}{MONO}
.mono{{font-family:'Mono',ui-monospace,monospace}}.serif{{font-family:'Fr',Georgia,serif}}
.pulse{{transform-box:fill-box;transform-origin:center;animation:pulse 2.4s ease-out infinite}}
@keyframes pulse{{0%{{transform:scale(1);opacity:.6}}100%{{transform:scale(2.8);opacity:0}}}}
@media (prefers-reduced-motion:reduce){{.pulse{{animation:none;opacity:0}}}}
</style>
{line}
{"".join(rows)}
</svg>'''


def divider() -> str:
    w, h, step = 1280, 40, 64
    stars = " ".join(star_path(x, h / 2, 11) for x in range(step // 2, w, step))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" aria-hidden="true">
<path d="{stars}" fill="none" stroke="#C98A2E" stroke-width="1.4" stroke-opacity=".75"/>
</svg>'''


SECTIONS = [
    ("01", "About", "WHO I AM"),
    ("02", "Selected work", "SHIPPED &amp; LIVE"),
    ("03", "Experience", "WORK · STUDY"),
    ("04", "Toolbox", "WHAT I BUILD WITH"),
    ("05", "Let’s talk", "OPEN TO OPPORTUNITIES"),
]


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "header.svg").write_text(header(), encoding="utf-8")
    (ASSETS / "divider.svg").write_text(divider(), encoding="utf-8")
    for mode, pal in (("dark", DARK), ("light", LIGHT)):
        for num, title, cap in SECTIONS:
            (ASSETS / f"s{num}-{mode}.svg").write_text(section(num, title, cap, pal), encoding="utf-8")
        (ASSETS / f"timeline-{mode}.svg").write_text(timeline(pal), encoding="utf-8")
    print("built", sorted(p.name for p in ASSETS.glob("*.svg")))


if __name__ == "__main__":
    main()
