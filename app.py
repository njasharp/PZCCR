import streamlit as st
import random
import time

st.set_page_config(
    page_title="Puzzoo — CCR Platform™",
    page_icon="🎰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Styling ----------
st.markdown("""
<style>
:root {
  --bg:#07060f; --bg2:#0c0a1a; --panel:#100e22; --line:rgba(255,255,255,.08);
  --txt:#eef0ff; --mut:#9aa0c3; --cyan:#22d3ee; --violet:#a855f7;
  --pink:#ec4899; --gold:#fbbf24;
}
.stApp {
  background:
    radial-gradient(700px 420px at 82% 8%,rgba(168,85,247,.18),transparent 60%),
    radial-gradient(620px 400px at 8% 78%,rgba(34,211,238,.10),transparent 60%),
    #07060f;
  color:var(--txt);
}
.block-container {max-width:1180px;padding-top:2rem;padding-bottom:4rem}
h1,h2,h3 {letter-spacing:-.025em}
.hero {
  padding:5.5rem 0 3rem;
}
.eyebrow {
  color:#22d3ee;text-transform:uppercase;letter-spacing:.2em;
  font-size:.78rem;font-weight:800;margin-bottom:1rem
}
.grad {
  background:linear-gradient(90deg,#22d3ee,#a855f7 55%,#ec4899);
  -webkit-background-clip:text;background-clip:text;color:transparent
}
.lead {color:#9aa0c3;font-size:1.05rem;line-height:1.7}
.chip {
  display:inline-block;padding:.4rem .8rem;margin:.25rem;border-radius:999px;
  border:1px solid rgba(255,255,255,.1);background:rgba(255,255,255,.035);
  color:#cfd3f0;font-size:.82rem;font-weight:650
}
.chip-gold {color:#fbbf24;border-color:rgba(251,191,36,.4)}
.card {
  background:linear-gradient(160deg,#151129,#0a0817);
  border:1px solid rgba(168,85,247,.28);border-radius:20px;
  padding:1.6rem; margin:.6rem 0;
}
.metric-card {
  background:rgba(255,255,255,.025);border:1px solid var(--line);
  border-radius:16px;padding:1.1rem;text-align:center
}
.metric-number {
  font-size:2.4rem;font-weight:900;
  background:linear-gradient(90deg,#22d3ee,#a855f7,#ec4899);
  -webkit-background-clip:text;background-clip:text;color:transparent
}
.metric-label {color:#9aa0c3;font-size:.85rem}
.module {
  min-height:210px;background:#100e22;border:1px solid rgba(255,255,255,.08);
  border-radius:18px;padding:1.5rem
}
.module-num {color:#22d3ee;font-weight:900;font-size:.82rem;letter-spacing:.1em}
.module h3 {margin:.45rem 0 .25rem}
.module p {color:#9aa0c3;font-style:italic}
.module li {color:#c6cade;margin:.4rem 0}
.slot {
  background:linear-gradient(160deg,#16122e,#0a0819);
  border:1px solid rgba(168,85,247,.45);border-radius:22px;padding:1.1rem;
  box-shadow:0 25px 65px rgba(0,0,0,.5)
}
.reel {
  background:linear-gradient(180deg,#1b1638,#0d0b1e);
  border:1px solid rgba(255,255,255,.08);border-radius:10px;
  text-align:center;padding:1.1rem .3rem;font-size:2rem
}
.nda {
  border:1px dashed rgba(251,191,36,.45);border-radius:14px;padding:1rem 1.2rem;
  background:rgba(251,191,36,.05);color:#e8d9a8;margin-top:1.3rem
}
.footer {border-top:1px solid var(--line);padding:2rem 0;color:#9aa0c3}
div[data-testid="stButton"] > button {
  border-radius:999px;border:1px solid rgba(255,255,255,.12);
  background:linear-gradient(90deg,#22d3ee,#a855f7 55%,#ec4899);
  color:#080611;font-weight:800
}
</style>
""", unsafe_allow_html=True)

# ---------- State ----------
if "reels" not in st.session_state:
    st.session_state.reels = ["7️⃣", "💎", "7️⃣"]
if "spin_count" not in st.session_state:
    st.session_state.spin_count = 0

symbols = ["7️⃣","💎","🔔","⭐","💲","🍀","🎰"]

def spin():
    st.session_state.reels = [random.choice(symbols) for _ in range(3)]
    st.session_state.spin_count += 1

# ---------- Navigation ----------
st.markdown("""
<div style="display:flex;justify-content:space-between;align-items:center;
padding:.7rem 0 1.2rem;border-bottom:1px solid rgba(255,255,255,.08)">
  <div style="font-size:1.45rem;font-weight:900">PUZ<span class="grad">ZOO</span>
    <div style="font-size:.58rem;letter-spacing:.3em;color:#9aa0c3">GAMES · CCR PLATFORM™</div>
  </div>
  <div style="color:#9aa0c3;font-size:.9rem">Platform&nbsp;&nbsp; Concepts&nbsp;&nbsp; Founder&nbsp;&nbsp; G2E 2026</div>
</div>
""", unsafe_allow_html=True)

# ---------- Hero ----------
st.markdown('<div class="hero">', unsafe_allow_html=True)
left, right = st.columns([1.15,.85], gap="large")

with left:
    st.markdown('<div class="eyebrow">● G2E 2026 · Las Vegas · Something different is coming</div>', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size:clamp(2.7rem,5vw,4.5rem);font-weight:900">We\'re bringing something <span class="grad">different</span> to Vegas this year.</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p class="lead">Meet <strong style="color:#eef0ff">CCR Platform™</strong> — a ground-up game engine
    built specifically for <strong style="color:#eef0ff">chance-based gaming</strong>.
    Not a reskin. Not an incremental update. A full rebuild, forged from decades of knowing
    exactly what keeps players engaged, staying, and returning.</p>
    """, unsafe_allow_html=True)

    chips = ["🎰 Slots","Lottery","Sweepstakes","Raffles","Instant Games"]
    st.markdown("".join(f'<span class="chip">{x}</span>' for x in chips) +
                '<span class="chip chip-gold">And beyond</span>', unsafe_allow_html=True)

    c1,c2 = st.columns(2)
    with c1:
        if st.button("Book a G2E meeting →", use_container_width=True):
            st.session_state.show_contact = True
    with c2:
        st.button("Explore the platform ↓", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    m = st.columns(4)
    for col, num, label in zip(m, ["12","5","1","30"], ["Concepts","Working prototypes","Patented mechanic","Years experience"]):
        with col:
            st.markdown(f'<div class="metric-card"><div class="metric-number">{num}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="slot">', unsafe_allow_html=True)
    st.markdown('<div style="display:flex;justify-content:space-between;color:#9aa0c3;font-size:.7rem;font-weight:800;letter-spacing:.2em">CCR™ <span style="color:#fbbf24">★★★★★</span></div><br>', unsafe_allow_html=True)
    r = st.columns(3)
    for col, value in zip(r, st.session_state.reels):
        with col:
            st.markdown(f'<div class="reel">{value}</div>', unsafe_allow_html=True)
    st.markdown('<br><div style="color:#9aa0c3;font-size:.65rem;letter-spacing:.15em">CHANCE-BASED · REBUILT FROM ZERO</div>', unsafe_allow_html=True)
    if st.button("SPIN", use_container_width=True):
        spin()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="margin-top:1rem;color:#22d3ee;font-weight:800">ONE PATENTED MECHANIC</div><div style="color:#9aa0c3">social · multiplayer · jackpots</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Stats ----------
st.markdown("---")
stats = st.columns(4)
for col, num, label in zip(stats, ["12","5","10","30"],
                            ["Game concepts in development","Working prototypes today","US patents held","Years in the games industry"]):
    with col:
        st.markdown(f'<div class="metric-card"><div class="metric-number">{num}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)

# ---------- Platform ----------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div class="eyebrow">The Engine</div>', unsafe_allow_html=True)
st.markdown('<h2>Built for chance-based gaming.<br><span class="grad">Designed for regulated markets.</span></h2>', unsafe_allow_html=True)
st.markdown('<p class="lead">CCR Platform™ is a full rebuild of the chance-based game engine — engineered with flexibility, scalability, and security at its core, and with regulated-market requirements in mind from day one.</p>', unsafe_allow_html=True)

modules = [
("01","Flexibility","One engine, every chance-based format.",
 ["Slots, lottery, sweepstakes, raffles & instant games on one core","Social & multiplayer modes built in"]),
("02","Scalability","From prototype to portfolio.",
 ["12 concepts → 5 working prototypes and growing","Architecture ready for operator-scale deployment"]),
("03","Security","Serious engineering, seriously protected.",
 ["Secure-by-design platform architecture","10 US patents behind the mechanics"]),
("04","Regulated Markets","Compliance considered from line one.",
 ["Built with regulated-market requirements in mind","Ready for certification and jurisdictional review"]),
]
cols = st.columns(2)
for i, (num,title,tag,items) in enumerate(modules):
    with cols[i%2]:
        st.markdown(f'<div class="module"><div class="module-num">{num}</div><h3>{title}</h3><p>{tag}</p><ul>{"".join("<li>"+x+"</li>" for x in items)}</ul></div>', unsafe_allow_html=True)

# ---------- Concepts ----------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div class="eyebrow">Behind the Scenes</div>', unsafe_allow_html=True)
st.markdown('<h2>The vision is already <span class="grad">taking shape.</span></h2>', unsafe_allow_html=True)
st.markdown('<p class="lead">Twelve concepts. Five working prototypes. One patented mechanic. More details under NDA — but here\'s the shape of what\'s coming.</p>', unsafe_allow_html=True)

concepts = [
("01","CCR Platform™ Core","Not a reskin. Not an incremental update. A full rebuild.",
 ["Ground-up engine purpose-built for chance-based play","Forged from decades of player-engagement expertise","Designed around what makes players stay — and return","Patented core mechanic at the heart of the system"]),
("02","12 Concepts · 5 Working Prototypes","Real builds, playable today — under NDA.",
 ["Slots spanning classic to next-gen","Lottery, sweepstakes, raffles & instant games","Social & multiplayer experiences","Jackpots engineered to be bigger and smarter"]),
("03","Where the Industry Is Headed","A paradigm shift is coming. Early movers win big here.",
 ["A new mechanic class operators haven't seen before","Engine economics built for the next era of iGaming","Full details shared in person, under NDA","See it live at G2E 2026 in Las Vegas"]),
]
for num, title, tag, items in concepts:
    items_html = "".join(
        f'<li style="color:#c6cade;margin:.35rem 0">{x}</li>'
        for x in items
    )
    card_html = f"""
    <div class="card">
        <div class="module-num">{num}</div>
        <h3>{title}</h3>
        <p style="color:#9aa0c3;font-style:italic">{tag}</p>
        <ul>{items_html}</ul>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

# ---------- Founder ----------
st.markdown("<br><br>", unsafe_allow_html=True)
f1,f2 = st.columns([.9,1.1], gap="large")
with f1:
    st.markdown("""
    <div class="card" style="text-align:center">
      <div style="width:104px;height:104px;border-radius:50%;margin:auto;display:flex;align-items:center;justify-content:center;
      font-size:2rem;font-weight:900;color:#090713;background:linear-gradient(90deg,#22d3ee,#a855f7,#ec4899)">ZO</div>
      <h3>Zeki Orak</h3>
      <div style="color:#22d3ee;font-weight:700">Founder & CEO · Puzzoo</div>
      <p class="lead" style="font-size:.92rem">30-year games-industry veteran. Vivendi Games published Puzzoo's mobile titles — two of them factory-installed on Nokia phones for the US market.</p>
      <div><span class="chip">Vivendi Games</span><span class="chip">Nokia · US market</span><span class="chip">Hasbro</span><span class="chip">Mattel</span><span class="chip">Fisher-Price</span><span class="chip">Tiger Electronics</span><span class="chip">10 US Patents</span></div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown('<div class="eyebrow">The Team Behind It</div>', unsafe_allow_html=True)
    st.markdown('<h2>Decades of knowing what keeps players <span class="grad">engaged.</span></h2>', unsafe_allow_html=True)
    st.markdown('<p class="lead">CCR Platform™ isn\'t a bet on a trend — it\'s the product of a career spent building games people love, for some of the biggest names in the business. That experience is baked into every line of the engine: what holds attention, what earns a return visit, and what survives in regulated markets.</p>', unsafe_allow_html=True)
    st.markdown('<div class="nda">🔒 <strong>Under NDA.</strong> The vision is already taking shape behind the scenes. Full architecture, prototypes and the patented mechanic are shared in person — 15 minutes at G2E is all it takes.</div>', unsafe_allow_html=True)

# ---------- G2E ----------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div class="card" style="text-align:center;padding:3rem 1.5rem">', unsafe_allow_html=True)
st.markdown('<div style="display:inline-block;color:#fbbf24;border:1px solid rgba(251,191,36,.4);border-radius:999px;padding:.45rem 1rem;font-size:.75rem;font-weight:800;letter-spacing:.2em">🎰 G2E 2026 · LAS VEGAS</div>', unsafe_allow_html=True)
st.markdown('<h2>Curious about what\'s next in iGaming?<br><span class="grad">Let\'s connect.</span></h2>', unsafe_allow_html=True)
st.markdown('<p class="lead" style="max-width:560px;margin:auto">15 minutes. Just a conversation and a demo about where the industry is headed. Drop a comment or DM Zeki to lock in a time.</p>', unsafe_allow_html=True)
a,b = st.columns(2)
with a:
    st.link_button("DM Zeki on LinkedIn →", "https://www.linkedin.com/in/zekiorak/", use_container_width=True)
with b:
    st.link_button("Email to book a slot", "mailto:info@puzzoo.com?subject=G2E%202026%20Meeting%20%E2%80%94%20CCR%20Platform", use_container_width=True)
st.markdown('<p style="color:#9aa0c3;margin-top:1.5rem">#G2E2026 &nbsp; #iGaming &nbsp; #GamingTechnology &nbsp; #GameDevelopment &nbsp; #GamingPlatform &nbsp; #Slots &nbsp; #Lottery &nbsp; #Sweepstakes &nbsp; #GameEngine &nbsp; #Innovation &nbsp; #Puzzoo &nbsp; #CCRPlatform</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Contact ----------
if st.session_state.get("show_contact"):
    st.markdown("### Book a G2E conversation")
    st.info("The original page routes visitors to Zeki via LinkedIn or email. This Streamlit version keeps those two contact paths above.")

st.markdown('<div class="footer"><strong style="color:#eef0ff">PUZZOO</strong> · CCR Platform™ — Real innovation. Real players. Real results.<br>© 2026 Puzzoo. CCR Platform™ is a trademark of Puzzoo. All rights reserved.</div>', unsafe_allow_html=True)
