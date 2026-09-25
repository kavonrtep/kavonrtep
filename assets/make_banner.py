#!/usr/bin/env python3
"""Generate the profile banner SVGs (light + dark).

The banner shows three annotation tracks; the element *type* is implicit
from its structure, so no text labels are needed:

  row 1  LTR retrotransposons  - two terminal arrows pointing the SAME way
                                 (direct repeats) around internal domains
  row 2  TIR DNA transposons   - two terminal arrows pointing INWARD
                                 (inverted repeats) around a transposase block
  row 3  satellite arrays      - runs of identical packed monomers,
                                 one array with a higher-order pattern

Behind the tracks sits a faint repeat-density profile with a centromeric peak.
Run:  python3 assets/make_banner.py
"""
import math

W, H = 1280, 320
L, R = 56, 1224                      # left / right content margin
DENS_BASE = 104                               # baseline of the density profile
ROWS = {"ltr": 148, "tir": 202, "sat": 256}   # row centre lines
RULER = 292

LIGHT = dict(
    name="light",
    bg="#fcfcfa", panel_a="#f7f9f7", panel_b="#eff3f1",
    grid="#e6e9e5", axis="#b6bab4", tick="#c9ccc6",
    ltr="#2e7d8f", ltr_arrow="#215f6e", ltr_dom="#7fb3bd", ltr_body="#cfe1e5",
    tir="#b07d2e", tir_arrow="#8d6320", tir_dom="#d8b271", tir_body="#eedfc4",
    sat="#6f5f9e", sat_alt="#9184c0", sat_body="#ddd7ec",
    dens_ltr="#2e7d8f", dens_tir="#b07d2e", dens_sat="#6f5f9e", dens_op=0.085,
)
DARK = dict(
    name="dark",
    bg="#0d1117", panel_a="#10161c", panel_b="#0d1319",
    grid="#1b2229", axis="#39424c", tick="#2a323a",
    ltr="#4fa6ba", ltr_arrow="#7fcddb", ltr_dom="#2d7181", ltr_body="#1a3b44",
    tir="#cf9b47", tir_arrow="#e7bd78", tir_dom="#8f6725", tir_body="#3d2f16",
    sat="#8d7ec8", sat_alt="#b0a4e0", sat_body="#2b2542",
    dens_ltr="#4fa6ba", dens_tir="#cf9b47", dens_sat="#8d7ec8", dens_op=0.13,
)

# ---------------------------------------------------------------- primitives
def arrow(x, y, w, h, direction, fill, op=1.0):
    """Pentagon 'feature arrow'. direction: +1 points right, -1 points left."""
    t = min(h * 0.55, w * 0.45)
    if direction > 0:
        pts = f"{x},{y} {x+w-t},{y} {x+w},{y+h/2} {x+w-t},{y+h} {x},{y+h}"
    else:
        pts = f"{x+w},{y} {x+t},{y} {x},{y+h/2} {x+t},{y+h} {x+w},{y+h}"
    o = f' opacity="{op}"' if op != 1.0 else ""
    return f'<polygon points="{pts}" fill="{fill}"{o}/>'

def rect(x, y, w, h, fill, rx=2, op=1.0):
    o = f' opacity="{op}"' if op != 1.0 else ""
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}"{o}/>'

# ------------------------------------------------------------------ elements
def ltr_element(x, w, strand, cy, p, kind="full"):
    """LTR retrotransposon.

    kind="full"      complete element: direct terminal repeats (both arrows
                     point the same way) around the internal region, whose
                     domains keep the real proportions of GAG/PROT/RT/RH/INT
    kind="solo"      solo LTR left behind by recombination: a single repeat
    kind="truncated" fragment: one terminal repeat, internal region breaking off

    The element is composed left-to-right and mirrored as a whole for the
    reverse strand, so a truncated element always breaks at its open end.
    """
    h = 30
    y = cy - h / 2
    if kind == "solo":
        return arrow(x, y, max(13, w), h, strand, p["ltr_arrow"])

    ltr_w = max(13, w * 0.14)
    shapes = []          # (kind, x, width, ...) in left-to-right orientation
    inner_x = x + ltr_w + 5
    inner_w = (w - 2 * ltr_w - 10) if kind == "full" else (w - ltr_w - 9)
    shapes.append(("rect", inner_x - 2, inner_w + 4, cy - h * 0.15, h * 0.30, p["ltr_body"], 1.0))
    prop, gap = [0.17, 0.10, 0.30, 0.13, 0.21], 5
    span = inner_w - gap * (len(prop) - 1)
    dx, dh, end = inner_x, h * 0.60, inner_x + inner_w
    for f in prop:
        dw = span * f
        if dw < 3 or dx >= end:
            break
        fade = 1.0
        if dx + dw > end:                      # truncated: last domain breaks off
            dw, fade = end - dx, 0.45
        shapes.append(("rect", dx, dw, cy - dh / 2, dh, p["ltr_dom"], fade))
        dx += dw + gap
    shapes.append(("arrow", x, ltr_w, y, h, p["ltr_arrow"], 1.0))
    if kind == "full":
        shapes.append(("arrow", x + w - ltr_w, ltr_w, y, h, p["ltr_arrow"], 1.0))

    out = []
    for kind_, sx, sw, sy, sh, fill, op in shapes:
        if strand < 0:                          # mirror about the element centre
            sx = 2 * x + w - sx - sw
        if kind_ == "rect":
            out.append(rect(sx, sy, sw, sh, fill, rx=2, op=op))
        else:
            out.append(arrow(sx, sy, sw, sh, strand, fill))
    return "".join(out)

def tir_element(x, w, cy, p):
    """DNA transposon: terminal repeats pointing INWARD (inverted repeats)
    around a slim body carrying the transposase block."""
    h = 26
    y = cy - h / 2
    tir_w = max(12, w * 0.17)
    out = []
    body_x, body_w = x + tir_w, w - 2 * tir_w
    if body_w > 6:
        out.append(rect(body_x - 2, cy - h * 0.14, body_w + 4, h * 0.28, p["tir_body"], rx=2))
        # transposase ORF in the middle of the element
        tp_w = body_w * 0.66
        out.append(rect(body_x + (body_w - tp_w) / 2, cy - h * 0.29, tp_w, h * 0.58,
                        p["tir"], rx=2))
    out.append(arrow(x, y, tir_w, h, +1, p["tir_arrow"]))
    out.append(arrow(x + w - tir_w, y, tir_w, h, -1, p["tir_arrow"]))
    return "".join(out)

def sat_array(x, mono_w, n, cy, p, hor=None, tall=1.0):
    """Tandem array of identical monomers. hor=k marks a k-monomer higher-order unit."""
    h = 24 * tall
    y = cy - h / 2
    gap = 1.6
    out = [rect(x - 2, cy - h * 0.62, n * (mono_w + gap) + 2, h * 1.24, p["sat_body"], rx=3, op=0.55)]
    for i in range(n):
        mx = x + i * (mono_w + gap)
        fill, mh = p["sat"], h
        if hor and i % hor == 0:      # first monomer of each higher-order unit
            fill, mh = p["sat_alt"], h * 1.16
        out.append(arrow(mx, cy - mh / 2, mono_w, mh, +1, fill))
    return "".join(out)

# ------------------------------------------------------- composition (tuned)
# Features sit on DISJOINT coordinates across all three tracks: one locus
# carries one annotation, as in a real non-overlapping repeat annotation.
#
#    68- 214  LTR element            908- 922  solo LTR
#   236- 328  TIR element            944-1032  TIR element
#   344- 397  satellite array       1052-1105  satellite array
#   418- 506  truncated LTR         1126-1224  LTR element
#   528- 590  TIR element
#   612- 888  centromeric satellite array (higher-order unit of 5 monomers)

# (x, width, strand, kind)
LTRS = [(68, 146, +1, "full"), (418, 88, -1, "truncated"),
        (908, 14, -1, "solo"), (1126, 98, +1, "full")]
# (x, width)
TIRS = [(236, 92), (528, 62), (944, 88)]
# (x, monomer width, n, higher-order period, height factor)
SATS = [(344, 9, 5, None, 0.95), (612, 9, 26, 5, 1.2), (1052, 9, 5, None, 0.95)]

def density_path():
    """Repeat-density profile along the sequence.

    Shaped like a real plant chromosome: a broad, saturating peak over the
    satellite-rich centromeric region in the middle and lower, bumpier density
    along the arms, where dispersed LTR/DNA elements dominate. The peak is
    centred on the large satellite array drawn in the bottom track.
    """
    # (centre, sigma, height) -- centre matches the big centromeric array
    peaks = [(140, 54, 0.46), (282, 42, 0.38), (458, 44, 0.40),
             (746, 122, 1.00), (986, 44, 0.40), (1160, 54, 0.48)]
    n = 320
    vals = []
    for i in range(n):
        x = L + (R - L) * i / (n - 1)
        v = 0.12
        for cx, sd, a in peaks:
            v += a * math.exp(-((x - cx) ** 2) / (2 * sd * sd))
        v += 0.035 * math.sin(x / 29.0) + 0.025 * math.sin(x / 11.0 + 1.4)
        vals.append(min(1.0, v))
    amp = 74.0
    d = f"M {L:.1f},{DENS_BASE}"
    for i, v in enumerate(vals):
        px = L + (R - L) * i / (n - 1)
        d += f" L {px:.1f},{DENS_BASE - (0.04 + 0.96 * v) * amp:.1f}"
    line = d
    d += f" L {R:.1f},{DENS_BASE} Z"
    return d, line

def build(p):
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'role="img" aria-label="Genome annotation tracks: repeat density profile above LTR '
         f'retrotransposons, TIR DNA transposons and satellite repeat arrays, with a '
         f'satellite-rich centromeric region in the middle">']
    s.append('<defs>'
             f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
             f'<stop offset="0" stop-color="{p["panel_a"]}"/><stop offset="1" stop-color="{p["panel_b"]}"/>'
             '</linearGradient>'
             f'<linearGradient id="dens" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0" stop-color="{p["dens_sat"]}" stop-opacity="{min(1, p["dens_op"]*6):.3f}"/>'
             f'<stop offset="1" stop-color="{p["dens_ltr"]}" stop-opacity="{p["dens_op"]*1.4:.3f}"/>'
             '</linearGradient></defs>')
    s.append(f'<rect width="{W}" height="{H}" fill="{p["bg"]}"/>')
    s.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
    for gx in range(L, R + 1, 56):
        s.append(f'<line x1="{gx}" y1="34" x2="{gx}" y2="{RULER}" stroke="{p["grid"]}" stroke-width="1"/>')
    # density profile, with its own baseline
    dp, dline = density_path()
    s.append(f'<path d="{dp}" fill="url(#dens)"/>')
    s.append(f'<path d="{dline}" fill="none" stroke="{p["dens_sat"]}" stroke-width="1.6" '
             f'stroke-linejoin="round" opacity="0.55"/>')
    s.append(f'<line x1="{L}" y1="{DENS_BASE}" x2="{R}" y2="{DENS_BASE}" stroke="{p["axis"]}" '
             f'stroke-width="1.1" opacity="0.45"/>')
    # per-row sequence baselines
    for cy in ROWS.values():
        s.append(f'<line x1="{L}" y1="{cy}" x2="{R}" y2="{cy}" stroke="{p["axis"]}" '
                 f'stroke-width="1.4" opacity="0.5"/>')
    cy = ROWS["ltr"]
    for x, w, strand, kind in LTRS:
        s.append(ltr_element(x, w, strand, cy, p, kind))
    cy = ROWS["tir"]
    for x, w in TIRS:
        s.append(tir_element(x, w, cy, p))
    cy = ROWS["sat"]
    for x, mw, cnt, hor, tall in SATS:
        s.append(sat_array(x, mw, cnt, cy, p, hor=hor, tall=tall))
    # coordinate ruler
    s.append(f'<line x1="{L}" y1="{RULER}" x2="{R}" y2="{RULER}" stroke="{p["axis"]}" stroke-width="1.2"/>')
    for i in range(0, 22):
        tx = L + (R - L) * i / 21
        long = (i % 5 == 0)
        s.append(f'<line x1="{tx:.1f}" y1="{RULER}" x2="{tx:.1f}" y2="{RULER + (8 if long else 4)}" '
                 f'stroke="{p["axis"] if long else p["tick"]}" stroke-width="1.2"/>')
    s.append('</svg>')
    return "\n".join(s)

for pal in (LIGHT, DARK):
    path = f"assets/banner-{pal['name']}.svg"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(build(pal) + "\n")
    print("wrote", path)
