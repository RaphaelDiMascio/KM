"""Charte graphique inspirée de Decathlon (research.md R3–R4)."""
from pptx.dml.color import RGBColor

BLUE = RGBColor(0x36, 0x43, 0xBA)
NAVY = RGBColor(0x10, 0x1F, 0x47)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT = RGBColor(0xF2, 0xF3, 0xF7)
ORANGE = RGBColor(0xFF, 0x6A, 0x13)
TEXT = RGBColor(0x1B, 0x1B, 0x1F)

TITLE_FONT = "Montserrat"
BODY_FONT = "Open Sans"

# Tailles en points, dimensions en pouces (convertis par les helpers de visuals.py)
TITLE_SIZE = 26
BODY_SIZE = 18
CAPTION_SIZE = 14
FOOTER_SIZE = 10

SLIDE_W = 13.333
SLIDE_H = 7.5
M = 0.6
CONTENT_TOP = 1.85
CONTENT_BOTTOM = 6.75
CONTENT_LEFT = 0.8
CONTENT_RIGHT = 12.53
