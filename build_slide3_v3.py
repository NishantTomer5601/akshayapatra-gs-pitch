"""Append proposed slide-3 v3: central $250k pie, gaps top-left/right,
solutions bottom-left/right."""
from deck_lib import *
from pptx import Presentation
from pptx.enum.chart import XL_CHART_TYPE

PATH = "AkshayaPatra_GS_Pitch.pptx"
prs = Presentation(PATH)

s = prs.slides.add_slide(prs.slide_layouts[6])
chrome(s, len(prs.slides._sldIdLst),
       "The two gaps — and the $250,000 that closes them",
       "The gaps highlighted in the supply chain, the grant that closes them, and the "
       "solution we build for each — all in one view.",
       takeaway="Two fixable gaps, two targeted builds — $250k of capital becomes "
                "$310k of savings, every year.")
_, tf = tb(s, SW - ML - 3.6, 0.06, 3.6, 0.20)
para(tf, "PROPOSED SLIDE 3 — v3 (pie quadrant)", size=7.5, color=GRAY, italic=True,
     align=PP_ALIGN.RIGHT, first=True, space_after=0)

QW = 3.05                       # quadrant width
LQX, RQX = ML, SW - ML - QW     # left/right quadrant x

# ---------------- top-left: gap 1 ----------------
cy1 = section(s, LQX, 1.50, QW, "GAP 1 — Procurement", accent=RED, size=10.5)
_, tf = tb(s, LQX, cy1, QW, 1.30)
para(tf, [("•  Manual indenting", True, TEXT),
          (" — blind to attendance, exams & holidays", False, TEXT)],
     size=7.8, first=True, line_spacing=1.0)
para(tf, [("•  Spot-buying", True, TEXT),
          (" at mandi peak prices; no price intelligence", False, TEXT)],
     size=7.8, line_spacing=1.0)
para(tf, [("•  No feedback loop", True, TEXT),
          (" on actual meal uptake", False, TEXT)], size=7.8, line_spacing=1.0)
para(tf, [("8–10% over-produced · +12% spot premium [dummy]", True, RED)],
     size=7.8, space_after=0, line_spacing=1.0)

# ---------------- top-right: gap 2 ----------------
cy2 = section(s, RQX, 1.50, QW, "GAP 2 — Distribution", accent=RED, size=10.5)
_, tf = tb(s, RQX, cy2, QW, 1.30)
para(tf, [("•  Static, driver-memory routes", True, TEXT),
          (" — late vans mean children stay hungry all day", False, TEXT)],
     size=7.8, first=True, line_spacing=1.0)
para(tf, [("•  Untracked vessels", True, TEXT),
          ("; adulteration & diversion risk en route", False, TEXT)],
     size=7.8, line_spacing=1.0)
para(tf, [("•  No proof-of-delivery", True, TEXT),
          (" — disputes go unresolved", False, TEXT)], size=7.8, line_spacing=1.0)
para(tf, [("6.2% miss lunch window · $35k/yr shrinkage [dummy]", True, RED)],
     size=7.8, space_after=0, line_spacing=1.0)

# ---------------- center: the $250k pie ----------------
cd = CategoryChartData()
cd.categories = ["Solution 1 — $150k", "Solution 2 — $100k"]
cd.add_series('s', [150, 100])
gf = s.shapes.add_chart(XL_CHART_TYPE.DOUGHNUT, Inches(3.58), Inches(2.55),
                        Inches(2.85), Inches(2.45), cd)
ch = gf.chart
ch.font.size = Pt(8); ch.font.name = SANS; ch.has_title = False
ch.has_legend = False
ser = ch.series[0]
for i, c in enumerate([NAVY, GREEN]):
    pt = ser.points[i]
    pt.format.fill.solid(); pt.format.fill.fore_color.rgb = c
    pt.format.line.color.rgb = WHITE; pt.format.line.width = Pt(1.5)
plot = ch.plots[0]
plot.has_data_labels = True
dl = plot.data_labels
dl.show_value = True
dl.number_format = '"$"0"k"'; dl.number_format_is_linked = False
dl.font.size = Pt(10); dl.font.bold = True; dl.font.color.rgb = WHITE
_, tf = tb(s, 3.58, 5.06, 2.85, 0.44)
para(tf, [("THE $250k GRANT", True, NAVY)], size=9.5, first=True, space_after=1,
     align=PP_ALIGN.CENTER)
para(tf, "60 / 40 — weighted to the costlier gap", size=7.2, color=GRAY,
     align=PP_ALIGN.CENTER, space_after=0, italic=True)

# quadrant connectors
dotted_arrow(s, LQX + QW + 0.10, 2.55, 4.15, 3.15, color=RED, width=1.1)      # gap1 -> pie
dotted_arrow(s, RQX - 0.10, 2.55, 5.85, 3.15, color=RED, width=1.1)           # gap2 -> pie
dotted_arrow(s, 4.10, 4.55, LQX + QW + 0.06, 5.05, color=NAVY, width=1.1)     # pie -> sol1
dotted_arrow(s, 5.90, 4.55, RQX - 0.06, 5.05, color=GREEN, width=1.1)         # pie -> sol2

# ---------------- bottom-left: solution 1 ----------------
S1Y = 4.30
rect(s, LQX, S1Y, QW, 1.95, fill=PALEBLUE, line=NAVY, line_w=1.0,
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)
_, tf = tb(s, LQX + 0.13, S1Y + 0.09, QW - 0.26, 1.80)
para(tf, [("SOLUTION 1\n“Annapurna AI” · $150k", True, NAVY)], size=9.5,
     first=True, space_after=3, line_spacing=0.95)
para(tf, [("What: ", True, NAVY),
          ("ML demand-forecasting & procurement planning for all 68 kitchens",
           False, TEXT)], size=8.2, line_spacing=1.04)
para(tf, [("How: ", True, NAVY),
          ("predicts school-level attendance; auto-generates indents & buying schedules",
           False, TEXT)], size=8.2, line_spacing=1.04)
para(tf, [("→ ~70% less waste  ·  est. $230k saved / yr [dummy]", True, GREEN)],
     size=8.3, space_after=0, line_spacing=1.05)

# ---------------- bottom-right: solution 2 ----------------
rect(s, RQX, S1Y, QW, 1.95, fill=PALEGREEN, line=GREEN, line_w=1.0,
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)
_, tf = tb(s, RQX + 0.13, S1Y + 0.09, QW - 0.26, 1.80)
para(tf, [("SOLUTION 2\n“Last-Mile Shield” · $100k", True, GREEN)], size=9.5,
     first=True, space_after=3, line_spacing=0.95)
para(tf, [("What: ", True, NAVY),
          ("AI routing + telematics (GPS, cameras, RFID) + geofenced smart locks",
           False, TEXT)], size=8.2, line_spacing=1.04)
para(tf, [("How: ", True, NAVY),
          ("drops sequenced to lunch bells; doors unlock only near a registered school",
           False, TEXT)], size=8.2, line_spacing=1.04)
para(tf, [("→ 99%+ on-time · −18% km  ·  est. $80k saved / yr [dummy]", True, GREEN)],
     size=8.3, space_after=0, line_spacing=1.05)

prs.save(PATH)
print("saved; total slides:", len(prs.slides._sldIdLst))
