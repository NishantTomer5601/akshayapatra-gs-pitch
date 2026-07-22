# Akshaya Patra × Goldman Sachs — Grant Pitch Deck (slides-as-code)

A 6-slide, 4:3 PowerPoint pitch proposing a $250k Goldman Sachs grant to
[The Akshaya Patra Foundation](https://www.akshayapatra.org/), generated
entirely from Python via [`python-pptx`](https://python-pptx.readthedocs.io/).

- `deck_lib.py` — shared design system (GS-style palette, typography, chrome,
  section headers, charts, arrows, placeholders)
- `build_deck.py` — the six slides; running it produces `AkshayaPatra_GS_Pitch.pptx`
- `AkshayaPatra_GS_Pitch.pptx` — pre-built copy of the deck (so you can grab the
  file without running anything)
- `preview/` — PNG renders of each slide

## Rebuild the deck

```bash
python3 -m venv venv && source venv/bin/activate   # optional but recommended
pip install -r requirements.txt
python build_deck.py                                # -> AkshayaPatra_GS_Pitch.pptx
```

Works on any machine with Python 3.9+; no PowerPoint installation required.

## Editing content

All slide text lives as plain strings in `build_deck.py` (slides are separated by
banner comments). Edit the strings, re-run the script, and the .pptx regenerates
with the design intact. Figures marked `[dummy]` are placeholders to replace with
verified numbers. Dashed grey boxes in the deck are image placeholders (logo,
photos, SDG tiles, partner logos).

Charts are native PowerPoint charts — their data can also be edited directly in
PowerPoint (right-click → Edit Data).

## Slide map

| # | Slide | Highlights |
|---|-------|-----------|
| 1 | Who is Akshaya Patra | hero band, journey line chart, scale stats, SDGs |
| 2 | Supply chain & the two gaps | chevron flow, validation callouts, GAP boxes |
| 3 | The $250k proposal | allocation bar, two solutions, savings flywheel |
| 4 | Solution 1 — demand forecasting | signals→indents flow, budget donut, savings |
| 5 | Solution 2 — smart distribution | three-layer fix, SLA stats, budget donut |
| 6 | Conclusion | testimonial, partnership equation, partners, the ask |
