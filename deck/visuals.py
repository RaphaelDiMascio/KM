"""Schémas en formes natives (éditables dans Google Slides).

Convention de nommage des formes (utilisée par check_deck.py) :
- TITLE, FOOTER*, HYPO_TAG, DECOR*, SOURCES* : exclus du compte de mots affichés ;
- VIS_<type>_<n> : formes d'un schéma.
"""
import math

from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.util import Inches, Pt

import theme as T


# --------------------------------------------------------------------------- helpers

def fill_text(tf, paras, size=16, color=T.TEXT, font=T.BODY_FONT, bold=False,
              italic=False, align=PP_ALIGN.LEFT, space_after=4):
    """Écrit une liste de paragraphes ; un paragraphe peut être (texte, {surcharges})."""
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    if isinstance(paras, str):
        paras = [paras]
    for i, p in enumerate(paras):
        spec = dict(size=size, color=color, font=font, bold=bold, italic=italic, align=align)
        if isinstance(p, tuple):
            text, over = p
            spec.update(over)
        else:
            text = p
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = spec["align"]
        para.space_after = Pt(space_after)
        run = para.add_run()
        run.text = text
        f = run.font
        f.name = spec["font"]
        f.size = Pt(spec["size"])
        f.bold = spec["bold"]
        f.italic = spec["italic"]
        f.color.rgb = spec["color"]


def text(slide, x, y, w, h, paras, name="TXT", anchor=MSO_ANCHOR.TOP, **kw):
    shp = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    shp.name = name
    tf = shp.text_frame
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.margin_top = tf.margin_bottom = Inches(0.03)
    fill_text(tf, paras, **kw)
    return shp


def box(slide, x, y, w, h, paras=None, fill=T.LIGHT, line=None, line_w=2.0,
        shape=MSO_SHAPE.ROUNDED_RECTANGLE, name="VIS", anchor=MSO_ANCHOR.MIDDLE,
        align=PP_ALIGN.CENTER, **kw):
    shp = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.name = name
    shp.shadow.inherit = False
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        shp.adjustments[0] = 0.12
    if fill is None:
        shp.fill.background()
    else:
        shp.fill.solid()
        shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(line_w)
    tf = shp.text_frame
    tf.vertical_anchor = anchor
    tf.margin_left = Inches(0.28 if align == PP_ALIGN.LEFT else 0.08)
    tf.margin_right = Inches(0.08)
    tf.margin_top = tf.margin_bottom = Inches(0.04)
    if paras:
        fill_text(tf, paras, align=align, **kw)
    return shp


class Namer:
    def __init__(self, kind):
        self.kind, self.i = kind, 0

    def __call__(self):
        self.i += 1
        return f"VIS_{self.kind}_{self.i}"


def head(txt, size=18, color=T.WHITE):
    return (txt, dict(bold=True, font=T.TITLE_FONT, size=size, color=color))


# --------------------------------------------------------------------------- schémas

def draw_cards(slide, d):
    """Cartes en grille : en-tête coloré + corps clair (slides 2, 3, 13)."""
    n = Namer("cards")
    items, cols = d["items"], d["cols"]
    rows = math.ceil(len(items) / cols)
    gap = 0.3
    x0, x1 = T.CONTENT_LEFT, T.CONTENT_RIGHT
    y0 = T.CONTENT_TOP
    y1 = 5.45 if (d.get("cta") or d.get("footnote")) else T.CONTENT_BOTTOM
    cw = (x1 - x0 - gap * (cols - 1)) / cols
    ch = (y1 - y0 - gap * (rows - 1)) / rows
    hh = d.get("head_h", 0.75)
    for i, it in enumerate(items):
        r, c = divmod(i, cols)
        x, y = x0 + c * (cw + gap), y0 + r * (ch + gap)
        accent = it.get("accent", False)
        box(slide, x, y, cw, hh, [head(it["head"], size=d.get("head_size", 20))],
            fill=T.ORANGE if accent else T.BLUE, shape=MSO_SHAPE.RECTANGLE, name=n())
        box(slide, x, y + hh, cw, ch - hh, [it["body"]], fill=T.LIGHT,
            shape=MSO_SHAPE.RECTANGLE, name=n(), size=d.get("body_size", 18), color=T.NAVY)
    if d.get("cta"):
        box(slide, x0, 5.75, x1 - x0, 0.9, [head(d["cta"], size=22)], fill=T.ORANGE, name=n())
    if d.get("footnote"):
        box(slide, x0, 5.8, x1 - x0, 0.7, [("✔ " + d["footnote"], dict(italic=True))],
            fill=None, line=T.BLUE, line_w=1.25, name=n(), size=15, color=T.NAVY)


def draw_iceberg(slide, d):
    n = Namer("iceberg")
    cx = 4.3
    box(slide, 0.6, 3.08, 8.0, 0.06, fill=T.BLUE, shape=MSO_SHAPE.RECTANGLE, name=n())
    box(slide, cx - 1.5, 1.75, 3.0, 1.33, fill=T.LIGHT, line=T.BLUE,
        shape=MSO_SHAPE.ISOSCELES_TRIANGLE, name=n())
    trap = box(slide, cx - 3.5, 3.14, 7.0, 3.45,
               [head(d["tacit_head"], size=19, color=T.ORANGE)] + d["tacit"],
               fill=T.NAVY, shape=MSO_SHAPE.TRAPEZOID, name=n(), size=16,
               color=T.WHITE, space_after=6)
    trap.adjustments[0] = 0.588
    text(slide, 5.75, 1.65, 2.9, 1.4,
         [head(d["explicit_head"], size=16, color=T.NAVY), d["explicit"]],
         name=n(), size=14, color=T.TEXT)
    box(slide, 9.0, 1.9, 3.7, 2.9,
        [(d["quote"], dict(italic=True, size=20, font=T.TITLE_FONT, color=T.NAVY)),
         head(d["author"], size=15, color=T.ORANGE)],
        fill=T.LIGHT, shape=MSO_SHAPE.RECTANGLE, name=n(), align=PP_ALIGN.LEFT,
        space_after=10)
    box(slide, 9.0, 1.9, 0.12, 2.9, fill=T.ORANGE, shape=MSO_SHAPE.RECTANGLE, name=n())


def draw_timeline(slide, d):
    n = Namer("timeline")
    x0, x1 = 1.0, 12.3

    def X(m):
        return x0 + (x1 - x0) * m / 18

    lanes = [1.8, 2.55, None, 3.95, 4.7]
    for ph, y in zip(d["phases"], [lanes[0], lanes[1], lanes[3], lanes[4]]):
        box(slide, X(ph["start"]), y, X(ph["end"]) - X(ph["start"]), 0.6,
            [head(ph["label"], size=13)], fill=ph["color"], name=n())
    for w in d["waves"]:
        box(slide, X(w["start"]) + 0.05, 3.25, X(w["end"]) - X(w["start"]) - 0.1, 0.48,
            [head(w["label"], size=13)], fill=T.ORANGE, name=n())
    box(slide, X(0), 5.45, X(18) - X(0), 0.5, [head(d["trust"], size=13, color=T.NAVY)],
        fill=T.LIGHT, line=T.BLUE, line_w=1.0, name=n())
    box(slide, x0, 6.15, x1 - x0, 0.03, fill=T.NAVY, shape=MSO_SHAPE.RECTANGLE, name=n())
    for m in d["ticks"]:
        box(slide, X(m) - 0.04, 6.08, 0.08, 0.17, fill=T.NAVY, shape=MSO_SHAPE.RECTANGLE, name=n())
        text(slide, X(m) - 0.4, 6.25, 0.8, 0.35, [f"M{m}"], name=n(), size=12,
             color=T.NAVY, align=PP_ALIGN.CENTER, bold=True)


def draw_seci(slide, d):
    n = Namer("seci")
    cw, ch = 3.45, 2.25
    pos = [(0.8, 1.8), (4.75, 1.8), (4.75, 4.5), (0.8, 4.5)]  # S, E, C, I
    fills = [T.BLUE, T.NAVY, T.BLUE, T.NAVY]
    for (label, action), (x, y), f in zip(d["cells"], pos, fills):
        box(slide, x, y, cw, ch, [head(label, size=20, color=T.ORANGE), action],
            fill=f, name=n(), size=17, color=T.WHITE, space_after=8)
    o = T.ORANGE
    box(slide, 4.3, 2.72, 0.4, 0.42, fill=o, shape=MSO_SHAPE.RIGHT_ARROW, name=n())
    box(slide, 6.27, 4.08, 0.42, 0.4, fill=o, shape=MSO_SHAPE.DOWN_ARROW, name=n())
    box(slide, 4.3, 5.42, 0.4, 0.42, fill=o, shape=MSO_SHAPE.LEFT_ARROW, name=n())
    box(slide, 2.32, 4.08, 0.42, 0.4, fill=o, shape=MSO_SHAPE.UP_ARROW, name=n())
    # Panneau des vagues
    y = 1.8
    for i, w in enumerate(d["waves"]):
        box(slide, 8.9, y, 3.6, 1.15, [head(w, size=16, color=T.NAVY)], fill=T.LIGHT,
            line=T.ORANGE, line_w=2.0, name=n())
        if i < len(d["waves"]) - 1:
            box(slide, 10.5, y + 1.22, 0.4, 0.42, fill=T.ORANGE, shape=MSO_SHAPE.DOWN_ARROW, name=n())
        y += 1.75


def draw_ba(slide, d):
    n = Namer("ba")
    box(slide, 0.8, 1.9, 4.6, 3.9, fill=None, line=T.BLUE, line_w=3.5, shape=MSO_SHAPE.OVAL, name=n())
    box(slide, 3.8, 1.9, 4.6, 3.9, fill=None, line=T.NAVY, line_w=3.5, shape=MSO_SHAPE.OVAL, name=n())
    box(slide, 3.9, 3.15, 1.4, 1.4, [head(d["center"], size=28)], fill=T.ORANGE,
        shape=MSO_SHAPE.OVAL, name=n())
    box(slide, 3.25, 4.68, 2.7, 0.38, [(d["center_sub"], dict(italic=True))], fill=T.WHITE,
        shape=MSO_SHAPE.RECTANGLE, name=n(), size=13, color=T.NAVY)
    text(slide, 1.15, 3.3, 2.6, 1.0, [head(d["left"][0], size=20, color=T.BLUE), d["left"][1]],
         name=n(), size=15, color=T.NAVY, align=PP_ALIGN.CENTER)
    text(slide, 5.45, 3.3, 2.7, 1.0, [head(d["right"][0], size=20, color=T.NAVY), d["right"][1]],
         name=n(), size=15, color=T.NAVY, align=PP_ALIGN.CENTER)
    y = 1.85
    for item in d["items"]:
        box(slide, 8.9, y, 3.65, 0.85, [item], fill=T.LIGHT, shape=MSO_SHAPE.RECTANGLE,
            name=n(), size=16, color=T.NAVY, align=PP_ALIGN.LEFT)
        box(slide, 8.9, y, 0.1, 0.85, fill=T.ORANGE, shape=MSO_SHAPE.RECTANGLE, name=n())
        y += 1.05
    box(slide, 0.8, 6.0, 11.75, 0.6, [(d["caption"], dict(italic=True))], fill=None,
        line=T.BLUE, line_w=1.25, name=n(), size=16, color=T.NAVY)


def draw_risk_benefit(slide, d):
    n = Namer("risk_benefit")
    cols = [(0.8, d["risks_head"], d["risks"], T.NAVY), (6.95, d["benefits_head"], d["benefits"], T.ORANGE)]
    for x, h, items, color in cols:
        box(slide, x, 1.8, 5.6, 0.65, [head(h, size=20)], fill=color, shape=MSO_SHAPE.RECTANGLE, name=n())
        y = 2.6
        for it in items:
            box(slide, x, y, 5.6, 0.68, [it], fill=T.LIGHT, shape=MSO_SHAPE.RECTANGLE, name=n(),
                size=18, color=T.NAVY, align=PP_ALIGN.LEFT)
            box(slide, x, y, 0.1, 0.68, fill=color, shape=MSO_SHAPE.RECTANGLE, name=n())
            y += 0.8
    box(slide, 0.8, 5.95, 11.75, 0.65, [head(d["band"], size=17, color=T.NAVY)], fill=None,
        line=T.BLUE, line_w=1.25, name=n())


def draw_trust(slide, d):
    n = Namer("trust")
    cw, gap = 2.74, 0.26
    for i, (h, body) in enumerate(d["criteria"]):
        x = 0.8 + i * (cw + gap)
        box(slide, x, 1.85, cw, 0.95, [head(h, size=17)], fill=T.BLUE, shape=MSO_SHAPE.RECTANGLE, name=n())
        box(slide, x, 2.8, cw, 2.2, [body], fill=T.LIGHT, shape=MSO_SHAPE.RECTANGLE, name=n(),
            size=18, color=T.NAVY)
    box(slide, 0.8, 5.4, 11.75, 0.95, [head(d["avoid"], size=18)], fill=T.ORANGE, name=n())


def draw_kpi(slide, d):
    n = Namer("kpi")
    text(slide, 0.8, 1.75, 4.6, 0.5, [head(d["gov_head"], size=18, color=T.BLUE)], name=n())
    fills = [T.NAVY, T.BLUE, T.LIGHT]
    colors = [T.WHITE, T.WHITE, T.NAVY]
    y = 2.3
    for i, (label, f, c) in enumerate(zip(d["gov"], fills, colors)):
        box(slide, 0.8, y, 4.4, 0.8, [head(label, size=16, color=c)], fill=f, name=n())
        if i < 2:
            box(slide, 2.8, y + 0.85, 0.4, 0.38, fill=T.ORANGE, shape=MSO_SHAPE.DOWN_ARROW, name=n())
        y += 1.28
    text(slide, 5.9, 1.75, 6.0, 0.5, [head(d["kpi_head"], size=18, color=T.BLUE)], name=n())
    for i, k in enumerate(d["kpis"]):
        r, c = divmod(i, 2)
        box(slide, 5.9 + c * 3.38, 2.3 + r * 1.65, 3.2, 1.45, [head(k, size=16, color=T.NAVY)],
            fill=T.LIGHT, line=T.BLUE, line_w=1.5, name=n())
    box(slide, 0.8, 6.0, 11.75, 0.6, [head(d["band"], size=16)], fill=T.ORANGE, name=n())


def draw_two_columns(slide, d):
    n = Namer("cols")
    box(slide, 0.8, 1.85, 5.6, 1.45, [(d["quote"], dict(italic=True, font=T.TITLE_FONT, size=19))],
        fill=T.NAVY, shape=MSO_SHAPE.RECTANGLE, name=n(), color=T.WHITE)
    text(slide, 0.8, 3.5, 5.6, 3.2, ["• " + b for b in d["left"]], name="COL_L", size=19,
         color=T.TEXT, space_after=12)
    box(slide, 6.95, 1.85, 5.6, 0.75, [head(d["right_head"], size=20)], fill=T.BLUE,
        shape=MSO_SHAPE.RECTANGLE, name=n())
    text(slide, 6.95, 2.8, 5.6, 3.9, ["• " + b for b in d["right"]], name="COL_R", size=19,
         color=T.TEXT, space_after=12)


def draw_side_card(slide, d):
    n = Namer("side")
    box(slide, 8.7, 1.9, 3.85, 0.8, [head(d["head"], size=19)], fill=T.ORANGE,
        shape=MSO_SHAPE.RECTANGLE, name=n())
    box(slide, 8.7, 2.7, 3.85, 2.2, [d["body"]], fill=T.LIGHT, shape=MSO_SHAPE.RECTANGLE,
        name=n(), size=19, color=T.NAVY)


def draw_sources(slide, d):
    n = Namer("sources")
    box(slide, 0.8, 1.75, 0.12, 4.9, fill=T.ORANGE, shape=MSO_SHAPE.RECTANGLE, name="DECOR_bar")
    half = math.ceil(len(d["sources"]) / 2)
    text(slide, 1.1, 1.75, 5.6, 4.4, d["sources"][:half], name="SOURCES_1", size=14,
         color=T.NAVY, space_after=8)
    text(slide, 6.95, 1.75, 5.6, 4.4, d["sources"][half:], name="SOURCES_2", size=14,
         color=T.NAVY, space_after=8)
    text(slide, 0.8, 6.3, 11.75, 0.45, [d["line"]], name=n(), size=14, color=T.BLUE,
         bold=True, align=PP_ALIGN.CENTER)


DRAWERS = {
    "cards": draw_cards,
    "iceberg": draw_iceberg,
    "timeline": draw_timeline,
    "seci": draw_seci,
    "ba": draw_ba,
    "risk_benefit": draw_risk_benefit,
    "trust": draw_trust,
    "kpi": draw_kpi,
    "two_columns": draw_two_columns,
    "side_card": draw_side_card,
    "sources": draw_sources,
}


def draw(slide, kind, data):
    if kind not in DRAWERS:
        raise NotImplementedError(kind)
    DRAWERS[kind](slide, data)
