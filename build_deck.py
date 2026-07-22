"""Akshaya Patra x Goldman Sachs pitch — v2: 4:3, open editorial layout (minimal boxes)."""
from deck_lib import *
import math

prs = new_deck()

# =====================================================================
# SLIDE 1
# =====================================================================
s = add_slide(prs)
chrome(s, 1, "Who is The Akshaya Patra Foundation?",
       "The world's largest NGO-run school meal programme — serving 2.3 million children "
       "every school day, so that hunger never interrupts education.",
       takeaway="“No child shall be deprived of education because of hunger” — "
                "at a scale no other NGO matches.")

# hero band
rect(s, ML, 1.42, SW - 2*ML, 0.80, fill=ORANGE, line=None)
img_placeholder(s, ML + 0.08, 1.51, 0.98, 0.62, "AKSHAYA PATRA\nlogo")
_, tf = tb(s, ML + 1.22, 1.42, SW - 2*ML - 1.36, 0.80, anchor=MSO_ANCHOR.MIDDLE)
para(tf, [("Over 1 in 3 children in India show signs of undernourishment", True, WHITE),
          (" — and hunger is a leading reason children drop out of school. Founded in "
           "2000 in Bengaluru with ", False, WHITE),
          ("1,500 children across 5 schools", True, WHITE),
          (", Akshaya Patra now runs the world's largest NGO-operated mid-day meal "
           "programme — a PPP with the Government of India that has served ", False, WHITE),
          ("4+ billion cumulative meals.", True, WHITE)],
     size=8, first=True, space_after=0, line_spacing=1.0)

LX, LW = ML, 4.42
RX, RW = 5.02, SW - ML - 5.02
vline(s, 4.77, 2.42, 6.45)

# L: who & why
cy = section(s, LX, 2.38, LW, "Who they are & why we chose them", accent=NAVY)
_, tf = tb(s, LX, cy, LW, 1.55)
para(tf, [("Mission: ", True, NAVY),
          ("eliminate classroom hunger by implementing the Mid-Day Meal Scheme in "
           "government schools while fighting child malnutrition across India.",
           False, TEXT)], size=8, first=True, line_spacing=1.02)
para(tf, [("Why Akshaya Patra: ", True, NAVY),
          ("our on-ground kitchen inspections and supply-chain review found world-class "
           "production — and ", False, TEXT),
          ("two clearly identified, fixable gaps", True, TEXT),
          (" where $250k unlocks compounding, year-on-year impact rather than one-off "
           "sustenance.", False, TEXT)], size=8, line_spacing=1.02)
para(tf, "✓ 25+ yrs of proven delivery   ✓ Govt-audited PPP   ✓ Tech-forward leadership",
     size=7.8, color=GREEN, bold=True, space_after=0)

# L: journey chart
cy = section(s, LX, 4.32, LW, "The journey — daily meals served (millions)", accent=BLUE)
line_chart(s, LX, cy + 0.02, LW, 1.42,
           ["2000", "2005", "2010", "2015", "2020", "2023", "2026"],
           [("Meals/day (M)", [0.001, 0.33, 1.20, 1.44, 1.80, 2.00, 2.30])], [NAVY],
           font_size=7)
_, tf = tb(s, LX, cy + 1.50, LW, 0.30)
para(tf, [("2012: ", True, TEXT), ("1 billionth meal   ·   ", False, TEXT),
          ("2019: ", True, TEXT), ("3 billionth served by Hon'ble PM   ·   ", False, TEXT),
          ("2024: ", True, TEXT), ("4 billion meals", False, TEXT)],
     size=6.8, first=True, space_after=0, color=GRAY)

# R: what they do
cy = section(s, RX, 2.38, RW, "What they do — the hub-and-spoke model", accent=MIDBLUE)
_, tf = tb(s, RX, cy, RW, 1.15)
para(tf, [("•  Centralised mega-kitchens ", True, TEXT),
          ("cook up to 100,000 meals each before 6 AM daily", False, TEXT)],
     size=7.8, first=True, line_spacing=1.0)
para(tf, [("•  Hub-and-spoke delivery ", True, TEXT),
          ("of hot, locally-adapted menus to school doorsteps", False, TEXT)],
     size=7.8, line_spacing=1.0)
para(tf, [("•  PPP funding ", True, TEXT),
          ("— govt subsidies + philanthropy; every $ leveraged ~3x", False, TEXT)],
     size=7.8, line_spacing=1.0)
para(tf, [("•  Beyond food: ", True, TEXT),
          ("scholarships, anganwadi feeding, disaster-relief kitchens", False, TEXT)],
     size=7.8, space_after=0, line_spacing=1.0)

# R: scale
cy = section(s, RX, 3.94, RW, "Scale at a glance (FY26)", accent=ORANGE)
qw = RW / 4
for i, (v, c) in enumerate([("2.3M", "meals served\nevery day"),
                            ("68", "mega-kitchens\nacross India"),
                            ("16", "states &\n2 UTs"),
                            ("24,000+", "govt schools\nserved")]):
    stat(s, RX + i*qw, cy + 0.02, qw, v, c, vsize=14, csize=6.8)

# R: SDGs
cy = section(s, RX, 5.12, RW, "Aligned to UN SDGs", accent=GREEN)
for i, (t1, t2) in enumerate([("SDG 2", "Zero Hunger"), ("SDG 4", "Quality Educ."),
                              ("SDG 17", "Partners")]):
    img_placeholder(s, RX + i * 0.72, cy + 0.04, 0.64, 0.64, t1, t2)
img_placeholder(s, RX + 2.28, cy + 0.04, RW - 2.28, 0.64,
                "\U0001F4F7 PHOTO: children at mid-day meal")

# =====================================================================
# SLIDE 2
# =====================================================================
s = add_slide(prs)
chrome(s, 2, "A world-class supply chain — with two blind spots",
       "We walked their kitchens, interviewed staff and mapped the end-to-end flow: "
       "production is best-in-class; the gaps sit at the first and last mile.",
       takeaway="A Formula-1 production line — fed by guesswork, delivered on hand-drawn "
                "maps. That is where we intervene.")

_, tf = tb(s, ML, 1.40, SW - 2*ML, 0.24)
para(tf, "Our diligence: 2 kitchen visits  •  12 staff interviews  •  procurement & route "
         "data review", size=8, color=GRAY, italic=True, first=True, space_after=0)

# borderless validation row
vx_list = [(ML, 3.0, "Audited & certified",
            "FSSAI-licensed, ISO 22000-certified kitchens; govt & third-party audits"),
           (ML + 3.15, 3.0, "Global recognition",
            "UK PM Rishi Sunak toured the Bengaluru kitchen — praised hygiene & automation"),
           (ML + 6.30, 2.9, "Our on-ground audit",
            "Gravity-flow cooking, 2-hr batch cycles, near-zero contamination risk")]
for vx, vw, t, d in vx_list:
    _, tf = tb(s, vx, 1.74, vw, 0.72)
    para(tf, [("✓ " + t, True, GREEN)], size=9, first=True, space_after=1)
    para(tf, d, size=7.2, color=TEXT, space_after=0, line_spacing=0.95)

# chevron flow
FY = 2.72; FH = 0.98
steps = [
    ("PROCURE-\nMENT", "Grains, dairy\nfrom mandis", RED, True),
    ("STORAGE", "Silos, cold\nrooms; FIFO", BLUE, False),
    ("PRE-\nPROCESS", "Auto roti lines,\nveg prep", BLUE, False),
    ("COOKING", "Steam cauldrons;\n100k by 6 AM", BLUE, False),
    ("QC &\nPACKING", "Lab-tested;\nsealed vessels", BLUE, False),
    ("DISTRIB-\nUTION", "Van fleet to\nschools by lunch", RED, True),
]
cw = 1.50; gap_w = 0.04
fx = ML
for i, (t, d, c, is_gap) in enumerate(steps):
    x = fx + i * (cw + gap_w)
    ch = rect(s, x, FY, cw, FH, fill=(PALERED if is_gap else PALEBLUE),
              line=(RED if is_gap else MIDBLUE), line_w=(1.5 if is_gap else 0.9),
              shape=MSO_SHAPE.CHEVRON)
    try: ch.adjustments[0] = 0.30
    except Exception: pass
    _, tf = tb(s, x + 0.20, FY + 0.08, cw - 0.32, FH - 0.16, anchor=MSO_ANCHOR.MIDDLE)
    para(tf, t.replace("-\n", ""), size=7.8, color=(RED if is_gap else NAVY), bold=True,
         first=True, align=PP_ALIGN.CENTER, space_after=1, line_spacing=0.9)
    para(tf, d, size=6, color=TEXT, align=PP_ALIGN.CENTER, space_after=0, line_spacing=0.9)

# arrows from validation texts to nodes
dotted_arrow(s, 4.4, 2.42, 4.9, FY - 0.04, color=GREEN, curve=True, width=1.0)
dotted_arrow(s, 7.6, 2.42, 7.2, FY - 0.04, color=GREEN, curve=True, width=1.0)

_, tf = tb(s, ML, FY + FH + 0.08, SW - 2*ML, 0.26)
para(tf, [("Steps 2–5 are best-in-class ", True, GREEN),
          ("— automated, audited, built to scale. No intervention needed.", False, GRAY)],
     size=8.5, first=True, align=PP_ALIGN.CENTER, space_after=0)

# gap boxes
GY = 4.40; GH = 1.82
g1x, g1w = ML, 4.50
rect(s, g1x, GY, g1w, GH, fill=WHITE, line=RED, line_w=1.25)
rect(s, g1x, GY, g1w, 0.32, fill=RED, line=None)
_, tf = tb(s, g1x + 0.12, GY + 0.045, g1w - 0.24, 0.26)
para(tf, "GAP 1 — PROCUREMENT: no demand forecasting", size=9, color=WHITE, bold=True,
     first=True, space_after=0)
_, tf = tb(s, g1x + 0.14, GY + 0.42, g1w - 0.28, GH - 0.52)
para(tf, [("•  Manual estimates", True, TEXT),
          (" — no view of school-level attendance, holidays or menu uptake", False, TEXT)],
     size=7.5, first=True, line_spacing=1.0)
para(tf, [("•  ~8–10% over-production", True, TEXT),
          (" wasted on low-attendance days [dummy]", False, TEXT)], size=7.5,
     line_spacing=1.0)
para(tf, [("•  Reactive spot-buying", True, TEXT),
          (" at mandi peak prices — up to 12% above plan [dummy]", False, TEXT)],
     size=7.5, line_spacing=1.0)
para(tf, [("•  No price intelligence", True, TEXT),
          (" — cheapest forward-buying windows are missed", False, TEXT)], size=7.5,
     line_spacing=1.0)
para(tf, [("•  Result: ", True, TEXT),
          ("higher cost per meal → fewer children fed per donor $", False, TEXT)],
     size=7.5, line_spacing=1.0)
para(tf, [("→ addressed by Solution 1 ($150k)", True, NAVY)], size=7.8, space_after=0)

g2x, g2w = ML + 4.70, 4.50
rect(s, g2x, GY, g2w, GH, fill=WHITE, line=RED, line_w=1.25)
rect(s, g2x, GY, g2w, 0.32, fill=RED, line=None)
_, tf = tb(s, g2x + 0.12, GY + 0.045, g2w - 0.24, 0.26)
para(tf, "GAP 2 — DISTRIBUTION: no route intelligence", size=9, color=WHITE, bold=True,
     first=True, space_after=0)
_, tf = tb(s, g2x + 0.14, GY + 0.42, g2w - 0.28, GH - 0.52)
para(tf, [("•  Static, driver-memory routes", True, TEXT),
          (" — 15–30 min past the lunch bell means children stay hungry all day",
           False, TEXT)], size=7.5, first=True, line_spacing=1.0)
para(tf, [("•  No telematics", True, TEXT),
          (" — vessels & utensils untracked; losses recur", False, TEXT)], size=7.5,
     line_spacing=1.0)
para(tf, [("•  Adulteration / diversion risk", True, TEXT),
          (" — unsealed vans can be offloaded at roadside dhabas", False, TEXT)],
     size=7.5, line_spacing=1.0)
para(tf, [("•  No proof-of-delivery", True, TEXT),
          (" — school shortfall disputes unresolved", False, TEXT)], size=7.5,
     line_spacing=1.0)
para(tf, [("•  Result: ", True, TEXT),
          ("missed lunch windows, fuel burn, shrinkage", False, TEXT)], size=7.5,
     line_spacing=1.0)
para(tf, [("→ addressed by Solution 2 ($100k)", True, NAVY)], size=7.8, space_after=0)

dotted_arrow(s, g1x + 0.8, GY, fx + 0.75, FY + FH + 0.03, color=RED, width=1.25)
dotted_arrow(s, g2x + 3.9, GY, fx + 5 * (cw + gap_w) + 0.75, FY + FH + 0.03,
             color=RED, width=1.25)

# =====================================================================
# SLIDE 3
# =====================================================================
s = add_slide(prs)
chrome(s, 3, "Our proposal — $250k deployed on the first & last mile",
       "Two targeted, technology-led interventions that convert the grant into permanent "
       "capability — not one year of operating expense.",
       takeaway="Not funding a year of operations — installing a permanent upgrade that "
                "pays for itself, every year.")

# allocation
cy = section(s, ML, 1.48, SW - 2*ML, "Allocation of the $250,000 grant", accent=NAVY)
bar_y = cy + 0.06; bar_h = 0.48
bx = ML + 0.15; bw_total = SW - 2*ML - 0.3
w1 = bw_total * 0.6; w2 = bw_total * 0.4
rect(s, bx, bar_y, w1, bar_h, fill=NAVY, line=None)
rect(s, bx + w1, bar_y, w2, bar_h, fill=GREEN, line=None)
_, tf = tb(s, bx, bar_y, w1, bar_h, anchor=MSO_ANCHOR.MIDDLE)
para(tf, "$150k — Solution 1: Predictive demand planning (60%)", size=9.5, color=WHITE,
     bold=True, align=PP_ALIGN.CENTER, first=True, space_after=0)
_, tf = tb(s, bx + w1, bar_y, w2, bar_h, anchor=MSO_ANCHOR.MIDDLE)
para(tf, "$100k — Solution 2:\nSmart distribution (40%)", size=9.5, color=WHITE,
     bold=True, align=PP_ALIGN.CENTER, first=True, space_after=0, line_spacing=0.95)
_, tf = tb(s, bx, bar_y + bar_h + 0.05, w1, 0.26)
para(tf, "Fixes the costliest gap first: waste & procurement inefficiency at source",
     size=7.2, color=GRAY, align=PP_ALIGN.CENTER, first=True, space_after=0)
_, tf = tb(s, bx + w1, bar_y + bar_h + 0.05, w2, 0.26)
para(tf, "Every meal on time, intact & untouched", size=7.2, color=GRAY,
     align=PP_ALIGN.CENTER, first=True, space_after=0)

# two solutions
S3Y = 2.92
vline(s, 4.77, S3Y + 0.05, 4.62)
cy = section(s, ML, S3Y, 4.42, "Solution 1 — “Annapurna AI” · $150k", accent=NAVY,
             size=10.5)
_, tf = tb(s, ML, cy, 4.42, 1.30)
para(tf, [("What: ", True, NAVY),
          ("ML demand-forecasting & procurement-planning platform across all 68 kitchens",
           False, TEXT)], size=7.8, first=True, line_spacing=1.0)
para(tf, [("How: ", True, NAVY),
          ("predicts school-level attendance from history, calendars & seasonality; "
           "auto-generates indents and forward procurement schedules", False, TEXT)],
     size=7.8, line_spacing=1.0)
para(tf, [("Impact: ", True, NAVY),
          ("cuts food waste ~70%, buys ahead of price spikes", False, TEXT),
          ("  →  est. $230k saved / yr [dummy]", True, GREEN)], size=7.8, space_after=0,
     line_spacing=1.0)

cy = section(s, 5.02, S3Y, SW - ML - 5.02, "Solution 2 — “Last-Mile Shield” · $100k",
             accent=GREEN, size=10.5)
_, tf = tb(s, 5.02, cy, SW - ML - 5.02, 1.30)
para(tf, [("What: ", True, NAVY),
          ("AI route optimisation + van telematics (GPS, cameras, RFID tags) + geofenced "
           "smart locks", False, TEXT)], size=7.8, first=True, line_spacing=1.0)
para(tf, [("How: ", True, NAVY),
          ("routes sequenced to each school's lunch bell; van doors unlock only within "
           "150 m of a registered school — no diversion, no adulteration", False, TEXT)],
     size=7.8, line_spacing=1.0)
para(tf, [("Impact: ", True, NAVY),
          ("99%+ on-time, −18% fleet km, zero shrinkage", False, TEXT),
          ("  →  est. $80k saved / yr [dummy]", True, GREEN)], size=7.8, space_after=0,
     line_spacing=1.0)

# flywheel — horizontal cycle
cy = section(s, ML, 4.55, SW - 2*ML, "The savings flywheel — how impact compounds",
             accent=ORANGE)
pw2, ph2 = 1.85, 0.52
pxs = [ML + 0.10 + i * (pw2 + 0.45) for i in range(4)]
ptexts = ["Grant funds\ntech — once", "Savings of\n$310k / yr", "Reinvested in\nmore meals",
          "More data →\nbetter models"]
pcols = [NAVY, GREEN, ORANGE, MIDBLUE]
py3 = cy + 0.04
for px3, t, c in zip(pxs, ptexts, pcols):
    rect(s, px3, py3, pw2, ph2, fill=WHITE, line=c, line_w=1.25,
         shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.25)
    _, tf = tb(s, px3, py3 + 0.02, pw2, ph2 - 0.04, anchor=MSO_ANCHOR.MIDDLE)
    para(tf, t, size=7.2, color=c, bold=True, align=PP_ALIGN.CENTER, first=True,
         space_after=0, line_spacing=0.92)
for i in range(3):
    dotted_arrow(s, pxs[i] + pw2 + 0.04, py3 + ph2/2, pxs[i+1] - 0.04, py3 + ph2/2,
                 color=GRAY, curve=False, width=1.1)
_, tf = tb(s, ML, py3 + ph2 + 0.04, SW - 2*ML, 0.20)
para(tf, "…and the cycle repeats — every year, without further funding", size=7,
     color=GRAY, italic=True, first=True, space_after=0, align=PP_ALIGN.CENTER)

# unlocks
cy = section(s, ML, 5.74, SW - 2*ML, "What the grant unlocks — every year, in perpetuity",
             accent=GREEN)
qw = (SW - 2*ML) / 5
for i, (v, c) in enumerate([("$310k", "combined annual\nsavings (1.24x grant)"),
                            ("+105,000", "additional children\nfed per year"),
                            ("~70%", "reduction in\nfood wastage"),
                            ("99%+", "meals inside the\nlunch window"),
                            ("<10 mo", "payback on the\nfull $250k")]):
    stat(s, ML + i*qw, cy - 0.06, qw, v, c, vsize=12.5, csize=6.3)

# =====================================================================
# SLIDE 4
# =====================================================================
s = add_slide(prs)
chrome(s, 4, "Solution 1 — “Annapurna AI”: predict demand, buy smart",
       "$150k builds a demand-forecasting and procurement-planning engine that ends "
       "over-production and peak-price buying across all 68 kitchens.",
       takeaway="Every rupee not wasted is a meal served — forecasting turns waste into "
                "105,000 more children fed each year.")

# left: problem
P4W = 3.45
cy = section(s, ML, 1.48, P4W, "The problem today", accent=RED)
_, tf = tb(s, ML, cy, P4W, 1.35)
para(tf, [("•  Manual, gut-feel indenting", True, TEXT),
          (" 3 days ahead — blind to attendance swings & holidays", False, TEXT)],
     size=7.6, first=True, line_spacing=1.0)
para(tf, [("•  Spot purchases", True, TEXT),
          (" at mandi peak prices when stocks run short", False, TEXT)], size=7.6,
     line_spacing=1.0)
para(tf, [("•  No feedback loop", True, TEXT),
          (" from schools on actual meal uptake", False, TEXT)], size=7.6,
     space_after=0, line_spacing=1.0)
qw = P4W / 2
stat(s, ML, cy + 1.02, qw, "8–10%", "meals over-produced\n& wasted [dummy]", color=RED,
     vsize=13, csize=6.8)
stat(s, ML + qw, cy + 1.02, qw, "+12%", "paid over plan on\nspot buys [dummy]", color=RED,
     vsize=13, csize=6.8)

# left: rollout
cy = section(s, ML, 3.50, P4W, "Rollout plan", accent=ORANGE)
_, tf = tb(s, ML, cy, P4W, 0.95)
para(tf, [("Mo 1–4: ", True, NAVY), ("pilot in 3 Bengaluru kitchens; baseline waste "
          "audit", False, TEXT)], size=7.4, first=True, line_spacing=1.0)
para(tf, [("Mo 5–8: ", True, NAVY), ("model tuning; procurement-ERP integration",
          False, TEXT)], size=7.4, line_spacing=1.0)
para(tf, [("Mo 9–12: ", True, NAVY), ("scale to all 68 kitchens; hand over to in-house "
          "tech team", False, TEXT)], size=7.4, space_after=0, line_spacing=1.0)

# left: waste chart
cy = section(s, ML, 4.74, P4W, "Food waste — % of production", accent=NAVY, size=10.5)
col_chart(s, ML, cy, P4W, 1.30, ["Today", "Yr 1", "Yr 2"],
          [("Waste %", [9.0, 4.5, 2.7])], [RED], gap=80, font_size=7)

# right: how it works
HX, HW = 4.15, SW - ML - 4.15
vline(s, 3.95, 1.55, 6.45)
cy = section(s, HX, 1.48, HW, "How it works — from signals to indents", accent=MIDBLUE)
fy = cy + 0.04
rect(s, HX, fy, HW, 0.66, fill=PALEBLUE, line=MIDBLUE, line_w=0.9,
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08)
_, tf = tb(s, HX + 0.12, fy + 0.05, HW - 0.24, 0.58)
para(tf, [("1 · DATA INPUTS   ", True, NAVY),
          ("school attendance feeds • academic calendars & holidays • menu cycles • "
           "mandi price APIs • weather & seasonality", False, TEXT)],
     size=7.4, first=True, space_after=0, line_spacing=1.0)
dotted_arrow(s, HX + HW/2, fy + 0.68, HX + HW/2, fy + 0.86, color=MIDBLUE, curve=False)
rect(s, HX, fy + 0.88, HW, 0.66, fill=NAVY, line=None,
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08)
_, tf = tb(s, HX + 0.12, fy + 0.93, HW - 0.24, 0.58)
para(tf, [("2 · ML FORECASTING ENGINE   ", True, WHITE),
          ("kitchen-wise meal-demand prediction (±2% target) • price-trend models flag "
           "the cheapest buying windows", False, WHITE)],
     size=7.4, first=True, space_after=0, line_spacing=1.0)
dotted_arrow(s, HX + HW/2, fy + 1.56, HX + HW/2, fy + 1.74, color=MIDBLUE, curve=False)
rect(s, HX, fy + 1.76, HW, 0.80, fill=PALEGREEN, line=GREEN, line_w=0.9,
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08)
_, tf = tb(s, HX + 0.12, fy + 1.82, HW - 0.24, 0.72)
para(tf, [("3 · OUTPUTS   ", True, GREEN),
          ("auto-generated daily indents per kitchen • forward procurement schedule & "
           "contract calendar • live waste dashboard • monthly savings report to donors "
           "(incl. GS)", False, TEXT)], size=7.4, first=True, space_after=0,
     line_spacing=1.0)

# right bottom: donut + savings side by side
DY = 4.74
cy = section(s, HX, DY, 2.75, "Where the $150k goes", accent=NAVY, size=10)
donut(s, HX - 0.05, cy - 0.04, 2.85, 1.48,
      ["Platform $60k", "Data infra $30k", "Team $25k", "ERP integr. $20k", "Conting. $15k"],
      [60, 30, 25, 20, 15], [NAVY, BLUE, MAGENTA, GOLD, GRAY],
      legend=XL_LEGEND_POSITION.BOTTOM, labels=False)
SX4 = 7.15
cy = section(s, SX4, DY, SW - ML - SX4, "Annual savings ($k)", accent=GREEN, size=10)
col_chart(s, SX4 - 0.05, cy, SW - ML - SX4 + 0.10, 1.28,
          ["Waste", "Buying", "Wkg cap"], [("$k/yr", [120, 85, 25])], [GREEN],
          gap=60, font_size=6.8)
_, tf = tb(s, SX4 - 0.05, cy + 1.32, SW - ML - SX4 + 0.10, 0.26)
para(tf, [("= $230k/yr → +105,000 children [dummy]", True, GREEN)], size=7,
     first=True, space_after=0, align=PP_ALIGN.CENTER)

# =====================================================================
# SLIDE 5
# =====================================================================
s = add_slide(prs)
chrome(s, 5, "Solution 2 — “Last-Mile Shield”: on time, intact, untouched",
       "$100k puts every van on an intelligent route and seals the last mile with "
       "telematics and geofenced locks — diversion becomes physically impossible.",
       takeaway="Every meal arrives on time, intact and untouched — by design, not by luck.")

# left: problem
cy = section(s, ML, 1.48, P4W, "The problem today", accent=RED)
_, tf = tb(s, ML, cy, P4W, 1.60)
para(tf, [("•  Missed lunch windows: ", True, TEXT),
          ("15–30 min late means children go hungry all day — non-negotiable",
           False, TEXT)], size=7.6, first=True, line_spacing=1.0)
para(tf, [("•  Static routes", True, TEXT),
          (" from driver memory — no live traffic, no lunch-bell sequencing", False, TEXT)],
     size=7.6, line_spacing=1.0)
para(tf, [("•  Untracked vessels", True, TEXT),
          (" leave daily with no tagging; losses recur", False, TEXT)], size=7.6,
     line_spacing=1.0)
para(tf, [("•  Open vans", True, TEXT),
          (" — meals can be offloaded / adulterated at dhabas en route", False, TEXT)],
     size=7.6, space_after=0, line_spacing=1.0)
qw = P4W / 2
stat(s, ML, cy + 1.42, qw, "6.2%", "deliveries miss the\nlunch window [dummy]", color=RED,
     vsize=13, csize=6.8)
stat(s, ML + qw, cy + 1.42, qw, "$35k/yr", "vessel & shrinkage\nlosses [dummy]", color=RED,
     vsize=13, csize=6.8)

# left: route map
cy = section(s, ML, 3.98, P4W, "Route redesign — 1 hub, 40 schools", accent=NAVY,
             size=10)
img_placeholder(s, ML, cy + 0.02, P4W, 1.35, "\U0001F5FA MAP: before vs after routes",
                "(insert optimised-route schematic; −18% km)")
_, tf = tb(s, ML, cy + 1.42, P4W, 0.40)
para(tf, [("3 vans freed per hub ", True, GREEN),
          ("→ redeployed to 12 new schools [dummy]", False, TEXT)], size=7,
     first=True, space_after=0, align=PP_ALIGN.CENTER)

# right: three layers
vline(s, 3.95, 1.55, 6.45)
HX, HW = 4.15, SW - ML - 4.15
cy = section(s, HX, 1.48, HW, "The fix — three integrated layers", accent=GREEN)
layers = [
    ("1 · ROUTE INTELLIGENCE", PALEBLUE, MIDBLUE,
     "AI planner sequences every drop to each school's lunch bell • live traffic "
     "re-routing • delay alerts to school + kitchen 30 min ahead"),
    ("2 · VEHICLE TELEMATICS", PALEGOLD, ORANGE,
     "GPS + in-van cameras on every vehicle • RFID tags on all vessels & utensils • "
     "automated end-of-day reconciliation — zero missing inventory"),
    ("3 · GEOFENCED INTEGRITY", PALEGREEN, GREEN,
     "Smart-locked doors open only within 150 m of a registered school • real-time "
     "tamper alerts • en-route offloading & adulteration made impossible"),
]
ly = cy + 0.04
for t, bg, bc, d in layers:
    rect(s, HX, ly, HW, 0.78, fill=bg, line=bc, line_w=0.9,
         shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.07)
    _, tf = tb(s, HX + 0.12, ly + 0.06, HW - 0.24, 0.68)
    para(tf, [(t, True, NAVY)], size=7.8, first=True, space_after=1)
    para(tf, d, size=7.2, color=TEXT, space_after=0, line_spacing=1.0)
    ly += 0.84

# right: SLA strip
_, tf = tb(s, HX, ly + 0.02, HW, 0.24)
para(tf, [("After implementation:  ", True, NAVY),
          ("99.5% in lunch window   ·   −18% fleet km   ·   0 unaccounted vessels",
           True, GREEN)], size=8.2, first=True, space_after=0)

# right bottom: donut + savings
DY = 4.74
cy = section(s, HX, DY, 2.75, "Where the $100k goes", accent=NAVY, size=10)
donut(s, HX - 0.05, cy - 0.04, 2.85, 1.48,
      ["Routing sw $35k", "Telematics $30k", "Smart locks $20k", "RFID $10k", "Ops $5k"],
      [35, 30, 20, 10, 5], [GREEN, TEAL, NAVY, GOLD, GRAY],
      legend=XL_LEGEND_POSITION.BOTTOM, labels=False)
SX4 = 7.15
cy = section(s, SX4, DY, SW - ML - SX4, "Annual savings ($k)", accent=GREEN, size=10)
col_chart(s, SX4 - 0.05, cy, SW - ML - SX4 + 0.10, 1.28,
          ["Fuel", "Vessels", "Food"], [("$k/yr", [45, 20, 15])], [GREEN],
          gap=60, font_size=6.8)
_, tf = tb(s, SX4 - 0.05, cy + 1.32, SW - ML - SX4 + 0.10, 0.26)
para(tf, [("= $80k/yr + trust that is priceless", True, GREEN)], size=7, first=True,
     space_after=0, align=PP_ALIGN.CENTER)

# =====================================================================
# SLIDE 6
# =====================================================================
s = add_slide(prs)
chrome(s, 6, "Conclusion — why Akshaya Patra, and why this proposal wins",
       "A proven engine of social mobility, a grant that compounds instead of depletes, "
       "and a partnership only Goldman Sachs can power.",
       takeaway="$250k that doesn't feed children for a year — it upgrades the engine "
                "that feeds them forever.")

LX6, LW6 = ML, 4.42
RX6, RW6 = 5.02, SW - ML - 5.02
vline(s, 4.77, 1.55, 6.45)

# L: testimonial
cy = section(s, LX6, 1.48, LW6, "Proven pathway out of poverty", accent=ORANGE)
img_placeholder(s, LX6, cy + 0.02, 0.95, 1.10, "\U0001F4F7\nKrishna\nKumar")
bub = rect(s, LX6 + 1.08, cy + 0.02, LW6 - 1.08, 1.10, fill=PALEGOLD, line=ORANGE,
           line_w=0.9, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.10)
_, tf = tb(s, LX6 + 1.20, cy + 0.09, LW6 - 1.30, 1.00)
para(tf, "“The mid-day meal was the reason I stayed in school. Today I manage portfolios "
         "instead of an empty stomach.”", size=7.4, color=TEXT, italic=True, first=True,
     space_after=2, line_spacing=1.0)
para(tf, [("— Krishna Kumar, ", True, NAVY),
          ("AVP, HSBC — former mid-day meal beneficiary", False, GRAY)], size=7,
     space_after=0)
_, tf = tb(s, LX6, cy + 1.24, LW6, 1.05)
para(tf, [("Beneficiary outcomes [dummy]:  ", True, NAVY),
          ("+18% enrolment & +12% attendance after programme entry  ·  ", False, TEXT),
          ("92% secondary completion", True, TEXT),
          (" vs 74% national avg  ·  alumni across banking, engineering, civil services "
           "& medicine", False, TEXT)], size=7.6, first=True, space_after=0,
     line_spacing=1.05)

# L: recognition
cy = section(s, LX6, 3.85, LW6, "Recognition & acknowledgements", accent=NAVY)
_, tf = tb(s, LX6, cy, LW6, 1.10)
para(tf, [("•  Padma Shri (2016)", True, TEXT), (" — Chairman Madhu Pandit Dasa",
          False, TEXT)], size=7.6, first=True, line_spacing=1.0)
para(tf, [("•  World's largest NGO school-lunch programme", True, TEXT),
          (" — global record", False, TEXT)], size=7.6, line_spacing=1.0)
para(tf, [("•  4-billionth meal", True, TEXT),
          (" milestone celebrated with Hon'ble PM of India", False, TEXT)], size=7.6,
     line_spacing=1.0)
para(tf, [("•  UK PM Rishi Sunak's kitchen visit", True, TEXT),
          (" — lauded hygiene & scale", False, TEXT)], size=7.6, space_after=0,
     line_spacing=1.0)

# L: partners
cy = section(s, LX6, 5.32, LW6, "Trusted by leading corporates", accent=TEAL)
pnames = ["Infosys", "TCS", "HDFC", "Amazon", "Airbus", "SBI"]
pw6 = (LW6 - 5 * 0.06) / 6
for i, p in enumerate(pnames):
    img_placeholder(s, LX6 + i * (pw6 + 0.06), cy + 0.02, pw6, 0.48, p)
_, tf = tb(s, LX6, cy + 0.56, LW6, 0.22)
para(tf, "+ 200 corporate & institutional donors [replace with logos]", size=6.5,
     color=GRAY, italic=True, first=True, space_after=0, align=PP_ALIGN.CENTER)

# R: equation
cy = section(s, RX6, 1.48, RW6, "The partnership equation", accent=MIDBLUE)
eq_y = cy + 0.10; ov = 1.06
ox1 = RX6 + 0.10
c1 = rect(s, ox1, eq_y, ov, 0.92, fill=PALEBLUE, line=NAVY, line_w=1.1,
          shape=MSO_SHAPE.OVAL)
_, tf = tb(s, ox1, eq_y + 0.12, ov, 0.68, anchor=MSO_ANCHOR.MIDDLE)
para(tf, "GS $250k\ncatalytic\ncapital", size=7, color=NAVY, bold=True,
     align=PP_ALIGN.CENTER, first=True, space_after=0, line_spacing=0.9)
rect(s, ox1 + ov + 0.12, eq_y + 0.33, 0.26, 0.26, fill=NAVY, line=None,
     shape=MSO_SHAPE.MATH_PLUS)
ox2 = ox1 + ov + 0.50
rect(s, ox2, eq_y, ov, 0.92, fill=PALEGOLD, line=ORANGE, line_w=1.1, shape=MSO_SHAPE.OVAL)
_, tf = tb(s, ox2, eq_y + 0.12, ov, 0.68, anchor=MSO_ANCHOR.MIDDLE)
para(tf, "AP's 2.3M\nmeals-a-day\nengine", size=7, color=ORANGE, bold=True,
     align=PP_ALIGN.CENTER, first=True, space_after=0, line_spacing=0.9)
rect(s, ox2 + ov + 0.12, eq_y + 0.33, 0.26, 0.26, fill=NAVY, line=None,
     shape=MSO_SHAPE.MATH_EQUAL)
ox3 = ox2 + ov + 0.50
rect(s, ox3, eq_y, ov, 0.92, fill=PALEGREEN, line=GREEN, line_w=1.1, shape=MSO_SHAPE.OVAL)
_, tf = tb(s, ox3, eq_y + 0.12, ov, 0.68, anchor=MSO_ANCHOR.MIDDLE)
para(tf, "Impact that\ncompounds\nyearly", size=7, color=GREEN, bold=True,
     align=PP_ALIGN.CENTER, first=True, space_after=0, line_spacing=0.9)
_, tf = tb(s, RX6, eq_y + 1.00, RW6, 0.42)
para(tf, "One-time capital → permanent capability → recurring savings → more children "
         "in school, every year after Year 1.", size=7.2, color=TEXT, first=True,
     space_after=0, align=PP_ALIGN.CENTER, line_spacing=1.0)

# R: why GS stands out
cy = section(s, RX6, 3.22, RW6, "Why the GS grant stands out here", accent=NAVY)
_, tf = tb(s, RX6, cy, RW6, 1.65)
para(tf, [("1 · Structural, not sustenance: ", True, NAVY),
          ("others fund meals for a year; GS funds the technology that makes every "
           "future meal cheaper.", False, TEXT)], size=7.5, first=True, line_spacing=1.0)
para(tf, [("2 · Plays to GS DNA: ", True, NAVY),
          ("forecasting, optimisation & risk controls — GS engineering can mentor the "
           "build pro bono.", False, TEXT)], size=7.5, line_spacing=1.0)
para(tf, [("3 · Measurable ROI: ", True, NAVY),
          ("$310k/yr audited savings; KPI dashboard shared quarterly with GS.",
           False, TEXT)], size=7.5, line_spacing=1.0)
para(tf, [("4 · Scalable blueprint: ", True, NAVY),
          ("proven once, extends to school-feeding programmes across South Asia & Africa.",
           False, TEXT)], size=7.5, space_after=0, line_spacing=1.0)

# R: ask & next steps
cy = section(s, RX6, 5.28, RW6, "The ask & next steps", accent=GREEN)
_, tf = tb(s, RX6, cy, RW6, 0.90)
para(tf, [("The ask: ", True, NAVY),
          ("$250,000 over 12 months in milestone-based tranches; joint GS–AP steering "
           "committee & quarterly KPI reviews.", False, TEXT)], size=7.5, first=True,
     line_spacing=1.0)
para(tf, [("Month 12: ", True, GREEN),
          ("both platforms live in all 68 kitchens — the savings flywheel spinning on "
           "its own.", True, TEXT)], size=7.5, space_after=0, line_spacing=1.0)

out = "AkshayaPatra_GS_Pitch.pptx"
prs.save(out)
print("saved:", out)
