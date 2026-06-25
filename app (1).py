import streamlit as st
import random
import string
import time
import json

st.set_page_config(
    page_title="🎪 Dino-Raptor-Blue-Killer",
    page_icon="🐉",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Creepster&family=Fredoka+One&family=Share+Tech+Mono&display=swap');
html, body, [class*="css"] { background:#05000f !important; color:#fbfbff !important; font-family:'Fredoka One',sans-serif; }
.stApp { background: radial-gradient(ellipse at top, #1a003a 0%, #05000f 70%); }
h1 { font-family:'Creepster',cursive; color:#FFD700; font-size:2.8em; text-shadow:0 0 20px #ffd40088,0 0 40px #a855f755; margin-bottom:0; }
h2,h3 { color:#A1C9F4; }
.stButton>button { background:linear-gradient(135deg,#7C3AED,#A855F7); color:#fbfbff; border:2px solid #FFD700; border-radius:14px; font-family:'Fredoka One',sans-serif; font-size:1.05em; padding:0.4em 1.2em; transition:all 0.2s; }
.stButton>button:hover { background:linear-gradient(135deg,#FFD700,#FF6B00); color:#1a003a; transform:scale(1.04); }
.stTextInput>div>div>input { background:#1a003a; color:#fbfbff; border:2px solid #7C3AED; border-radius:10px; font-family:'Fredoka One',sans-serif; }
.stSelectbox>div>div { background:#1a003a; color:#fbfbff; border:2px solid #7C3AED; border-radius:10px; }
.stRadio>div { background:#1a003a22; border-radius:10px; padding:8px; }
.stTabs [data-baseweb="tab-list"] { background:#1a003a; border-radius:12px; }
.stTabs [data-baseweb="tab"] { color:#A1C9F4; font-family:'Fredoka One',sans-serif; font-size:1em; }
.stTabs [aria-selected="true"] { color:#FFD700 !important; border-bottom:3px solid #FFD700; }
.stExpander { background:#1a003a55; border:1px solid #7C3AED44; border-radius:12px; }
div[data-testid="stMetricValue"] { color:#FFD700; font-family:'Creepster',cursive; font-size:2em; }
.stMarkdown hr { border-color:#7C3AED44; }
::-webkit-scrollbar { width:6px; } ::-webkit-scrollbar-track { background:#1a003a; } ::-webkit-scrollbar-thumb { background:#7C3AED; border-radius:4px; }
</style>
""", unsafe_allow_html=True)

def ss(k, v):
    if k not in st.session_state:
        st.session_state[k] = v

ss("page", "store"); ss("logged_in", False); ss("username", ""); ss("gender", "boy")
ss("platform", "PC"); ss("character", None); ss("current_zone", "circus_tent")
ss("room_locked", False); ss("in_bathroom", False); ss("chat_messages", [])
ss("berichten", {}); ss("action_log", []); ss("energy", 100); ss("hunger", 100); ss("thirst", 100)
ss("rooms", {
    "public_lobby": {"name":"🎪 Public Lobby","zone":"circus_tent","players":["Pomni","Ragatha"],"private":False,"code":"","locked":False,"max":16},
    "beach_vibes":  {"name":"🏖 Beach Vibes","zone":"beach","players":["Zooble"],"private":False,"code":"","locked":False,"max":16},
    "void_crew":    {"name":"🌑 Void Crew","zone":"void","players":["Jax","Gangle"],"private":True,"code":"VOID99","locked":False,"max":8},
})
ss("my_room_id", None); ss("current_room", None)
ss("leaderboard", [
    {"name":"Dino Raptor","score":9999,"char":"🐉","badge":"👑"},
    {"name":"Pomni","score":420,"char":"🃏","badge":"⭐"},
    {"name":"Ragatha","score":380,"char":"🧸","badge":"🌸"},
    {"name":"Jax","score":310,"char":"🐇","badge":"😏"},
    {"name":"Gangle","score":290,"char":"🎭","badge":"🎭"},
    {"name":"Zooble","score":250,"char":"🧩","badge":"🌊"},
    {"name":"Kinger","score":200,"char":"♔","badge":"♔"},
    {"name":"Bubble","score":150,"char":"🫧","badge":"💙"},
])

CHARACTERS = {
    "dino_raptor":{"name":"Dino Raptor","emoji":"🐉","color":"#FFD700","role":"Supreme Leader","gender":"male","powers":["✈ Fly","⚡ Teleport","👻 Phase Walls","🌍 Reality Control"]},
    "pomni":      {"name":"Pomni","emoji":"🃏","color":"#4FC3F7","role":"Jester","gender":"female","powers":[]},
    "ragatha":    {"name":"Ragatha","emoji":"🧸","color":"#E91E63","role":"Rag Doll","gender":"female","powers":[]},
    "jax":        {"name":"Jax","emoji":"🐇","color":"#7C3AED","role":"Trickster","gender":"male","powers":["⚡ Minor Teleport"]},
    "gangle":     {"name":"Gangle","emoji":"🎭","color":"#FF8A80","role":"Marionette","gender":"female","powers":[]},
    "zooble":     {"name":"Zooble","emoji":"🧩","color":"#4CAF50","role":"Shapeshifter","gender":"non_binary","powers":["🔄 Shapeshift"]},
    "kinger":     {"name":"Kinger","emoji":"♔","color":"#FFD700","role":"Chess King","gender":"male","powers":[]},
    "bubble":     {"name":"Bubble","emoji":"🫧","color":"#E0F7FA","role":"Helper Sphere","gender":"non_binary","powers":["🫧 Float","👻 Phase","💫 Buff"]},
    "custom":     {"name":"Custom","emoji":"✨","color":"#FF69B4","role":"Custom Character","gender":"custom","powers":[]},
}

ZONES = {
    "void":        {"name":"The Void","emoji":"🌑","color":"#1a0030","npcs":["Jax","Gangle"]},
    "moon":        {"name":"Moon","emoji":"🌙","color":"#1a1a3e","npcs":["Pomni"]},
    "sun":         {"name":"Sun Zone","emoji":"☀","color":"#FF6B00","npcs":["Kinger"]},
    "beach":       {"name":"Beach","emoji":"🏖","color":"#00BCD4","npcs":["Zooble"]},
    "fairground":  {"name":"Fairground","emoji":"🎡","color":"#E91E63","npcs":["Ragatha"]},
    "circus_tent": {"name":"Circus Tent","emoji":"🎪","color":"#FF1744","npcs":["Pomni","Bubble"]},
    "throne_room": {"name":"Throne Room","emoji":"🏰","color":"#FFD700","npcs":["Dino Raptor"]},
}

NPC_DIALOGUES = {
    "Dino Raptor": ["Welcome to MY circus. Try to keep up.","I built this world. Every pixel belongs to me.","Need something? Ask nicely."],
    "Pomni":   ["I don't know how I got here but I really want to leave.","Has anyone seen a way out? Asking for me.","Okay okay okay. I can do this. Probably."],
    "Ragatha": ["Hey! You look like you could use a friend!","Everything will be okay, I just know it!","Want to explore together?"],
    "Jax":     ["Oh great, another one. Welcome to the fun house. Not.","Yeah yeah I'll help. Don't make it weird.","Bored. So incredibly bored."],
    "Gangle":  ["Oh... hello. I was just expressing my feelings.","The void isn't so bad once you accept the emptiness.","You came to talk to me? That's the nicest thing."],
    "Zooble":  ["What. What do you want.","Fine. I'll help. But I'm not happy about it.","The beach is the only place I feel like myself."],
    "Kinger":  ["Oh! Oh dear. A visitor. Is that — are you friendly?","I've been here the longest. Seen things.","Chess? Want to play chess?"],
    "Bubble":  ["Bloop! Hi!","Bubble bubble bubble!","Bloooop. That means I like you."],
}

WORD_FILTER = ["fuck","shit","damn","bitch","ass","crap","hell","bastard","dick","pussy","cock"]

def filter_message(msg):
    m = msg
    for w in WORD_FILTER:
        m = m.replace(w, "⭐"*len(w))
        m = m.replace(w.upper(), "⭐"*len(w))
        m = m.replace(w.capitalize(), "⭐"*len(w))
    if "🖕" in m: m = m.replace("🖕","👋")
    return m

def gen_code(): return ''.join(random.choices(string.ascii_uppercase+string.digits, k=6))
def is_dino(): return st.session_state.username.strip().lower() in ["dino raptor","dino_raptor","dinoraptor"]

def page_store():
    st.markdown("<h1>🐉 DINO-RAPTOR-BLUE-KILLER</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#A1C9F4;margin-top:0'>🎪 Amazing Digital Circus — Online</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2,1,1])
    with col1:
        st.markdown("""
        <div style='background:linear-gradient(135deg,#1a003a,#2d0060);border:2px solid #FFD700;border-radius:18px;padding:24px;'>
        <p style='color:#fbfbff;font-size:1.1em;'>
        🎮 Join the most amazing circus in the digital universe!<br><br>
        ✅ Play on <b>PC</b> or <b>PS5</b> — no download needed<br>
        ✅ 8 characters + create your own<br>
        ✅ 7 explorable world zones<br>
        ✅ Private rooms with secret codes<br>
        ✅ Real-time chat, voice & video calls<br>
        ✅ Your own room: PC, laptop, bed, bathroom, PS5<br>
        ✅ Guns, actions, NPC dialogue<br>
        ✅ For ages <b>13+</b>
        </p></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style='background:#1a003a;border:2px solid #7C3AED;border-radius:14px;padding:16px;text-align:center;'>
        <div style='font-size:4em;'>🎪</div>
        <div style='color:#FFD700;font-size:1.3em;font-family:Creepster,cursive;'>AMAZING</div>
        <div style='color:#fbfbff;font-size:0.9em;'>DIGITAL CIRCUS</div>
        <div style='color:#A1C9F4;font-size:0.8em;margin-top:8px;'>v4.0 Online</div></div>""", unsafe_allow_html=True)
        st.markdown("""
        <div style='background:#0a1a0a;border:2px solid #17b26a;border-radius:10px;padding:10px;margin-top:8px;text-align:center;'>
        <div style='color:#17b26a;font-size:0.85em;'>🟢 AVAILABLE ON</div>
        <div style='color:#fbfbff;font-size:0.9em;'>PC • PS5 • Browser</div>
        <div style='color:#909094;font-size:0.75em;margin-top:4px;'>Search: dino-raptor-blue-killer</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style='background:#1a1a0a;border:2px solid #FFD700;border-radius:14px;padding:16px;text-align:center;'>
        <div style='color:#FFD700;font-size:1.1em;'>🎮 HOW TO PLAY</div>
        <div style='color:#fbfbff;font-size:0.85em;margin-top:8px;'>
        <b>PC:</b> Open this URL<br><br><b>PS5:</b> Browser → paste URL<br><br><b>Chrome:</b> Paste URL → play!
        </div></div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("🎭 Meet the Characters")
    char_cols = st.columns(9)
    for i,(cid,c) in enumerate(CHARACTERS.items()):
        with char_cols[i]:
            st.markdown(f"""
            <div style='background:{c["color"]}22;border:2px solid {c["color"]};border-radius:12px;padding:8px;text-align:center;'>
            <div style='font-size:2.2em;'>{c["emoji"]}</div>
            <div style='color:{c["color"]};font-size:0.8em;font-weight:bold;'>{c["name"]}</div>
            <div style='color:#909094;font-size:0.65em;'>{c["role"]}</div></div>""", unsafe_allow_html=True)
    st.markdown("---")
    _,col_b,_ = st.columns(3)
    with col_b:
        if st.button("🚀  PLAY NOW  —  FREE", use_container_width=True):
            st.session_state.page = "age_gate"; st.rerun()

def page_age_gate():
    st.markdown("<h1>🔞 Age Verification</h1>", unsafe_allow_html=True)
    _,c2,_ = st.columns([1,2,1])
    with c2:
        st.markdown("""<div style='background:#1a003a;border:2px solid #FFD700;border-radius:18px;padding:28px;text-align:center;'>
        <div style='font-size:3em;'>🎂</div><h3 style='color:#FFD700;'>How old are you?</h3></div>""", unsafe_allow_html=True)
        age = st.number_input("Enter your age", min_value=1, max_value=120, value=16, step=1)
        confirm = st.checkbox("I confirm I am 13 years old or older")
        if st.button("✅ Confirm & Continue", use_container_width=True):
            if age >= 13 and confirm: st.session_state.page = "login"; st.rerun()
            elif age < 13: st.error("❌ Sorry! This game is only for players 13 and older.")
            else: st.warning("⚠️ Please check the confirmation box.")
        if st.button("← Back", use_container_width=True): st.session_state.page = "store"; st.rerun()

def page_login():
    st.markdown("<h1>🎪 Create Your Player</h1>", unsafe_allow_html=True)
    c1,c2 = st.columns([1,2])
    with c1:
        st.markdown("### 1️⃣ Your Identity")
        username = st.text_input("Choose your game name", max_chars=20, placeholder="e.g. Dino Raptor")
        gender = st.radio("Are you a...?", ["Boy 👦","Girl 👧","Non-Binary 🌈"])
        platform = st.radio("Platform", ["PC 🖥","PS5 🎮"])
        st.markdown("### 2️⃣ Pick a Character")
        selected_char = st.selectbox("Base character", options=list(CHARACTERS.keys()),
            format_func=lambda k: f"{CHARACTERS[k]['emoji']} {CHARACTERS[k]['name']} — {CHARACTERS[k]['role']}")
        st.markdown("### 3️⃣ Customize")
        skin = st.selectbox("Skin tone", ["porcelain","ivory","beige","light_tan","medium_tan","olive","brown","dark_brown","ebony","blue_tint","gold_shimmer"])
        hair = st.selectbox("Hair style", ["short_straight","medium_wavy","long_curly","ponytail","twin_pigtails","afro","mohawk","bald","two_toned"])
        hair_c = st.selectbox("Hair color", ["black","brown","blonde","red","pink","purple","blue","white","rainbow"])
        outfit = st.selectbox("Outfit style", ["casual","streetwear","circus","fantasy","royal","sporty","techno","beach"])
        st.markdown("### 4️⃣ Special")
        has_wings = st.checkbox("Wings 🪶"); has_horns = st.checkbox("Horns 🦄"); glow_eyes = st.checkbox("Glowing eyes ✨")
        aura = st.color_picker("Power aura color", "#7C3AED")
    with c2:
        st.markdown("### 👤 Preview")
        ch = CHARACTERS.get(selected_char, CHARACTERS["custom"])
        is_dr = username.strip().lower() in ["dino raptor","dino_raptor","dinoraptor"]
        st.markdown(f"""
        <div style='background:linear-gradient(135deg,{ch["color"]}22,#1a003a);border:3px solid {ch["color"]};border-radius:20px;padding:28px;text-align:center;'>
        <div style='font-size:5em;'>{ch["emoji"]}</div>
        <h2 style='color:{ch["color"]};margin:8px 0;'>{username if username else "???"}</h2>
        <div style='color:#A1C9F4;'>{ch["role"]} · {gender}</div>
        {"<div style=\"color:#FFD700;font-size:1.1em;margin-top:8px;\">👑 SUPREME LEADER 👑</div>" if is_dr else ""}
        <hr style='border-color:{ch["color"]}44;'/>
        <div style='text-align:left;'>
        Skin: {skin} | Hair: {hair} ({hair_c})<br>Outfit: {outfit} | Aura: <span style='color:{aura};'>■</span><br>
        {"🪶 Wings " if has_wings else ""}{"🦄 Horns " if has_horns else ""}{"✨ Glow Eyes" if glow_eyes else ""}
        </div></div>""", unsafe_allow_html=True)
        if is_dr: st.success("👑 You are Supreme Leader: FLY ✈ + TELEPORT ⚡ + PHASE WALLS 👻 + REALITY CONTROL 🌍")
        st.markdown("""<div style='background:#1a003a;border:1px solid #7C3AED;border-radius:12px;padding:12px;margin-top:12px;'>
        <b style='color:#A1C9F4;'>📦 Your Room:</b><br>
        <span style='color:#909094;font-size:0.9em;'>🖥 Gaming PC | 💻 Gaming Laptop | 🛏 King Bed | 🚿 Bathroom | 📺 PS5 | 📱 Phone | 🔫 Gun | 🔒 Lock</span></div>""", unsafe_allow_html=True)
        if st.button("🚀 Enter the Circus!", use_container_width=True):
            if not username.strip(): st.error("❌ Please enter a name!")
            else:
                st.session_state.username = username.strip()
                st.session_state.gender = gender.split(" ")[0].lower()
                st.session_state.platform = "PC" if "PC" in platform else "PS5"
                st.session_state.character = selected_char
                st.session_state.logged_in = True
                st.session_state.page = "game"
                rid = f"room_{username.lower().replace(' ','_')}"
                st.session_state.my_room_id = rid
                st.session_state.rooms[rid] = {"name":f"🏠 {username}'s Room","zone":"throne_room" if is_dr else "circus_tent",
                    "players":[username],"private":True,"code":gen_code(),"locked":False,"max":8,"owner":username}
                st.rerun()

def page_game():
    user = st.session_state.username
    char = CHARACTERS.get(st.session_state.character, CHARACTERS["custom"])
    zone = ZONES.get(st.session_state.current_zone, ZONES["circus_tent"])
    dr = is_dino()
    with st.sidebar:
        st.markdown(f"""<div style='background:linear-gradient(135deg,{char["color"]}33,#1a003a);border:2px solid {char["color"]};border-radius:14px;padding:12px;text-align:center;'>
        <div style='font-size:2.5em;'>{char["emoji"]}</div>
        <b style='color:{char["color"]};font-size:1.1em;'>{user}</b><br>
        <span style='color:#909094;font-size:0.85em;'>{char["role"]}</span>
        {"<br><span style=\"color:#FFD700;\">👑 Supreme Leader</span>" if dr else ""}
        </div>""", unsafe_allow_html=True)
        st.progress(st.session_state.energy/100, text=f"⚡ Energy: {st.session_state.energy}%")
        st.progress(st.session_state.hunger/100, text=f"🍔 Hunger: {st.session_state.hunger}%")
        st.progress(st.session_state.thirst/100, text=f"💧 Thirst: {st.session_state.thirst}%")
        st.markdown(f"""<div style='background:{zone["color"]}22;border:1px solid {zone["color"]};border-radius:10px;padding:8px;text-align:center;'>
        <span style='font-size:1.5em;'>{zone["emoji"]}</span> <b style='color:#fbfbff;'>{zone["name"]}</b></div>""", unsafe_allow_html=True)
        if dr:
            for p in ["✈ Fly","⚡ Teleport","👻 Phase Walls","🌍 Reality Control"]:
                if st.button(p, key=f"pw_{p}", use_container_width=True):
                    st.session_state.action_log.append(f"⚡ {user} uses {p}!"); st.toast(f"⚡ {p} activated!")
        if st.button("🚪 Log Out", use_container_width=True):
            st.session_state.page = "store"; st.session_state.logged_in = False; st.rerun()

    tab_world,tab_room,tab_chat,tab_rooms,tab_lb = st.tabs(["🌍 World","🏠 My Room","💬 Chat & Calls","🎪 Rooms","🏆 Leaderboard"])

    with tab_world:
        st.markdown(f"<h2>🌍 {zone['emoji']} {zone['name']}</h2>", unsafe_allow_html=True)
        zone_cols = st.columns(7)
        for i,(zid,z) in enumerate(ZONES.items()):
            with zone_cols[i]:
                active = zid == st.session_state.current_zone
                st.markdown(f"""<div style='background:{z["color"]}{"44" if active else "15"};border:2px solid {"#FFD700" if active else z["color"]};border-radius:12px;padding:8px;text-align:center;'>
                <div style='font-size:1.8em;'>{z["emoji"]}</div>
                <div style='color:#fbfbff;font-size:0.75em;font-weight:bold;'>{z["name"]}</div>
                {"<div style=\"color:#FFD700;font-size:0.7em;\">● HERE</div>" if active else ""}
                </div>""", unsafe_allow_html=True)
                if not active:
                    if st.button("Go", key=f"zone_{zid}", use_container_width=True):
                        st.session_state.current_zone = zid
                        st.session_state.action_log.append(f"{'⚡' if dr else '🚶'} {user} {'teleported' if dr else 'traveled'} to {z['name']}!")
                        st.rerun()
        st.markdown("---")
        st.markdown(f"### {zone['emoji']} NPCs in {zone['name']}")
        if zone["npcs"]:
            npc_cols = st.columns(len(zone["npcs"]))
            for i,npc in enumerate(zone["npcs"]):
                with npc_cols[i]:
                    ch_data = next((c for c in CHARACTERS.values() if c["name"]==npc),None)
                    color = ch_data["color"] if ch_data else "#A1C9F4"
                    emoji = ch_data["emoji"] if ch_data else "🤖"
                    dialogue = random.choice(NPC_DIALOGUES.get(npc,["..."]))
                    st.markdown(f"""<div style='background:{color}22;border:2px solid {color};border-radius:14px;padding:14px;'>
                    <div style='font-size:2em;'>{emoji}</div><b style='color:{color};'>{npc}</b><br>
                    <span style='color:#fbfbff;font-style:italic;'>&quot;{dialogue}&quot;</span></div>""", unsafe_allow_html=True)
                    if st.button(f"Talk to {npc}", key=f"talk_{npc}_{i}", use_container_width=True):
                        reply = random.choice(NPC_DIALOGUES.get(npc,["..."]))
                        st.session_state.chat_messages.append({"sender":npc,"msg":reply,"time":time.strftime("%H:%M"),"npc":True})
                        st.toast(f"{emoji} {npc}: {reply[:50]}")
        if st.session_state.action_log:
            st.markdown("---")
            st.markdown("**📜 Action Log**")
            for entry in reversed(st.session_state.action_log[-8:]):
                st.markdown(f"<span style='color:#909094;font-size:0.85em;'>{entry}</span>", unsafe_allow_html=True)

    with tab_room:
        st.markdown("<h2>🏠 Your Room</h2>", unsafe_allow_html=True)
        lc,bc = st.columns(2)
        with lc:
            locked = st.session_state.room_locked
            st.markdown(f"<div style='color:{'#f04438' if locked else '#17b26a'};font-size:1.1em;font-weight:bold;'>{'🔒 LOCKED' if locked else '🔓 Unlocked'}</div>", unsafe_allow_html=True)
            if locked:
                if st.button("🔓 Unlock Room", use_container_width=True): st.session_state.room_locked = False; st.rerun()
            else:
                if st.button("🔒 Lock Room", use_container_width=True): st.session_state.room_locked = True; st.rerun()
        with bc:
            if st.button("🚿 Bathroom" if not st.session_state.in_bathroom else "🚪 Leave Bathroom", use_container_width=True):
                st.session_state.in_bathroom = not st.session_state.in_bathroom; st.rerun()
        if st.session_state.in_bathroom:
            st.markdown("""<div style='background:#0a1a2a;border:2px solid #00BCD4;border-radius:14px;padding:18px;'>
            <h3 style='color:#00BCD4;'>🚿 Bathroom</h3>
            <span style='color:#909094;'>Shower 🚿 · Sink 🪥 · Mirror 🪞 · Toilet 🚽</span></div>""", unsafe_allow_html=True)
        else:
            r1,r2 = st.columns(2)
            items_l = [("🖥 Gaming PC","RTX 9090 · 128GB RAM","Gaming only","#A1C9F4"),("🛏 King Bed","Neon underglow · runes","Sleep to restore energy","#8DE5A1"),("📺 PS5 Screen","77-inch curved OLED","Play PS5 games","#003087")]
            items_r = [("💻 Gaming Laptop","RGB hinge","Gaming + Chat + Calls","#FFB482"),("📱 Smartphone","Always in inventory","Messages · Calls · Apps","#FF9F9B"),("🔫 Sidearm","Pistol (no bazooka)","Combat in battle zones","#D0BBFF")]
            with r1:
                for label,desc,use,color in items_l:
                    st.markdown(f"""<div style='background:{color}15;border:2px solid {color};border-radius:12px;padding:14px;margin-bottom:10px;'>
                    <b style='color:{color};'>{label}</b><br><span style='color:#909094;font-size:0.85em;'>{desc}</span><br>
                    <span style='color:#fbfbff;font-size:0.85em;'>Use: {use}</span></div>""", unsafe_allow_html=True)
            with r2:
                for label,desc,use,color in items_r:
                    st.markdown(f"""<div style='background:{color}15;border:2px solid {color};border-radius:12px;padding:14px;margin-bottom:10px;'>
                    <b style='color:{color};'>{label}</b><br><span style='color:#909094;font-size:0.85em;'>{desc}</span><br>
                    <span style='color:#fbfbff;font-size:0.85em;'>Use: {use}</span></div>""", unsafe_allow_html=True)
            st.markdown("### ⚡ Actions")
            actions = [("😴 Sleep","sleep","+50 energy","energy",50),("🍔 Eat","eat","+30 hunger","hunger",30),("💧 Drink","drink","+20 thirst","thirst",20),("🚬 Smoke","smoke","Cosmetic 💨",None,0),("💨 Vape","vape","Cosmetic ☁",None,0),("🍺 Alcohol","alcohol","Cosmetic 🥴",None,0)]
            ac1,ac2,ac3 = st.columns(3)
            action_cols = [ac1,ac2,ac3,ac1,ac2,ac3]
            for (label,aid,effect,stat,val),col in zip(actions,action_cols):
                with col:
                    if st.button(f"{label}\n{effect}", key=f"act_{aid}", use_container_width=True):
                        if stat and val: st.session_state[stat] = min(100, st.session_state[stat]+val)
                        st.session_state.action_log.append(f"🎮 {user} — {label} {effect}"); st.toast(f"{label} — {effect}")

    with tab_chat:
        st.markdown("<h2>💬 Chat, Calls & Berichten</h2>", unsafe_allow_html=True)
        ct1,ct2 = st.columns([2,1])
        with ct1:
            st.markdown("**💬 Zone Chat**")
            chat_box = st.container(height=280)
            with chat_box:
                if not st.session_state.chat_messages:
                    st.markdown("<span style='color:#909094;'>No messages yet. Say something!</span>", unsafe_allow_html=True)
                for msg in st.session_state.chat_messages[-20:]:
                    name = msg["sender"]; is_me = name==user; is_npc = msg.get("npc",False)
                    color = "#FFD700" if name in ["Dino Raptor","Dino_Raptor"] else ("#A1C9F4" if is_me else ("#FF8A80" if is_npc else "#8DE5A1"))
                    align = "right" if is_me else "left"
                    st.markdown(f"""<div style='text-align:{align};margin:4px 0;'>
                    <span style='color:{color};font-size:0.85em;font-weight:bold;'>{name}</span>
                    <span style='color:#909094;font-size:0.7em;'> {msg["time"]}</span><br>
                    <span style='background:#1a003a;padding:4px 10px;border-radius:10px;color:#fbfbff;font-size:0.9em;display:inline-block;'>{msg["msg"]}</span></div>""", unsafe_allow_html=True)
            msg_in = st.text_input("Type a message...", key="chat_input", placeholder="Type here...")
            _,sc2 = st.columns([3,1])
            with sc2:
                if st.button("Send 📤", use_container_width=True):
                    if msg_in.strip():
                        st.session_state.chat_messages.append({"sender":user,"msg":filter_message(msg_in.strip()),"time":time.strftime("%H:%M"),"npc":False}); st.rerun()
        with ct2:
            st.markdown("""<div style='background:#1a003a;border:2px solid #7C3AED;border-radius:12px;padding:12px;'>
            <b style='color:#A1C9F4;'>📱 Phone App</b><br>
            <span style='color:#909094;font-size:0.85em;'>• 💬 Berichten<br>• 📞 Bellen<br>• 🎥 Video Bellen<br>• 🎙 Voice Chat<br>• 📡 Push-to-Talk</span></div>""", unsafe_allow_html=True)
            call_target = st.selectbox("Bel", [c["name"] for c in CHARACTERS.values() if c["name"]!=user], key="call_s")
            cc1,cc2 = st.columns(2)
            with cc1:
                if st.button("📞 Bellen", use_container_width=True): st.toast(f"📞 Bezig met bellen naar {call_target}..."); st.session_state.action_log.append(f"📞 {user} belde {call_target}")
            with cc2:
                if st.button("🎥 Video", use_container_width=True): st.toast(f"🎥 Video bellen naar {call_target}..."); st.session_state.action_log.append(f"🎥 {user} video belde {call_target}")
            bm_target = st.selectbox("Naar", [c["name"] for c in CHARACTERS.values() if c["name"]!=user], key="bm_s")
            bm_text = st.text_input("Bericht", key="bm_in", placeholder="Type bericht...")
            if st.button("📨 Verstuur", use_container_width=True):
                if bm_text.strip():
                    if bm_target not in st.session_state.berichten: st.session_state.berichten[bm_target]=[]
                    st.session_state.berichten[bm_target].append({"van":user,"msg":filter_message(bm_text.strip()),"time":time.strftime("%H:%M")})
                    st.toast(f"📨 Gestuurd naar {bm_target}!")
            st.markdown("""<div style='background:#1a003a;border:1px solid #17b26a;border-radius:10px;padding:10px;margin-top:8px;'>
            <span style='color:#17b26a;font-size:0.8em;'>🚫 Filter actief:</span><br>
            <span style='color:#909094;font-size:0.75em;'>Schelden → ⭐ · Middelvinger → 👋</span></div>""", unsafe_allow_html=True)

    with tab_rooms:
        st.markdown("<h2>🎪 Game Rooms</h2>", unsafe_allow_html=True)
        rc1,rc2 = st.columns([2,1])
        with rc1:
            st.markdown("**🌍 Public Rooms**")
            for rid,room in st.session_state.rooms.items():
                if not room["private"]:
                    z = ZONES.get(room["zone"],{}); pc=len(room["players"]); pm=room["max"]
                    st.markdown(f"""<div style='background:#1a003a;border:2px solid #7C3AED;border-radius:12px;padding:14px;margin-bottom:8px;'>
                    <b style='color:#fbfbff;'>{room["name"]}</b><span style='float:right;color:#A1C9F4;'>{pc}/{pm}</span><br>
                    <span style='background:{z.get("color","#7C3AED")}33;color:{z.get("color","#A1C9F4")};border-radius:6px;padding:2px 8px;font-size:0.8em;'>{z.get("emoji","🌍")} {z.get("name","Zone")}</span>
                    {"&nbsp;<span style="color:#17b26a;font-size:0.8em;">🔓 Open</span>" if not room.get("locked") else "<span style="color:#f04438;font-size:0.8em;">🔒 Locked</span>"}
                    </div>""", unsafe_allow_html=True)
                    if not room.get("locked") or dr:
                        if st.button(f"Join {room['name']}", key=f"join_{rid}"):
                            if user not in room["players"]: room["players"].append(user)
                            st.session_state.current_room=rid; st.session_state.current_zone=room["zone"]
                            st.toast(f"✅ Joined {room['name']}!"); st.rerun()
        with rc2:
            st.markdown("**🔒 Create Private Room**")
            rname = st.text_input("Room name", placeholder="My Secret Room", key="new_room_name")
            rzone = st.selectbox("Zone", list(ZONES.keys()), format_func=lambda k: f"{ZONES[k]['emoji']} {ZONES[k]['name']}", key="new_room_zone")
            rprivate = st.checkbox("Private room", value=True, key="new_room_priv")
            if st.button("➕ Create Room", use_container_width=True, key="create_room_btn"):
                if rname.strip():
                    rid_new = f"room_{gen_code().lower()}"; code = gen_code() if rprivate else ""
                    st.session_state.rooms[rid_new] = {"name":f"🏠 {rname.strip()}","zone":rzone,"players":[user],"private":rprivate,"code":code,"locked":False,"max":8,"owner":user}
                    st.session_state.current_room=rid_new; st.session_state.current_zone=rzone
                    if rprivate: st.success(f"✅ Room created! Code: **{code}**")
                    else: st.success("✅ Room created!")
                    st.rerun()
            st.markdown("**🔑 Join with Code**")
            jcode = st.text_input("Enter room code", max_chars=6, placeholder="ABC123", key="join_code")
            if st.button("🔑 Join", use_container_width=True, key="join_code_btn"):
                found = False
                for rid,room in st.session_state.rooms.items():
                    if room.get("code","").upper()==jcode.upper():
                        found=True
                        if room.get("locked") and not dr: st.error("🔒 Room is locked!")
                        else:
                            if user not in room["players"]: room["players"].append(user)
                            st.session_state.current_room=rid; st.session_state.current_zone=room["zone"]
                            st.success(f"✅ Joined {room['name']}!"); st.rerun()
                if not found: st.error("❌ Wrong code! Ask the host.")
            if st.session_state.my_room_id and st.session_state.my_room_id in st.session_state.rooms:
                my_room = st.session_state.rooms[st.session_state.my_room_id]
                st.markdown("---"); st.markdown("**🏠 Your Room Code:**")
                st.code(my_room.get("code","PUBLIC"), language=None)
                if my_room.get("locked"):
                    if st.button("🔓 Unlock My Room", use_container_width=True, key="unlock_myroom"): my_room["locked"]=False; st.rerun()
                else:
                    if st.button("🔒 Lock My Room", use_container_width=True, key="lock_myroom"): my_room["locked"]=True; st.rerun()

    with tab_lb:
        st.markdown("<h2>🏆 Leaderboard</h2>", unsafe_allow_html=True)
        medals = ["🥇","🥈","🥉"]+["🏅"]*(len(st.session_state.leaderboard)-3)
        for player,medal in zip(st.session_state.leaderboard,medals):
            is_me_lb = player["name"].lower()==user.lower()
            st.markdown(f"""<div style='background:{"#2d1a00" if is_me_lb else "#1a0030"};border:2px solid {"#FFD700" if is_me_lb else "#7C3AED"};border-radius:12px;padding:12px;margin-bottom:6px;display:flex;align-items:center;'>
            <span style='font-size:1.5em;margin-right:10px;'>{medal}</span>
            <span style='font-size:1.3em;margin-right:8px;'>{player["char"]}</span>
            <b style='color:{"#FFD700" if is_me_lb else "#fbfbff"};flex:1;'>{player["name"]}</b>
            <span style='color:#A1C9F4;'>{player["badge"]}</span>
            <span style='color:#FFD700;font-family:Creepster,cursive;font-size:1.2em;margin-left:16px;'>{player["score"]:,} pts</span></div>""", unsafe_allow_html=True)
        if dr:
            st.markdown("---"); st.markdown("**👑 Supreme Leader Controls**")
            kick_target = st.selectbox("Kick player", [p["name"] for p in st.session_state.leaderboard if p["name"]!=user], key="kick_select")
            if st.button(f"🦵 Kick {kick_target}"):
                st.warning(f"⚡ {kick_target} has been kicked!")
                st.session_state.action_log.append(f"🦵 Dino Raptor kicked {kick_target}!")

page = st.session_state.page
if page=="store": page_store()
elif page=="age_gate": page_age_gate()
elif page=="login": page_login()
elif page=="game":
    if not st.session_state.logged_in: st.session_state.page="store"; st.rerun()
    else: page_game()
else: st.session_state.page="store"; st.rerun()
