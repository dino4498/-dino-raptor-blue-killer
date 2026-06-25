import streamlit as st
import random
import string
import time
import json

st.set_page_config(
    page_title="Dino-Raptor-Blue-Killer",
    page_icon="dragon",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Creepster&family=Fredoka+One&display=swap');
html, body, [class*="css"] { background:#05000f !important; color:#fbfbff !important; font-family:'Fredoka One',sans-serif; }
.stApp { background: radial-gradient(ellipse at top, #1a003a 0%, #05000f 70%); }
h1 { font-family:'Creepster',cursive; color:#FFD700; font-size:2.8em; text-shadow:0 0 20px #ffd40088; margin-bottom:0; }
h2,h3 { color:#A1C9F4; }
.stButton>button { background:linear-gradient(135deg,#7C3AED,#A855F7); color:#fbfbff; border:2px solid #FFD700; border-radius:14px; padding:0.4em 1.2em; transition:all 0.2s; }
.stButton>button:hover { background:linear-gradient(135deg,#FFD700,#FF6B00); color:#1a003a; }
.stTextInput>div>div>input { background:#1a003a; color:#fbfbff; border:2px solid #7C3AED; border-radius:10px; }
.stTabs [data-baseweb="tab-list"] { background:#1a003a; border-radius:12px; }
.stTabs [data-baseweb="tab"] { color:#A1C9F4; }
.stTabs [aria-selected="true"] { color:#FFD700 !important; border-bottom:3px solid #FFD700; }
</style>
""", unsafe_allow_html=True)

def ss(k, v):
    if k not in st.session_state:
        st.session_state[k] = v

ss("page", "store")
ss("logged_in", False)
ss("username", "")
ss("gender", "boy")
ss("platform", "PC")
ss("character", None)
ss("current_zone", "circus_tent")
ss("room_locked", False)
ss("in_bathroom", False)
ss("chat_messages", [])
ss("berichten", {})
ss("action_log", [])
ss("energy", 100)
ss("hunger", 100)
ss("thirst", 100)
ss("rooms", {
    "public_lobby": {"name":"Public Lobby","zone":"circus_tent","players":["Pomni","Ragatha"],"private":False,"code":"","locked":False,"max":16},
    "beach_vibes":  {"name":"Beach Vibes","zone":"beach","players":["Zooble"],"private":False,"code":"","locked":False,"max":16},
    "void_crew":    {"name":"Void Crew","zone":"void","players":["Jax","Gangle"],"private":True,"code":"VOID99","locked":False,"max":8},
})
ss("my_room_id", None)
ss("current_room", None)
ss("leaderboard", [
    {"name":"Dino Raptor","score":9999,"char":"dragon","badge":"crown"},
    {"name":"Pomni","score":420,"char":"joker","badge":"star"},
    {"name":"Ragatha","score":380,"char":"teddy bear","badge":"flower"},
    {"name":"Jax","score":310,"char":"rabbit","badge":"smirk"},
    {"name":"Gangle","score":290,"char":"masks","badge":"masks"},
    {"name":"Zooble","score":250,"char":"puzzle","badge":"wave"},
    {"name":"Kinger","score":200,"char":"chess king","badge":"crown"},
    {"name":"Bubble","score":150,"char":"bubble","badge":"blue heart"},
])

CHARACTERS = {
    "dino_raptor":{"name":"Dino Raptor","emoji":"dragon","color":"#FFD700","role":"Supreme Leader","gender":"male","powers":["Fly","Teleport","Phase Walls","Reality Control"]},
    "pomni":      {"name":"Pomni","emoji":"joker","color":"#4FC3F7","role":"Jester","gender":"female","powers":[]},
    "ragatha":    {"name":"Ragatha","emoji":"teddy","color":"#E91E63","role":"Rag Doll","gender":"female","powers":[]},
    "jax":        {"name":"Jax","emoji":"rabbit","color":"#7C3AED","role":"Trickster","gender":"male","powers":["Minor Teleport"]},
    "gangle":     {"name":"Gangle","emoji":"masks","color":"#FF8A80","role":"Marionette","gender":"female","powers":[]},
    "zooble":     {"name":"Zooble","emoji":"puzzle","color":"#4CAF50","role":"Shapeshifter","gender":"non_binary","powers":["Shapeshift"]},
    "kinger":     {"name":"Kinger","emoji":"king","color":"#FFD700","role":"Chess King","gender":"male","powers":[]},
    "bubble":     {"name":"Bubble","emoji":"bubble","color":"#E0F7FA","role":"Helper Sphere","gender":"non_binary","powers":["Float","Phase","Buff"]},
    "custom":     {"name":"Custom","emoji":"sparkles","color":"#FF69B4","role":"Custom Character","gender":"custom","powers":[]},
}

ZONES = {
    "void":        {"name":"The Void","emoji":"new moon","color":"#1a0030","npcs":["Jax","Gangle"]},
    "moon":        {"name":"Moon","emoji":"crescent moon","color":"#1a1a3e","npcs":["Pomni"]},
    "sun":         {"name":"Sun Zone","emoji":"sun","color":"#FF6B00","npcs":["Kinger"]},
    "beach":       {"name":"Beach","emoji":"beach","color":"#00BCD4","npcs":["Zooble"]},
    "fairground":  {"name":"Fairground","emoji":"ferris wheel","color":"#E91E63","npcs":["Ragatha"]},
    "circus_tent": {"name":"Circus Tent","emoji":"circus tent","color":"#FF1744","npcs":["Pomni","Bubble"]},
    "throne_room": {"name":"Throne Room","emoji":"castle","color":"#FFD700","npcs":["Dino Raptor"]},
}

NPC_DIALOGUES = {
    "Dino Raptor": ["Welcome to MY circus. Try to keep up.","I built this world. Every pixel belongs to me.","Need something? Ask nicely."],
    "Pomni": ["I do not know how I got here but I really want to leave.","Has anyone seen a way out? Asking for me.","Okay okay okay. I can do this. Probably."],
    "Ragatha": ["Hey! You look like you could use a friend!","Everything will be okay, I just know it!","Want to explore together?"],
    "Jax": ["Oh great, another one. Welcome to the fun house. Not.","Yeah yeah I will help. Do not make it weird.","Bored. So incredibly bored."],
    "Gangle": ["Oh... hello. I was just expressing my feelings.","The void is not so bad once you accept the emptiness.","You came to talk to me? That is the nicest thing."],
    "Zooble": ["What. What do you want.","Fine. I will help. But I am not happy about it.","The beach is the only place I feel like myself."],
    "Kinger": ["Oh! Oh dear. A visitor. Are you friendly?","I have been here the longest. Seen things.","Chess? Want to play chess?"],
    "Bubble": ["Bloop! Hi!","Bubble bubble bubble!","Bloooop. That means I like you."],
}

WORD_FILTER = ["fuck","shit","damn","bitch","ass","crap","hell","bastard","dick","pussy","cock"]

def filter_message(msg):
    m = msg
    for w in WORD_FILTER:
        m = m.replace(w, "star" * len(w))
        m = m.replace(w.upper(), "star" * len(w))
        m = m.replace(w.capitalize(), "star" * len(w))
    return m

def gen_code():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=6))

def is_dino():
    return st.session_state.username.strip().lower() in ["dino raptor","dino_raptor","dinoraptor"]

def card(content, border_color="#7C3AED", bg_extra="15"):
    return "<div style='background:" + border_color + bg_extra + ";border:2px solid " + border_color + ";border-radius:12px;padding:14px;margin-bottom:8px;'>" + content + "</div>"

def page_store():
    st.markdown("<h1>DINO-RAPTOR-BLUE-KILLER</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#A1C9F4;margin-top:0'>Amazing Digital Circus Online</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2,1,1])
    with col1:
        st.markdown(card(
            "<p style='color:#fbfbff;font-size:1.1em;'>Join the most amazing circus in the digital universe!<br><br>"
            "Play on PC or PS5 - no download needed<br>"
            "8 characters plus create your own<br>"
            "7 explorable world zones<br>"
            "Private rooms with secret codes<br>"
            "Real-time chat, voice and video calls<br>"
            "Your own room: PC, laptop, bed, bathroom, PS5<br>"
            "Guns, actions, NPC dialogue<br>"
            "For ages 13+</p>",
            "#FFD700", "22"
        ), unsafe_allow_html=True)
    with col2:
        st.markdown(card(
            "<div style='text-align:center;'>"
            "<div style='font-size:4em;'>circus</div>"
            "<div style='color:#FFD700;font-size:1.3em;'>AMAZING DIGITAL CIRCUS</div>"
            "<div style='color:#A1C9F4;font-size:0.8em;'>v4.0 Online</div>"
            "<div style='color:#17b26a;margin-top:8px;'>AVAILABLE ON PC, PS5, Browser</div>"
            "<div style='color:#909094;font-size:0.75em;'>Search: dino-raptor-blue-killer</div>"
            "</div>",
            "#7C3AED"
        ), unsafe_allow_html=True)
    with col3:
        st.markdown(card(
            "<div style='text-align:center;color:#fbfbff;'>"
            "<b style='color:#FFD700;'>HOW TO PLAY</b><br><br>"
            "<b>PC Store:</b> Search dino-raptor-blue-killer<br><br>"
            "<b>PS5 Store:</b> Open browser, type the link<br><br>"
            "<b>Chrome/Edge:</b> Paste URL and play!"
            "</div>",
            "#FFD700"
        ), unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("Meet the Characters")
    char_cols = st.columns(len(CHARACTERS))
    for i, (cid, c) in enumerate(CHARACTERS.items()):
        with char_cols[i]:
            cc = c["color"]
            st.markdown(
                "<div style='background:" + cc + "22;border:2px solid " + cc + ";border-radius:12px;padding:8px;text-align:center;'>"
                "<div style='font-size:2em;'>" + c["emoji"] + "</div>"
                "<div style='color:" + cc + ";font-size:0.8em;font-weight:bold;'>" + c["name"] + "</div>"
                "<div style='color:#909094;font-size:0.7em;'>" + c["role"] + "</div>"
                "</div>",
                unsafe_allow_html=True
            )
    st.markdown("---")
    col_a, col_b, col_c = st.columns(3)
    with col_b:
        if st.button("PLAY NOW - FREE", use_container_width=True):
            st.session_state.page = "age_gate"
            st.rerun()

def page_age_gate():
    st.markdown("<h1>Age Verification</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        st.markdown(card("<div style='text-align:center;'><div style='font-size:3em;'>cake</div><h3 style='color:#FFD700;'>How old are you?</h3></div>", "#FFD700", "22"), unsafe_allow_html=True)
        age = st.number_input("Enter your age", min_value=1, max_value=120, value=16, step=1)
        confirm = st.checkbox("I confirm I am 13 years old or older")
        if st.button("Confirm and Continue", use_container_width=True):
            if age >= 13 and confirm:
                st.session_state.page = "login"
                st.rerun()
            elif age < 13:
                st.error("Sorry! This game is only for players 13 and older.")
            else:
                st.warning("Please check the confirmation box.")
        if st.button("Back to Store", use_container_width=True):
            st.session_state.page = "store"
            st.rerun()

def page_login():
    st.markdown("<h1>Create Your Player</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns([1,2])
    with c1:
        st.markdown("### Your Identity")
        username = st.text_input("Choose your game name", max_chars=20, placeholder="e.g. Dino Raptor")
        gender = st.radio("Are you a...?", ["Boy", "Girl", "Non-Binary"])
        platform = st.radio("Platform", ["PC", "PS5"])
        st.markdown("### Pick a Character")
        selected_char = st.selectbox(
            "Base character",
            options=list(CHARACTERS.keys()),
            format_func=lambda k: CHARACTERS[k]["name"] + " - " + CHARACTERS[k]["role"],
        )
        st.markdown("### Customize")
        skin = st.selectbox("Skin tone", ["porcelain","ivory","beige","light_tan","medium_tan","olive","brown","dark_brown","ebony","blue_tint","gold_shimmer"])
        hair = st.selectbox("Hair style", ["short_straight","medium_wavy","long_curly","ponytail","afro","mohawk","bald"])
        hair_c = st.selectbox("Hair color", ["black","brown","blonde","red","pink","purple","blue","white","rainbow"])
        outfit = st.selectbox("Outfit style", ["casual","streetwear","circus","fantasy","royal","sporty","techno","beach"])
        st.markdown("### Special")
        has_wings = st.checkbox("Wings")
        has_horns = st.checkbox("Horns")
        glow_eyes = st.checkbox("Glowing eyes")
        aura = st.color_picker("Power aura color", "#7C3AED")
    with c2:
        st.markdown("### Character Preview")
        ch = CHARACTERS.get(selected_char, CHARACTERS["custom"])
        is_dr = username.strip().lower() in ["dino raptor","dino_raptor","dinoraptor"]
        cc = ch["color"]
        display_name = username if username else "???"
        leader_html = "<div style='color:#FFD700;font-size:1.1em;margin-top:8px;'>SUPREME LEADER</div>" if is_dr else ""
        extras = []
        if has_wings: extras.append("Wings")
        if has_horns: extras.append("Horns")
        if glow_eyes: extras.append("Glowing Eyes")
        extras_html = " - ".join(extras) if extras else ""
        st.markdown(
            "<div style='background:linear-gradient(135deg," + cc + "22,#1a003a);border:3px solid " + cc + ";border-radius:20px;padding:28px;text-align:center;'>"
            "<div style='font-size:5em;'>" + ch["emoji"] + "</div>"
            "<h2 style='color:" + cc + ";margin:8px 0;'>" + display_name + "</h2>"
            "<div style='color:#A1C9F4;'>" + ch["role"] + " - " + gender + "</div>"
            + leader_html +
            "<hr style='border-color:" + cc + "44;margin:16px 0;'>"
            "<div style='text-align:left;color:#909094;font-size:0.9em;'>"
            "Skin: <span style='color:#fbfbff;'>" + skin + "</span> - "
            "Hair: <span style='color:#fbfbff;'>" + hair + " (" + hair_c + ")</span><br>"
            "Outfit: <span style='color:#fbfbff;'>" + outfit + "</span> - "
            "Aura: <span style='color:" + aura + ";'>square</span><br>"
            "<span style='color:#A1C9F4;'>" + extras_html + "</span>"
            "</div></div>",
            unsafe_allow_html=True
        )
        if ch.get("powers"):
            st.markdown("**Powers:**")
            for p in ch["powers"]:
                st.markdown("- " + p)
        if is_dr:
            st.success("As Dino Raptor: FLY + TELEPORT + PHASE WALLS + REALITY CONTROL + KICK PLAYERS")
        st.markdown("")
        if st.button("Enter the Circus!", use_container_width=True):
            if not username.strip():
                st.error("Please enter a name!")
            else:
                st.session_state.username = username.strip()
                st.session_state.gender = gender.lower()
                st.session_state.platform = "PC" if platform == "PC" else "PS5"
                st.session_state.character = selected_char
                st.session_state.logged_in = True
                st.session_state.page = "game"
                rid = "room_" + username.lower().replace(" ","_")
                st.session_state.my_room_id = rid
                st.session_state.rooms[rid] = {
                    "name": username + " Room",
                    "zone": "throne_room" if is_dr else "circus_tent",
                    "players": [username],
                    "private": True,
                    "code": gen_code(),
                    "locked": False,
                    "max": 8,
                    "owner": username,
                }
                st.rerun()

def page_game():
    user = st.session_state.username
    char = CHARACTERS.get(st.session_state.character, CHARACTERS["custom"])
    zone = ZONES.get(st.session_state.current_zone, ZONES["circus_tent"])
    dr = is_dino()
    cc = char["color"]
    zc = zone["color"]

    with st.sidebar:
        leader_line = "<br><b style='color:#FFD700;'>Supreme Leader</b>" if dr else ""
        st.markdown(
            "<div style='background:" + cc + "33;border:2px solid " + cc + ";border-radius:14px;padding:12px;text-align:center;'>"
            "<div style='font-size:2.5em;'>" + char["emoji"] + "</div>"
            "<b style='color:" + cc + ";font-size:1.1em;'>" + user + "</b><br>"
            "<span style='color:#909094;font-size:0.85em;'>" + char["role"] + " - " + st.session_state.gender + "</span><br>"
            "<span style='color:#A1C9F4;font-size:0.8em;'>" + st.session_state.platform + "</span>"
            + leader_line + "</div>",
            unsafe_allow_html=True
        )
        st.markdown("**Stats**")
        st.progress(st.session_state.energy/100, text="Energy: " + str(st.session_state.energy) + "%")
        st.progress(st.session_state.hunger/100, text="Hunger: " + str(st.session_state.hunger) + "%")
        st.progress(st.session_state.thirst/100, text="Thirst: " + str(st.session_state.thirst) + "%")
        st.markdown("**Zone**")
        st.markdown(
            "<div style='background:" + zc + "22;border:1px solid " + zc + ";border-radius:10px;padding:8px;text-align:center;'>"
            "<b style='color:#fbfbff;'>" + zone["emoji"] + " " + zone["name"] + "</b></div>",
            unsafe_allow_html=True
        )
        if dr:
            st.markdown("**Powers**")
            for p in ["Fly","Teleport","Phase Walls","Reality Control"]:
                if st.button(p, key="pw_" + p, use_container_width=True):
                    st.session_state.action_log.append(user + " uses " + p + "!")
                    st.toast(p + " activated!")
        st.markdown("---")
        if st.button("Log Out", use_container_width=True):
            for k in ["logged_in","page","username","character","current_zone"]:
                if k in st.session_state: del st.session_state[k]
            st.session_state.page = "store"
            st.rerun()

    tab_world, tab_room, tab_chat, tab_rooms, tab_lb = st.tabs(["World","My Room","Chat","Rooms","Leaderboard"])

    with tab_world:
        st.markdown("<h2>Explore the World</h2>", unsafe_allow_html=True)
        zone_cols = st.columns(7)
        for i, (zid, z) in enumerate(ZONES.items()):
            with zone_cols[i]:
                active = zid == st.session_state.current_zone
                border = "#FFD700" if active else z["color"]
                bg = z["color"] + ("44" if active else "15")
                here = "<div style='color:#FFD700;font-size:0.7em;'>HERE</div>" if active else ""
                st.markdown(
                    "<div style='background:" + bg + ";border:2px solid " + border + ";border-radius:12px;padding:8px;text-align:center;'>"
                    "<div style='font-size:1.8em;'>" + z["emoji"] + "</div>"
                    "<div style='color:#fbfbff;font-size:0.75em;'>" + z["name"] + "</div>"
                    + here + "</div>",
                    unsafe_allow_html=True
                )
                if not active:
                    if st.button("Go", key="zone_" + zid, use_container_width=True):
                        st.session_state.current_zone = zid
                        action = "teleported" if dr else "traveled"
                        st.session_state.action_log.append(user + " " + action + " to " + z["name"])
                        st.rerun()
        st.markdown("---")
        st.markdown("### NPCs in " + zone["emoji"] + " " + zone["name"])
        npc_list = zone["npcs"]
        npc_cols = st.columns(max(len(npc_list), 1))
        for i, npc in enumerate(npc_list):
            with npc_cols[i]:
                dialogue = random.choice(NPC_DIALOGUES.get(npc, ["..."]))
                ch_data = next((c for c in CHARACTERS.values() if c["name"] == npc), None)
                nc = ch_data["color"] if ch_data else "#A1C9F4"
                ne = ch_data["emoji"] if ch_data else "robot"
                st.markdown(
                    "<div style='background:" + nc + "22;border:2px solid " + nc + ";border-radius:14px;padding:14px;'>"
                    "<div style='font-size:2em;'>" + ne + "</div>"
                    "<b style='color:" + nc + ";'>" + npc + "</b><br>"
                    "<span style='color:#fbfbff;font-style:italic;'>" + dialogue + "</span>"
                    "</div>",
                    unsafe_allow_html=True
                )
                if st.button("Talk to " + npc, key="talk_" + npc + "_" + str(i), use_container_width=True):
                    reply = random.choice(NPC_DIALOGUES.get(npc, ["..."]))
                    st.session_state.chat_messages.append({"sender": npc, "msg": reply, "time": time.strftime("%H:%M"), "npc": True})
                    st.toast(npc + ": " + reply[:50])
        if st.session_state.action_log:
            st.markdown("---")
            st.markdown("**Action Log**")
            for entry in reversed(st.session_state.action_log[-8:]):
                st.markdown("<span style='color:#909094;font-size:0.85em;'>" + entry + "</span>", unsafe_allow_html=True)

    with tab_room:
        st.markdown("<h2>Your Room</h2>", unsafe_allow_html=True)
        lock_col, bath_col = st.columns(2)
        with lock_col:
            locked = st.session_state.room_locked
            lock_color = "#f04438" if locked else "#17b26a"
            lock_text = "LOCKED" if locked else "Unlocked"
            st.markdown("<div style='color:" + lock_color + ";font-size:1.1em;font-weight:bold;'>" + lock_text + "</div>", unsafe_allow_html=True)
            if locked:
                if st.button("Unlock Room", use_container_width=True):
                    st.session_state.room_locked = False
                    st.rerun()
            else:
                if st.button("Lock Room", use_container_width=True):
                    st.session_state.room_locked = True
                    st.rerun()
        with bath_col:
            bath_label = "Leave Bathroom" if st.session_state.in_bathroom else "Go to Bathroom"
            if st.button(bath_label, use_container_width=True):
                st.session_state.in_bathroom = not st.session_state.in_bathroom
                st.rerun()
        if st.session_state.in_bathroom:
            st.markdown(card("<h3 style='color:#00BCD4;'>Bathroom</h3><span style='color:#909094;'>shower, sink, mirror, toilet</span>", "#00BCD4"), unsafe_allow_html=True)
        else:
            r1, r2 = st.columns(2)
            items_left = [
                ("gaming_pc", "Gaming PC", "RTX 9090, 128GB RAM, 10TB SSD", "Gaming only", "#A1C9F4"),
                ("bed",       "King Bed",  "Neon underglow, rune headboard", "Sleep to restore energy", "#8DE5A1"),
                ("ps5_screen","PS5 Screen","77-inch curved OLED", "Play PS5 games", "#4FC3F7"),
            ]
            items_right = [
                ("gaming_laptop","Gaming Laptop","RGB hinge, all-in-one", "Gaming + Chat + Video calls", "#FFB482"),
                ("phone",        "Smartphone",   "Always in inventory",  "Messages, Calls, Apps", "#FF9F9B"),
                ("gun",          "Sidearm",       "Pistol (no bazooka)", "Combat in battle zones", "#D0BBFF"),
            ]
            with r1:
                for iid, lbl, desc, use, col in items_left:
                    st.markdown(card("<b style='color:" + col + ";'>" + lbl + "</b><br><span style='color:#909094;font-size:0.85em;'>" + desc + "</span><br><span style='color:#fbfbff;font-size:0.85em;'>Use: " + use + "</span>", col), unsafe_allow_html=True)
            with r2:
                for iid, lbl, desc, use, col in items_right:
                    st.markdown(card("<b style='color:" + col + ";'>" + lbl + "</b><br><span style='color:#909094;font-size:0.85em;'>" + desc + "</span><br><span style='color:#fbfbff;font-size:0.85em;'>Use: " + use + "</span>", col), unsafe_allow_html=True)
            st.markdown("### Actions")
            actions = [
                ("Sleep",  "sleep",   "+50 energy",   "energy", 50),
                ("Eat",    "eat",     "+30 hunger",   "hunger", 30),
                ("Drink",  "drink",   "+20 thirst",   "thirst", 20),
                ("Smoke",  "smoke",   "Cosmetic",     None, 0),
                ("Vape",   "vape",    "Cosmetic",     None, 0),
                ("Alcohol","alcohol", "Cosmetic",     None, 0),
            ]
            ac1, ac2, ac3 = st.columns(3)
            action_cols = [ac1, ac2, ac3, ac1, ac2, ac3]
            for (label, aid, effect, stat, val), col in zip(actions, action_cols):
                with col:
                    if st.button(label + " - " + effect, key="act_" + aid, use_container_width=True):
                        if stat and val:
                            st.session_state[stat] = min(100, st.session_state[stat] + val)
                        st.session_state.action_log.append(user + " " + label.lower() + "s - " + effect)
                        st.toast(label + " - " + effect)

    with tab_chat:
        st.markdown("<h2>Chat, Calls and Berichten</h2>", unsafe_allow_html=True)
        ct1, ct2 = st.columns([2,1])
        with ct1:
            st.markdown("**Zone Chat**")
            chat_box = st.container(height=280)
            with chat_box:
                if not st.session_state.chat_messages:
                    st.markdown("<span style='color:#909094;'>No messages yet. Say something!</span>", unsafe_allow_html=True)
                for msg in st.session_state.chat_messages[-20:]:
                    name = msg["sender"]
                    is_me = name == user
                    is_npc = msg.get("npc", False)
                    if name in ["Dino Raptor","Dino_Raptor"]:
                        mc = "#FFD700"
                    elif is_me:
                        mc = "#A1C9F4"
                    elif is_npc:
                        mc = "#FF8A80"
                    else:
                        mc = "#8DE5A1"
                    align = "right" if is_me else "left"
                    npc_tag = " [NPC]" if is_npc else ""
                    st.markdown(
                        "<div style='text-align:" + align + ";margin:4px 0;'>"
                        "<span style='color:" + mc + ";font-size:0.85em;font-weight:bold;'>" + name + npc_tag + "</span>"
                        "<span style='color:#909094;font-size:0.7em;'> " + msg["time"] + "</span><br>"
                        "<span style='background:#1a003a;padding:4px 10px;border-radius:10px;color:#fbfbff;font-size:0.9em;display:inline-block;'>" + msg["msg"] + "</span>"
                        "</div>",
                        unsafe_allow_html=True
                    )
            msg_in = st.text_input("Type a message...", key="chat_input", placeholder="Type here...")
            sc1, sc2 = st.columns([3,1])
            with sc2:
                if st.button("Send", use_container_width=True):
                    if msg_in.strip():
                        clean = filter_message(msg_in.strip())
                        st.session_state.chat_messages.append({"sender":user,"msg":clean,"time":time.strftime("%H:%M"),"npc":False})
                        st.rerun()
        with ct2:
            st.markdown("**Bellen and Voice**")
            call_options = [c["name"] for c in CHARACTERS.values() if c["name"] != user]
            call_target = st.selectbox("Kies contact", call_options, key="call_select")
            cc1, cc2 = st.columns(2)
            with cc1:
                if st.button("Bellen", use_container_width=True):
                    st.toast("Bezig met bellen naar " + call_target + "...")
            with cc2:
                if st.button("Video", use_container_width=True):
                    st.toast("Video bellen naar " + call_target + "...")
            bm_options = [c["name"] for c in CHARACTERS.values() if c["name"] != user]
            bm_target = st.selectbox("Naar", bm_options, key="bm_select")
            bm_text = st.text_input("Bericht", key="bm_input", placeholder="Type bericht...")
            if st.button("Verstuur", use_container_width=True):
                if bm_text.strip():
                    clean = filter_message(bm_text.strip())
                    if bm_target not in st.session_state.berichten:
                        st.session_state.berichten[bm_target] = []
                    st.session_state.berichten[bm_target].append({"van":user,"msg":clean,"time":time.strftime("%H:%M")})
                    st.toast("Bericht gestuurd naar " + bm_target + "!")
            st.markdown(card("<span style='color:#17b26a;font-size:0.8em;'>Filter actief: Schelden = stars - Middelvinger = hand wave</span>", "#17b26a"), unsafe_allow_html=True)

    with tab_rooms:
        st.markdown("<h2>Game Rooms</h2>", unsafe_allow_html=True)
        r_col1, r_col2 = st.columns([2,1])
        with r_col1:
            st.markdown("**Public Rooms**")
            for rid, room in st.session_state.rooms.items():
                if not room["private"]:
                    z = ZONES.get(room["zone"], {})
                    zc2 = z.get("color","#7C3AED")
                    ze = z.get("emoji","world")
                    zn = z.get("name","Zone")
                    room_locked = room.get("locked", False)
                    lock_status = "Locked" if room_locked else "Open"
                    lock_color2 = "#f04438" if room_locked else "#17b26a"
                    st.markdown(
                        "<div style='background:#1a003a;border:2px solid #7C3AED;border-radius:12px;padding:14px;margin-bottom:8px;'>"
                        "<b style='color:#fbfbff;'>" + room["name"] + "</b>"
                        "<span style='float:right;color:#A1C9F4;'>" + str(len(room["players"])) + "/" + str(room["max"]) + " players</span><br>"
                        "<span style='background:" + zc2 + "33;color:" + zc2 + ";border-radius:6px;padding:2px 8px;font-size:0.8em;'>" + ze + " " + zn + "</span>"
                        " <span style='color:" + lock_color2 + ";font-size:0.8em;'>" + lock_status + "</span>"
                        "</div>",
                        unsafe_allow_html=True
                    )
                    if not room_locked or dr:
                        if st.button("Join " + room["name"], key="join_" + rid, use_container_width=False):
                            if user not in room["players"]:
                                room["players"].append(user)
                            st.session_state.current_room = rid
                            st.session_state.current_zone = room["zone"]
                            st.toast("Joined " + room["name"] + "!")
                            st.rerun()
        with r_col2:
            st.markdown("**Create Private Room**")
            rname = st.text_input("Room name", placeholder="My Secret Room", key="new_room_name")
            rzone = st.selectbox("Zone", list(ZONES.keys()), format_func=lambda k: ZONES[k]["name"], key="new_room_zone")
            rprivate = st.checkbox("Private room", value=True, key="new_room_priv")
            if st.button("Create Room", use_container_width=True, key="create_room_btn"):
                if rname.strip():
                    rid_new = "room_" + gen_code().lower()
                    code = gen_code() if rprivate else ""
                    st.session_state.rooms[rid_new] = {
                        "name": rname.strip(),
                        "zone": rzone,
                        "players": [user],
                        "private": rprivate,
                        "code": code,
                        "locked": False,
                        "max": 8,
                        "owner": user,
                    }
                    st.session_state.current_room = rid_new
                    st.session_state.current_zone = rzone
                    if rprivate:
                        st.success("Room created! Your secret code: " + code)
                    else:
                        st.success("Room created!")
                    st.rerun()
            st.markdown("**Join with Code**")
            jcode = st.text_input("Enter room code", max_chars=6, placeholder="ABC123", key="join_code")
            if st.button("Join", use_container_width=True, key="join_code_btn"):
                found = False
                for rid, room in st.session_state.rooms.items():
                    if room.get("code","").upper() == jcode.upper():
                        found = True
                        if room.get("locked") and not dr:
                            st.error("Room is locked! Ask the host to unlock.")
                        else:
                            if user not in room["players"]:
                                room["players"].append(user)
                            st.session_state.current_room = rid
                            st.session_state.current_zone = room["zone"]
                            st.success("Joined " + room["name"] + "!")
                            st.rerun()
                if not found:
                    st.error("Wrong code! Ask the host for the correct code.")
            if st.session_state.my_room_id and st.session_state.my_room_id in st.session_state.rooms:
                my_room = st.session_state.rooms[st.session_state.my_room_id]
                st.markdown("---")
                st.markdown("**Your Room Code:**")
                st.code(my_room.get("code","PUBLIC"), language=None)
                if my_room.get("locked"):
                    if st.button("Unlock My Room", use_container_width=True, key="unlock_myroom"):
                        my_room["locked"] = False
                        st.rerun()
                else:
                    if st.button("Lock My Room", use_container_width=True, key="lock_myroom"):
                        my_room["locked"] = True
                        st.rerun()

    with tab_lb:
        st.markdown("<h2>Leaderboard</h2>", unsafe_allow_html=True)
        lb_data = st.session_state.leaderboard
        medals = ["gold","silver","bronze"] + ["medal"] * (len(lb_data) - 3)
        for i, (player, medal) in enumerate(zip(lb_data, medals)):
            is_me_lb = player["name"].lower() == user.lower()
            bg = "#2d1a00" if is_me_lb else "#1a0030"
            border = "#FFD700" if is_me_lb else "#7C3AED"
            nc = "#FFD700" if is_me_lb else "#fbfbff"
            st.markdown(
                "<div style='background:" + bg + ";border:2px solid " + border + ";border-radius:12px;padding:12px;margin-bottom:6px;display:flex;align-items:center;'>"
                "<span style='font-size:1.5em;margin-right:10px;'>" + medal + "</span>"
                "<span style='font-size:1.3em;margin-right:8px;'>" + player["char"] + "</span>"
                "<b style='color:" + nc + ";flex:1;'>" + player["name"] + "</b>"
                "<span style='color:#A1C9F4;'>" + player["badge"] + "</span>"
                "<span style='color:#FFD700;font-size:1.2em;margin-left:16px;'>" + str(player["score"]) + " pts</span>"
                "</div>",
                unsafe_allow_html=True
            )
        if dr:
            st.markdown("---")
            st.markdown("**Supreme Leader Controls**")
            kick_options = [p["name"] for p in lb_data if p["name"] != user]
            kick_target = st.selectbox("Kick player", kick_options, key="kick_select")
            if st.button("Kick " + kick_target, use_container_width=False):
                st.warning(kick_target + " has been kicked by the Supreme Leader!")
                st.session_state.action_log.append("Dino Raptor kicked " + kick_target + "!")

page = st.session_state.page
if page == "store":
    page_store()
elif page == "age_gate":
    page_age_gate()
elif page == "login":
    page_login()
elif page == "game":
    if not st.session_state.logged_in:
        st.session_state.page = "store"
        st.rerun()
    else:
        page_game()
else:
    st.session_state.page = "store"
    st.rerun()
