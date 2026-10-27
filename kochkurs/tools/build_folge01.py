"""Generates the static scene files for Mias Kueche, Folge 1. Output is plain, editable HTML."""
import random, os

OUT = __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__)))
INK = "#3A2418"
SKIN = "#F2C29B"
HAIR = "#4A2C1D"
RED = "#E8553D"
SHIRT = "#F7C548"
BLUE = "#4D7CC2"


def mia(P, flour=False):
    """Mia, viewBox 0 0 400 560. Pivots: neck 200 265, shoulders 128/272 305, eyes 200 175."""
    return f"""
<g id="{P}-mia">
 <g id="{P}-body">
  <path d="M104 318 Q200 262 296 318 L330 560 L70 560 Z" fill="{SHIRT}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
  <path d="M138 340 L262 340 L290 560 L110 560 Z" fill="{RED}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
  <path d="M146 342 L166 292 M254 342 L234 292" stroke="{RED}" stroke-width="16" stroke-linecap="round"/>
  <rect x="168" y="400" width="64" height="46" rx="8" fill="#F27561" stroke="{INK}" stroke-width="5"/>
  <rect x="182" y="258" width="36" height="36" fill="{SKIN}" stroke="{INK}" stroke-width="6"/>
 </g>
 <g id="{P}-armL">
  <path d="M128 305 L98 400 L118 482" fill="none" stroke="{INK}" stroke-width="50" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M128 305 L98 400 L118 482" fill="none" stroke="{SKIN}" stroke-width="38" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="126" cy="318" r="32" fill="{SHIRT}" stroke="{INK}" stroke-width="6"/>
  <circle cx="118" cy="486" r="26" fill="{SKIN}" stroke="{INK}" stroke-width="6"/>
 </g>
 <g id="{P}-armR">
  <path d="M272 305 L302 400 L282 482" fill="none" stroke="{INK}" stroke-width="50" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M272 305 L302 400 L282 482" fill="none" stroke="{SKIN}" stroke-width="38" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="274" cy="318" r="32" fill="{SHIRT}" stroke="{INK}" stroke-width="6"/>
  <circle cx="282" cy="486" r="26" fill="{SKIN}" stroke="{INK}" stroke-width="6"/>
 </g>
 <g id="{P}-armRb" opacity="0">
  <path d="M272 305 L330 392 L250 262" fill="none" stroke="{INK}" stroke-width="50" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M272 305 L330 392 L250 262" fill="none" stroke="{SKIN}" stroke-width="38" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="274" cy="318" r="32" fill="{SHIRT}" stroke="{INK}" stroke-width="6"/>
  <path d="M244 262 L226 232 M226 232 L214 214 M226 232 L222 210 M226 232 L232 208 M226 232 L240 210" stroke="#9AA3AD" stroke-width="7" stroke-linecap="round"/>
  <path d="M206 206 Q222 192 244 204 L238 214 Q222 206 210 214 Z" fill="#E3A653" stroke="{INK}" stroke-width="4"/>
  <circle cx="250" cy="262" r="26" fill="{SKIN}" stroke="{INK}" stroke-width="6"/>
 </g>
 <g id="{P}-head">
  <circle cx="92" cy="118" r="50" fill="{HAIR}" stroke="{INK}" stroke-width="6"/>
  <circle cx="308" cy="118" r="50" fill="{HAIR}" stroke="{INK}" stroke-width="6"/>
  <circle cx="102" cy="182" r="20" fill="{SKIN}" stroke="{INK}" stroke-width="6"/>
  <circle cx="298" cy="182" r="20" fill="{SKIN}" stroke="{INK}" stroke-width="6"/>
  <circle cx="200" cy="172" r="100" fill="{SKIN}" stroke="{INK}" stroke-width="6"/>
  <path d="M100 160 Q104 66 200 64 Q296 66 300 160 Q284 118 246 116 Q226 92 196 112 Q170 96 150 118 Q118 120 100 160 Z" fill="{HAIR}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
  <path d="M116 112 Q200 40 284 112" fill="none" stroke="{RED}" stroke-width="16" stroke-linecap="round"/>
  <path d="M146 146 Q160 138 174 146 M226 146 Q240 138 254 146" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <g id="{P}-eyes">
   <ellipse cx="160" cy="176" rx="11" ry="15" fill="{INK}"/><circle cx="164" cy="170" r="4" fill="#fff"/>
   <ellipse cx="240" cy="176" rx="11" ry="15" fill="{INK}"/><circle cx="244" cy="170" r="4" fill="#fff"/>
  </g>
  <path id="{P}-eyesC" opacity="0" d="M147 180 Q160 166 173 180 M227 180 Q240 166 253 180" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cx="134" cy="210" r="17" fill="#F59E8B" opacity="0.75"/>
  <circle cx="266" cy="210" r="17" fill="#F59E8B" opacity="0.75"/>
  <g fill="#C98A62"><circle cx="128" cy="196" r="3"/><circle cx="140" cy="202" r="3"/><circle cx="272" cy="196" r="3"/><circle cx="260" cy="202" r="3"/></g>
  <path d="M194 196 Q200 204 206 196" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <path id="{P}-m-smile" d="M172 226 Q200 250 228 226" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <g id="{P}-m-open" opacity="0"><ellipse cx="200" cy="236" rx="20" ry="24" fill="#8C2F25" stroke="{INK}" stroke-width="5"/><ellipse cx="200" cy="250" rx="11" ry="7" fill="#E46F68"/></g>
  <g id="{P}-m-grin" opacity="0"><path d="M164 222 Q200 278 236 222 Z" fill="#8C2F25" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/><path d="M170 225 L230 225 L226 234 L174 234 Z" fill="#fff"/></g>
  <g id="{P}-m-chew" opacity="0"><ellipse cx="200" cy="232" rx="14" ry="8" fill="#8C2F25" stroke="{INK}" stroke-width="5"/></g>
  <g id="{P}-flour" opacity="{1 if flour else 0}" fill="#FFFFFF">
   <circle cx="200" cy="196" r="13"/><circle cx="212" cy="188" r="8"/><circle cx="148" cy="214" r="10"/><circle cx="160" cy="220" r="6"/>
   <circle cx="238" cy="126" r="9"/><circle cx="252" cy="132" r="6"/>
  </g>
 </g>
</g>"""


RIG_JS = """
    function rig(P) {
      const q = (s) => "#" + P + "-" + s;
      return {
        blink(t) {
          tl.to(q("eyes"), { scaleY: 0.1, svgOrigin: "200 176", duration: 0.06, ease: "power1.in" }, t);
          tl.to(q("eyes"), { scaleY: 1, svgOrigin: "200 176", duration: 0.09, ease: "power1.out" }, t + 0.06);
        },
        mouth(t, name) {
          ["smile", "open", "grin", "chew"].forEach((m) => tl.set(q("m-" + m), { opacity: m === name ? 1 : 0 }, t));
        },
        eyes(t, closed) {
          tl.set(q("eyes"), { opacity: closed ? 0 : 1 }, t);
          tl.set(q("eyesC"), { opacity: closed ? 1 : 0 }, t);
        },
        breathe(t0, t1) {
          const n = Math.max(1, Math.floor((t1 - t0) / 0.9));
          tl.fromTo(q("body"), { y: 0 }, { y: -4, duration: 0.9, ease: "sine.inOut", yoyo: true, repeat: n - 1 }, t0);
        },
        head(t, rot, d) {
          tl.to(q("head"), { rotation: rot, svgOrigin: "200 265", duration: d || 0.3, ease: "back.out(1.6)" }, t);
        },
        arm(t, side, rot, d, ease) {
          const o = side === "L" ? "128 305" : "272 305";
          tl.to(q("arm" + side), { rotation: rot, svgOrigin: o, duration: d || 0.35, ease: ease || "back.out(1.4)" }, t);
        },
      };
    }
"""

CSS_COMMON = """
    #root { position: absolute; inset: 0; overflow: hidden; font-family: "Nunito", sans-serif; color: #3A2418; }
    .wall { position: absolute; inset: 0; background-color: #BFE3D0;
      background-image: linear-gradient(#F4FBF7 4px, transparent 4px), linear-gradient(90deg, #F4FBF7 4px, transparent 4px);
      background-size: 120px 120px; background-position: -2px -2px; }
    .ctop { position: absolute; left: 0; right: 0; top: 780px; height: 66px; background: #E7A973;
      border-top: 6px solid #3A2418; border-bottom: 6px solid #3A2418; }
    .cfront { position: absolute; left: 0; right: 0; top: 846px; bottom: 0; background-color: #C98450;
      background-image: repeating-linear-gradient(0deg, transparent 0 38px, rgba(140, 82, 40, 0.35) 38px 41px); }
    .wood { position: absolute; inset: 0; background: #D9965F; }
    .title { position: absolute; font-weight: 900; letter-spacing: -0.01em; line-height: 1; }
    .w { display: inline-block; }
"""


def grain(seed, n=26):
    r = random.Random(seed)
    paths = []
    for i in range(n):
        y = 20 + i * 42 + r.uniform(-8, 8)
        d = f"M-20 {y:.0f}"
        x = -20
        while x < 1960:
            x2 = x + r.uniform(160, 320)
            d += f" Q{(x + x2) / 2:.0f} {y + r.uniform(-14, 14):.0f} {x2:.0f} {y:.0f}"
            x = x2
        w = r.choice([2, 3, 3, 4])
        paths.append(f'<path d="{d}" fill="none" stroke="#C07F4A" stroke-width="{w}" opacity="0.45"/>')
    # two knots
    paths.append('<ellipse cx="1650" cy="210" rx="34" ry="12" fill="none" stroke="#B3733F" stroke-width="3" opacity="0.5"/>')
    paths.append('<ellipse cx="260" cy="930" rx="28" ry="10" fill="none" stroke="#B3733F" stroke-width="3" opacity="0.5"/>')
    return f'<svg class="grain" width="1920" height="1080" viewBox="0 0 1920 1080" style="position:absolute;inset:0">{"".join(paths)}</svg>'


def scene(cid, css, body, js, vars_json=None):
    v = f" data-composition-variables='{vars_json}'" if vars_json else ""
    return f"""<template>
  <style>{CSS_COMMON}{css}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="1920" data-height="1080"{v}>
{body}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
{RIG_JS}{js}
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""


def words(prefix, text):
    return " ".join(f'<span class="w {prefix}-w">{w}</span>' for w in text.split(" "))


# ---------------------------------------------------------------- 1 intro
def intro():
    css = """
    #i-cam { position: absolute; inset: 0; transform-origin: 1390px 700px; }
    #i-window { position: absolute; left: 90px; top: 110px; width: 380px; height: 330px; background: #CDEBFA;
      border: 6px solid #3A2418; border-radius: 10px; box-shadow: inset 0 0 0 14px #FFFFFF; }
    #i-window::before { content: ""; position: absolute; left: 50%; top: 0; bottom: 0; width: 12px; margin-left: -6px; background: #FFFFFF; }
    #i-window::after { content: ""; position: absolute; top: 50%; left: 0; right: 0; height: 12px; margin-top: -6px; background: #FFFFFF; }
    #i-sill { position: absolute; left: 70px; top: 440px; width: 420px; height: 26px; background: #FFFFFF; border: 6px solid #3A2418; border-radius: 6px; }
    #i-plant { position: absolute; left: 380px; top: 340px; width: 90px; height: 104px; }
    #i-mia { position: absolute; left: 520px; top: 216px; width: 560px; height: 784px; }
    #i-book { position: absolute; left: 1200px; top: 326px; width: 380px; height: 480px; }
    #i-heute { left: 1110px; top: 112px; font-size: 64px; }
    #i-rezept { left: 1110px; top: 182px; font-size: 120px; color: #C23B26; }
"""
    body = f"""    <div class="wall"></div>
    <div id="i-cam">
      <div id="i-window"></div><div id="i-sill"></div>
      <svg id="i-plant" viewBox="0 0 90 104"><path d="M45 60 Q20 30 10 6 Q40 18 45 60 Q52 20 80 10 Q70 40 45 60" fill="#5FAF6E" stroke="#3A2418" stroke-width="5" stroke-linejoin="round"/><path d="M18 58 L72 58 L64 100 L26 100 Z" fill="#D9774B" stroke="#3A2418" stroke-width="5" stroke-linejoin="round"/></svg>
      <svg id="i-mia" viewBox="0 0 400 560">{mia("im")}</svg>
      <div class="ctop"></div><div class="cfront"></div>
      <svg id="i-book" viewBox="0 0 380 480">
        <rect x="6" y="6" width="350" height="468" rx="14" fill="#4D7CC2" stroke="#3A2418" stroke-width="6"/>
        <rect x="350" y="20" width="24" height="444" rx="6" fill="#FFF3DC" stroke="#3A2418" stroke-width="5"/>
        <rect x="6" y="6" width="36" height="468" rx="10" fill="#3A63A3" stroke="#3A2418" stroke-width="6"/>
        <rect x="74" y="60" width="250" height="84" rx="8" fill="#FFF3DC" stroke="#3A2418" stroke-width="5"/>
        <text x="199" y="117" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="44" fill="#3A2418">REZEPTE</text>
        <ellipse cx="199" cy="236" rx="96" ry="26" fill="#FFFFFF" stroke="#3A2418" stroke-width="5"/>
        <ellipse cx="199" cy="222" rx="74" ry="18" fill="#E8B15C" stroke="#3A2418" stroke-width="5"/>
        <ellipse cx="199" cy="206" rx="74" ry="18" fill="#E8B15C" stroke="#3A2418" stroke-width="5"/>
        <ellipse cx="199" cy="190" rx="74" ry="18" fill="#E8B15C" stroke="#3A2418" stroke-width="5"/>
      </svg>
      <div id="i-heute" class="title">{words("ih", "Heute:")}</div>
      <div id="i-rezept" class="title">{words("ir", "Pfannkuchen!")}</div>
    </div>"""
    js = """
    const m = rig("im");
    // the book drops onto the counter from Mia's raised hands
    tl.fromTo("#i-book", { y: -330, rotation: -8 }, { y: 0, rotation: 0, duration: 0.4, ease: "power3.in" }, 0);
    tl.fromTo("#i-book", { scaleY: 1 }, { scaleY: 0.94, transformOrigin: "50% 100%", duration: 0.06, yoyo: true, repeat: 1, ease: "power1.out" }, 0.4);
    tl.fromTo("#im-armR", { rotation: -120 }, { rotation: -40, svgOrigin: "272 305", duration: 0.42, ease: "power3.in" }, 0);
    tl.fromTo("#im-armL", { rotation: 30 }, { rotation: 10, svgOrigin: "128 305", duration: 0.5, ease: "power2.out" }, 0.05);
    m.mouth(0, "grin");
    // the take: she leans in to the camera, mouth open on the announcement
    tl.fromTo("#im-mia", { y: 0 }, { y: -18, duration: 0.5, ease: "back.out(1.8)" }, 0.55);
    m.head(0.55, -6, 0.4);
    m.mouth(0.9, "open");
    m.mouth(2.2, "grin");
    m.head(2.2, 4, 0.5);
    m.blink(1.6); m.blink(3.4); m.blink(4.9);
    m.mouth(3.3, "smile");
    m.arm(3.0, "L", 40, 0.4);
    m.arm(3.9, "L", 14, 0.5, "power2.inOut");
    m.breathe(0.6, 5.6);
    // title, word by word
    tl.fromTo(".ih-w", { opacity: 0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.14, ease: "power4.out" }, 1.0);
    tl.fromTo(".ir-w", { opacity: 0, filter: "blur(8px)", scale: 0.92 }, { opacity: 1, filter: "blur(0px)", scale: 1, duration: 0.3, ease: "expo.out" }, 1.3);
    tl.to(["#i-heute", "#i-rezept"], { opacity: 0, filter: "blur(8px)", duration: 0.2, ease: "power2.in", stagger: 0.06 }, 5.5);
    // push into the blue cover: it becomes the next frame
    tl.to("#i-cam", { scale: 6.4, duration: 1.1, ease: "power3.in" }, 5.9);
    m.head(5.9, 0, 0.3);
"""
    return scene("intro", css, body, js)


# ---------------------------------------------------------------- 2 zutaten
def hand_svg(rot):
    # a child's arm pointing up along -y, fingertips at the top; rotated to come in from an edge
    return f"""<svg class="z-hand" viewBox="0 0 160 760" style="transform: rotate({rot}deg)">
      <rect x="38" y="150" width="84" height="640" rx="40" fill="{SKIN}" stroke="{INK}" stroke-width="6"/>
      <rect x="28" y="430" width="104" height="360" rx="30" fill="{SHIRT}" stroke="{INK}" stroke-width="6"/>
      <ellipse cx="80" cy="110" rx="62" ry="70" fill="{SKIN}" stroke="{INK}" stroke-width="6"/>
      <path d="M40 70 L40 40 M64 58 L64 22 M90 58 L90 24 M114 70 L114 44" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
    </svg>"""


ITEMS = [
    # id, x, y (centre), w, h, label, label dx, dy, entry dir (dx,dy) offscreen, hand rotation
    ("mehl", 430, 330, 260, 320, "200 g Mehl", -40, 190, (-900, 0), 90),
    ("milch", 1490, 320, 340, 180, "300 ml Milch", -60, 130, (900, 0), -90),
    ("eier", 400, 790, 300, 170, "2 Eier", 0, 140, (-900, 0), 90),
    ("salz", 1520, 800, 260, 140, "1 Prise Salz", -60, -140, (900, 0), -90),
    ("zucker", 960, 150, 380, 120, "1 EL Zucker", 250, -20, (0, -700), 180),
    ("butter", 960, 950, 260, 140, "Butter zum Braten", 260, -30, (0, 700), 0),
]

ITEM_ART = {
    "mehl": f"""<svg viewBox="0 0 260 320"><path d="M30 60 L230 60 L238 310 L22 310 Z" fill="#F3E6CF" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
      <path d="M30 60 L50 14 L210 14 L230 60 Z" fill="#E6D3B0" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
      <rect x="54" y="120" width="152" height="70" rx="8" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>
      <text x="130" y="170" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="44" fill="{INK}">MEHL</text>
      <path d="M130 290 L130 214 M130 234 Q112 226 108 210 Q126 214 130 234 Q134 214 152 210 Q148 226 130 234 M130 256 Q112 248 108 232 Q126 236 130 256 Q134 236 152 232 Q148 248 130 256" fill="#E3A653" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/></svg>""",
    "milch": f"""<svg viewBox="0 0 340 180"><path d="M20 40 Q20 20 40 20 L220 20 Q240 20 250 50 L268 64 L300 64 L300 116 L268 116 L250 130 Q240 160 220 160 L40 160 Q20 160 20 140 Z" fill="#F7FBFF" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
      <rect x="296" y="56" width="34" height="68" rx="8" fill="{BLUE}" stroke="{INK}" stroke-width="6"/>
      <rect x="60" y="48" width="140" height="84" rx="10" fill="{BLUE}" stroke="{INK}" stroke-width="5"/>
      <text x="130" y="104" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="36" fill="#FFFFFF">MILCH</text></svg>""",
    "eier": f"""<svg viewBox="0 0 300 170"><ellipse cx="80" cy="90" rx="62" ry="74" transform="rotate(-18 80 90)" fill="#D9A066" stroke="{INK}" stroke-width="6"/>
      <ellipse cx="216" cy="86" rx="62" ry="74" transform="rotate(14 216 86)" fill="#E0AC74" stroke="{INK}" stroke-width="6"/>
      <ellipse cx="62" cy="62" rx="14" ry="20" fill="#F2CDA0"/><ellipse cx="200" cy="58" rx="14" ry="20" fill="#F5D6AE"/></svg>""",
    "salz": f"""<svg viewBox="0 0 260 140"><rect x="20" y="24" width="170" height="92" rx="20" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>
      <path d="M190 30 L232 38 Q244 70 232 102 L190 110 Z" fill="#B9C2CB" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
      <circle cx="214" cy="56" r="4" fill="{INK}"/><circle cx="220" cy="72" r="4" fill="{INK}"/><circle cx="214" cy="88" r="4" fill="{INK}"/>
      <text x="104" y="84" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="34" fill="{INK}">SALZ</text></svg>""",
    "zucker": f"""<svg viewBox="0 0 380 120"><rect x="16" y="50" width="220" height="24" rx="12" fill="#B9C2CB" stroke="{INK}" stroke-width="6"/>
      <ellipse cx="292" cy="62" rx="76" ry="50" fill="#B9C2CB" stroke="{INK}" stroke-width="6"/>
      <path d="M232 70 Q240 26 290 22 Q346 24 352 72 Q300 96 232 70 Z" fill="#FFFFFF" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
      <g fill="#E9E4DA"><circle cx="270" cy="50" r="5"/><circle cx="300" cy="40" r="5"/><circle cx="322" cy="58" r="5"/><circle cx="288" cy="66" r="5"/></g></svg>""",
    "butter": f"""<svg viewBox="0 0 260 140"><path d="M10 30 L250 20 L250 120 L10 130 Z" fill="#F0E2C2" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
      <rect x="40" y="34" width="160" height="80" rx="8" fill="#F8D66D" stroke="{INK}" stroke-width="6"/>
      <path d="M200 26 L250 20 L250 120 L200 126 Z" fill="#E3C98F" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/></svg>""",
}

BOWL = f"""<svg viewBox="0 0 560 560"><circle cx="280" cy="280" r="262" fill="#FAFAF7" stroke="{INK}" stroke-width="6"/>
  <circle cx="280" cy="280" r="246" fill="none" stroke="{BLUE}" stroke-width="12"/>
  <circle cx="280" cy="280" r="214" fill="#EFEDE6" stroke="{INK}" stroke-width="4"/>
  <path d="M120 170 Q170 100 260 86" fill="none" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round" opacity="0.9"/></svg>"""


def zutaten():
    css = """
    .z-place { position: absolute; }
    .z-item { position: absolute; left: 0; top: 0; width: 100%; height: 100%; }
    .z-item svg { width: 100%; height: 100%; display: block; overflow: visible; }
    .z-handwrap { position: absolute; left: 50%; top: 50%; width: 0; height: 0; }
    .z-hand { position: absolute; width: 160px; height: 760px; left: -80px; top: -40px; transform-origin: 80px 40px; overflow: visible; }
    .z-labelw { position: absolute; }
    .z-label { white-space: nowrap; font-weight: 800; font-size: 44px; padding: 10px 22px 12px;
      background: #FFF8EC; border: 5px solid #3A2418; border-radius: 6px; box-shadow: 0 8px 0 rgba(58, 36, 24, 0.18); }
    #z-bowl { position: absolute; left: 680px; top: 260px; width: 560px; height: 560px; }
    #z-cover { position: absolute; inset: 0; background: #4D7CC2; }
"""
    places = []
    for (iid, x, y, w, h, label, ldx, ldy, (ex, ey), hrot) in ITEMS:
        places.append(f"""    <div id="z-{iid}" class="z-place" style="left:{x - w // 2}px; top:{y - h // 2}px; width:{w}px; height:{h}px">
      <div id="z-{iid}-hand" class="z-handwrap">{hand_svg(hrot)}</div>
      <div id="z-{iid}-art" class="z-item">{ITEM_ART[iid]}</div>
    </div>
    <div id="z-{iid}-label" class="z-labelw" style="left:{x + ldx - 120}px; top:{y + ldy - 34}px"><div class="z-label" style="transform: rotate({-3 if ldx <= 0 else 2}deg)">{label}</div></div>""")
    body = f"""    <div class="wood"></div>
    {grain(7)}
{chr(10).join(places)}
    <div id="z-bowlplace" class="z-place" style="left:680px; top:260px; width:560px; height:560px">
      <div id="z-bowl-hand" class="z-handwrap">{hand_svg(0).replace('top: -40px', 'top: 220px')}</div>
      <div id="z-bowl-art" class="z-item">{BOWL}</div>
    </div>
    <div id="z-cover"></div>"""
    js = """
    // the blue cover lifts off like a page and reveals the counter
    tl.fromTo("#z-cover", { y: 0, rotation: 0 }, { y: -1200, rotation: -4, duration: 0.55, ease: "power3.in" }, 0.05);
    const items = """ + str([[i[0], i[8][0], i[8][1]] for i in ITEMS]) + """;
    items.forEach(([id, ex, ey], k) => {
      const t = 0.9 + k * 1.8;
      const hx = ex === 0 ? 0 : (ex < 0 ? -1 : 1), hy = ey === 0 ? 0 : (ey < 0 ? -1 : 1);
      tl.fromTo("#z-" + id, { x: ex, y: ey }, { x: 0, y: 0, duration: 0.55, ease: "expo.out" }, t);
      tl.fromTo("#z-" + id + "-art", { scale: 1 }, { scale: 1.05, duration: 0.08, yoyo: true, repeat: 1, ease: "power1.out" }, t + 0.5);
      tl.fromTo("#z-" + id + "-hand", { x: 0, y: 0 }, { x: hx * 1100, y: hy * 800, duration: 0.45, ease: "power3.in" }, t + 0.7);
      tl.fromTo("#z-" + id + "-label", { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(1.7)" }, t + 0.55);
    });
    // the bowl comes in last, into the middle
    tl.fromTo("#z-bowlplace", { y: 900 }, { y: 0, duration: 0.6, ease: "expo.out" }, 11.6);
    tl.fromTo("#z-bowl-hand", { y: 0 }, { y: 900, duration: 0.45, ease: "power3.in" }, 12.4);
"""
    return scene("zutaten", css, body, js)


# ---------------------------------------------------------------- 3 ruehren
def ruehren():
    r = random.Random(11)
    sugar = "".join(f'<circle cx="{280 + r.uniform(-70, 70):.0f}" cy="{280 + r.uniform(-60, 60):.0f}" r="5" fill="#FFFFFF" stroke="#D9D2C4" stroke-width="2"/>' for _ in range(18))
    lumps = "".join(f'<circle cx="{280 + r.uniform(-150, 150):.0f}" cy="{280 + r.uniform(-150, 150):.0f}" r="{r.uniform(8, 14):.0f}" fill="#E2C384"/>' for _ in range(16))
    puffs = "".join(f'<circle class="r-puff" cx="{960 + r.uniform(-260, 260):.0f}" cy="{540 + r.uniform(-200, 200):.0f}" r="{r.uniform(120, 220):.0f}" fill="#FFFFFF"/>' for _ in range(14))
    css = """
    #r-cam { position: absolute; inset: 0; }
    #r-over { position: absolute; inset: 0; }
    #r-bowl { position: absolute; left: 680px; top: 260px; width: 560px; height: 560px; overflow: visible; }
    #r-whisk { position: absolute; left: 680px; top: 260px; width: 560px; height: 560px; overflow: visible; }
    .r-step { position: absolute; left: 110px; top: 96px; font-size: 76px; }
    #r-step3 { left: 1250px; top: 96px; }
    #r-pour1 { position: absolute; left: 930px; top: -40px; width: 60px; height: 600px; background: #FFFFFF; border: 5px solid #3A2418; border-top: 0; border-radius: 0 0 30px 30px; transform-origin: 50% 0; }
    #r-pour2 { position: absolute; left: 1060px; top: -40px; width: 46px; height: 560px; background: #F7FBFF; border: 5px solid #3A2418; border-top: 0; border-radius: 0 0 24px 24px; transform-origin: 50% 0; }
    #r-puffs { position: absolute; inset: 0; }
    #r-close { position: absolute; inset: 0; opacity: 0; }
    #r-batter, #r-lumps, #r-egg1, #r-egg2, #r-sugar, .r-puff { opacity: 0; }
    #r-mia { position: absolute; left: 260px; top: -60px; width: 1400px; height: 1960px; }
"""
    body = f"""    <div id="r-cam">
      <div id="r-over">
        <div class="wood"></div>
        {grain(13)}
        <div id="r-pour1"></div><div id="r-pour2"></div>
        <svg id="r-bowl" viewBox="0 0 560 560">
          <circle cx="280" cy="280" r="262" fill="#FAFAF7" stroke="{INK}" stroke-width="6"/>
          <circle cx="280" cy="280" r="246" fill="none" stroke="{BLUE}" stroke-width="12"/>
          <circle cx="280" cy="280" r="214" fill="#EFEDE6" stroke="{INK}" stroke-width="4"/>
          <circle id="r-batter" cx="280" cy="280" r="206" fill="#F3D9A4"/>
          <g id="r-lumps">{lumps}</g>
          <ellipse id="r-flourmound" cx="280" cy="284" rx="104" ry="86" fill="#FFFFFF" stroke="#E2DED4" stroke-width="4"/>
          <g id="r-sugar">{sugar}</g>
          <g id="r-egg1"><path d="M150 250 Q160 196 214 204 Q250 230 230 280 Q190 300 150 250 Z" fill="#FFFDF5" stroke="#E6E0CF" stroke-width="3"/><circle cx="194" cy="246" r="26" fill="#F5A623" stroke="{INK}" stroke-width="4"/></g>
          <g id="r-egg2"><path d="M330 300 Q336 250 392 258 Q420 296 396 334 Q350 346 330 300 Z" fill="#FFFDF5" stroke="#E6E0CF" stroke-width="3"/><circle cx="372" cy="298" r="26" fill="#F5A623" stroke="{INK}" stroke-width="4"/></g>
          <path d="M120 170 Q170 100 260 86" fill="none" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round" opacity="0.9"/>
        </svg>
        <svg id="r-whisk" viewBox="0 0 560 560">
          <g id="r-whiskg">
            <rect x="340" y="250" width="320" height="40" rx="20" fill="#C9884F" stroke="{INK}" stroke-width="6"/>
            <path d="M340 270 Q260 170 170 230 Q150 270 170 310 Q260 370 340 270 M340 270 Q250 200 190 250 Q180 270 190 290 Q250 340 340 270 M340 270 L180 270" fill="none" stroke="#9AA3AD" stroke-width="8" stroke-linecap="round"/>
          </g>
        </svg>
        <div id="r-step1" class="title r-step" data-layout-allow-overlap>{words("r1", "Mehl, Zucker, Salz")}</div>
        <div id="r-step2" class="title r-step" data-layout-allow-overlap>{words("r2", "2 Eier rein")}</div>
        <div id="r-step3" class="title r-step" data-layout-allow-overlap>{words("r3", "Milch dazu –")}<br>{words("r3", "rühren!")}</div>
      </div>
      <div id="r-close">
        <div class="wall"></div>
        <svg id="r-mia" viewBox="0 0 400 560">{mia("rm", flour=True)}</svg>
      </div>
      <svg id="r-puffs" viewBox="0 0 1920 1080">{puffs}</svg>
    </div>"""
    js = """
    const m = rig("rm");
    // flour pours in, the mound grows
    tl.fromTo("#r-step1 .r1-w", { opacity: 0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.14, stagger: 0.08, ease: "power4.out" }, 0.3);
    tl.fromTo("#r-pour1", { scaleY: 0 }, { scaleY: 1, duration: 0.35, ease: "power2.in" }, 0.4);
    tl.fromTo("#r-flourmound", { attr: { rx: 8, ry: 6 } }, { attr: { rx: 104, ry: 86 }, duration: 1.4, ease: "power2.out" }, 0.7);
    tl.to("#r-pour1", { scaleY: 0, transformOrigin: "50% 100%", duration: 0.3, ease: "power2.in" }, 2.0);
    tl.fromTo("#r-sugar", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 2.2);
    tl.to("#r-step1", { opacity: 0, filter: "blur(8px)", duration: 0.18, ease: "power2.in" }, 3.0);
    // two eggs drop in
    tl.fromTo("#r-step2 .r2-w", { opacity: 0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.14, stagger: 0.08, ease: "power4.out" }, 3.2);
    tl.fromTo("#r-egg1", { opacity: 0, scale: 1.6 }, { opacity: 1, scale: 1, svgOrigin: "194 246", duration: 0.25, ease: "back.out(2)" }, 3.4);
    tl.fromTo("#r-egg2", { opacity: 0, scale: 1.6 }, { opacity: 1, scale: 1, svgOrigin: "372 298", duration: 0.25, ease: "back.out(2)" }, 3.8);
    tl.to("#r-step2", { opacity: 0, filter: "blur(8px)", duration: 0.18, ease: "power2.in" }, 5.5);
    // milk and whisking: the batter turns smooth
    tl.fromTo("#r-step3 .r3-w", { opacity: 0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.14, stagger: 0.08, ease: "power4.out" }, 5.7);
    tl.fromTo("#r-pour2", { scaleY: 0 }, { scaleY: 1, duration: 0.3, ease: "power2.in" }, 5.8);
    tl.to("#r-pour2", { scaleY: 0, transformOrigin: "50% 100%", duration: 0.3, ease: "power2.in" }, 6.8);
    tl.fromTo("#r-batter", { opacity: 0, attr: { r: 80 } }, { opacity: 1, attr: { r: 206 }, duration: 1.2, ease: "power2.out" }, 6.0);
    tl.fromTo("#r-lumps", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 6.3);
    tl.to(["#r-flourmound", "#r-sugar", "#r-egg1", "#r-egg2"], { opacity: 0, duration: 0.9, ease: "power1.inOut" }, 6.4);
    tl.fromTo("#r-whisk", { opacity: 0, x: 300 }, { opacity: 1, x: 0, duration: 0.4, ease: "expo.out" }, 6.2);
    tl.fromTo("#r-whiskg", { rotation: 0 }, { rotation: 900, svgOrigin: "280 280", duration: 2.4, ease: "none" }, 6.5);
    tl.to("#r-lumps", { opacity: 0, duration: 1.4, ease: "power1.in" }, 7.2);
    tl.to("#r-step3", { opacity: 0, filter: "blur(8px)", duration: 0.18, ease: "power2.in" }, 8.4);
    // the flour cloud
    tl.fromTo(".r-puff", { opacity: 1, scale: 0, transformOrigin: "50% 50%" }, { opacity: 1, scale: 1.6, duration: 0.45, stagger: 0.015, ease: "expo.out" }, 8.6);
    tl.set("#r-over", { opacity: 0 }, 9.05);
    tl.set("#r-close", { opacity: 1 }, 9.05);
    tl.to(".r-puff", { opacity: 0, scale: 2.4, duration: 0.8, stagger: 0.02, ease: "power2.out" }, 9.1);
    // close-up: flour on her nose, she laughs
    m.mouth(9.05, "grin"); m.eyes(9.05, true);
    tl.fromTo("#rm-head", { rotation: -3 }, { rotation: 3, svgOrigin: "200 265", duration: 0.22, yoyo: true, repeat: 5, ease: "sine.inOut" }, 9.2);
    m.eyes(10.6, false); m.blink(11.0);
    // whip left to the stove
    tl.to("#r-cam", { x: -1900, filter: "blur(14px)", duration: 0.4, ease: "power3.in" }, 11.6);
"""
    return scene("ruehren", css, body, js)


# ---------------------------------------------------------------- 4 braten
def braten():
    r = random.Random(23)
    bubbles = "".join(f'<circle class="b-bub" cx="{900 + r.uniform(-150, 150):.0f}" cy="{688 + r.uniform(-34, 34):.0f}" r="{r.uniform(5, 9):.0f}" fill="none" stroke="#B67A35" stroke-width="3"/>' for _ in range(14))
    spots = "".join(f'<ellipse cx="{900 + r.uniform(-140, 140):.0f}" cy="{688 + r.uniform(-30, 30):.0f}" rx="{r.uniform(12, 24):.0f}" ry="{r.uniform(5, 9):.0f}" fill="#B9762F" opacity="0.7"/>' for _ in range(9))
    css = """
    #b-cam { position: absolute; inset: 0; }
    .b-bub { opacity: 0; }
    #b-set { position: absolute; inset: 0; }
    #b-mia { position: absolute; left: 1260px; top: 216px; width: 560px; height: 784px; }
    #b-safe { left: 120px; top: 120px; font-size: 60px; }
    #b-wenden { left: 120px; top: 120px; font-size: 96px; }
"""
    body = f"""    <div id="b-cam">
      <div class="wall"></div>
      <svg id="b-mia" viewBox="0 0 400 560">{mia("bm")}</svg>
      <div class="ctop"></div><div class="cfront"></div>
      <svg id="b-set" viewBox="0 0 1920 1080">
        <rect x="560" y="786" width="700" height="54" rx="6" fill="#3B3734" stroke="{INK}" stroke-width="6"/>
        <g fill="#F2B544" stroke="{INK}" stroke-width="4"><path d="M780 786 l14 -26 l14 26 Z"/><path d="M880 786 l14 -30 l14 30 Z"/><path d="M980 786 l14 -26 l14 26 Z"/></g>
        <g fill="#FFFFFF" stroke="{INK}" stroke-width="5"><circle cx="680" cy="920" r="34"/><circle cx="1140" cy="920" r="34"/></g>
        <g id="b-pan">
          <path d="M650 690 L700 760 Q900 800 1100 760 L1150 690 Z" fill="#3B3B3B" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
          <ellipse cx="900" cy="690" rx="250" ry="70" fill="#4A4A4A" stroke="{INK}" stroke-width="6"/>
          <ellipse cx="900" cy="692" rx="222" ry="56" fill="#2C2C2C"/>
          <rect x="360" y="676" width="300" height="34" rx="17" fill="#B67A45" stroke="{INK}" stroke-width="6"/>
          <g id="b-cake">
            <ellipse id="b-cakeA" cx="900" cy="688" rx="196" ry="50" fill="#F3D9A4" stroke="{INK}" stroke-width="5"/>
            <g id="b-bubs">{bubbles}</g>
            <g id="b-cakeB" opacity="0"><ellipse cx="900" cy="688" rx="196" ry="50" fill="#D99A45" stroke="{INK}" stroke-width="5"/>{spots}</g>
          </g>
          <path id="b-batterpour" d="M884 0 L916 0 L916 688 L884 688 Z" fill="#F3D9A4" stroke="{INK}" stroke-width="5"/>
        </g>
        <g id="b-papa">
          <rect x="-120" y="640" width="520" height="120" rx="56" fill="{BLUE}" stroke="{INK}" stroke-width="6"/>
          <rect x="360" y="652" width="70" height="96" rx="18" fill="#3A63A3" stroke="{INK}" stroke-width="6"/>
          <path d="M420 650 Q500 640 540 668 Q560 694 530 718 Q490 740 420 736 Z" fill="#E8B48F" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
          <path d="M470 706 Q500 716 528 706 M466 684 Q500 690 534 684" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
        </g>
      </svg>
      <div id="b-safe" class="title">{words("bs", "Am Herd hilft immer ein Großer")}</div>
      <div id="b-wenden" class="title">{words("bw", "Blasen? Jetzt wenden!")}</div>
    </div>"""
    js = """
    const m = rig("bm");
    // arriving from the whip
    tl.fromTo("#b-cam", { x: 1900, filter: "blur(14px)" }, { x: 0, filter: "blur(0px)", duration: 0.45, ease: "expo.out" }, 0);
    tl.fromTo(".bs-w", { opacity: 0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.14, stagger: 0.07, ease: "power4.out" }, 0.6);
    tl.to("#b-safe", { opacity: 0, filter: "blur(8px)", duration: 0.2, ease: "power2.in" }, 4.4);
    // Mia points at the pan
    m.arm(0.7, "L", 80, 0.4);
    m.head(0.7, -8, 0.4);
    m.mouth(0.7, "open");
    m.mouth(1.6, "smile");
    m.blink(2.4); m.blink(5.2);
    m.arm(4.0, "L", 20, 0.5, "power2.inOut");
    m.breathe(1.0, 7.4);
    // batter pours, the pancake spreads, bubbles rise
    tl.fromTo("#b-batterpour", { attr: { d: "M884 0 L916 0 L916 0 L884 0 Z" } }, { attr: { d: "M884 0 L916 0 L916 688 L884 688 Z" }, duration: 0.4, ease: "power2.in" }, 1.0);
    tl.fromTo("#b-cakeA", { attr: { rx: 10, ry: 4 } }, { attr: { rx: 196, ry: 50 }, duration: 1.6, ease: "power2.out" }, 1.3);
    tl.to("#b-batterpour", { attr: { d: "M884 688 L916 688 L916 688 L884 688 Z" }, duration: 0.3, ease: "power2.in" }, 2.6);
    tl.to(".b-bub", { opacity: 1, duration: 0.2, stagger: 0.18 }, 3.2);
    tl.to("#b-cakeA", { fill: "#EDC57E", duration: 3.0, ease: "none" }, 3.0);
    tl.fromTo(".bw-w", { opacity: 0, filter: "blur(6px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.14, stagger: 0.08, ease: "power4.out" }, 5.6);
    m.head(5.6, 6, 0.3);
    tl.to("#b-wenden", { opacity: 0, filter: "blur(8px)", duration: 0.2, ease: "power2.in" }, 7.3);
    // the flip: Papa tips the pan, the pancake flies, turns and lands golden side up
    tl.to(["#b-pan", "#b-papa"], { rotation: -5, svgOrigin: "480 694", duration: 0.15, ease: "power2.in" }, 7.4);
    tl.to(["#b-pan", "#b-papa"], { rotation: 0, svgOrigin: "480 694", duration: 0.3, ease: "power2.out" }, 7.55);
    tl.to("#b-cake", { y: -430, duration: 0.45, ease: "power2.out" }, 7.5);
    tl.to("#b-cake", { y: 0, duration: 0.4, ease: "power2.in" }, 7.95);
    tl.fromTo("#b-cake", { scaleY: 1, rotation: 0 }, { scaleY: 0.04, rotation: 8, svgOrigin: "900 688", duration: 0.42, ease: "power1.in" }, 7.5);
    tl.set(["#b-cakeA", "#b-bubs"], { opacity: 0 }, 7.92);
    tl.set("#b-cakeB", { opacity: 1 }, 7.92);
    tl.to("#b-cake", { scaleY: 1, rotation: 0, svgOrigin: "900 688", duration: 0.43, ease: "power1.out" }, 7.92);
    tl.to("#b-cake", { scaleY: 0.85, svgOrigin: "900 688", duration: 0.08, ease: "power2.out", yoyo: true, repeat: 1 }, 8.35);
    // Mia cheers
    m.mouth(8.4, "grin"); m.eyes(8.4, true);
    m.arm(8.4, "L", 155, 0.35); m.arm(8.48, "R", -150, 0.35);
    tl.fromTo("#bm-mia", { y: 0 }, { y: -40, duration: 0.25, ease: "power2.out", yoyo: true, repeat: 3 }, 8.4);
    m.eyes(10.0, false);
    m.arm(10.4, "L", 20, 0.5, "power2.inOut"); m.arm(10.5, "R", 0, 0.5, "power2.inOut");
    m.mouth(10.4, "smile"); m.blink(11.0);
    // the pancake slides off towards the plate
    tl.to("#b-cake", { x: 2100, y: -260, duration: 0.6, ease: "power3.in" }, 12.2);
"""
    return scene("braten", css, body, js)


# ---------------------------------------------------------------- 5 probieren
def probieren():
    cakes = "".join(f'<ellipse cx="300" cy="{170 - i * 30}" rx="230" ry="50" fill="{c}" stroke="{INK}" stroke-width="5"/>'
                    for i, c in enumerate(["#D99A45", "#DDA24F", "#D99A45", "#E0A957"]))
    css = """
    #p-mia { position: absolute; left: 582px; top: 30px; width: 756px; height: 1058px; }
    #p-plate { position: absolute; left: 660px; top: 620px; width: 600px; height: 300px; overflow: visible; }
    #p-mmh { left: 1370px; top: 250px; font-size: 150px; }
    #p-flood { position: absolute; inset: 0; background: #E8553D; clip-path: circle(0% at 960px 760px); }
"""
    body = f"""    <div class="wall"></div>
    <svg id="p-mia" viewBox="0 0 400 560">{mia("pm")}</svg>
    <div class="ctop"></div><div class="cfront"></div>
    <svg id="p-plate" viewBox="0 0 600 300">
      <ellipse cx="300" cy="226" rx="296" ry="64" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>
      <ellipse cx="300" cy="222" rx="236" ry="44" fill="#F1EFEA"/>
      {cakes}
      <g id="p-top"><ellipse cx="300" cy="50" rx="230" ry="50" fill="#D99A45" stroke="{INK}" stroke-width="5"/>
        <path d="M150 40 Q220 10 300 20 Q390 14 440 46 Q420 70 400 64 L398 110 Q390 118 384 108 L382 66 Q300 80 250 70 L246 96 Q240 104 234 96 L232 66 Q180 62 150 40 Z" fill="#9A5A1E" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>
        <rect x="268" y="16" width="64" height="30" rx="6" fill="#F8D66D" stroke="{INK}" stroke-width="5"/></g>
    </svg>
    <div id="p-mmh" class="title">{words("pw", "Mmmh!")}</div>
    <div id="p-flood"></div>"""
    js = """
    const m = rig("pm");
    // the pancake from the pan lands on top of the stack
    tl.fromTo("#p-top", { x: -1300, y: -500 }, { x: 0, y: 0, duration: 0.35, ease: "power2.out" }, 0);
    tl.fromTo("#p-plate", { scaleY: 1 }, { scaleY: 0.95, transformOrigin: "50% 100%", duration: 0.07, yoyo: true, repeat: 1 }, 0.35);
    m.mouth(0, "open");
    m.head(0.3, -5, 0.3);
    m.mouth(0.8, "smile");
    m.blink(1.0);
    m.breathe(0.4, 7.0);
    // a bite: the arm comes up with the fork
    tl.set("#pm-armR", { opacity: 0 }, 1.5);
    tl.set("#pm-armRb", { opacity: 1 }, 1.5);
    tl.fromTo("#pm-armRb", { rotation: 40 }, { rotation: 0, svgOrigin: "272 305", duration: 0.4, ease: "back.out(1.5)" }, 1.5);
    m.mouth(1.6, "open");
    m.head(1.6, 4, 0.3);
    m.mouth(1.95, "chew");
    m.eyes(2.0, true);
    tl.set("#pm-armRb", { opacity: 0 }, 2.2);
    tl.set("#pm-armR", { opacity: 1 }, 2.2);
    for (let i = 0; i < 8; i++) m.mouth(2.2 + i * 0.22, i % 2 ? "chew" : "smile");
    tl.fromTo("#pm-head", { y: 0 }, { y: 6, duration: 0.22, yoyo: true, repeat: 7, ease: "sine.inOut" }, 2.2);
    // "Mmmh!" lands, she beams
    m.mouth(4.1, "grin");
    m.head(4.1, -7, 0.35);
    tl.fromTo("#p-mmh", { opacity: 0, scale: 0.7, filter: "blur(8px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.35, ease: "back.out(1.8)" }, 4.2);
    m.arm(4.3, "L", 40, 0.35);
    m.eyes(5.6, false); m.blink(6.2);
    tl.to("#p-mmh", { opacity: 0, filter: "blur(8px)", duration: 0.2, ease: "power2.in" }, 6.9);
    // red flood from the apron into the end card
    tl.to("#p-flood", { clipPath: "circle(120% at 960px 760px)", duration: 0.8, ease: "power2.inOut" }, 7.2);
"""
    return scene("probieren", css, body, js)


# ---------------------------------------------------------------- 6 ende
def ende():
    css = """
    #e-ground { position: absolute; inset: 0; background: #E8553D; }
    #e-mia { position: absolute; left: 150px; top: 260px; width: 600px; height: 840px; }
    #e-name { left: 820px; top: 330px; font-size: 156px; color: #FFF8EC; }
    #e-name span { display: inline-block; }
    #e-next { left: 828px; top: 540px; font-size: 64px; color: #FFF8EC; font-weight: 800; }
    #e-next b { font-weight: 900; color: #3A2418; }
"""
    letters = "".join(f'<span class="e-l">{c if c != " " else "&nbsp;"}</span>' for c in "Mias Küche")
    body = f"""    <div id="e-ground"></div>
    <svg id="e-mia" viewBox="0 0 400 560">{mia("em")}</svg>
    <div id="e-name" class="title">{letters}</div>
    <div id="e-next" class="title">Morgen: <b data-var-text="morgen">Pizza-Schnecken</b></div>"""
    js = """
    const m = rig("em");
    tl.fromTo("#e-mia", { y: 420 }, { y: 0, duration: 0.6, ease: "expo.out" }, 0);
    m.mouth(0, "grin");
    tl.fromTo(".e-l", { opacity: 0.25, filter: "blur(6px)", y: 0 }, { opacity: 1, filter: "blur(0px)", duration: 0.14, stagger: 0.07, ease: "power4.out" }, 0.25);
    tl.fromTo("#e-next", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.2, ease: "power4.out" }, 1.6);
    // she waves
    m.arm(0.5, "R", -150, 0.4);
    tl.to("#em-armR", { rotation: -125, svgOrigin: "272 305", duration: 0.25, yoyo: true, repeat: 5, ease: "sine.inOut" }, 0.9);
    m.head(0.9, 6, 0.4);
    m.mouth(1.6, "open");
    m.mouth(2.3, "grin");
    m.blink(2.8);
    m.arm(2.6, "R", 0, 0.6, "power2.inOut");
    m.head(2.6, 0, 0.5);
    m.breathe(1.0, 5.8);
    m.blink(4.6);
"""
    vars_json = '[{"id":"morgen","type":"string","label":"Morgen","default":"Pizza-Schnecken"}]'
    return scene("ende", css, body, js, vars_json)


SCENES = [("intro", 0, 7, intro), ("zutaten", 7, 14, zutaten), ("ruehren", 21, 12, ruehren),
          ("braten", 33, 13, braten), ("probieren", 46, 8, probieren), ("ende", 54, 6, ende)]

# sound: picture time, file, volume. Start = picture - peak + 1 frame.
PEAK = {"buch-knall": 0.073, "whoosh": 0.162, "whoosh-kurz": 0.162, "pop": 0.12, "glitzer": 0.027, "chime": 0.418}
DUR = {"buch-knall": 2.116, "whoosh": 0.575, "whoosh-kurz": 0.575, "pop": 0.72, "glitzer": 1.802, "chime": 2.544}
CUES = [
    ("knall", 0.4, "buch-knall", 0.45),
    ("rein", 6.9, "whoosh", 0.5),
    ("pop1", 8.45, "pop", 0.55), ("pop2", 10.25, "pop", 0.45), ("pop3", 12.05, "pop", 0.6),
    ("pop4", 13.85, "pop", 0.45), ("pop5", 15.65, "pop", 0.55), ("pop6", 17.45, "pop", 0.45),
    ("schuessel", 19.15, "pop", 0.65),
    ("ei1", 24.6, "pop", 0.5), ("ei2", 25.0, "pop", 0.4),
    ("mehlwolke", 29.75, "whoosh", 0.45),
    ("wisch", 32.85, "whoosh-kurz", 0.5),
    ("flip", 40.6, "whoosh-kurz", 0.55), ("landung", 41.36, "pop", 0.6),
    ("stapel", 46.36, "pop", 0.5),
    ("mmh", 50.22, "glitzer", 0.5),
    ("flut", 53.7, "whoosh", 0.35),
    ("morgen", 55.6, "chime", 0.5),
]


def index():
    hosts = "\n".join(f"""      <div id="{cid}" class="clip" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html"
        data-start="{s}" data-duration="{d}" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>"""
                      for cid, s, d, _ in SCENES)
    audio = "\n".join(f"""      <audio id="sfx-{n}" class="clip" src="assets/sfx/{f}.mp3" data-start="{max(0, t - PEAK[f] + 0.033):.3f}" data-duration="{DUR[f]}" data-track-index="{2 + k % 2}" data-volume="{v}"></audio>"""
                      for k, (n, t, f, v) in enumerate(CUES))
    return f"""<!doctype html>
<html lang="de">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>Mias Küche – Folge 1: Pfannkuchen</title>
    <script src="assets/lib/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: #BFE3D0; }}
      #root {{ position: relative; width: 100%; height: 100%; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="60" data-width="1920" data-height="1080">
{hosts}
{audio}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""


os.makedirs(f"{OUT}/compositions", exist_ok=True)
for cid, _, _, fn in SCENES:
    open(f"{OUT}/compositions/{cid}.html", "w").write(fn())
open(f"{OUT}/index.html", "w").write(index())
print("ok")
