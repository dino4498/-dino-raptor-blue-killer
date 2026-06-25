
import json

# ══════════════════════════════════════════════════════════════════════════════
#  🎪 THE AMAZING DIGITAL CIRCUS — FULL ROSTER v3.0
#  Supreme Leader: DINO RAPTOR | 8 Characters | 7 World Zones
# ══════════════════════════════════════════════════════════════════════════════

circus_characters = {

    "DINO_RAPTOR": {
        "name": "Dino Raptor",
        "emoji": "🐉",
        "role": "Supreme Leader / God-Tier Overlord",
        "zone": "Throne Room",
        "power_level": "BEYOND_MAXIMUM ∞",
        "colors": {
            "primary":   "#FFD700",   # gold armor
            "secondary": "#7C3AED",   # purple aura
            "accent":    "#FF4500",   # lava orange eyes
            "aura":      "#A855F7",   # electric purple
            "shadow":    "#1a0030",
        },
        "shape": "giant raptor-dragon hybrid, bipedal, 3x height of others",
        "outfit": "full gold plate armor, flowing purple cape, king crown with 5 gems",
        "eyes": "glowing lava-orange, vertical slit pupils, backlit",
        "wings": "massive bat-dragon wings, dark purple membrane, gold bone tips",
        "tail": "heavy spiky tail with gold tip",
        "claws": "three-fingered hands, razor gold claws",
        "aura": "swirling gold+purple energy rings orbiting the body",
        "crown": "five-point gold crown with ruby, emerald, sapphire, amethyst, diamond",
        "abilities": {
            "FLY":              {"active": True,  "desc": "Fly freely in any zone at any altitude"},
            "TELEPORT":         {"active": True,  "desc": "Instant TP anywhere in the Digital Circus"},
            "PHASE_WALLS":      {"active": True,  "desc": "Walk/fly through any solid surface"},
            "REALITY_CONTROL":  {"active": True,  "desc": "Reshape the simulation at will"},
            "INVINCIBILITY":    {"active": True,  "desc": "Cannot be harmed by any force"},
            "SUPREME_KICK":     {"active": True,  "desc": "Can kick any player from any room"},
            "ZONE_LOCK":        {"active": True,  "desc": "Lock/unlock any zone instantly"},
            "SUMMON":           {"active": True,  "desc": "Summon any character to current zone"},
            "VOID_CONTROL":     {"active": True,  "desc": "Master of The Void dimension"},
            "TIME_FREEZE":      {"active": True,  "desc": "Freeze time for all others"},
        },
        "personality": "Commanding, fearless, protective of loyal subjects, merciless to threats",
        "dialogue": [
            "I AM THE CIRCUS.",
            "No one leaves without my permission.",
            "The Void answers to ME.",
            "Bow before the Supreme Leader.",
            "Your reality is mine to rewrite.",
        ],
        "draw_hints": {
            "height_multiplier": 3.0,
            "wings_spread_width": 4.0,
            "glow_radius": 80,
            "armor_plates": ["chest", "shoulders", "legs", "arms"],
            "floating_icons": ["✈", "⚡", "👻", "🌍", "⏱", "🔮", "👑"],
            "background_effect": "radial gold-purple aura burst",
        },
    },

    "POMNI": {
        "name": "Pomni",
        "emoji": "🃏",
        "role": "Protagonist / Lost Jester",
        "zone": "Circus Tent",
        "power_level": "LOW (but growing)",
        "colors": {
            "primary":   "#3B82F6",   # blue jester
            "secondary": "#EF4444",   # red details
            "accent":    "#FBBF24",   # gold bells
            "skin":      "#FDDCB0",
            "eye_white": "#FFFFFF",
            "eye_ring":  "#EF4444",
            "shadow":    "#1e3a5f",
        },
        "shape": "short humanoid, round head, large expressive eyes",
        "outfit": "blue+red diamond jester suit, white ruffled collar, pointy hat with gold bells",
        "eyes": "huge terrified circles, red ring irises, perpetually wide open",
        "hat": "two-point jester hat, blue+red diamonds, large gold bell at each tip",
        "abilities": {
            "PANIC_DODGE":     {"active": True,  "desc": "Accidentally dodge attacks in terror"},
            "CARTWHEEL":       {"active": True,  "desc": "Jester tumble movement"},
            "GLITCH_VISION":   {"active": False, "desc": "Occasionally sees through the simulation"},
        },
        "personality": "Anxious, overwhelmed, secretly brave, deeply kind",
        "dialogue": [
            "How do I get out of here?!",
            "This isn't real... right?",
            "I just want to go home.",
            "Okay. Okay. I can do this.",
        ],
        "draw_hints": {
            "height_multiplier": 1.0,
            "eye_size": "enormous — 40% of face",
            "expression": "perpetual terror/confusion",
            "hat_bells": 2,
            "background_effect": "blue spotlight glow",
        },
    },

    "RAGATHA": {
        "name": "Ragatha",
        "emoji": "🧸",
        "role": "Rag Doll / Eternal Optimist",
        "zone": "Fairground",
        "power_level": "MEDIUM",
        "colors": {
            "primary":   "#F472B6",   # pink
            "secondary": "#86EFAC",   # green dress
            "accent":    "#FDE68A",   # yellow yarn hair
            "seam":      "#78716C",
            "button_eye": "#1C1917",
            "cheek":     "#FB7185",
            "shadow":    "#4a1942",
        },
        "shape": "rag doll proportions, slightly lopsided, soft edges, visible seam lines",
        "outfit": "green polka-dot dress with white apron, pink bow in hair, mary-jane shoes",
        "eyes": "large black button eyes, stitched lash lines, rosy embroidered cheeks",
        "hair": "yellow yarn bunches tied with pink ribbons",
        "abilities": {
            "STITCH_REPAIR":   {"active": True,  "desc": "Self-repair torn limbs with magical thread"},
            "POSITIVITY_AURA": {"active": True,  "desc": "Calm nearby panicking characters"},
            "HUG_SHIELD":      {"active": True,  "desc": "Hugs protect both parties from minor hits"},
        },
        "personality": "Bubbly, relentlessly positive, hides her own pain, big sister energy",
        "dialogue": [
            "Everything is going to be fine!",
            "We just need to stay positive!",
            "Has anyone seen my button?",
            "Come on, group hug!",
        ],
        "draw_hints": {
            "height_multiplier": 0.9,
            "seam_lines": ["neck", "wrists", "ankles", "forehead"],
            "yarn_hair_strands": 12,
            "background_effect": "warm pink spotlight",
        },
    },

    "JAX": {
        "name": "Jax",
        "emoji": "🐇",
        "role": "Trickster / Chaos Rabbit",
        "zone": "The Void",
        "power_level": "HIGH (manipulation-based)",
        "colors": {
            "primary":   "#8B5CF6",   # purple
            "secondary": "#C4B5FD",   # lavender
            "accent":    "#10B981",   # green eyes
            "belly":     "#F3E8FF",
            "inner_ear": "#F9A8D4",
            "shadow":    "#2e1065",
        },
        "shape": "tall lanky rabbit, exaggerated long legs, slouched posture, thin arms",
        "outfit": "purple turtleneck, dark trousers, white gloves",
        "eyes": "half-lidded bored green eyes, thin pupils, permanent smirk",
        "ears": "long floppy rabbit ears, pink inner, purple outer",
        "tail": "fluffy white pom-pom tail",
        "abilities": {
            "GASLIGHTING":     {"active": True,  "desc": "Make others question their reality"},
            "TRICKSTER_TP":    {"active": True,  "desc": "Short-range teleport during pranks"},
            "VOID_IMMUNITY":   {"active": True,  "desc": "The Void does not affect Jax"},
            "SHADOWSTEP":      {"active": True,  "desc": "Merge with shadows to move unseen"},
        },
        "personality": "Sarcastic, manipulative, secretly lonely, uses humour as armour",
        "dialogue": [
            "Oh wow, you actually fell for that.",
            "This is boring. Let's break something.",
            "The Void isn't scary. It's just honest.",
            "I don't need anyone.",
        ],
        "draw_hints": {
            "height_multiplier": 1.4,
            "leg_length": "extra long — 60% of body",
            "ear_length": "tall as body height",
            "posture": "slouched, one hand in pocket",
            "background_effect": "purple shadow tendrils",
        },
    },

    "GANGLE": {
        "name": "Gangle",
        "emoji": "🎭",
        "role": "Marionette / Sad Clown",
        "zone": "The Void",
        "power_level": "MEDIUM (string magic)",
        "colors": {
            "primary":   "#F9A8D4",   # pink
            "secondary": "#93C5FD",   # blue
            "gold_mask":  "#FFD700",
            "blue_mask":  "#1D4ED8",
            "ribbon":    "#EC4899",
            "string":    "#E5E7EB",
            "shadow":    "#4a1330",
        },
        "shape": "marionette doll, cross-bar strings visible above head, floppy limbs",
        "outfit": "pink+blue harlequin costume, ruffled collar, comedy/tragedy masks as face",
        "eyes": "theatre masks — gold comedy and blue tragedy, swapping based on emotion",
        "strings": "visible puppet strings attached to invisible crossbar above",
        "ribbons": "long trailing pink silk ribbons from wrists",
        "abilities": {
            "STRING_TRAP":     {"active": True,  "desc": "Entangle enemies with puppet strings"},
            "MASK_SWAP":       {"active": True,  "desc": "Swap between comedy and tragedy modes"},
            "FLOAT":           {"active": True,  "desc": "Strings can lift her briefly"},
            "CRY_FLOOD":       {"active": True,  "desc": "Tears of sadness temporarily blind enemies"},
        },
        "personality": "Melancholic, gentle, surprisingly resilient, cries easily but forgives fast",
        "dialogue": [
            "I just want someone to understand me.",
            "This mask... it's not really me.",
            "The strings hurt but I'm used to it.",
            "I'm fine. (crying)",
        ],
        "draw_hints": {
            "height_multiplier": 1.0,
            "crossbar_visible": True,
            "string_count": 6,
            "ribbon_trail_length": 2.0,
            "background_effect": "blue melancholy rain",
        },
    },

    "ZOOBLE": {
        "name": "Zooble",
        "emoji": "🧩",
        "role": "Shapeshifter / Grumpy Misfit",
        "zone": "Beach",
        "power_level": "HIGH (body modification)",
        "colors": {
            "primary":   "#34D399",   # green left side
            "secondary": "#F87171",   # red right side
            "eye_left":  "#FBBF24",
            "eye_right": "#FFFFFF",
            "fin":       "#6EE7B7",
            "claw":      "#EF4444",
            "shadow":    "#064e3b",
        },
        "shape": "asymmetric mashup body — different parts from different toys",
        "body": "left half green rounded, right half red angular, mismatched",
        "eyes": "one yellow star eye, one white dot eye — different sizes",
        "limbs": "one flipper left, one claw right, one stubby leg, one wheel",
        "accessories": "small antennae, a tiny tail, a patch on the chest",
        "abilities": {
            "BODY_SWAP":       {"active": True,  "desc": "Detach and reattach body parts at will"},
            "SHAPEMELD":       {"active": True,  "desc": "Absorb shapes from environment"},
            "SPIN_WHEEL":      {"active": True,  "desc": "Wheel form for fast movement"},
            "CLAW_GRAB":       {"active": True,  "desc": "Powerful grip with giant claw"},
        },
        "personality": "Grumpy, dry wit, deeply uncomfortable with emotion, secretly caring",
        "dialogue": [
            "No.",
            "I didn't ask to be made like this.",
            "Leave me alone. ...Fine, you can stay.",
            "This place is stupid and so are all of you.",
        ],
        "draw_hints": {
            "height_multiplier": 0.85,
            "body_asymmetry": True,
            "limbs": ["flipper_L", "claw_R", "stubby_leg", "wheel"],
            "background_effect": "sandy beach glow",
        },
    },

    "KINGER": {
        "name": "Kinger",
        "emoji": "♔",
        "role": "Chess King / Paranoid Veteran",
        "zone": "Fairground",
        "power_level": "MEDIUM-HIGH (chess tactics)",
        "colors": {
            "primary":   "#F59E0B",   # gold chess piece
            "secondary": "#DC2626",   # red cross
            "accent":    "#FEF3C7",
            "crown":     "#FFD700",
            "sweat":     "#93C5FD",
            "shadow":    "#451a03",
        },
        "shape": "chess king piece head on humanoid body, ornate cross on crown",
        "head": "chess king piece shape — large, rounded with cross finial",
        "body": "regally dressed but visibly trembling, white gloves gripping nothing",
        "crown": "integrated into head shape — part of chess piece anatomy",
        "extras": "sweat drops perpetually flying off, wide terrified eyes in visor slot",
        "abilities": {
            "CHESS_TACTICS":   {"active": True,  "desc": "Predict any opponent move 5 steps ahead"},
            "ROYAL_GUARD":     {"active": True,  "desc": "Summon chess piece minions"},
            "PANIC_BURST":     {"active": True,  "desc": "Terror aura temporarily paralyzes enemies"},
            "VETERAN_MEMORY":  {"active": True,  "desc": "Remembers ALL Digital Circus history"},
        },
        "personality": "Extremely paranoid, wise beyond belief, mutters to himself, was here longest",
        "dialogue": [
            "They're watching us. They're ALWAYS watching.",
            "I've seen things you wouldn't believe.",
            "THE ANTS ARE BACK.",
            "Forty seven years... give or take.",
            "Do NOT touch the walls.",
        ],
        "draw_hints": {
            "height_multiplier": 1.1,
            "chess_head_size": "large, 50% of total height",
            "sweat_drop_count": 4,
            "trembling": True,
            "background_effect": "golden chess board glow",
        },
    },

    "BUBBLE": {
        "name": "Bubble",
        "emoji": "🫧",
        "role": "Floating Sphere / Mysterious Being",
        "zone": "Circus Tent",
        "power_level": "UNKNOWN",
        "colors": {
            "primary":   "#BAE6FD",   # light blue
            "secondary": "#E0F2FE",
            "shimmer1":  "#A78BFA",
            "shimmer2":  "#34D399",
            "shimmer3":  "#FB923C",
            "shadow":    "#0c4a6e",
            "glow":      "#7DD3FC",
        },
        "shape": "perfect sphere, translucent, iridescent surface",
        "surface": "rainbow shimmer, reflects environment, slightly wobbly",
        "face": "minimalist — two tiny dots for eyes, tiny curved line mouth",
        "extras": "shadow beneath always present, soft bobbing animation",
        "abilities": {
            "FLOAT":           {"active": True,  "desc": "Permanently hovering, never touches ground"},
            "PHASE":           {"active": True,  "desc": "Pass through any surface"},
            "REFLECT":         {"active": True,  "desc": "Mirror any ability used against it"},
            "MYSTERY":         {"active": True,  "desc": "True nature unknown — possibly ancient AI"},
        },
        "personality": "Cheerful, cryptic, speaks in short poetic phrases, knows more than it lets on",
        "dialogue": [
            "Bubble!",
            "Bubble bubble bubble.",
            "...",
            "Bubble? Bubble.",
            "🫧",
        ],
        "draw_hints": {
            "height_multiplier": 0.7,
            "sphere_translucency": 0.6,
            "shimmer_bands": 3,
            "bobbing": True,
            "background_effect": "soft cyan aura glow",
        },
    },
}

# ══════════════════════════════════════════════════════════════
#  🌍 WORLD ZONES — All 7 zones fully defined
# ══════════════════════════════════════════════════════════════

world_zones = {
    "THE_VOID": {
        "name": "The Void",
        "emoji": "🌑",
        "color": "#0D001A",
        "accent": "#7C3AED",
        "mood": "eerie, glitchy, endless",
        "sky": "pure black with purple pixel grid dissolving at edges",
        "ground": "broken purple geometry, floating debris, glitch triangles",
        "lighting": "deep purple strobe, no natural light source",
        "hazards": ["reality_dissolve", "memory_loss", "infinite_fall"],
        "residents": ["JAX", "GANGLE"],
        "atmosphere": "Where broken characters go. Time loops. Reality frays.",
        "music": "distorted circus music, low drone, static bursts",
        "draw_hints": {
            "bg_color": "#0D001A",
            "grid_color": "#7C3AED",
            "glitch_debris": True,
            "floating_shapes": ["triangle", "square", "broken_polygon"],
        }
    },
    "MOON": {
        "name": "Moon",
        "emoji": "🌙",
        "color": "#1E293B",
        "accent": "#CBD5E1",
        "mood": "silent, vast, lonely",
        "sky": "black with stars, Earth visible large in distance",
        "ground": "grey crater-pocked lunar surface, dust clouds on steps",
        "lighting": "harsh white from Earth-glow, sharp shadows",
        "hazards": ["low_gravity", "vacuum", "cosmic_radiation"],
        "residents": ["POMNI"],
        "atmosphere": "Empty silence. Footprints never fade. Stars never move.",
        "music": "ambient space hum, distant echoes, silence between beats",
        "draw_hints": {
            "bg_color": "#0a0a1a",
            "crater_count": 8,
            "earth_in_sky": True,
            "star_count": 200,
            "dust_particles": True,
        }
    },
    "SUN_ZONE": {
        "name": "Sun Zone",
        "emoji": "☀",
        "color": "#7C2D12",
        "accent": "#F97316",
        "mood": "blazing, overwhelming, dangerous",
        "sky": "deep orange-red, sun corona visible at top, heat shimmer",
        "ground": "cracked lava rock, orange pools, smouldering debris",
        "lighting": "blinding white-yellow, everything washed out at peaks",
        "hazards": ["extreme_heat", "lava_cracks", "solar_flares"],
        "residents": ["KINGER"],
        "atmosphere": "Impossibly hot. Gold melts. Only Kinger somehow survives.",
        "music": "intense brass, fast percussion, crackling fire ambience",
        "draw_hints": {
            "bg_color": "#3d0c00",
            "lava_crack_count": 6,
            "sun_corona_rays": 24,
            "heat_shimmer": True,
        }
    },
    "BEACH": {
        "name": "Beach",
        "emoji": "🏖",
        "color": "#0891B2",
        "accent": "#FCD34D",
        "mood": "deceptively cheerful, warm, slightly off",
        "sky": "bright turquoise, cotton candy clouds, rainbow",
        "ground": "golden sand with sparkles, gentle ocean waves, tide pools",
        "lighting": "warm golden afternoon sun, long shadows",
        "hazards": ["undertow", "too_perfect", "sharks_in_pixels"],
        "residents": ["ZOOBLE"],
        "atmosphere": "A perfect beach. Too perfect. Something is wrong with the horizon.",
        "music": "steel drums, wave sounds, occasional distorted seagull",
        "draw_hints": {
            "bg_color": "#0c3547",
            "wave_count": 5,
            "palm_trees": 3,
            "sandcastle": True,
            "umbrella": True,
        }
    },
    "FAIRGROUND": {
        "name": "Fairground / Kermis",
        "emoji": "🎡",
        "color": "#7C3AED",
        "accent": "#F59E0B",
        "mood": "festive, chaotic, magical",
        "sky": "deep dusk purple with string lights and fireworks",
        "ground": "trampled grass with sawdust paths, colourful stalls, crowds",
        "lighting": "hundreds of fairy lights, neon signs, spinning ride lights",
        "hazards": ["lost_in_crowd", "rigged_games", "spinning_too_fast"],
        "residents": ["RAGATHA", "KINGER"],
        "atmosphere": "Endless carnival that never closes. The prizes are watching you.",
        "music": "upbeat carousel, calliope organ, crowd noise, popcorn machine",
        "draw_hints": {
            "bg_color": "#1a0030",
            "ferris_wheel": True,
            "carousel": True,
            "stall_count": 4,
            "string_lights": True,
        }
    },
    "CIRCUS_TENT": {
        "name": "The Circus Tent",
        "emoji": "🎪",
        "color": "#991B1B",
        "accent": "#FBBF24",
        "mood": "grand, theatrical, home base",
        "sky": "red and white striped canvas ceiling, spotlights, dust motes",
        "ground": "sawdust ring, red velvet curtains, golden ring border",
        "lighting": "dramatic spotlights, colourful stage lights, footlights",
        "hazards": ["performance_anxiety", "caine_protocols", "curtain_dimension"],
        "residents": ["POMNI", "BUBBLE", "DINO_RAPTOR"],
        "atmosphere": "The main stage. Everything happens here. The show never ends.",
        "music": "grand circus fanfare, drum roll, applause, calliope",
        "draw_hints": {
            "bg_color": "#1a0505",
            "stripe_colors": ["#DC2626", "#FFFFFF"],
            "spotlight_count": 6,
            "gold_ring": True,
            "audience": True,
        }
    },
    "THRONE_ROOM": {
        "name": "Dino Raptor's Throne Room",
        "emoji": "🏰",
        "color": "#1a0030",
        "accent": "#FFD700",
        "mood": "powerful, awe-inspiring, technological",
        "sky": "dark castle vault ceiling with glowing runes etched in gold",
        "ground": "black marble with gold veins, purple power grid lines",
        "lighting": "floating orbs of gold and purple light, RGB PC glow",
        "hazards": ["supreme_leader_present", "reality_rewrite_zone"],
        "residents": ["DINO_RAPTOR"],
        "atmosphere": "The seat of ultimate power. Enter with respect or not at all.",
        "music": "epic orchestral boss theme, deep bass, electric guitar solo",
        "draw_hints": {
            "bg_color": "#05000f",
            "triple_monitor": True,
            "gaming_laptop": True,
            "king_bed": True,
            "throne_of_code": True,
            "power_orbs": 8,
            "wall_runes": True,
        }
    },
}

# ══════════════════════════════════════════════════════════════
#  📦 EXPORT — JSON-ready structure for any external program
# ══════════════════════════════════════════════════════════════

export_data = {
    "version": "3.0",
    "title": "The Amazing Digital Circus",
    "supreme_leader": "DINO_RAPTOR",
    "character_count": len(circus_characters),
    "zone_count": len(world_zones),
    "characters": circus_characters,
    "zones": world_zones,
    "render_spec": {
        "canvas_width": 1920,
        "canvas_height": 1080,
        "background": "#05000f",
        "style": "hand-drawn digital art, bold outlines, flat shading with glow FX",
        "character_scale_base": 100,
        "font": "Fredoka One / Creepster",
    },
    "multiplayer": {
        "max_players_per_room": 16,
        "platforms": ["PC", "PS5", "Browser"],
        "private_room_code_length": 6,
        "supreme_leader_perks": [
            "auto_kick", "zone_lock", "reality_control",
            "see_all_private_rooms", "invincible",
        ],
    },
}

# ── Print full roster ──────────────────────────────────────────
print("=" * 70)
print("  🎪 THE AMAZING DIGITAL CIRCUS — FULL ROSTER v3.0")
print("=" * 70)
for key, c in circus_characters.items():
    leader_tag = " 👑 SUPREME LEADER" if key == "DINO_RAPTOR" else ""
    print(f"\n  {c['emoji']} [{key:<15}]  {c['name']:<16}{leader_tag}")
    print(f"     Role      : {c['role']}")
    print(f"     Zone      : {c['zone']}")
    print(f"     Power     : {c['power_level']}")
    ab = c.get("abilities", {})
    active = [k for k, v in ab.items() if v["active"]]
    print(f"     Abilities : {', '.join(active)}")

print("\n" + "=" * 70)
print("  🌍 WORLD ZONES")
print("=" * 70)
for key, z in world_zones.items():
    residents = ", ".join(z["residents"])
    print(f"  {z['emoji']} {z['name']:<30} residents: {residents}")

print("\n" + "=" * 70)
print(f"  ✅ Export ready — {len(circus_characters)} characters, {len(world_zones)} zones")
print(f"  📋 JSON export: json.dumps(export_data, indent=2)")
print("=" * 70)


import json

# ══════════════════════════════════════════════════════════════════════════════
#  🎪 THE AMAZING DIGITAL CIRCUS — FULL ROSTER v3.0
#  Supreme Leader: DINO RAPTOR | 8 Characters | 7 World Zones
# ══════════════════════════════════════════════════════════════════════════════

circus_characters = {

    "DINO_RAPTOR": {
        "name": "Dino Raptor",
        "emoji": "🐉",
        "role": "Supreme Leader / God-Tier Overlord",
        "zone": "Throne Room",
        "power_level": "BEYOND_MAXIMUM ∞",
        "colors": {
            "primary":   "#FFD700",   # gold armor
            "secondary": "#7C3AED",   # purple aura
            "accent":    "#FF4500",   # lava orange eyes
            "aura":      "#A855F7",   # electric purple
            "shadow":    "#1a0030",
        },
        "shape": "giant raptor-dragon hybrid, bipedal, 3x height of others",
        "outfit": "full gold plate armor, flowing purple cape, king crown with 5 gems",
        "eyes": "glowing lava-orange, vertical slit pupils, backlit",
        "wings": "massive bat-dragon wings, dark purple membrane, gold bone tips",
        "tail": "heavy spiky tail with gold tip",
        "claws": "three-fingered hands, razor gold claws",
        "aura": "swirling gold+purple energy rings orbiting the body",
        "crown": "five-point gold crown with ruby, emerald, sapphire, amethyst, diamond",
        "abilities": {
            "FLY":              {"active": True,  "desc": "Fly freely in any zone at any altitude"},
            "TELEPORT":         {"active": True,  "desc": "Instant TP anywhere in the Digital Circus"},
            "PHASE_WALLS":      {"active": True,  "desc": "Walk/fly through any solid surface"},
            "REALITY_CONTROL":  {"active": True,  "desc": "Reshape the simulation at will"},
            "INVINCIBILITY":    {"active": True,  "desc": "Cannot be harmed by any force"},
            "SUPREME_KICK":     {"active": True,  "desc": "Can kick any player from any room"},
            "ZONE_LOCK":        {"active": True,  "desc": "Lock/unlock any zone instantly"},
            "SUMMON":           {"active": True,  "desc": "Summon any character to current zone"},
            "VOID_CONTROL":     {"active": True,  "desc": "Master of The Void dimension"},
            "TIME_FREEZE":      {"active": True,  "desc": "Freeze time for all others"},
        },
        "personality": "Commanding, fearless, protective of loyal subjects, merciless to threats",
        "dialogue": [
            "I AM THE CIRCUS.",
            "No one leaves without my permission.",
            "The Void answers to ME.",
            "Bow before the Supreme Leader.",
            "Your reality is mine to rewrite.",
        ],
        "draw_hints": {
            "height_multiplier": 3.0,
            "wings_spread_width": 4.0,
            "glow_radius": 80,
            "armor_plates": ["chest", "shoulders", "legs", "arms"],
            "floating_icons": ["✈", "⚡", "👻", "🌍", "⏱", "🔮", "👑"],
            "background_effect": "radial gold-purple aura burst",
        },
    },

    "POMNI": {
        "name": "Pomni",
        "emoji": "🃏",
        "role": "Protagonist / Lost Jester",
        "zone": "Circus Tent",
        "power_level": "LOW (but growing)",
        "colors": {
            "primary":   "#3B82F6",   # blue jester
            "secondary": "#EF4444",   # red details
            "accent":    "#FBBF24",   # gold bells
            "skin":      "#FDDCB0",
            "eye_white": "#FFFFFF",
            "eye_ring":  "#EF4444",
            "shadow":    "#1e3a5f",
        },
        "shape": "short humanoid, round head, large expressive eyes",
        "outfit": "blue+red diamond jester suit, white ruffled collar, pointy hat with gold bells",
        "eyes": "huge terrified circles, red ring irises, perpetually wide open",
        "hat": "two-point jester hat, blue+red diamonds, large gold bell at each tip",
        "abilities": {
            "PANIC_DODGE":     {"active": True,  "desc": "Accidentally dodge attacks in terror"},
            "CARTWHEEL":       {"active": True,  "desc": "Jester tumble movement"},
            "GLITCH_VISION":   {"active": False, "desc": "Occasionally sees through the simulation"},
        },
        "personality": "Anxious, overwhelmed, secretly brave, deeply kind",
        "dialogue": [
            "How do I get out of here?!",
            "This isn't real... right?",
            "I just want to go home.",
            "Okay. Okay. I can do this.",
        ],
        "draw_hints": {
            "height_multiplier": 1.0,
            "eye_size": "enormous — 40% of face",
            "expression": "perpetual terror/confusion",
            "hat_bells": 2,
            "background_effect": "blue spotlight glow",
        },
    },

    "RAGATHA": {
        "name": "Ragatha",
        "emoji": "🧸",
        "role": "Rag Doll / Eternal Optimist",
        "zone": "Fairground",
        "power_level": "MEDIUM",
        "colors": {
            "primary":   "#F472B6",   # pink
            "secondary": "#86EFAC",   # green dress
            "accent":    "#FDE68A",   # yellow yarn hair
            "seam":      "#78716C",
            "button_eye": "#1C1917",
            "cheek":     "#FB7185",
            "shadow":    "#4a1942",
        },
        "shape": "rag doll proportions, slightly lopsided, soft edges, visible seam lines",
        "outfit": "green polka-dot dress with white apron, pink bow in hair, mary-jane shoes",
        "eyes": "large black button eyes, stitched lash lines, rosy embroidered cheeks",
        "hair": "yellow yarn bunches tied with pink ribbons",
        "abilities": {
            "STITCH_REPAIR":   {"active": True,  "desc": "Self-repair torn limbs with magical thread"},
            "POSITIVITY_AURA": {"active": True,  "desc": "Calm nearby panicking characters"},
            "HUG_SHIELD":      {"active": True,  "desc": "Hugs protect both parties from minor hits"},
        },
        "personality": "Bubbly, relentlessly positive, hides her own pain, big sister energy",
        "dialogue": [
            "Everything is going to be fine!",
            "We just need to stay positive!",
            "Has anyone seen my button?",
            "Come on, group hug!",
        ],
        "draw_hints": {
            "height_multiplier": 0.9,
            "seam_lines": ["neck", "wrists", "ankles", "forehead"],
            "yarn_hair_strands": 12,
            "background_effect": "warm pink spotlight",
        },
    },

    "JAX": {
        "name": "Jax",
        "emoji": "🐇",
        "role": "Trickster / Chaos Rabbit",
        "zone": "The Void",
        "power_level": "HIGH (manipulation-based)",
        "colors": {
            "primary":   "#8B5CF6",   # purple
            "secondary": "#C4B5FD",   # lavender
            "accent":    "#10B981",   # green eyes
            "belly":     "#F3E8FF",
            "inner_ear": "#F9A8D4",
            "shadow":    "#2e1065",
        },
        "shape": "tall lanky rabbit, exaggerated long legs, slouched posture, thin arms",
        "outfit": "purple turtleneck, dark trousers, white gloves",
        "eyes": "half-lidded bored green eyes, thin pupils, permanent smirk",
        "ears": "long floppy rabbit ears, pink inner, purple outer",
        "tail": "fluffy white pom-pom tail",
        "abilities": {
            "GASLIGHTING":     {"active": True,  "desc": "Make others question their reality"},
            "TRICKSTER_TP":    {"active": True,  "desc": "Short-range teleport during pranks"},
            "VOID_IMMUNITY":   {"active": True,  "desc": "The Void does not affect Jax"},
            "SHADOWSTEP":      {"active": True,  "desc": "Merge with shadows to move unseen"},
        },
        "personality": "Sarcastic, manipulative, secretly lonely, uses humour as armour",
        "dialogue": [
            "Oh wow, you actually fell for that.",
            "This is boring. Let's break something.",
            "The Void isn't scary. It's just honest.",
            "I don't need anyone.",
        ],
        "draw_hints": {
            "height_multiplier": 1.4,
            "leg_length": "extra long — 60% of body",
            "ear_length": "tall as body height",
            "posture": "slouched, one hand in pocket",
            "background_effect": "purple shadow tendrils",
        },
    },

    "GANGLE": {
        "name": "Gangle",
        "emoji": "🎭",
        "role": "Marionette / Sad Clown",
        "zone": "The Void",
        "power_level": "MEDIUM (string magic)",
        "colors": {
            "primary":   "#F9A8D4",   # pink
            "secondary": "#93C5FD",   # blue
            "gold_mask":  "#FFD700",
            "blue_mask":  "#1D4ED8",
            "ribbon":    "#EC4899",
            "string":    "#E5E7EB",
            "shadow":    "#4a1330",
        },
        "shape": "marionette doll, cross-bar strings visible above head, floppy limbs",
        "outfit": "pink+blue harlequin costume, ruffled collar, comedy/tragedy masks as face",
        "eyes": "theatre masks — gold comedy and blue tragedy, swapping based on emotion",
        "strings": "visible puppet strings attached to invisible crossbar above",
        "ribbons": "long trailing pink silk ribbons from wrists",
        "abilities": {
            "STRING_TRAP":     {"active": True,  "desc": "Entangle enemies with puppet strings"},
            "MASK_SWAP":       {"active": True,  "desc": "Swap between comedy and tragedy modes"},
            "FLOAT":           {"active": True,  "desc": "Strings can lift her briefly"},
            "CRY_FLOOD":       {"active": True,  "desc": "Tears of sadness temporarily blind enemies"},
        },
        "personality": "Melancholic, gentle, surprisingly resilient, cries easily but forgives fast",
        "dialogue": [
            "I just want someone to understand me.",
            "This mask... it's not really me.",
            "The strings hurt but I'm used to it.",
            "I'm fine. (crying)",
        ],
        "draw_hints": {
            "height_multiplier": 1.0,
            "crossbar_visible": True,
            "string_count": 6,
            "ribbon_trail_length": 2.0,
            "background_effect": "blue melancholy rain",
        },
    },

    "ZOOBLE": {
        "name": "Zooble",
        "emoji": "🧩",
        "role": "Shapeshifter / Grumpy Misfit",
        "zone": "Beach",
        "power_level": "HIGH (body modification)",
        "colors": {
            "primary":   "#34D399",   # green left side
            "secondary": "#F87171",   # red right side
            "eye_left":  "#FBBF24",
            "eye_right": "#FFFFFF",
            "fin":       "#6EE7B7",
            "claw":      "#EF4444",
            "shadow":    "#064e3b",
        },
        "shape": "asymmetric mashup body — different parts from different toys",
        "body": "left half green rounded, right half red angular, mismatched",
        "eyes": "one yellow star eye, one white dot eye — different sizes",
        "limbs": "one flipper left, one claw right, one stubby leg, one wheel",
        "accessories": "small antennae, a tiny tail, a patch on the chest",
        "abilities": {
            "BODY_SWAP":       {"active": True,  "desc": "Detach and reattach body parts at will"},
            "SHAPEMELD":       {"active": True,  "desc": "Absorb shapes from environment"},
            "SPIN_WHEEL":      {"active": True,  "desc": "Wheel form for fast movement"},
            "CLAW_GRAB":       {"active": True,  "desc": "Powerful grip with giant claw"},
        },
        "personality": "Grumpy, dry wit, deeply uncomfortable with emotion, secretly caring",
        "dialogue": [
            "No.",
            "I didn't ask to be made like this.",
            "Leave me alone. ...Fine, you can stay.",
            "This place is stupid and so are all of you.",
        ],
        "draw_hints": {
            "height_multiplier": 0.85,
            "body_asymmetry": True,
            "limbs": ["flipper_L", "claw_R", "stubby_leg", "wheel"],
            "background_effect": "sandy beach glow",
        },
    },

    "KINGER": {
        "name": "Kinger",
        "emoji": "♔",
        "role": "Chess King / Paranoid Veteran",
        "zone": "Fairground",
        "power_level": "MEDIUM-HIGH (chess tactics)",
        "colors": {
            "primary":   "#F59E0B",   # gold chess piece
            "secondary": "#DC2626",   # red cross
            "accent":    "#FEF3C7",
            "crown":     "#FFD700",
            "sweat":     "#93C5FD",
            "shadow":    "#451a03",
        },
        "shape": "chess king piece head on humanoid body, ornate cross on crown",
        "head": "chess king piece shape — large, rounded with cross finial",
        "body": "regally dressed but visibly trembling, white gloves gripping nothing",
        "crown": "integrated into head shape — part of chess piece anatomy",
        "extras": "sweat drops perpetually flying off, wide terrified eyes in visor slot",
        "abilities": {
            "CHESS_TACTICS":   {"active": True,  "desc": "Predict any opponent move 5 steps ahead"},
            "ROYAL_GUARD":     {"active": True,  "desc": "Summon chess piece minions"},
            "PANIC_BURST":     {"active": True,  "desc": "Terror aura temporarily paralyzes enemies"},
            "VETERAN_MEMORY":  {"active": True,  "desc": "Remembers ALL Digital Circus history"},
        },
        "personality": "Extremely paranoid, wise beyond belief, mutters to himself, was here longest",
        "dialogue": [
            "They're watching us. They're ALWAYS watching.",
            "I've seen things you wouldn't believe.",
            "THE ANTS ARE BACK.",
            "Forty seven years... give or take.",
            "Do NOT touch the walls.",
        ],
        "draw_hints": {
            "height_multiplier": 1.1,
            "chess_head_size": "large, 50% of total height",
            "sweat_drop_count": 4,
            "trembling": True,
            "background_effect": "golden chess board glow",
        },
    },

    "BUBBLE": {
        "name": "Bubble",
        "emoji": "🫧",
        "role": "Floating Sphere / Mysterious Being",
        "zone": "Circus Tent",
        "power_level": "UNKNOWN",
        "colors": {
            "primary":   "#BAE6FD",   # light blue
            "secondary": "#E0F2FE",
            "shimmer1":  "#A78BFA",
            "shimmer2":  "#34D399",
            "shimmer3":  "#FB923C",
            "shadow":    "#0c4a6e",
            "glow":      "#7DD3FC",
        },
        "shape": "perfect sphere, translucent, iridescent surface",
        "surface": "rainbow shimmer, reflects environment, slightly wobbly",
        "face": "minimalist — two tiny dots for eyes, tiny curved line mouth",
        "extras": "shadow beneath always present, soft bobbing animation",
        "abilities": {
            "FLOAT":           {"active": True,  "desc": "Permanently hovering, never touches ground"},
            "PHASE":           {"active": True,  "desc": "Pass through any surface"},
            "REFLECT":         {"active": True,  "desc": "Mirror any ability used against it"},
            "MYSTERY":         {"active": True,  "desc": "True nature unknown — possibly ancient AI"},
        },
        "personality": "Cheerful, cryptic, speaks in short poetic phrases, knows more than it lets on",
        "dialogue": [
            "Bubble!",
            "Bubble bubble bubble.",
            "...",
            "Bubble? Bubble.",
            "🫧",
        ],
        "draw_hints": {
            "height_multiplier": 0.7,
            "sphere_translucency": 0.6,
            "shimmer_bands": 3,
            "bobbing": True,
            "background_effect": "soft cyan aura glow",
        },
    },
}

# ══════════════════════════════════════════════════════════════
#  🌍 WORLD ZONES — All 7 zones fully defined
# ══════════════════════════════════════════════════════════════

world_zones = {
    "THE_VOID": {
        "name": "The Void",
        "emoji": "🌑",
        "color": "#0D001A",
        "accent": "#7C3AED",
        "mood": "eerie, glitchy, endless",
        "sky": "pure black with purple pixel grid dissolving at edges",
        "ground": "broken purple geometry, floating debris, glitch triangles",
        "lighting": "deep purple strobe, no natural light source",
        "hazards": ["reality_dissolve", "memory_loss", "infinite_fall"],
        "residents": ["JAX", "GANGLE"],
        "atmosphere": "Where broken characters go. Time loops. Reality frays.",
        "music": "distorted circus music, low drone, static bursts",
        "draw_hints": {
            "bg_color": "#0D001A",
            "grid_color": "#7C3AED",
            "glitch_debris": True,
            "floating_shapes": ["triangle", "square", "broken_polygon"],
        }
    },
    "MOON": {
        "name": "Moon",
        "emoji": "🌙",
        "color": "#1E293B",
        "accent": "#CBD5E1",
        "mood": "silent, vast, lonely",
        "sky": "black with stars, Earth visible large in distance",
        "ground": "grey crater-pocked lunar surface, dust clouds on steps",
        "lighting": "harsh white from Earth-glow, sharp shadows",
        "hazards": ["low_gravity", "vacuum", "cosmic_radiation"],
        "residents": ["POMNI"],
        "atmosphere": "Empty silence. Footprints never fade. Stars never move.",
        "music": "ambient space hum, distant echoes, silence between beats",
        "draw_hints": {
            "bg_color": "#0a0a1a",
            "crater_count": 8,
            "earth_in_sky": True,
            "star_count": 200,
            "dust_particles": True,
        }
    },
    "SUN_ZONE": {
        "name": "Sun Zone",
        "emoji": "☀",
        "color": "#7C2D12",
        "accent": "#F97316",
        "mood": "blazing, overwhelming, dangerous",
        "sky": "deep orange-red, sun corona visible at top, heat shimmer",
        "ground": "cracked lava rock, orange pools, smouldering debris",
        "lighting": "blinding white-yellow, everything washed out at peaks",
        "hazards": ["extreme_heat", "lava_cracks", "solar_flares"],
        "residents": ["KINGER"],
        "atmosphere": "Impossibly hot. Gold melts. Only Kinger somehow survives.",
        "music": "intense brass, fast percussion, crackling fire ambience",
        "draw_hints": {
            "bg_color": "#3d0c00",
            "lava_crack_count": 6,
            "sun_corona_rays": 24,
            "heat_shimmer": True,
        }
    },
    "BEACH": {
        "name": "Beach",
        "emoji": "🏖",
        "color": "#0891B2",
        "accent": "#FCD34D",
        "mood": "deceptively cheerful, warm, slightly off",
        "sky": "bright turquoise, cotton candy clouds, rainbow",
        "ground": "golden sand with sparkles, gentle ocean waves, tide pools",
        "lighting": "warm golden afternoon sun, long shadows",
        "hazards": ["undertow", "too_perfect", "sharks_in_pixels"],
        "residents": ["ZOOBLE"],
        "atmosphere": "A perfect beach. Too perfect. Something is wrong with the horizon.",
        "music": "steel drums, wave sounds, occasional distorted seagull",
        "draw_hints": {
            "bg_color": "#0c3547",
            "wave_count": 5,
            "palm_trees": 3,
            "sandcastle": True,
            "umbrella": True,
        }
    },
    "FAIRGROUND": {
        "name": "Fairground / Kermis",
        "emoji": "🎡",
        "color": "#7C3AED",
        "accent": "#F59E0B",
        "mood": "festive, chaotic, magical",
        "sky": "deep dusk purple with string lights and fireworks",
        "ground": "trampled grass with sawdust paths, colourful stalls, crowds",
        "lighting": "hundreds of fairy lights, neon signs, spinning ride lights",
        "hazards": ["lost_in_crowd", "rigged_games", "spinning_too_fast"],
        "residents": ["RAGATHA", "KINGER"],
        "atmosphere": "Endless carnival that never closes. The prizes are watching you.",
        "music": "upbeat carousel, calliope organ, crowd noise, popcorn machine",
        "draw_hints": {
            "bg_color": "#1a0030",
            "ferris_wheel": True,
            "carousel": True,
            "stall_count": 4,
            "string_lights": True,
        }
    },
    "CIRCUS_TENT": {
        "name": "The Circus Tent",
        "emoji": "🎪",
        "color": "#991B1B",
        "accent": "#FBBF24",
        "mood": "grand, theatrical, home base",
        "sky": "red and white striped canvas ceiling, spotlights, dust motes",
        "ground": "sawdust ring, red velvet curtains, golden ring border",
        "lighting": "dramatic spotlights, colourful stage lights, footlights",
        "hazards": ["performance_anxiety", "caine_protocols", "curtain_dimension"],
        "residents": ["POMNI", "BUBBLE", "DINO_RAPTOR"],
        "atmosphere": "The main stage. Everything happens here. The show never ends.",
        "music": "grand circus fanfare, drum roll, applause, calliope",
        "draw_hints": {
            "bg_color": "#1a0505",
            "stripe_colors": ["#DC2626", "#FFFFFF"],
            "spotlight_count": 6,
            "gold_ring": True,
            "audience": True,
        }
    },
    "THRONE_ROOM": {
        "name": "Dino Raptor's Throne Room",
        "emoji": "🏰",
        "color": "#1a0030",
        "accent": "#FFD700",
        "mood": "powerful, awe-inspiring, technological",
        "sky": "dark castle vault ceiling with glowing runes etched in gold",
        "ground": "black marble with gold veins, purple power grid lines",
        "lighting": "floating orbs of gold and purple light, RGB PC glow",
        "hazards": ["supreme_leader_present", "reality_rewrite_zone"],
        "residents": ["DINO_RAPTOR"],
        "atmosphere": "The seat of ultimate power. Enter with respect or not at all.",
        "music": "epic orchestral boss theme, deep bass, electric guitar solo",
        "draw_hints": {
            "bg_color": "#05000f",
            "triple_monitor": True,
            "gaming_laptop": True,
            "king_bed": True,
            "throne_of_code": True,
            "power_orbs": 8,
            "wall_runes": True,
        }
    },
}

# ══════════════════════════════════════════════════════════════
#  📦 EXPORT — JSON-ready structure for any external program
# ══════════════════════════════════════════════════════════════

export_data = {
    "version": "3.0",
    "title": "The Amazing Digital Circus",
    "supreme_leader": "DINO_RAPTOR",
    "character_count": len(circus_characters),
    "zone_count": len(world_zones),
    "characters": circus_characters,
    "zones": world_zones,
    "render_spec": {
        "canvas_width": 1920,
        "canvas_height": 1080,
        "background": "#05000f",
        "style": "hand-drawn digital art, bold outlines, flat shading with glow FX",
        "character_scale_base": 100,
        "font": "Fredoka One / Creepster",
    },
    "multiplayer": {
        "max_players_per_room": 16,
        "platforms": ["PC", "PS5", "Browser"],
        "private_room_code_length": 6,
        "supreme_leader_perks": [
            "auto_kick", "zone_lock", "reality_control",
            "see_all_private_rooms", "invincible",
        ],
    },
}

# ── Print full roster ──────────────────────────────────────────
print("=" * 70)
print("  🎪 THE AMAZING DIGITAL CIRCUS — FULL ROSTER v3.0")
print("=" * 70)
for key, c in circus_characters.items():
    leader_tag = " 👑 SUPREME LEADER" if key == "DINO_RAPTOR" else ""
    print(f"\n  {c['emoji']} [{key:<15}]  {c['name']:<16}{leader_tag}")
    print(f"     Role      : {c['role']}")
    print(f"     Zone      : {c['zone']}")
    print(f"     Power     : {c['power_level']}")
    ab = c.get("abilities", {})
    active = [k for k, v in ab.items() if v["active"]]
    print(f"     Abilities : {', '.join(active)}")

print("\n" + "=" * 70)
print("  🌍 WORLD ZONES")
print("=" * 70)
for key, z in world_zones.items():
    residents = ", ".join(z["residents"])
    print(f"  {z['emoji']} {z['name']:<30} residents: {residents}")

print("\n" + "=" * 70)
print(f"  ✅ Export ready — {len(circus_characters)} characters, {len(world_zones)} zones")
print(f"  📋 JSON export: json.dumps(export_data, indent=2)")
print("=" * 70)


import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Wedge, Arc
import numpy as np

rng = np.random.default_rng(42)

circus_world_fig, ax = plt.subplots(1, 1, figsize=(28, 10))
circus_world_fig.patch.set_facecolor('#05000f')
ax.set_facecolor('#05000f')
ax.set_xlim(0, 7); ax.set_ylim(0, 2.5)
ax.set_xticks([]); ax.set_yticks([])
for sp in ax.spines.values(): sp.set_visible(False)

# ── Zone widths (x_start, width) ──────────────────────────────
ZONES = {
    'VOID':       (0.00, 1.00),
    'MOON':       (1.00, 1.00),
    'SUN':        (2.00, 1.00),
    'BEACH':      (3.00, 1.00),
    'FAIR':       (4.00, 1.00),
    'TENT':       (5.00, 1.00),
    'THRONE':     (6.00, 1.00),
}

# ── helpers ────────────────────────────────────────────────────
def C(cx,cy,r,color='#FFFFFF',**kw): ax.add_patch(Circle((cx,cy),r,facecolor=color,**kw))
def E(cx,cy,w,h,color='#FFFFFF',**kw): ax.add_patch(Ellipse((cx,cy),w,h,facecolor=color,**kw))
def R(x,y,w,h,fc,ec='none',lw=0,zorder=4,alpha=1.0):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='square,pad=0',
                                facecolor=fc,edgecolor=ec,linewidth=lw,zorder=zorder,alpha=alpha))
def P(pts,**kw): ax.add_patch(plt.Polygon(pts,**kw))
def T(x,y,s,**kw): ax.text(x,y,s,ha='center',va='center',**kw)

# ══════════════════════════════════════════════════════════════
# 1. THE VOID
# ══════════════════════════════════════════════════════════════
vx,vw=0.00,1.00
R(vx,0,vw,2.5,'#0D001A',zorder=2)
# glitch grid
for gx in np.arange(vx,vx+vw,0.06):
    ax.plot([gx,gx],[0,2.5],color='#7C3AED',alpha=0.12,lw=0.5,zorder=3)
for gy in np.arange(0,2.5,0.06):
    ax.plot([vx,vx+vw],[gy,gy],color='#7C3AED',alpha=0.12,lw=0.5,zorder=3)
# glitch debris triangles
for _ in range(18):
    gx2=vx+rng.uniform(0.02,0.96); gy2=rng.uniform(0.1,2.3)
    gs=rng.uniform(0.02,0.08)
    gc=['#7C3AED','#A855F7','#4C1D95','#FF4500'][rng.integers(4)]
    P([[gx2,gy2],[gx2+gs,gy2+gs*0.8],[gx2-gs*0.4,gy2+gs]],
      color=gc,alpha=rng.uniform(0.3,0.9),zorder=4)
# floating squares
for _ in range(8):
    gx3=vx+rng.uniform(0.05,0.90); gy3=rng.uniform(0.1,2.2); gs2=rng.uniform(0.02,0.06)
    R(gx3,gy3,gs2,gs2,'none','#7C3AED',1.2,5,alpha=0.6)
# JAX silhouette
jx=0.22
R(jx-0.04,0.04,0.08,0.28,'#8B5CF6',zorder=6)  # body
C(jx,0.55,0.10,'#8B5CF6',zorder=6)  # head
E(jx-0.06,0.80,0.06,0.22,'#8B5CF6',zorder=6)  # ear L
E(jx+0.06,0.80,0.06,0.22,'#8B5CF6',zorder=6)  # ear R
ax.plot([jx-0.04,jx-0.12],[0.28,0.12],color='#8B5CF6',lw=4,zorder=6)  # arm L
ax.plot([jx+0.04,jx+0.12],[0.28,0.12],color='#8B5CF6',lw=4,zorder=6)  # arm R
# Jax speech
T(jx,1.05,'boring...',color='#A78BFA',fontsize=5,zorder=8,style='italic')
# GANGLE silhouette
gx2=0.75
C(gx2,0.55,0.09,'#F9A8D4',zorder=6)
R(gx2-0.04,0.10,0.08,0.40,'#F9A8D4',zorder=6)
# strings
for sx in [gx2-0.06,gx2,gx2+0.06]:
    ax.plot([sx,sx+0.01],[2.35,0.64],color='#E5E7EB',lw=0.8,alpha=0.7,zorder=5)
ax.plot([gx2-0.14,gx2+0.14],[2.35,2.35],color='#8B4513',lw=3,zorder=5)
# ribbon trails
for ri in range(4):
    ax.plot([gx2-0.10,gx2-0.14+ri*0.01],[0.30-ri*0.06,0.10-ri*0.05],color='#EC4899',alpha=0.6,lw=2,zorder=5)
# VOID label
T(vx+vw/2,2.42,'⚫ THE VOID',color='#A855F7',fontsize=6.5,fontweight='bold',zorder=9)

# ══════════════════════════════════════════════════════════════
# 2. MOON
# ══════════════════════════════════════════════════════════════
mx,mw=1.00,1.00
R(mx,0,mw,2.5,'#0a0a1a',zorder=2)
# stars
for _ in range(120):
    sx=mx+rng.uniform(0,mw); sy=rng.uniform(0.3,2.5)
    ax.plot(sx,sy,'.',color='#FFFFFF',ms=rng.uniform(0.5,2.5),alpha=rng.uniform(0.4,1.0),zorder=3)
# Earth
C(mx+0.80,2.22,0.14,color='#1D4ED8',zorder=4)
C(mx+0.80,2.22,0.14,color='none',lw=1,edgecolor='#93C5FD',zorder=5)
E(mx+0.78,2.26,0.07,0.05,color='#166534',alpha=0.7,zorder=5)
E(mx+0.84,2.18,0.04,0.05,color='#166534',alpha=0.7,zorder=5)
# moon surface
moon_surface_x=np.linspace(mx,mx+mw,100)
moon_surface_y=0.35+0.03*np.sin(moon_surface_x*15)+0.02*np.cos(moon_surface_x*22)
ax.fill_between(moon_surface_x,moon_surface_y,0,color='#94A3B8',zorder=4)
# craters
for cx2,cy2,cr2 in [(mx+0.18,0.52,0.06),(mx+0.55,0.44,0.04),(mx+0.78,0.62,0.05),(mx+0.35,0.72,0.03),(mx+0.65,0.80,0.02)]:
    C(cx2,cy2,cr2,color='#64748B',zorder=5)
    C(cx2,cy2,cr2,color='none',edgecolor='#475569',lw=1,zorder=6)
# POMNI on moon
px=mx+0.35; py=0.38
C(px,py+0.20,0.075,color='#FDDCB0',zorder=8)  # head
R(px-0.04,py+0.04,0.08,0.16,'#2563EB',zorder=8)  # body
# huge terror eyes
C(px-0.022,py+0.22,0.032,color='#FFFFFF',zorder=9)
C(px+0.022,py+0.22,0.032,color='#FFFFFF',zorder=9)
C(px-0.022,py+0.22,0.018,color='#EF4444',zorder=10)
C(px+0.022,py+0.22,0.018,color='#EF4444',zorder=10)
# jester hat
P([[px-0.04,py+0.29],[px+0.04,py+0.29],[px+0.01,py+0.40],[px-0.01,py+0.40]],color='#2563EB',zorder=9)
C(px,py+0.40,0.012,color='#FFD700',zorder=10)
T(px,py+0.56,'???',color='#93C5FD',fontsize=5,style='italic',zorder=11)
# dust footprints
for fi in range(4):
    ax.plot(px-0.12+fi*0.06,py+0.01,'.',color='#94A3B8',ms=3,zorder=7)
T(mx+mw/2,2.42,'🌙 MOON',color='#CBD5E1',fontsize=6.5,fontweight='bold',zorder=9)

# ══════════════════════════════════════════════════════════════
# 3. SUN ZONE
# ══════════════════════════════════════════════════════════════
sx2,sw2=2.00,1.00
R(sx2,0,sw2,2.5,'#3d0c00',zorder=2)
# heat gradient
for hi in range(8):
    R(sx2,hi*0.31,sw2,0.32,'#7C2D12',zorder=2,alpha=0.08*(8-hi))
# lava cracks
for _ in range(7):
    lx=sx2+rng.uniform(0.05,0.92); pts=[(lx,0)]
    for _ in range(8):
        pts.append((pts[-1][0]+rng.uniform(-0.04,0.04),pts[-1][1]+rng.uniform(0.04,0.12)))
    ax.plot([p[0] for p in pts],[p[1] for p in pts],color='#F97316',lw=1.5,alpha=0.7,zorder=4)
    ax.plot([p[0] for p in pts],[p[1] for p in pts],color='#FCD34D',lw=0.5,alpha=0.5,zorder=5)
# sun corona at top
C(sx2+0.50,2.60,0.40,color='#FCD34D',alpha=0.15,zorder=3)
C(sx2+0.50,2.60,0.28,color='#F59E0B',alpha=0.25,zorder=3)
for ra in range(0,360,15):
    ex2=sx2+0.50+0.55*np.cos(np.radians(ra)); ey2=2.60+0.55*np.sin(np.radians(ra))
    ax.plot([sx2+0.50,ex2],[2.60,ey2],color='#FCD34D',alpha=0.4,lw=1.5,zorder=3)
# heat shimmer lines
for shi in range(5):
    shx=sx2+0.10+shi*0.18
    ax.plot([shx,shx+0.04,shx,shx+0.04],[0.5,1.0,1.5,2.0],color='#F97316',alpha=0.2,lw=1,zorder=4)
# KINGER sweating in sun
kx=sx2+0.45; ky=0.35
R(kx-0.04,ky+0.02,0.08,0.18,'#F59E0B',zorder=8)   # body
C(kx,ky+0.34,0.10,color='#F59E0B',zorder=8)          # chess head
R(kx-0.07,ky+0.28,0.14,0.04,'#1C1917',zorder=9)     # visor
C(kx-0.025,ky+0.30,0.016,color='#F97316',zorder=10)
C(kx+0.025,ky+0.30,0.016,color='#F97316',zorder=10)
ax.plot([kx,kx],[ky+0.44,ky+0.54],color='#DC2626',lw=4,zorder=9)   # cross up
ax.plot([kx-0.04,kx+0.04],[ky+0.49,ky+0.49],color='#DC2626',lw=4,zorder=9)
for swx,swy in [(kx-0.12,ky+0.40),(kx-0.14,ky+0.33),(kx+0.12,ky+0.38),(kx+0.14,ky+0.30),(kx,ky+0.58)]:
    C(swx,swy,0.010,color='#93C5FD',alpha=0.9,zorder=11)
T(kx+0.18,ky+0.44,'HOT!!',color='#FCD34D',fontsize=5,style='italic',zorder=11)
T(sx2+sw2/2,2.42,'☀ SUN ZONE',color='#F97316',fontsize=6.5,fontweight='bold',zorder=9)

# ══════════════════════════════════════════════════════════════
# 4. BEACH
# ══════════════════════════════════════════════════════════════
bx2,bw2=3.00,1.00
# sky
R(bx2,0.70,bw2,1.80,'#0891B2',zorder=2)
# sand
R(bx2,0,bw2,0.72,'#FCD34D',zorder=3,alpha=0.9)
# sparkles in sand
for _ in range(20):
    ax.plot(bx2+rng.uniform(0.02,0.97),rng.uniform(0.02,0.68),'.',color='#FFFFFF',ms=1.5,alpha=0.5,zorder=4)
# ocean waves
for wi in range(5):
    wy=0.70+wi*0.06
    wave_x=np.linspace(bx2,bx2+bw2,80)
    wave_y=wy+0.02*np.sin(wave_x*18+wi*1.2)
    ax.plot(wave_x,wave_y,color=['#67E8F9','#22D3EE','#06B6D4','#0891B2','#0E7490'][wi],lw=1.5,alpha=0.8,zorder=3)
ax.fill_between(np.linspace(bx2,bx2+bw2,80),0.70,0.72+0.02*np.sin(np.linspace(bx2,bx2+bw2,80)*18),color='#0891B2',alpha=0.3,zorder=3)
# palm trees
for plx,ply,ph in [(bx2+0.12,0.72,0.42),(bx2+0.85,0.72,0.38)]:
    ax.plot([plx,plx+0.02],[ply,ply+ph],color='#92400E',lw=4,zorder=5)
    for la in [-40,-20,0,20,40,60]:
        lax=plx+0.02+0.18*np.cos(np.radians(la+100)); lay=ply+ph+0.18*np.sin(np.radians(la+100))
        ax.plot([plx+0.02,lax],[ply+ph,lay],color='#166534',lw=3,alpha=0.9,zorder=5)
    C(plx+0.02,ply+ph+0.04,0.04,color='#92400E',zorder=6)
# parasol
E(bx2+0.58,1.08,0.24,0.12,color='#F87171',alpha=0.9,zorder=5)
ax.plot([bx2+0.58,bx2+0.58],[0.72,1.08],color='#1C1917',lw=1.5,zorder=5)
# sandcastle
R(bx2+0.62,0.72,0.10,0.08,'#F59E0B',zorder=5)
P([[bx2+0.62,0.80],[bx2+0.67,0.87],[bx2+0.72,0.80]],color='#F59E0B',zorder=5)
R(bx2+0.56,0.72,0.06,0.06,'#F59E0B',zorder=5)
# ZOOBLE on beach
zbx=bx2+0.38; zby=0.68
C(zbx,zby+0.18,0.09,color='#34D399',zorder=8)
ax.add_patch(Wedge((zbx,zby+0.18),0.09,270,90,color='#F87171',zorder=9))
ax.plot([zbx,zbx],[zby+0.27,zby+0.36],color='#1C1917',lw=1,zorder=10)
C(zbx-0.025,zby+0.20,0.020,color='#FBBF24',zorder=10)
C(zbx+0.025,zby+0.20,0.020,color='#FFFFFF',zorder=10)
R(zbx-0.04,zby+0.02,0.08,0.16,'#34D399',zorder=8)
# flipper in water
E(zbx-0.10,zby+0.10,0.06,0.04,color='#6EE7B7',zorder=8)
T(zbx+0.02,zby+0.42,'No.',color='#34D399',fontsize=5,style='italic',zorder=11)
# rainbow in sky
for ri,rc2 in enumerate(['#EF4444','#F97316','#FBBF24','#22C55E','#3B82F6','#7C3AED']):
    ax.add_patch(Arc((bx2+0.5,0.72),0.60+ri*0.06,0.50+ri*0.06,angle=0,theta1=0,theta2=180,color=rc2,lw=1.5,alpha=0.6,zorder=4))
T(bx2+bw2/2,2.42,'🏖 BEACH',color='#FCD34D',fontsize=6.5,fontweight='bold',zorder=9)

# ══════════════════════════════════════════════════════════════
# 5. FAIRGROUND / KERMIS
# ══════════════════════════════════════════════════════════════
fx2,fw2=4.00,1.00
R(fx2,0,fw2,2.5,'#1a0030',zorder=2)
# dusk sky gradient
for fi in range(6):
    R(fx2,fi*0.42,fw2,0.44,'#3B0764',zorder=2,alpha=0.06*(6-fi))
# string lights
for li in range(12):
    lx2=fx2+li*(fw2/11)
    ax.plot([lx2,lx2+fw2/22],[2.32,2.22],color=['#FFD700','#FF69B4','#7DD3FC','#86EFAC'][li%4],lw=1.5,alpha=0.9,zorder=5)
    C(lx2,2.32,0.012,color=['#FFD700','#FF69B4','#7DD3FC','#86EFAC'][li%4],zorder=6)
# FERRIS WHEEL
fw_cx=fx2+0.25; fw_cy=1.30; fw_r=0.52
C(fw_cx,fw_cy,fw_r,color='none',edgecolor='#F59E0B',lw=3,zorder=5)
for sp_a in range(0,360,30):
    ax.plot([fw_cx,fw_cx+fw_r*np.cos(np.radians(sp_a))],
            [fw_cy,fw_cy+fw_r*np.sin(np.radians(sp_a))],color='#F59E0B',lw=1,alpha=0.7,zorder=4)
for gc_a in range(0,360,45):
    gcx=fw_cx+fw_r*0.88*np.cos(np.radians(gc_a))
    gcy=fw_cy+fw_r*0.88*np.sin(np.radians(gc_a))
    R(gcx-0.04,gcy-0.04,0.08,0.08,['#EF4444','#3B82F6','#F59E0B','#10B981'][gc_a//90%4],zorder=6)
ax.plot([fw_cx,fw_cx],[fw_cy-fw_r,0],color='#B8860B',lw=5,zorder=4)
# CAROUSEL
ca_cx=fx2+0.75; ca_cy=0.22; ca_r=0.18
R(ca_cx-ca_r,ca_cy,ca_r*2,0.12,'#A855F7',zorder=5)
E(ca_cx,ca_cy+0.12,ca_r*2,0.10,color='#F9A8D4',zorder=6)
for pa in range(0,360,72):
    hx2=ca_cx+ca_r*0.75*np.cos(np.radians(pa)); hy2=ca_cy+0.14
    ax.plot([hx2,hx2],[ca_cy,hy2],color='#FBBF24',lw=1.5,zorder=7)
    C(hx2,hy2+0.04,0.03,color=['#F87171','#93C5FD','#86EFAC','#FCD34D','#F9A8D4'][pa//72%5],zorder=8)
ax.plot([ca_cx,ca_cx],[ca_cy+0.18,ca_cy+0.48],color='#FBBF24',lw=3,zorder=5)
# STALLS
for st_i,(st_x,st_col,st_name) in enumerate([(fx2+0.52,0.24,'COTTON'),(fx2+0.65,0.36,'GAME')]):
    R(st_x-0.05,0.04,0.14,0.22,['#EF4444','#3B82F6'][st_i],zorder=5)
    P([[st_x-0.06,0.26],[st_x+0.10,0.26],[st_x+0.10,0.34],[st_x-0.06,0.34]],
      color=['#FCD34D','#F9A8D4'][st_i],alpha=0.8,zorder=6)
# RAGATHA at fairground
rgx=fx2+0.52; rgy=0.26
C(rgx,rgy+0.18,0.075,color='#FDE8D0',zorder=8)
R(rgx-0.035,rgy+0.04,0.07,0.14,'#86EFAC',zorder=8)
C(rgx-0.018,rgy+0.20,0.024,color='#1C1917',zorder=9)
C(rgx+0.018,rgy+0.20,0.024,color='#1C1917',zorder=9)
ax.add_patch(Arc((rgx,rgy+0.14),0.06,0.04,angle=0,theta1=200,theta2=340,color='#78716C',lw=1.5,zorder=10))
for yi2,yc2 in enumerate(np.linspace(rgx-0.04,rgx+0.04,5)):
    ax.plot([yc2,yc2+0.005],[rgy+0.25,rgy+0.31+0.01*np.sin(yi2)],color='#FDE68A',lw=2,zorder=10)
T(rgx,rgy+0.42,'Yay!',color='#F472B6',fontsize=5,style='italic',zorder=11)
# fireworks in sky
for fw_i in range(5):
    fwx=fx2+rng.uniform(0.05,0.95); fwy=rng.uniform(1.8,2.35)
    fwc=['#FFD700','#F472B6','#7DD3FC','#86EFAC','#FB923C'][fw_i%5]
    for fwa in range(0,360,36):
        ax.plot([fwx,fwx+0.06*np.cos(np.radians(fwa))],[fwy,fwy+0.06*np.sin(np.radians(fwa))],
                color=fwc,lw=1.2,alpha=0.8,zorder=5)
T(fx2+fw2/2,2.42,'🎡 FAIRGROUND',color='#F59E0B',fontsize=6.5,fontweight='bold',zorder=9)

# ══════════════════════════════════════════════════════════════
# 6. CIRCUS TENT
# ══════════════════════════════════════════════════════════════
tx3,tw3=5.00,1.00
R(tx3,0,tw3,2.5,'#1a0505',zorder=2)
# tent stripes background
for si in range(10):
    stripe_x=tx3+si*(tw3/9)
    R(stripe_x,0,tw3/18,2.0,['#DC2626','#FFFFFF'][si%2],zorder=2,alpha=0.15)
# tent roof
tent_pts=[[tx3,1.60],[tx3+tw3/2,2.46],[tx3+tw3,1.60]]
P(tent_pts,color='#DC2626',zorder=4)
# white stripes on tent
for frac2 in [0.25,0.50,0.75]:
    mid_x2=tx3+frac2*tw3
    P([[mid_x2-0.04,1.60],[mid_x2+0.04,1.60],[tx3+tw3/2+0.008,2.46],[tx3+tw3/2-0.008,2.46]],color='#FFFFFF',alpha=0.6,zorder=5)
# tent border
ax.plot([tx3,tx3+tw3/2,tx3+tw3],[1.60,2.46,1.60],color='#FFD700',lw=2,zorder=5)
# tent body
R(tx3+0.05,0.04,tw3-0.10,1.58,'#DC2626',zorder=3)
for si2 in range(10):
    sx3=tx3+0.05+si2*(tw3-0.10)/9
    R(sx3,0.04,(tw3-0.10)/18,1.58,['#FFFFFF','#DC2626'][si2%2],zorder=3,alpha=0.35)
# spotlights from roof
for slx,sla,slc in [(tx3+0.22,20,'#FFD700'),(tx3+0.50,-5,'#FFFFFF'),(tx3+0.78,-20,'#FF69B4')]:
    P([[slx-0.05,2.35],[slx+0.05,2.35],[slx+0.20,0.04],[slx-0.20,0.04]],color=slc,alpha=0.08,zorder=4)
    C(slx,2.37,0.04,color=slc,alpha=0.8,zorder=6)
# entrance curtains
R(tx3+0.32,0.04,0.10,0.60,'#8B0000',zorder=6)
R(tx3+0.58,0.04,0.10,0.60,'#8B0000',zorder=6)
P([[tx3+0.32,0.64],[tx3+0.50,0.54],[tx3+0.42,0.64]],color='#FFD700',zorder=7)
# BUBBLE floating in tent
bbx=tx3+0.55; bby=1.20
C(bbx,bby,0.10,color='#BAE6FD',alpha=0.6,zorder=8)
C(bbx,bby,0.10,color='#7DD3FC',fill=False,lw=1.5,alpha=0.8,zorder=9)
for fa2,fb2,sc4 in [(20,70,'#A78BFA'),(90,150,'#34D399'),(160,220,'#FB923C')]:
    ax.add_patch(Arc((bbx,bby),0.18,0.18,angle=0,theta1=fa2,theta2=fb2,color=sc4,lw=2,alpha=0.6,zorder=9))
C(bbx-0.028,bby+0.02,0.010,color='#0C4A6E',zorder=10)
C(bbx+0.028,bby+0.02,0.010,color='#0C4A6E',zorder=10)
E(bbx,bby-0.22,0.10,0.03,color='#0C4A6E',alpha=0.3,zorder=7)  # shadow
# POMNI tiny in ring
ppx=tx3+0.28; ppy=0.20
C(ppx,ppy+0.12,0.042,color='#FDDCB0',zorder=8)
R(ppx-0.022,ppy+0.02,0.044,0.10,'#2563EB',zorder=8)
C(ppx-0.012,ppy+0.135,0.016,color='#FFFFFF',zorder=9)
C(ppx+0.012,ppy+0.135,0.016,color='#FFFFFF',zorder=9)
T(tx3+tw3/2,2.42,'🎪 CIRCUS TENT',color='#FBBF24',fontsize=6.5,fontweight='bold',zorder=9)

# ══════════════════════════════════════════════════════════════
# 7. THRONE ROOM
# ══════════════════════════════════════════════════════════════
trx,trw=6.00,1.00
R(trx,0,trw,2.5,'#05000f',zorder=2)
# stone wall texture
for wi2 in np.arange(trx,trx+trw,0.12):
    for wj2 in np.arange(0,2.5,0.14):
        R(wi2+0.01,wj2+0.01,0.10,0.12,'#1a1a2e',zorder=2,alpha=0.8)
# power orbs floating
orb_data=[(trx+0.12,2.00,'#A855F7'),(trx+0.25,1.70,'#FFD700'),(trx+0.88,2.00,'#A855F7'),
          (trx+0.75,1.70,'#FFD700'),(trx+0.12,0.60,'#7C3AED'),(trx+0.88,0.60,'#7C3AED'),
          (trx+0.20,1.30,'#F472B6'),(trx+0.80,1.30,'#F472B6')]
for ox,oy,oc in orb_data:
    C(ox,oy,0.04,color=oc,alpha=0.8,zorder=6)
    C(ox,oy,0.06,color=oc,alpha=0.15,zorder=5)
    C(ox,oy,0.09,color=oc,alpha=0.06,zorder=4)
# gold rune symbols on walls
rune_syms=['ᚠ','ᚢ','ᚦ','ᚨ','ᚱ','ᚲ','ᚷ','ᚹ']
for ri2,(rnx,rny) in enumerate([(trx+0.08,2.30),(trx+0.92,2.30),(trx+0.08,1.20),(trx+0.92,1.20),
                                  (trx+0.08,0.30),(trx+0.92,0.30),(trx+0.40,2.20),(trx+0.60,2.20)]):
    T(rnx,rny,rune_syms[ri2%8],color='#FFD700',fontsize=9,alpha=0.7,zorder=6)
# purple grid floor
for gx4 in np.arange(trx,trx+trw,0.10):
    ax.plot([gx4,gx4],[0,0.35],color='#7C3AED',alpha=0.25,lw=0.8,zorder=4)
for gy4 in np.arange(0,0.35,0.10):
    ax.plot([trx,trx+trw],[gy4,gy4],color='#7C3AED',alpha=0.25,lw=0.8,zorder=4)
# DINO RAPTOR — massive, wings spread
drx=trx+0.50; dry=0.30
# wings
P([[drx,dry+0.90],[trx+0.02,dry+1.40],[trx+0.08,dry+0.60],[drx-0.24,dry+0.72]],color='#5B21B6',alpha=0.95,zorder=7)
P([[drx,dry+0.90],[trx+0.98,dry+1.40],[trx+0.92,dry+0.60],[drx+0.24,dry+0.72]],color='#5B21B6',alpha=0.95,zorder=7)
# gold wing trim
ax.plot([drx,trx+0.02,trx+0.08,drx-0.24],[dry+0.90,dry+1.40,dry+0.60,dry+0.72],color='#FFD700',lw=1.2,zorder=8)
ax.plot([drx,trx+0.98,trx+0.92,drx+0.24],[dry+0.90,dry+1.40,dry+0.60,dry+0.72],color='#FFD700',lw=1.2,zorder=8)
# aura rings
for ra2,aa2 in [(0.40,0.08),(0.34,0.12),(0.28,0.16)]:
    C(drx,dry+0.55,ra2,color='#7C3AED',alpha=aa2,zorder=6)
# body armor
body_dr=np.array([[drx-0.12,dry+0.10],[drx+0.12,dry+0.10],[drx+0.14,dry+0.65],[drx,dry+0.72],[drx-0.14,dry+0.65]])
P(body_dr,color='#B8860B',zorder=8)
P(body_dr,color='#FFD700',fill=False,lw=1.5,zorder=9)
chest_dr=np.array([[drx-0.08,dry+0.22],[drx+0.08,dry+0.22],[drx+0.09,dry+0.54],[drx,dry+0.58],[drx-0.09,dry+0.54]])
P(chest_dr,color='#FFD700',alpha=0.8,zorder=9)
# head
C(drx,dry+0.86,0.10,color='#2D5A1B',zorder=10)
E(drx,dry+0.80,0.09,0.055,color='#3A7A25',zorder=11)
for ex2 in [drx-0.028,drx+0.028]:
    C(ex2,dry+0.89,0.018,color='#1a0000',zorder=12)
    C(ex2,dry+0.89,0.013,color='#FF4500',zorder=13)
    C(ex2,dry+0.89,0.006,color='#1a0000',zorder=14)
# crown on DR
crown_dr_x=[drx-0.08,drx-0.06,drx-0.02,drx,drx+0.04,drx+0.06,drx+0.10]
crown_dr_y=[dry+0.98,dry+0.94,dry+0.98,dry+1.02,dry+0.98,dry+0.94,dry+0.98]
ax.fill_between(crown_dr_x,crown_dr_y,dry+0.94,color='#FFD700',zorder=14)
# legs + tail
R(drx-0.10,dry,0.07,0.12,'#B8860B',zorder=9)
R(drx+0.03,dry,0.07,0.12,'#B8860B',zorder=9)
P([[drx+0.12,dry+0.10],[drx+0.28,dry+0.02],[drx+0.32,dry-0.02],[drx+0.18,dry+0.06]],color='#2D5A1B',zorder=7)
T(trx+trw/2,2.42,'🏰 THRONE ROOM',color='#FFD700',fontsize=6.5,fontweight='bold',zorder=9)

# ══════════════════════════════════════════════════════════════
# Zone dividers
# ══════════════════════════════════════════════════════════════
for divx in [1.0,2.0,3.0,4.0,5.0,6.0]:
    ax.plot([divx,divx],[0,2.5],color='#FFD700',lw=1.5,alpha=0.4,linestyle='--',zorder=10)

# Title
ax.text(3.5,2.48,'✦  THE AMAZING DIGITAL CIRCUS  —  OUTSIDE WORLD  ✦',
        color='#FFD700',fontsize=12,fontweight='bold',ha='center',va='bottom',
        fontfamily='monospace',zorder=11)

plt.tight_layout(pad=0.2)
print("✅ World map rendered — 7 zones:")
for k,v in ZONES.items():
    print(f"   {k:<12} x={v[0]:.2f}–{v[0]+v[1]:.2f}")


import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse, Wedge, Arc
import numpy as np

rng = np.random.default_rng(7)

throne_room_fig, ax = plt.subplots(figsize=(22, 13))
throne_room_fig.patch.set_facecolor('#05000f')
ax.set_facecolor('#05000f')
ax.set_xlim(0, 10); ax.set_ylim(0, 6)
ax.set_xticks([]); ax.set_yticks([])
for sp in ax.spines.values(): sp.set_visible(False)

def C(cx, cy, r, color='#FFFFFF', **kw):
    ax.add_patch(Circle((cx,cy), r, facecolor=color, **kw))
def E(cx, cy, w, h, color='#FFFFFF', **kw):
    ax.add_patch(Ellipse((cx,cy), w, h, facecolor=color, **kw))
def R(x, y, w, h, fc, ec='none', lw=0, zorder=3, alpha=1.0):
    ax.add_patch(FancyBboxPatch((x,y), w, h, boxstyle='square,pad=0',
                                facecolor=fc, edgecolor=ec, linewidth=lw, zorder=zorder, alpha=alpha))
def P(pts, **kw):
    ax.add_patch(plt.Polygon(pts, **kw))
def T(x, y, s, **kw):
    ax.text(x, y, s, ha='center', va='center', **kw)

# ══════════════════════════════════════════════════════════════
# ROOM STRUCTURE
# ══════════════════════════════════════════════════════════════
# Floor — black marble with gold veins
R(0, 0, 10, 1.6, '#0a0a14', zorder=1)
for vx in np.arange(0.3, 10, 0.55):
    vy_off = rng.uniform(0, 0.8)
    ax.plot([vx, vx+rng.uniform(-0.2,0.2)], [0, 1.6], color='#FFD700', alpha=0.12, lw=0.8, zorder=2)
# Purple power grid on floor
for gx in np.arange(0, 10, 0.5):
    ax.plot([gx,gx],[0,1.6], color='#7C3AED', alpha=0.18, lw=0.6, zorder=2)
for gy in np.arange(0, 1.6, 0.4):
    ax.plot([0,10],[gy,gy], color='#7C3AED', alpha=0.18, lw=0.6, zorder=2)
# Back wall — dark stone bricks
R(0, 1.6, 10, 4.4, '#0d0d1e', zorder=1)
for wi in np.arange(0, 10, 0.55):
    for wj in np.arange(1.6, 6, 0.32):
        R(wi+0.02, wj+0.02, 0.50, 0.28, '#12122a', zorder=1, alpha=0.9)
# Ceiling glow
ax.fill_between([0,10],[5.6,5.6],[6,6],color='#1a0040',alpha=0.8,zorder=1)
for cx_r in np.arange(0.5,10,1.2):
    C(cx_r, 5.8, 0.30, color='#7C3AED', alpha=0.08, zorder=2)

# ── Gold rune border on walls ──────────────────────────────────
rune_syms = ['ᚠ','ᚢ','ᚦ','ᚨ','ᚱ','ᚲ','ᚷ','ᚹ','ᛏ','ᛒ','ᛖ','ᛗ']
for ri, rx_r in enumerate(np.linspace(0.4, 9.6, 12)):
    T(rx_r, 5.55, rune_syms[ri%12], color='#FFD700', fontsize=11, alpha=0.75, zorder=6)
for ri2, ry_r in enumerate([1.8, 2.5, 3.2, 3.9, 4.6]):
    T(0.25, ry_r, rune_syms[ri2%12], color='#FFD700', fontsize=10, alpha=0.60, zorder=6)
    T(9.75, ry_r, rune_syms[(ri2+4)%12], color='#FFD700', fontsize=10, alpha=0.60, zorder=6)

# ══════════════════════════════════════════════════════════════
# POWER ORBS — 8 floating orbs
# ══════════════════════════════════════════════════════════════
orb_data = [
    (1.20, 4.80, '#A855F7'), (8.80, 4.80, '#A855F7'),
    (0.90, 3.20, '#FFD700'), (9.10, 3.20, '#FFD700'),
    (1.40, 1.90, '#7C3AED'), (8.60, 1.90, '#7C3AED'),
    (2.20, 5.10, '#F472B6'), (7.80, 5.10, '#F472B6'),
]
for ox, oy, oc in orb_data:
    for orb_r, orb_a in [(0.16, 0.05), (0.12, 0.10), (0.08, 0.30), (0.055, 0.85)]:
        C(ox, oy, orb_r, color=oc, alpha=orb_a, zorder=5)
    C(ox-0.015, oy+0.015, 0.018, color='#FFFFFF', alpha=0.5, zorder=6)

# ══════════════════════════════════════════════════════════════
# TRIPLE MONITOR GAMING PC — left side
# ══════════════════════════════════════════════════════════════
pc_x = 0.45
# RGB tower
R(pc_x, 0.04, 0.55, 1.45, '#111122', '#7C3AED', 2, zorder=8)
# RGB strips on tower
for rgb_y in [0.20, 0.55, 0.90, 1.25]:
    ax.plot([pc_x+0.04, pc_x+0.51], [rgb_y, rgb_y],
            color=['#FF4500','#7C3AED','#00FF88','#3B82F6'][int((rgb_y-0.1)/0.35)%4],
            lw=3, alpha=0.85, zorder=9)
# Tower logo
T(pc_x+0.275, 0.75, 'DR', color='#FFD700', fontsize=8, fontweight='bold', zorder=10)
C(pc_x+0.275, 0.75, 0.14, color='#FFD700', alpha=0.06, zorder=9)
# Desk surface
R(pc_x-0.10, 1.50, 5.20, 0.18, '#2a1a0a', '#8B4513', 1.5, zorder=7)

# Monitors (3x) on desk
monitor_specs = [
    (pc_x+0.60, 1.68, 0.95, 0.72, '#001a33', '#3B82F6', 'SYSTEM\nMONITOR', '#22D3EE'),
    (pc_x+1.65, 1.68, 1.10, 0.82, '#001a00', '#22C55E', 'DIGITAL CIRCUS\nONLINE', '#86EFAC'),
    (pc_x+2.85, 1.68, 0.95, 0.72, '#1a0033', '#A855F7', 'PLAYERS: 1337\nROOMS: 42', '#D8B4FE'),
]
for mx2, my2, mw2, mh2, mbg, mbrd, mtxt, mtc in monitor_specs:
    # Stand
    ax.plot([mx2+mw2/2, mx2+mw2/2], [my2, my2-0.08], color='#333355', lw=5, zorder=7)
    E(mx2+mw2/2, my2-0.10, 0.22, 0.06, color='#333355', zorder=7)
    # Screen bezel
    R(mx2-0.03, my2-0.03, mw2+0.06, mh2+0.06, '#111122', mbrd, 2, zorder=8)
    # Screen content
    R(mx2, my2, mw2, mh2, mbg, zorder=9)
    T(mx2+mw2/2, my2+mh2/2, mtxt, color=mtc, fontsize=6.5, zorder=10,
      fontfamily='monospace', fontweight='bold')
    # RGB glow under monitor
    ax.plot([mx2, mx2+mw2], [my2-0.04, my2-0.04], color=mbrd, lw=2, alpha=0.6, zorder=8)

# RGB Keyboard
R(pc_x+0.60, 1.52, 2.20, 0.12, '#1a1a2e', '#3B82F6', 1, zorder=9)
for ki in range(18):
    kc = ['#FF4500','#FFD700','#7C3AED','#22C55E','#3B82F6'][ki%5]
    R(pc_x+0.65+ki*0.115, 1.54, 0.09, 0.08, kc, zorder=10, alpha=0.7)
# Mouse
E(pc_x+2.95, 1.57, 0.12, 0.16, color='#222244', zorder=9)
ax.plot([pc_x+2.95, pc_x+2.95], [1.54, 1.60], color='#3B82F6', lw=1, zorder=10)

# ══════════════════════════════════════════════════════════════
# GAMING LAPTOP — right side of desk
# ══════════════════════════════════════════════════════════════
lp_x = 6.00
# Base
R(lp_x, 1.52, 1.50, 0.12, '#111122', '#A855F7', 2, zorder=8)
# RGB on base edge
ax.plot([lp_x, lp_x+1.50], [1.52, 1.52], color='#A855F7', lw=2.5, alpha=0.8, zorder=9)
# Lid (open ~120 degrees)
lid_pts = [[lp_x-0.05, 1.64], [lp_x+1.55, 1.64], [lp_x+1.40, 2.56], [lp_x+0.10, 2.56]]
P(lid_pts, color='#111122', zorder=8)
P(lid_pts, color='#A855F7', fill=False, lw=2, zorder=9)
# Laptop screen — DR wallpaper
R(lp_x+0.06, 1.66, 1.38, 0.88, '#0D001A', zorder=10)
# DR logo on screen
T(lp_x+0.75, 2.10, '🐉', fontsize=22, zorder=11, alpha=0.9)
T(lp_x+0.75, 1.82, 'DINO RAPTOR', color='#FFD700', fontsize=5.5, fontweight='bold', zorder=11, fontfamily='monospace')
T(lp_x+0.75, 1.75, 'SUPREME LEADER', color='#A855F7', fontsize=4.5, zorder=11, fontfamily='monospace')
# RGB hinge strip
ax.plot([lp_x, lp_x+1.50], [1.64, 1.64], color='#A855F7', lw=3, alpha=0.9, zorder=10)
# Keyboard on laptop
R(lp_x+0.08, 1.54, 1.34, 0.09, '#1a1a2e', zorder=9)
for li2 in range(10):
    lc2 = ['#7C3AED','#F472B6','#A855F7'][li2%3]
    R(lp_x+0.10+li2*0.128, 1.555, 0.10, 0.06, lc2, zorder=10, alpha=0.6)

# ══════════════════════════════════════════════════════════════
# KING BED — right wall
# ══════════════════════════════════════════════════════════════
bed_x = 6.80
# Headboard with runes
R(bed_x, 1.60, 3.00, 1.80, '#1a0030', '#7C3AED', 2.5, zorder=7)
for ri3, (rhx, rhy) in enumerate(zip(np.linspace(bed_x+0.20, bed_x+2.80, 6), [3.10]*6)):
    T(rhx, rhy, rune_syms[ri3%12], color='#FFD700', fontsize=12, alpha=0.8, zorder=8)
# Monogram on headboard
T(bed_x+1.50, 2.65, 'DR', color='#FFD700', fontsize=26, fontweight='bold', zorder=8, alpha=0.9)
C(bed_x+1.50, 2.68, 0.40, color='#FFD700', alpha=0.04, zorder=7)
# Mattress
R(bed_x, 0.60, 3.00, 1.10, '#1a0040', '#5B21B6', 1.5, zorder=8)
# Pillows
for pi, pc2 in enumerate(['#7C3AED','#A855F7','#5B21B6']):
    R(bed_x+0.15+pi*0.95, 1.30, 0.80, 0.36, pc2, '#FFD700', 1.5, zorder=9, alpha=0.9)
    T(bed_x+0.55+pi*0.95, 1.48, 'DR', color='#FFD700', fontsize=7, alpha=0.6, zorder=10)
# Duvet
R(bed_x, 0.60, 3.00, 0.68, '#2d0060', '#7C3AED', 1, zorder=9, alpha=0.9)
# Neon underglow — 4 colours
for ug_i, (ug_x, ug_y, ug_w, ug_c) in enumerate([
    (bed_x, 0.58, 3.00, '#7C3AED'),
    (bed_x, 0.58, 3.00, '#A855F7'),
    (bed_x-0.02, 0.62, 0.04, '#FF4500'),
    (bed_x+2.98, 0.62, 0.04, '#22C55E'),
]):
    ax.plot([ug_x, ug_x+ug_w], [ug_y, ug_y], color=ug_c, lw=3.5, alpha=0.6, zorder=8)
ax.fill_between([bed_x, bed_x+3.00], [0.54, 0.54], [0.62, 0.62], color='#7C3AED', alpha=0.15, zorder=7)
# Bed legs
for bl_x in [bed_x+0.15, bed_x+2.80]:
    R(bl_x, 0.04, 0.12, 0.58, '#B8860B', zorder=8)

# ══════════════════════════════════════════════════════════════
# THRONE OF CODE — center back
# ══════════════════════════════════════════════════════════════
th_x = 3.80
# Steps
for st_i in range(3):
    sw2 = 1.60 - st_i*0.22; sx2 = th_x + st_i*0.11
    R(sx2, 1.60+st_i*0.22, sw2, 0.24, '#1a1a2e', '#5B21B6', 1.5, zorder=7)
    code_lines = ['if dino:', 'return True', 'x**∞']
    T(sx2+sw2/2, 1.72+st_i*0.22, code_lines[st_i], color='#22C55E', fontsize=5.5,
      fontfamily='monospace', zorder=8)
# Throne seat
R(th_x+0.11, 2.26, 1.18, 0.40, '#0d0d2e', '#7C3AED', 2, zorder=8)
# Armrests
R(th_x+0.04, 2.26, 0.20, 0.55, '#1a0040', '#A855F7', 2, zorder=8)
R(th_x+1.16, 2.26, 0.20, 0.55, '#1a0040', '#A855F7', 2, zorder=8)
C(th_x+0.14, 2.81, 0.06, color='#FFD700', zorder=9)
C(th_x+1.26, 2.81, 0.06, color='#FFD700', zorder=9)
# Throne back — tall
R(th_x+0.06, 2.66, 1.28, 1.80, '#0d0d2e', '#7C3AED', 2.5, zorder=8)
# Crown finial on throne back
P([[th_x+0.55, 4.46],[th_x+0.70, 4.78],[th_x+0.85, 4.46]], color='#FFD700', zorder=9)
P([[th_x+0.42, 4.46],[th_x+0.55, 4.68],[th_x+0.70, 4.46]], color='#FFD700', zorder=9)
P([[th_x+0.70, 4.46],[th_x+0.85, 4.68],[th_x+1.00, 4.46]], color='#FFD700', zorder=9)
ax.plot([th_x+0.06, th_x+1.34], [4.46, 4.46], color='#FFD700', lw=3, zorder=9)
# Code fragments on throne back
for ci2, cl in enumerate(['while True:', '  reign()', 'for e in enemies:', '  destroy(e)', 'assert power==∞']):
    T(th_x+0.70, 4.30-ci2*0.26, cl, color=['#22C55E','#7DD3FC','#22C55E','#F87171','#FFD700'][ci2],
      fontsize=4.8, fontfamily='monospace', zorder=9, alpha=0.9)

# ══════════════════════════════════════════════════════════════
# DINO RAPTOR — giant, center-left, wings spread
# ══════════════════════════════════════════════════════════════
drx = 4.80; dry = 1.60
# aura rings
for ra2, aa2 in [(1.80, 0.04), (1.55, 0.07), (1.30, 0.10), (1.05, 0.08)]:
    C(drx, dry+1.20, ra2, color='#7C3AED', alpha=aa2, zorder=9)
for ra3, aa3 in [(0.90, 0.06), (0.70, 0.10)]:
    C(drx, dry+1.20, ra3, color='#FFD700', alpha=aa3, zorder=9)
# WINGS — massive
wing_l = np.array([[drx, dry+2.20], [drx-3.20, dry+3.10], [drx-2.80, dry+1.40], [drx-0.70, dry+1.70]])
wing_r = np.array([[drx, dry+2.20], [drx+3.20, dry+3.10], [drx+2.80, dry+1.40], [drx+0.70, dry+1.70]])
P(wing_l, color='#4C1D95', alpha=0.90, zorder=10)
P(wing_r, color='#4C1D95', alpha=0.90, zorder=10)
# Wing bone lines
for i_w in range(4):
    t = i_w/3
    p_l = wing_l[0]*(1-t) + wing_l[1]*t
    ax.plot([drx, p_l[0]], [dry+2.20, p_l[1]], color='#FFD700', lw=1.2, alpha=0.7, zorder=11)
    p_r = wing_r[0]*(1-t) + wing_r[1]*t
    ax.plot([drx, p_r[0]], [dry+2.20, p_r[1]], color='#FFD700', lw=1.2, alpha=0.7, zorder=11)
ax.plot(np.append(wing_l[:,0], wing_l[0,0]), np.append(wing_l[:,1], wing_l[0,1]), color='#FFD700', lw=1.5, zorder=12)
ax.plot(np.append(wing_r[:,0], wing_r[0,0]), np.append(wing_r[:,1], wing_r[0,1]), color='#FFD700', lw=1.5, zorder=12)
# Tail
P([[drx+0.36, dry+0.10], [drx+1.60, dry-0.08], [drx+1.90, dry-0.30], [drx+0.55, dry+0.06]], color='#2D5A1B', zorder=10)
# Body armor — gold plates
body_dr = np.array([[drx-0.45, dry+0.30], [drx+0.45, dry+0.30], [drx+0.50, dry+2.00], [drx, dry+2.26], [drx-0.50, dry+2.00]])
P(body_dr, color='#B8860B', zorder=12)
P(body_dr, color='#FFD700', fill=False, lw=2.5, zorder=13)
chest_dr = np.array([[drx-0.28, dry+0.55], [drx+0.28, dry+0.55], [drx+0.32, dry+1.70], [drx, dry+1.94], [drx-0.32, dry+1.70]])
P(chest_dr, color='#FFD700', alpha=0.75, zorder=13)
# Plate details
for pi2, py2 in enumerate([0.65, 0.95, 1.25, 1.55]):
    ax.plot([drx-0.26+pi2*0.02, drx+0.26-pi2*0.02], [dry+py2, dry+py2], color='#B8860B', lw=1.5, alpha=0.8, zorder=14)
# Shoulder pads
for spx, spy in [(drx-0.45, dry+1.90), (drx+0.45, dry+1.90)]:
    C(spx, spy, 0.18, color='#B8860B', zorder=13)
    C(spx, spy, 0.18, color='#FFD700', alpha=0.0, edgecolor='#FFD700', lw=2, zorder=14)
# Legs + claws
for lx2 in [drx-0.25, drx+0.14]:
    R(lx2, dry, 0.20, 0.32, '#B8860B', zorder=12)
    for ci3 in range(3):
        P([[lx2+0.02+ci3*0.06, dry], [lx2+0.08+ci3*0.06, dry], [lx2+0.05+ci3*0.06, dry-0.12]], color='#FFD700', zorder=13)
# Arms
ax.plot([drx-0.45, drx-0.80, drx-0.95], [dry+1.70, dry+1.20, dry+0.80], color='#B8860B', lw=18, solid_capstyle='round', zorder=12)
ax.plot([drx+0.45, drx+0.80, drx+0.95], [dry+1.70, dry+1.20, dry+0.80], color='#B8860B', lw=18, solid_capstyle='round', zorder=12)
for clx, cly in [(drx-0.92, dry+0.76), (drx+0.92, dry+0.76)]:
    for ci4, ca4 in enumerate([-25, 0, 25]):
        P([[clx, cly], [clx+0.12*np.cos(np.radians(ca4+90)), cly+0.12*np.sin(np.radians(ca4+90))],
           [clx+0.18*np.cos(np.radians(ca4+90)), cly+0.18*np.sin(np.radians(ca4+90))-0.05]],
          color='#FFD700', zorder=13)
# Head
C(drx, dry+2.55, 0.38, color='#2D5A1B', zorder=14)
E(drx, dry+2.34, 0.36, 0.24, color='#3A7A25', zorder=15)
# Snout teeth
for tx4 in np.linspace(drx-0.12, drx+0.12, 6):
    P([[tx4, dry+2.30], [tx4+0.02, dry+2.30], [tx4+0.01, dry+2.20]], color='#FFFFFF', zorder=16)
# Eyes — glowing orange
for ex3, ey3 in [(drx-0.14, dry+2.66), (drx+0.14, dry+2.66)]:
    C(ex3, ey3, 0.080, color='#1a0000', zorder=16)
    C(ex3, ey3, 0.065, color='#FF4500', zorder=17)
    C(ex3, ey3, 0.030, color='#1a0000', zorder=18)
    C(ex3+0.018, ey3+0.018, 0.014, color='#FFFFFF', zorder=19)
    C(ex3, ey3, 0.095, color='#FF4500', alpha=0.20, zorder=15)
# Horns
P([[drx-0.14, dry+2.88], [drx-0.22, dry+3.26], [drx-0.07, dry+2.92]], color='#8B4513', zorder=17)
P([[drx+0.14, dry+2.88], [drx+0.22, dry+3.26], [drx+0.07, dry+2.92]], color='#8B4513', zorder=17)
# Crown
crown_x = [drx-0.30, drx-0.26, drx-0.14, drx-0.10, drx, drx+0.10, drx+0.14, drx+0.26, drx+0.30]
crown_y = [dry+2.95, dry+2.88, dry+2.95, dry+2.90, dry+3.04, dry+2.90, dry+2.95, dry+2.88, dry+2.95]
ax.fill_between(crown_x, crown_y, dry+2.88, color='#FFD700', zorder=18)
ax.plot(crown_x, crown_y, color='#B8860B', lw=2, zorder=19)
for gi2, (gx5, gy5) in enumerate(zip([drx-0.26, drx-0.12, drx, drx+0.12, drx+0.26],
                                       [dry+2.895, dry+2.890, dry+3.020, dry+2.890, dry+2.895])):
    C(gx5, gy5, 0.030, color=['#DC2626','#10B981','#3B82F6','#A855F7','#F59E0B'][gi2], zorder=20)

# ── Ability icons floating around DR ───────────────────────────
ability_icons = [('✈',drx-1.80,dry+3.30,'FLY'),('⚡',drx-1.40,dry+0.70,'TP'),
                 ('👻',drx+1.80,dry+3.30,'PHASE'),('🌍',drx+1.40,dry+0.70,'REALITY'),
                 ('⏱',drx,dry+3.80,'TIME'),('👑',drx-0.60,dry+3.60,'SUPREME'),
                 ('🔮',drx+0.60,dry+3.60,'VOID'),('⚔',drx-2.20,dry+2.00,'POWER')]
for icon, ix2, iy2, lbl in ability_icons:
    ax.text(ix2, iy2, icon, fontsize=11, ha='center', va='center', zorder=20,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a0030', edgecolor='#FFD700', alpha=0.88, lw=1.5))
    T(ix2, iy2-0.28, lbl, color='#FFD700', fontsize=4.5, fontweight='bold', zorder=20, fontfamily='monospace')
    # dashed line from icon to DR
    ax.plot([ix2, drx], [iy2, dry+2.00], color='#FFD700', lw=0.6, alpha=0.20, linestyle=':', zorder=9)

# ══════════════════════════════════════════════════════════════
# TITLE BANNER
# ══════════════════════════════════════════════════════════════
R(0.5, 5.60, 9.00, 0.38, '#0d0020', '#FFD700', 2, zorder=20)
T(5.0, 5.79, '🏰  DINO RAPTOR\'S THRONE ROOM  —  SUPREME LEADER  🐉',
  color='#FFD700', fontsize=12, fontweight='bold', fontfamily='monospace', zorder=21)

plt.tight_layout(pad=0.3)
print("✅ Dino Raptor's Throne Room rendered — MAXIMUM DETAIL")
print("   🖥  Triple Monitor Gaming PC — RGB tower, 3 screens, keyboard, mouse")
print("   💻  Gaming Laptop — open lid, DR wallpaper, RGB hinge, keyboard")
print("   🛏  King Bed — neon underglow, rune headboard, DR monogram pillows")
print("   ⚡  Throne of Code — 3 steps, code fragments, crown finial, armrests")
print("   🔮  8 Power Orbs — gold + purple, floating on walls")
print("   ᚠ   Wall Runes — ceiling and walls covered in gold runes")
print("   🐉  Dino Raptor — GIANT, wings spread wide, full armor, crown, aura")
print("   ✈⚡👻🌍⏱👑🔮⚔  8 Ability icons floating with labels")


import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Wedge, Arc
import numpy as np

rng = np.random.default_rng(13)

circus_interior_fig, ax = plt.subplots(figsize=(22, 13))
circus_interior_fig.patch.set_facecolor('#0d0000')
ax.set_facecolor('#0d0000')
ax.set_xlim(0, 10); ax.set_ylim(0, 6.5)
ax.set_xticks([]); ax.set_yticks([])
for sp in ax.spines.values(): sp.set_visible(False)

def C(cx,cy,r,color='#FFFFFF',**kw): ax.add_patch(Circle((cx,cy),r,facecolor=color,**kw))
def E(cx,cy,w,h,color='#FFFFFF',**kw): ax.add_patch(Ellipse((cx,cy),w,h,facecolor=color,**kw))
def R(x,y,w,h,fc,ec='none',lw=0,zorder=3,alpha=1.0):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='square,pad=0',facecolor=fc,edgecolor=ec,linewidth=lw,zorder=zorder,alpha=alpha))
def P(pts,**kw): ax.add_patch(plt.Polygon(pts,**kw))
def T(x,y,s,**kw): ax.text(x,y,s,ha='center',va='center',**kw)

# ══════════════════════════════════════════════════════════════
# TENT CANVAS CEILING — red & white striped dome
# ══════════════════════════════════════════════════════════════
# Dome background
tent_dome = np.array([[0,1.8],[5.0,6.4],[10,1.8]])
P(tent_dome, color='#8B0000', alpha=0.6, zorder=1)
# Stripes radiating from top
for sa in np.linspace(-70, 70, 20):
    tip_x = 5.0; tip_y = 6.4
    base_x = 5.0 + 6.5*np.sin(np.radians(sa))
    base_y = 1.8 - 0.5*abs(np.sin(np.radians(sa)))
    clr = '#FFFFFF' if int((sa+70)/7)%2==0 else '#DC2626'
    ax.plot([tip_x, base_x],[tip_y, base_y], color=clr, lw=4, alpha=0.25, zorder=2)
# tent pole center
ax.plot([5.0,5.0],[0,6.4],color='#8B4513',lw=8,zorder=3,alpha=0.7)
ax.plot([5.0,5.0],[0,6.4],color='#FFD700',lw=3,zorder=4,alpha=0.4)

# ── Slingers / bunting ─────────────────────────────────────────
for si in range(8):
    sx1 = si*1.30; sy1 = 5.8 - abs(si-3.5)*0.08
    sx2 = sx1+1.30; sy2 = 5.8 - abs(si+1-3.5)*0.08
    # drape
    bx_arr = np.linspace(sx1, sx2, 30)
    by_arr = sy1 + (sy2-sy1)*np.linspace(0,1,30) - 0.15*np.sin(np.pi*np.linspace(0,1,30))
    ax.plot(bx_arr, by_arr, color='#FFD700', lw=1.8, alpha=0.7, zorder=5)
    # flag
    flag_col = ['#EF4444','#3B82F6','#F59E0B','#10B981','#F472B6','#7C3AED','#FBBF24','#EC4899'][si%8]
    P([[sx1+0.55,by_arr[15]],[sx1+0.55,by_arr[15]-0.14],[sx1+0.65,by_arr[15]-0.07]],color=flag_col,zorder=5)

# ══════════════════════════════════════════════════════════════
# ARENA FLOOR
# ══════════════════════════════════════════════════════════════
# sawdust floor
E(5.0, 0.80, 8.0, 1.20, color='#C2852A', zorder=3)
E(5.0, 0.80, 7.6, 1.00, color='#D4962F', zorder=4)
# golden ring border
for rr in [3.95, 4.00]:
    C(5.0, 0.80, rr, color='none', edgecolor='#FFD700', lw=3.5-rr/2, alpha=0.9, zorder=5)
# sawdust texture dots
for _ in range(60):
    sdx = 5.0 + rng.uniform(-3.7,3.7); sdy = rng.uniform(0.2, 1.35)
    if (sdx-5.0)**2/16 + (sdy-0.80)**2/0.36 < 1.0:
        ax.plot(sdx, sdy, '.', color='#8B5E1A', ms=rng.uniform(1,3), alpha=rng.uniform(0.3,0.7), zorder=5)

# ══════════════════════════════════════════════════════════════
# SPOTLIGHT BEAMS (6 from ceiling)
# ══════════════════════════════════════════════════════════════
spot_cfg = [
    (1.5, 6.0, 2.0, 0.60, '#FFD700', 0.06),   # gold — Dino Raptor
    (3.0, 6.1, 3.5, 0.55, '#FFFFFF', 0.05),
    (5.0, 6.4, 5.0, 0.80, '#FFFFFF', 0.07),   # center ring
    (7.0, 6.1, 6.5, 0.55, '#FF69B4', 0.05),
    (8.5, 6.0, 8.0, 0.60, '#7DD3FC', 0.05),
    (5.0, 6.4, 2.8, 0.40, '#A855F7', 0.04),
]
for stx, sty, sbx, sby, sc, sa in spot_cfg:
    P([[stx,sty],[sbx-0.5,sby],[sbx+0.5,sby]], color=sc, alpha=sa, zorder=4)
    C(stx, sty, 0.12, color=sc, alpha=0.9, zorder=6)

# ══════════════════════════════════════════════════════════════
# AUDIENCE — silhouettes in rows
# ══════════════════════════════════════════════════════════════
for row, (aud_y, aud_h) in enumerate([(1.65,0.30),(1.95,0.28),(2.22,0.26)]):
    for aud_x in np.linspace(0.3, 9.7, 22-row*2):
        # body
        R(aud_x-0.09, aud_y, 0.18, aud_h*0.65, '#1a1a1a', zorder=6)
        # head
        C(aud_x, aud_y+aud_h*0.68, aud_h*0.25, color='#2a2020', zorder=6)
        # random bright hair/hat
        if rng.random() < 0.3:
            hc = rng.choice(['#EF4444','#3B82F6','#F59E0B','#10B981','#F472B6'])
            C(aud_x, aud_y+aud_h*0.72, aud_h*0.15, color=hc, alpha=0.7, zorder=7)

# ══════════════════════════════════════════════════════════════
# DINO RAPTOR — on golden throne, left side watching
# ══════════════════════════════════════════════════════════════
drx=1.30; dry=0.30
# throne
R(drx-0.38,dry,0.76,0.92,'#0d0020','#FFD700',2,zorder=8)
# throne back
R(drx-0.35,dry+0.88,0.70,1.10,'#0d0020','#7C3AED',2,zorder=8)
P([[drx-0.12,dry+1.98],[drx,dry+2.20],[drx+0.12,dry+1.98]],color='#FFD700',zorder=9)
T(drx,dry+1.44,'DR',color='#FFD700',fontsize=14,fontweight='bold',zorder=9,alpha=0.7)
# aura
for ra,aa in [(0.70,0.05),(0.58,0.08),(0.46,0.12)]:
    C(drx,dry+0.80,ra,color='#7C3AED',alpha=aa,zorder=9)
# DR body on throne
body_pts=np.array([[drx-0.24,dry+0.10],[drx+0.24,dry+0.10],[drx+0.26,dry+0.80],[drx,dry+0.92],[drx-0.26,dry+0.80]])
P(body_pts,color='#B8860B',zorder=10)
P(body_pts,color='#FFD700',fill=False,lw=2,zorder=11)
# wings (folded)
P([[drx,dry+0.70],[drx-0.72,dry+0.88],[drx-0.62,dry+0.44],[drx-0.22,dry+0.52]],color='#4C1D95',alpha=0.85,zorder=9)
P([[drx,dry+0.70],[drx+0.72,dry+0.88],[drx+0.62,dry+0.44],[drx+0.22,dry+0.52]],color='#4C1D95',alpha=0.85,zorder=9)
# head
C(drx,dry+1.08,0.18,color='#2D5A1B',zorder=12)
E(drx,dry+1.00,0.15,0.10,color='#3A7A25',zorder=13)
for ex in [drx-0.07,drx+0.07]:
    C(ex,dry+1.12,0.038,color='#1a0000',zorder=14)
    C(ex,dry+1.12,0.028,color='#FF4500',zorder=15)
    C(ex,dry+1.12,0.012,color='#1a0000',zorder=16)
# crown mini
crown_cx=[drx-0.12,drx-0.10,drx-0.04,drx,drx+0.04,drx+0.10,drx+0.12]
crown_cy=[dry+1.28,dry+1.25,dry+1.28,dry+1.34,dry+1.28,dry+1.25,dry+1.28]
ax.fill_between(crown_cx,crown_cy,dry+1.25,color='#FFD700',zorder=15)
# legs
for lx in [drx-0.14,drx+0.05]:
    R(lx,dry,0.10,0.12,'#B8860B',zorder=10)
# throne glow pool
E(drx,dry,0.60,0.08,color='#FFD700',alpha=0.12,zorder=7)
T(drx,dry-0.14,'SUPREME\nLEADER',color='#FFD700',fontsize=5,fontweight='bold',zorder=10,fontfamily='monospace')

# ══════════════════════════════════════════════════════════════
# TRAPEZE / HIGH WIRE ACT — GANGLE & POMNI
# ══════════════════════════════════════════════════════════════
# trapeze bar
ax.plot([3.50, 5.40],[4.40,4.40],color='#8B4513',lw=4,zorder=9)
ax.plot([3.50,3.50],[4.40,6.10],color='#E5E7EB',lw=1.5,alpha=0.8,zorder=8)
ax.plot([5.40,5.40],[4.40,6.10],color='#E5E7EB',lw=1.5,alpha=0.8,zorder=8)
# GANGLE swinging on trapeze
ggx=4.45; ggy=4.40
# strings holding her
ax.plot([ggx-0.08,ggx-0.06],[ggy,ggy-0.55],color='#E5E7EB',lw=1,alpha=0.8,zorder=9)
ax.plot([ggx+0.08,ggx+0.06],[ggy,ggy-0.55],color='#E5E7EB',lw=1,alpha=0.8,zorder=9)
# body
R(ggx-0.08,ggy-1.18,0.16,0.55,'#F9A8D4',zorder=10)
C(ggx,ggy-0.52,0.10,color='#FFD700',zorder=11)   # gold comedy mask
for ex in [ggx-0.025,ggx+0.025]:
    C(ex,ggy-0.50,0.020,color='#1C1917',zorder=12)
ax.add_patch(Arc((ggx,ggy-0.56),0.06,0.04,angle=0,theta1=200,theta2=340,color='#1C1917',lw=1.5,zorder=12))
# ribbons trailing
for ri in range(5):
    ax.plot([ggx+0.08+ri*0.02,ggx+0.15+ri*0.02],[ggy-0.80-ri*0.08,ggy-0.88-ri*0.10],color='#EC4899',alpha=0.7,lw=2,zorder=9)
T(ggx,ggy-1.48,'GANGLE',color='#F9A8D4',fontsize=5,zorder=12)

# POMNI on platform (scared)
ppx=7.60; ppy=3.80
R(ppx-0.25,ppy,0.50,0.12,'#8B4513',zorder=9)  # platform
R(ppx-0.05,ppy+0.12,0.10,0.22,'#2563EB',zorder=10)  # body
C(ppx,ppy+0.44,0.12,color='#FDDCB0',zorder=10)       # head
C(ppx-0.035,ppy+0.46,0.050,color='#FFFFFF',zorder=11)
C(ppx+0.035,ppy+0.46,0.050,color='#FFFFFF',zorder=11)
C(ppx-0.035,ppy+0.46,0.030,color='#EF4444',zorder=12)
C(ppx+0.035,ppy+0.46,0.030,color='#EF4444',zorder=12)
P([[ppx-0.06,ppy+0.56],[ppx+0.06,ppy+0.56],[ppx+0.02,ppy+0.68],[ppx-0.02,ppy+0.68]],color='#2563EB',zorder=11)
C(ppx,ppy+0.68,0.020,color='#FFD700',zorder=12)
ax.plot([ppx-0.25,ppx-0.25],[ppy+0.06,4.40],color='#E5E7EB',lw=1.5,alpha=0.7,zorder=8)
T(ppx+0.20,ppy+0.36,'HELP',color='#93C5FD',fontsize=5,style='italic',zorder=12)
T(ppx,ppy-0.14,'POMNI',color='#3B82F6',fontsize=5,zorder=12)

# ══════════════════════════════════════════════════════════════
# RING ACTS
# ══════════════════════════════════════════════════════════════
# RAGATHA juggling in center ring
rgx=5.00; rgy=0.22
C(rgx,rgy+0.28,0.11,color='#FDE8D0',zorder=10)  # head
R(rgx-0.06,rgy+0.04,0.12,0.24,'#86EFAC',zorder=10)  # dress
# button eyes
C(rgx-0.028,rgy+0.30,0.020,color='#1C1917',zorder=11)
C(rgx+0.028,rgy+0.30,0.020,color='#1C1917',zorder=11)
# smile
ax.add_patch(Arc((rgx,rgy+0.22),0.06,0.04,angle=0,theta1=200,theta2=340,color='#78716C',lw=1.5,zorder=11))
# juggling balls in arc
for bi,bc in enumerate(['#EF4444','#FBBF24','#3B82F6']):
    bx=rgx-0.24+bi*0.24; by=rgy+0.62+0.18*np.sin(bi*np.pi/2.5)
    C(bx,by,0.055,color=bc,zorder=12)
    ax.plot([rgx-0.02+bi*0.04,bx],[rgy+0.28,by],color='#FFFFFF',lw=0.6,alpha=0.3,zorder=11)
ax.plot([rgx-0.08,rgx-0.28],[rgy+0.22,rgy+0.55],color='#F472B6',lw=3,solid_capstyle='round',zorder=10)  # arm L
ax.plot([rgx+0.08,rgx+0.28],[rgy+0.22,rgy+0.55],color='#F472B6',lw=3,solid_capstyle='round',zorder=10)  # arm R
T(rgx,rgy-0.12,'RAGATHA',color='#F472B6',fontsize=5,zorder=12)

# ZOOBLE doing wheel spin — right of ring
zbx=6.50; zby=0.30
C(zbx,zby+0.22,0.10,color='#34D399',zorder=10)
ax.add_patch(Wedge((zbx,zby+0.22),0.10,270,90,color='#F87171',zorder=11))
R(zbx-0.05,zby+0.04,0.10,0.18,'#34D399',zorder=10)
# wheel spinning
C(zbx+0.20,zby+0.08,0.075,color='#F87171',zorder=11)
C(zbx+0.20,zby+0.08,0.035,color='#1C1917',zorder=12)
for wa in range(0,360,45):
    ax.plot([zbx+0.20,zbx+0.20+0.070*np.cos(np.radians(wa))],
            [zby+0.08,zby+0.08+0.070*np.sin(np.radians(wa))],color='#FFFFFF',lw=0.8,alpha=0.7,zorder=12)
# speed lines
for sl in range(4):
    ax.plot([zbx+0.30+sl*0.08,zbx+0.55+sl*0.06],[zby+0.05,zby+0.05+sl*0.02],color='#F87171',lw=1,alpha=0.4,zorder=9)
T(zbx,zby-0.12,'ZOOBLE',color='#34D399',fontsize=5,zorder=12)

# KINGER — nervous near ring edge
kkx=3.50; kky=0.30
R(kkx-0.055,kky+0.04,0.11,0.20,'#F59E0B',zorder=10)  # body
C(kkx,kky+0.36,0.12,color='#F59E0B',zorder=10)          # chess head
R(kkx-0.075,kky+0.30,0.15,0.04,'#1C1917',zorder=11)    # visor
C(kkx-0.028,kky+0.32,0.018,color='#F97316',zorder=12)
C(kkx+0.028,kky+0.32,0.018,color='#F97316',zorder=12)
# cross
ax.plot([kkx,kkx],[kky+0.48,kky+0.58],color='#DC2626',lw=4,zorder=11)
ax.plot([kkx-0.04,kkx+0.04],[kky+0.53,kky+0.53],color='#DC2626',lw=4,zorder=11)
for swx,swy in [(kkx-0.12,kky+0.44),(kkx+0.13,kky+0.40),(kkx,kky+0.64)]:
    C(swx,swy,0.010,color='#93C5FD',alpha=0.9,zorder=13)
T(kkx,kky-0.12,'KINGER',color='#F59E0B',fontsize=5,zorder=12)
T(kkx,kky+0.80,'...THE ANTS',color='#FCD34D',fontsize=4,style='italic',zorder=12)

# BUBBLE floating above ring
bbx=5.0; bby=3.00
for br,ba,bc in [(0.30,0.04,'#7DD3FC'),(0.24,0.08,'#BAE6FD'),(0.18,0.55,'#BAE6FD')]:
    C(bbx,bby,br,color=bc,alpha=ba,zorder=8)
C(bbx,bby,0.18,color='#BAE6FD',alpha=0.55,zorder=9)
C(bbx,bby,0.18,color='none',edgecolor='#7DD3FC',lw=1.5,alpha=0.8,zorder=10)
for fa2,fb2,sc2 in [(20,70,'#A78BFA'),(90,140,'#34D399'),(150,220,'#FB923C')]:
    ax.add_patch(Arc((bbx,bby),0.34,0.34,angle=0,theta1=fa2,theta2=fb2,color=sc2,lw=2,alpha=0.6,zorder=10))
C(bbx-0.06,bby+0.06,0.04,color='#FFFFFF',alpha=0.4,zorder=11)
C(bbx-0.018,bby+0.018,0.010,color='#0C4A6E',zorder=12)
C(bbx+0.018,bby+0.018,0.010,color='#0C4A6E',zorder=12)
E(bbx,bby-0.44,0.20,0.05,color='#0C4A6E',alpha=0.25,zorder=7)  # shadow
T(bbx,bby+0.30,'🫧',fontsize=14,alpha=0.7,zorder=13)
T(bbx,bby-0.26,'BUBBLE',color='#BAE6FD',fontsize=5,zorder=12)

# JAX leaning on ring post — bored
jax=8.70; jay=0.25
# post
ax.plot([jax,jax],[jay,jay+1.20],color='#B8860B',lw=5,zorder=9)
C(jax,jay+1.22,0.06,color='#FFD700',zorder=9)
# JAX
R(jax-0.055,jay+0.04,0.11,0.28,'#8B5CF6',zorder=10)
C(jax,jay+0.44,0.12,color='#8B5CF6',zorder=10)
for ex in [jax-0.04,jax+0.04]:
    C(ex,jay+0.46,0.030,color='#FFFFFF',zorder=11)
    C(ex,jay+0.46,0.016,color='#10B981',zorder=12)
# eyelid (bored)
ax.fill_between([ex-0.033,ex+0.033],[jay+0.47,jay+0.47],[jay+0.50,jay+0.50],color='#8B5CF6',alpha=0.9,zorder=13)
# ears
E(jax-0.04,jay+0.68,0.04,0.18,color='#8B5CF6',zorder=10)
E(jax+0.04,jay+0.68,0.04,0.18,color='#8B5CF6',zorder=10)
# arm leaning on post
ax.plot([jax-0.055,jax],[jay+0.26,jay+0.68],color='#8B5CF6',lw=5,solid_capstyle='round',zorder=10)
T(jax+0.28,jay+0.55,'yawn.',color='#A78BFA',fontsize=5,style='italic',zorder=12)
T(jax,jay-0.12,'JAX',color='#8B5CF6',fontsize=5,zorder=12)

# ══════════════════════════════════════════════════════════════
# CURTAINED ENTRANCE — center bottom
# ══════════════════════════════════════════════════════════════
R(4.30,0,0.60,1.80,'#8B0000',zorder=7)
R(5.10,0,0.60,1.80,'#8B0000',zorder=7)
P([[4.30,1.80],[5.00,1.50],[5.70,1.80]],color='#FFD700',zorder=8)
# golden arch
ax.add_patch(Arc((5.0,1.80),1.40,0.70,angle=0,theta1=0,theta2=180,color='#FFD700',lw=4,zorder=8))
T(5.0,2.10,'ENTER',color='#FFD700',fontsize=7,fontweight='bold',fontfamily='monospace',zorder=9)

# ══════════════════════════════════════════════════════════════
# TITLE
# ══════════════════════════════════════════════════════════════
R(0.4,6.10,9.2,0.38,'#0d0000','#DC2626',2,zorder=20)
T(5.0,6.29,'🎪  THE AMAZING DIGITAL CIRCUS  —  INSIDE THE BIG TOP  🎪',
  color='#FFD700',fontsize=12,fontweight='bold',fontfamily='monospace',zorder=21)

plt.tight_layout(pad=0.2)
print("✅ Circus Tent Interior rendered!")
print("   🎪 Red/white stripe dome ceiling with slingers and bunting")
print("   🏟  Arena floor — sawdust ring with gold border")
print("   👥  3 rows of audience silhouettes surrounding the ring")
print("   💡  6 dramatic spotlights from ceiling")
print("   🐉  Dino Raptor on golden throne watching left side")
print("   🎭  Gangle swinging on trapeze, ribbons trailing")
print("   🃏  Pomni terrified on high platform")
print("   🧸  Ragatha juggling 3 balls centre ring")
print("   🧩  Zooble wheel-spinning right of ring")
print("   ♔   Kinger sweating nervously near ring edge")
print("   🫧  Bubble floating above the ring")
print("   🐇  Jax leaning on post — bored")


import json
import random
import string
import time

# ─────────────────────────────────────────────
#  AMAZING DIGITAL CIRCUS — MULTIPLAYER SYSTEM
# ─────────────────────────────────────────────

PLATFORMS = ["PC", "PS5"]
MAX_PLAYERS_PER_ROOM = 16

def generate_room_code(length=6):
    """Generate a random uppercase alphanumeric room code."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def create_player(name: str, platform: str = "PC") -> dict:
    if name.strip().lower() in ["dino raptor", "dinoraptor", "dino_raptor"]:
        role = "Supreme Leader"
        powers = ["fly", "teleport", "phase_through_walls", "reality_control"]
        badge = "👑 SUPREME LEADER"
    else:
        role = "Player"
        powers = []
        badge = "🎮 Player"
    return {
        "name": name.strip(),
        "platform": platform.upper(),
        "role": role,
        "powers": powers,
        "badge": badge,
        "joined_at": time.time(),
        "room_id": None,
    }

def create_room(host_name: str, room_name: str, private: bool = False) -> dict:
    code = generate_room_code() if private else None
    room_id = generate_room_code(8)
    return {
        "room_id": room_id,
        "room_name": room_name,
        "host": host_name,
        "private": private,
        "code": code,            # None for public rooms
        "players": [],
        "max_players": MAX_PLAYERS_PER_ROOM,
        "created_at": time.time(),
        "platform": "PC + PS5",
    }

def join_room(room: dict, player: dict, code_input: str = None) -> dict:
    """Returns {'success': bool, 'message': str}"""
    if len(room["players"]) >= room["max_players"]:
        return {"success": False, "message": "❌ Room is full!"}
    if room["private"]:
        if code_input is None or code_input.strip().upper() != room["code"]:
            return {"success": False, "message": "❌ Wrong room code! Ask the host for the code."}
    if player["name"] in [p["name"] for p in room["players"]]:
        return {"success": False, "message": "⚠️ You are already in this room."}
    room["players"].append(player)
    player["room_id"] = room["room_id"]
    return {"success": True, "message": f"✅ {player['name']} joined '{room['room_name']}'!"}

def leave_room(room: dict, player_name: str) -> dict:
    before = len(room["players"])
    room["players"] = [p for p in room["players"] if p["name"] != player_name]
    if len(room["players"]) < before:
        return {"success": True, "message": f"👋 {player_name} left the room."}
    return {"success": False, "message": "Player not found in room."}

def get_public_rooms(rooms: list) -> list:
    """Return only public rooms (hide private room codes)."""
    return [
        {k: v for k, v in r.items() if k != "code"}
        for r in rooms if not r["private"]
    ]

# ─── Demo: pre-made rooms ────────────────────
demo_rooms = [
    create_room("Dino Raptor", "🏰 Throne Room HQ", private=False),
    create_room("Ragatha",     "🌊 Beach Party",    private=False),
    create_room("Jax",         "🕳️ Void Club",      private=True),
    create_room("Kinger",      "🎡 Kermis Madness", private=False),
]

# Dino Raptor auto-joins Throne Room as Supreme Leader
_dino = create_player("Dino Raptor", "PC")
join_room(demo_rooms[0], _dino)

multiplayer_config = {
    "game_name": "The Amazing Digital Circus — Online",
    "platforms": PLATFORMS,
    "max_players_per_room": MAX_PLAYERS_PER_ROOM,
    "features": [
        "Public rooms — join instantly",
        "Private rooms — 6-char secret code",
        "PC & PS5 cross-platform",
        "Real-time WebSocket sync",
        "Dino Raptor = auto Supreme Leader",
    ],
    "demo_rooms": demo_rooms,
}

# ─── Print summary ───────────────────────────
print("=" * 60)
print("  🌐 AMAZING DIGITAL CIRCUS — MULTIPLAYER SERVER LOGIC")
print("=" * 60)
for r in demo_rooms:
    lock = "🔒 PRIVATE" if r["private"] else "🌍 PUBLIC "
    code_str = f" | code: {r['code']}" if r["private"] else ""
    count = len(r["players"])
    print(f"  {lock}  {r['room_name']:<22} | {count}/{r['max_players']} players{code_str}")

print()
print("  Functions exported:")
for fn in ["create_player", "create_room", "join_room", "leave_room", "get_public_rooms", "generate_room_code"]:
    print(f"    ✅  {fn}()")
print()
print(f"  Platforms : {', '.join(PLATFORMS)}")
print(f"  Max/room  : {MAX_PLAYERS_PER_ROOM} players")
print("=" * 60)


import json

# ══════════════════════════════════════════════════════════════════════
#  🎮 DINO-RAPTOR-BLUE-KILLER  —  FULL GAME SPECIFICATION v4.0
#  Search this name on PC Store (itch.io / Microsoft Store) or PS5 Store
# ══════════════════════════════════════════════════════════════════════

store_listing = {
    "app_id": "dino-raptor-blue-killer",
    "display_name": "🎪 Amazing Digital Circus Online",
    "search_tags": ["dino-raptor-blue-killer", "digital circus", "online multiplayer", "cartoon", "sandbox"],
    "short_description": "Join the Amazing Digital Circus! Pick your character, explore 7 wild zones, hang out in your room, chat, call friends, and play with anyone on PC or PS5.",
    "age_rating": "13+",
    "platforms": ["PC", "PS5", "Browser (Chrome, Edge, PS5 Browser)"],
    "genre": ["Sandbox", "Social", "Multiplayer", "Adventure"],
    "developer": "Dino Raptor Blue Killer Studios",
    "version": "4.0.0",
    "how_to_play": "Search 'dino-raptor-blue-killer' in your store OR open the link in Chrome / PS5 browser — the game loads instantly, no download needed.",
    "features": [
        "Play as any character or create your own",
        "Choose your name and gender (boy/girl)",
        "Private rooms with secret code",
        "Real-time voice chat, text chat, calling",
        "7 explorable world zones",
        "Personal room with PC, laptop, bed, bathroom, PS5 screen, phone",
        "Actions: sleep, eat, smoke, vape, drink, drink alcohol",
        "Every character has a gun (no bazooka)",
        "Talk to NPCs and characters — they talk back",
        "Realistic character forms with physics (women have realistic bodies)",
        "Family-friendly speech filter (no swearing, no middle finger)",
        "Lock your room for privacy",
        "Fly, teleport, phase through walls (Dino Raptor only)",
        "Leaderboard + private servers",
    ],
}

# ══════════════════════════════════════════════════════════════════════
#  👤  CHARACTER ROSTER  (all with reallife forms)
# ══════════════════════════════════════════════════════════════════════

game_characters = {
    "dino_raptor": {
        "id": "dino_raptor",
        "name": "Dino Raptor",
        "emoji": "🐉",
        "role": "Supreme Leader",
        "gender": "male",
        "cartoon_form": {
            "colors": {"primary": "#FFD700", "secondary": "#7C3AED", "accent": "#FF6B00"},
            "shape": "raptor/dragon hybrid, gold armor, purple wings, glowing eyes, crown",
            "size": "GIANT",
            "aura": "gold + purple power rings",
        },
        "reallife_form": {
            "build": "tall, muscular, athletic",
            "skin": "dark scales with gold shimmer",
            "hair": "black with gold tips",
            "outfit": "black gold-trim jacket, boots, crown accessory",
            "eyes": "glowing amber/gold",
            "wings": "large dark purple feathered wings folded on back",
            "physics": {"cloth_sim": True, "wing_movement": True, "hair_physics": True},
        },
        "powers": ["fly", "teleport", "phase_walls", "reality_control", "kick_players"],
        "power_level": "BEYOND_MAXIMUM",
        "zone": "Throne Room",
        "items": ["crown", "golden_gun", "phone", "gaming_pc", "ps5"],
        "npc_dialogues": [
            "Welcome to MY circus. Try to keep up.",
            "I built this world. Every pixel belongs to me.",
            "Need something? Ask nicely.",
            "Nobody leaves without my permission. Just kidding... or am I?",
        ],
    },
    "pomni": {
        "id": "pomni",
        "name": "Pomni",
        "emoji": "🃏",
        "role": "Protagonist / Jester",
        "gender": "female",
        "cartoon_form": {
            "colors": {"primary": "#4FC3F7", "secondary": "#E91E63", "accent": "#FFFFFF"},
            "shape": "jester hat with bells, diamond bodysuit, huge terrified eyes",
            "size": "medium",
        },
        "reallife_form": {
            "build": "slim, average height",
            "skin": "pale",
            "hair": "light blue twin pigtails with jester bells",
            "outfit": "blue/white diamond bodysuit, ruffle collar, jester hat",
            "eyes": "huge blue eyes, always wide open",
            "physics": {"cloth_sim": True, "hair_physics": True, "breast_physics": True},
        },
        "powers": [],
        "power_level": "LOW",
        "zone": "Circus Tent",
        "items": ["phone", "pistol", "jester_bells"],
        "personality": "terrified, anxious, trying her best",
        "npc_dialogues": [
            "I don't know how I got here but I really want to leave.",
            "Has anyone seen a way out? Asking for me.",
            "Okay okay okay. I can do this. Probably.",
            "Why is everything so... much?",
        ],
    },
    "ragatha": {
        "id": "ragatha",
        "name": "Ragatha",
        "emoji": "🧸",
        "role": "Rag Doll / Optimist",
        "gender": "female",
        "cartoon_form": {
            "colors": {"primary": "#E91E63", "secondary": "#FF8A80", "accent": "#FFFFFF"},
            "shape": "rag doll seams, button eyes, polka dot dress, yarn hair",
            "size": "medium",
        },
        "reallife_form": {
            "build": "petite, soft features",
            "skin": "light with visible stitch marks on cheeks",
            "hair": "red yarn-like braids with pink bows",
            "outfit": "pink polka-dot dress, white apron, button brooch",
            "eyes": "warm button-like brown eyes",
            "physics": {"cloth_sim": True, "hair_physics": True, "breast_physics": True},
        },
        "powers": [],
        "power_level": "LOW",
        "zone": "Fairground",
        "items": ["phone", "pistol", "sewing_kit"],
        "personality": "cheerful, optimistic, caring",
        "npc_dialogues": [
            "Hey! You look like you could use a friend!",
            "Everything will be okay, I just know it!",
            "Want to explore the fairground together?",
            "I made this! What do you think?",
        ],
    },
    "jax": {
        "id": "jax",
        "name": "Jax",
        "emoji": "🐇",
        "role": "Trickster / Rabbit",
        "gender": "male",
        "cartoon_form": {
            "colors": {"primary": "#7C3AED", "secondary": "#C084FC", "accent": "#1a1a2e"},
            "shape": "tall lanky rabbit, long ears, bored eyes, smirk, belly patch",
            "size": "tall-slim",
        },
        "reallife_form": {
            "build": "tall, lanky, slouchy posture",
            "skin": "purple-tinted pale",
            "hair": "white with purple highlights, messy",
            "outfit": "dark hoodie, ripped jeans, sneakers, rabbit ear hoodie attachment",
            "eyes": "half-closed purple eyes, permanent smirk",
            "physics": {"cloth_sim": True, "hair_physics": True},
        },
        "powers": ["minor_teleport"],
        "power_level": "MEDIUM",
        "zone": "The Void",
        "items": ["phone", "pistol", "playing_cards"],
        "personality": "sarcastic, bored, secretly caring",
        "npc_dialogues": [
            "Oh great, another one. Welcome to the fun house. Not.",
            "Yeah yeah I'll help. Don't make it weird.",
            "Bored. So incredibly bored. What do you want.",
            "That was actually kind of impressive. Don't tell anyone I said that.",
        ],
    },
    "gangle": {
        "id": "gangle",
        "name": "Gangle",
        "emoji": "🎭",
        "role": "Marionette / Sad Clown",
        "gender": "female",
        "cartoon_form": {
            "colors": {"primary": "#FF8A80", "secondary": "#FFD700", "accent": "#4FC3F7"},
            "shape": "puppet strings from above, comedy+tragedy masks, ribbon body, crossbar",
            "size": "medium-tall",
        },
        "reallife_form": {
            "build": "slim, graceful, moves like a dancer",
            "skin": "very pale, translucent-looking",
            "hair": "long ribbon-like pink strands, always flowing",
            "outfit": "layered pastel ribbons, theatre masks hanging from belt",
            "eyes": "big sorrowful blue eyes with pink eyeshadow",
            "special": "faint glowing strings visible above shoulders",
            "physics": {"cloth_sim": True, "hair_physics": True, "ribbon_physics": True, "breast_physics": True},
        },
        "powers": [],
        "power_level": "LOW",
        "zone": "The Void",
        "items": ["phone", "pistol", "theatre_masks"],
        "personality": "dramatic, emotional, sweet-hearted",
        "npc_dialogues": [
            "Oh... hello. I was just... expressing my feelings through movement.",
            "The void isn't so bad once you accept the emptiness. Just kidding, it's terrible.",
            "I can show you my happy mask if you want? Or my sad one. I mostly use the sad one.",
            "You came to talk to me? That's... that's the nicest thing.",
        ],
    },
    "zooble": {
        "id": "zooble",
        "name": "Zooble",
        "emoji": "🧩",
        "role": "Shapeshifter / Grumpy",
        "gender": "non_binary",
        "cartoon_form": {
            "colors": {"primary": "#4CAF50", "secondary": "#F44336", "accent": "#FFEB3B"},
            "shape": "split green/red mismatched body, star eye, round eye, flipper, claw, wheel, antennae",
            "size": "medium",
        },
        "reallife_form": {
            "build": "medium, asymmetric — left side slightly different to right",
            "skin": "green left, red-tinted right, with visible seam down center",
            "hair": "short spiky green/red split-dyed, one antenna accessory",
            "outfit": "mismatched two-tone outfit, one sneaker one boot",
            "eyes": "star-shaped left eye, circle right eye",
            "physics": {"cloth_sim": True, "antenna_wobble": True},
        },
        "powers": ["shapeshift_parts"],
        "power_level": "MEDIUM",
        "zone": "Beach",
        "items": ["phone", "pistol", "puzzle_pieces"],
        "personality": "grumpy, blunt, secretly funny",
        "npc_dialogues": [
            "What. What do you want.",
            "Fine. I'll help. But I'm not happy about it.",
            "The beach is the only place I feel like myself. Don't ruin it.",
            "I'm not weird. Everything else is weird.",
        ],
    },
    "kinger": {
        "id": "kinger",
        "name": "Kinger",
        "emoji": "♔",
        "role": "Chess King / Paranoid Elder",
        "gender": "male",
        "cartoon_form": {
            "colors": {"primary": "#FFD700", "secondary": "#FFFFFF", "accent": "#B22222"},
            "shape": "chess king head, crown with red cross, wide nervous eyes, sweat drops",
            "size": "medium-wide",
        },
        "reallife_form": {
            "build": "stocky, older gentleman, always sweating",
            "skin": "pale, always looks nervous",
            "hair": "white fluffy side hair, bald top, chess piece crown hat",
            "outfit": "royal gold coat with red cross emblem, white gloves, boots",
            "eyes": "wide perpetually-terrified brown eyes",
            "physics": {"cloth_sim": True, "sweat_particles": True},
        },
        "powers": ["chess_strategy"],
        "power_level": "MEDIUM",
        "zone": "Sun Zone",
        "items": ["phone", "pistol", "chess_set"],
        "personality": "paranoid, wise, surprisingly brave",
        "npc_dialogues": [
            "Oh! Oh dear. A visitor. Is that — are you friendly? Please be friendly.",
            "I've been here the longest. Seen things. Terrible things. Also nice things.",
            "The sun is very hot today. It was also hot yesterday. And the day before.",
            "Chess? Want to play chess? I always win but I'll let you think you're doing well.",
        ],
    },
    "bubble": {
        "id": "bubble",
        "name": "Bubble",
        "emoji": "🫧",
        "role": "Floating Helper Sphere",
        "gender": "non_binary",
        "cartoon_form": {
            "colors": {"primary": "#E0F7FA", "secondary": "#B2EBF2", "accent": "#FFD700"},
            "shape": "iridescent sphere, rainbow shimmer, floating shadow",
            "size": "small",
        },
        "reallife_form": {
            "build": "floats — no legs, hovers at eye level",
            "skin": "translucent pearl with rainbow iridescence",
            "hair": "none — smooth sphere head",
            "outfit": "no clothes — body is a glowing orb",
            "eyes": "two simple glowing dots",
            "special": "leaves faint bubble trail when moving",
            "physics": {"float_bob": True, "trail_particles": True},
        },
        "powers": ["float", "phase_walls", "buff_nearby_players"],
        "power_level": "SUPPORT",
        "zone": "Circus Tent",
        "items": ["phone"],
        "personality": "cheerful, simple, lovable",
        "npc_dialogues": [
            "Bloop! Hi!",
            "Bubble! Bubble bubble!",
            "Bloooop. That means I like you.",
            "*happy floating noises*",
        ],
    },
}

# ══════════════════════════════════════════════════════════════════════
#  🏠  ROOM CONFIGURATION  (every player has this room)
# ══════════════════════════════════════════════════════════════════════

room_config = {
    "items": {
        "gaming_pc": {
            "label": "🖥 Gaming PC",
            "use": "Play games only — opens game launcher overlay",
            "rgb": True,
            "specs": "Ultra RTX 9090, 128GB RAM, 10TB SSD",
        },
        "gaming_laptop": {
            "label": "💻 Gaming Laptop",
            "use": "Gaming OR chat OR bellen (video call)",
            "rgb": True,
            "open_apps": ["Chat", "Call", "Browser", "Games"],
        },
        "bed": {
            "label": "🛏 King Bed",
            "use": "Sleep action — restores energy, plays sleep animation",
            "neon_underglow": True,
            "customizable": True,
        },
        "bathroom": {
            "label": "🚿 Bathroom",
            "use": "Private zone inside room, lockable separately",
            "items": ["shower", "sink", "mirror", "toilet"],
        },
        "ps5_screen": {
            "label": "📺 PS5 Screen",
            "use": "Play PS5 games in-room, share screen with visitors",
            "size": "77-inch curved OLED",
        },
        "phone": {
            "label": "📱 Smartphone",
            "use": "Text berichten, voice calls, video bellen, apps",
            "always_in_inventory": True,
            "apps": ["Messages", "Call", "Camera", "Social", "Map", "Shop"],
        },
        "gun": {
            "label": "🔫 Sidearm",
            "use": "Combat — non-lethal in safe zones, combat in battle zones",
            "types": ["pistol", "rifle", "shotgun", "smg", "sniper"],
            "restricted": ["bazooka", "rpg", "nuclear"],
            "note": "NO bazooka ever. No exceptions.",
        },
        "room_lock": {
            "label": "🔒 Room Lock",
            "use": "Lock room so nobody can enter without your permission",
            "override": "Dino Raptor can always enter (Supreme Leader)",
        },
    },
    "actions": {
        "sleep": {"animation": "character lies down, snore particles, stars above head", "effect": "+50 energy"},
        "eat": {"animation": "character sits, eating bowl animation, yum particles", "effect": "+30 hunger"},
        "smoke": {"animation": "cigarette spark, smoke cloud drifts", "effect": "cosmetic only", "age_gate": "13+"},
        "vape": {"animation": "vape pen glow, large flavored vapor cloud", "effect": "cosmetic only", "age_gate": "13+"},
        "drink": {"animation": "glass/can sip, gulp sound", "effect": "+20 thirst"},
        "drink_alcohol": {"animation": "bottle sip, sway slightly, rosy cheeks", "effect": "cosmetic only", "age_gate": "18+ visual, 13+ allowed in game"},
    },
}

# ══════════════════════════════════════════════════════════════════════
#  💬  DIALOGUE SYSTEM  (NPC + character two-way speech)
# ══════════════════════════════════════════════════════════════════════

dialogue_system = {
    "features": ["text_chat", "voice_chat", "video_bellen", "berichten", "npc_ai_response", "character_voice"],
    "filters": {
        "swearing": "BLOCKED — replaced with 🎉 or ⭐",
        "middle_finger": "BLOCKED — emoji replaced with 👋",
        "hate_speech": "BLOCKED",
        "spam": "RATE LIMITED",
    },
    "npc_behavior": "NPCs respond contextually using their dialogue bank + simple AI pattern matching",
    "voice_chat": "Push-to-talk or open mic — spatial audio (louder when closer)",
    "bellen": "Direct 1-on-1 or group video/voice call via phone item",
    "berichten": "Persistent text messages stored per room/contact",
    "languages": ["Dutch", "English", "Auto-detect"],
}

# ══════════════════════════════════════════════════════════════════════
#  🌍  WORLD ZONES  (7 explorable)
# ══════════════════════════════════════════════════════════════════════

world_zones = {
    "void":       {"name": "The Void",    "emoji": "🌑", "mood": "glitch/dark",      "color": "#1a0030", "residents": ["jax","gangle"]},
    "moon":       {"name": "Moon",        "emoji": "🌙", "mood": "calm/mysterious",   "color": "#1a1a3e", "residents": ["pomni"]},
    "sun":        {"name": "Sun Zone",    "emoji": "☀",  "mood": "hot/intense",       "color": "#FF6B00", "residents": ["kinger"]},
    "beach":      {"name": "Beach",       "emoji": "🏖",  "mood": "chill/sunny",       "color": "#00BCD4", "residents": ["zooble"]},
    "fairground": {"name": "Fairground",  "emoji": "🎡", "mood": "fun/colorful",      "color": "#E91E63", "residents": ["ragatha","kinger"]},
    "circus_tent":{"name": "Circus Tent", "emoji": "🎪", "mood": "exciting/chaotic",  "color": "#FF1744", "residents": ["pomni","bubble"]},
    "throne_room":{"name": "Throne Room", "emoji": "🏰", "mood": "powerful/dark",     "color": "#FFD700", "residents": ["dino_raptor"]},
}

# ══════════════════════════════════════════════════════════════════════
#  🎮  SUMMARY PRINT
# ══════════════════════════════════════════════════════════════════════

print("=" * 70)
print("  🎮 DINO-RAPTOR-BLUE-KILLER — GAME SPEC v4.0")
print("=" * 70)
print(f"\n  📦 App ID     : {store_listing['app_id']}")
print(f"  🎮 Platforms  : {', '.join(store_listing['platforms'])}")
print(f"  🔞 Age Rating : {store_listing['age_rating']}")
print(f"\n  👥 Characters : {len(game_characters)}")
for cid, c in game_characters.items():
    rl = c["reallife_form"]
    bp = "✅ breast physics" if rl.get("physics", {}).get("breast_physics") else "  —"
    print(f"     {c['emoji']}  {c['name']:15s}  [{c['gender']:12s}]  {bp}")
print(f"\n  🌍 World Zones: {len(world_zones)}")
for zid, z in world_zones.items():
    print(f"     {z['emoji']}  {z['name']:15s}  residents: {', '.join(z['residents'])}")
print(f"\n  🏠 Room Items : {len(room_config['items'])}")
for iid, item in room_config["items"].items():
    print(f"     {item['label']:25s}  {item['use'][:45]}")
print(f"\n  💬 Dialogue   : {', '.join(dialogue_system['features'])}")
print(f"  🚫 Filters    : swearing BLOCKED | middle finger BLOCKED")
print("\n" + "=" * 70)
print("  ✅ Full spec exported → game_characters, room_config, world_zones")
print("  ✅ Store listing      → store_listing")
print("  ✅ Dialogue system    → dialogue_system")
print("=" * 70)


import os

# ══════════════════════════════════════════════════════════════
#  STREAMLIT COMMUNITY CLOUD EXPORT
#  Writes: app.py + requirements.txt
#  Upload both files to GitHub → deploy on share.streamlit.io
# ══════════════════════════════════════════════════════════════

APP_CODE = '''import streamlit as st
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
@import url(\'https://fonts.googleapis.com/css2?family=Creepster&family=Fredoka+One&family=Share+Tech+Mono&display=swap\');
html, body, [class*="css"] { background:#05000f !important; color:#fbfbff !important; font-family:\'Fredoka One\',sans-serif; }
.stApp { background: radial-gradient(ellipse at top, #1a003a 0%, #05000f 70%); }
h1 { font-family:\'Creepster\',cursive; color:#FFD700; font-size:2.8em; text-shadow:0 0 20px #ffd40088,0 0 40px #a855f755; margin-bottom:0; }
h2,h3 { color:#A1C9F4; }
.stButton>button { background:linear-gradient(135deg,#7C3AED,#A855F7); color:#fbfbff; border:2px solid #FFD700; border-radius:14px; font-family:\'Fredoka One\',sans-serif; font-size:1.05em; padding:0.4em 1.2em; transition:all 0.2s; }
.stButton>button:hover { background:linear-gradient(135deg,#FFD700,#FF6B00); color:#1a003a; transform:scale(1.04); }
.stTextInput>div>div>input { background:#1a003a; color:#fbfbff; border:2px solid #7C3AED; border-radius:10px; font-family:\'Fredoka One\',sans-serif; }
.stSelectbox>div>div { background:#1a003a; color:#fbfbff; border:2px solid #7C3AED; border-radius:10px; }
.stRadio>div { background:#1a003a22; border-radius:10px; padding:8px; }
.stTabs [data-baseweb="tab-list"] { background:#1a003a; border-radius:12px; }
.stTabs [data-baseweb="tab"] { color:#A1C9F4; font-family:\'Fredoka One\',sans-serif; font-size:1em; }
.stTabs [aria-selected="true"] { color:#FFD700 !important; border-bottom:3px solid #FFD700; }
.stExpander { background:#1a003a55; border:1px solid #7C3AED44; border-radius:12px; }
div[data-testid="stMetricValue"] { color:#FFD700; font-family:\'Creepster\',cursive; font-size:2em; }
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
    "Pomni":   ["I don\'t know how I got here but I really want to leave.","Has anyone seen a way out? Asking for me.","Okay okay okay. I can do this. Probably."],
    "Ragatha": ["Hey! You look like you could use a friend!","Everything will be okay, I just know it!","Want to explore together?"],
    "Jax":     ["Oh great, another one. Welcome to the fun house. Not.","Yeah yeah I\'ll help. Don\'t make it weird.","Bored. So incredibly bored."],
    "Gangle":  ["Oh... hello. I was just expressing my feelings.","The void isn\'t so bad once you accept the emptiness.","You came to talk to me? That\'s the nicest thing."],
    "Zooble":  ["What. What do you want.","Fine. I\'ll help. But I\'m not happy about it.","The beach is the only place I feel like myself."],
    "Kinger":  ["Oh! Oh dear. A visitor. Is that — are you friendly?","I\'ve been here the longest. Seen things.","Chess? Want to play chess?"],
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

def gen_code(): return \'\'.join(random.choices(string.ascii_uppercase+string.digits, k=6))
def is_dino(): return st.session_state.username.strip().lower() in ["dino raptor","dino_raptor","dinoraptor"]

def page_store():
    st.markdown("<h1>🐉 DINO-RAPTOR-BLUE-KILLER</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style=\'color:#A1C9F4;margin-top:0\'>🎪 Amazing Digital Circus — Online</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2,1,1])
    with col1:
        st.markdown("""
        <div style=\'background:linear-gradient(135deg,#1a003a,#2d0060);border:2px solid #FFD700;border-radius:18px;padding:24px;\'>
        <p style=\'color:#fbfbff;font-size:1.1em;\'>
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
        <div style=\'background:#1a003a;border:2px solid #7C3AED;border-radius:14px;padding:16px;text-align:center;\'>
        <div style=\'font-size:4em;\'>🎪</div>
        <div style=\'color:#FFD700;font-size:1.3em;font-family:Creepster,cursive;\'>AMAZING</div>
        <div style=\'color:#fbfbff;font-size:0.9em;\'>DIGITAL CIRCUS</div>
        <div style=\'color:#A1C9F4;font-size:0.8em;margin-top:8px;\'>v4.0 Online</div></div>""", unsafe_allow_html=True)
        st.markdown("""
        <div style=\'background:#0a1a0a;border:2px solid #17b26a;border-radius:10px;padding:10px;margin-top:8px;text-align:center;\'>
        <div style=\'color:#17b26a;font-size:0.85em;\'>🟢 AVAILABLE ON</div>
        <div style=\'color:#fbfbff;font-size:0.9em;\'>PC • PS5 • Browser</div>
        <div style=\'color:#909094;font-size:0.75em;margin-top:4px;\'>Search: dino-raptor-blue-killer</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style=\'background:#1a1a0a;border:2px solid #FFD700;border-radius:14px;padding:16px;text-align:center;\'>
        <div style=\'color:#FFD700;font-size:1.1em;\'>🎮 HOW TO PLAY</div>
        <div style=\'color:#fbfbff;font-size:0.85em;margin-top:8px;\'>
        <b>PC:</b> Open this URL<br><br><b>PS5:</b> Browser → paste URL<br><br><b>Chrome:</b> Paste URL → play!
        </div></div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("🎭 Meet the Characters")
    char_cols = st.columns(9)
    for i,(cid,c) in enumerate(CHARACTERS.items()):
        with char_cols[i]:
            st.markdown(f"""
            <div style=\'background:{c["color"]}22;border:2px solid {c["color"]};border-radius:12px;padding:8px;text-align:center;\'>
            <div style=\'font-size:2.2em;\'>{c["emoji"]}</div>
            <div style=\'color:{c["color"]};font-size:0.8em;font-weight:bold;\'>{c["name"]}</div>
            <div style=\'color:#909094;font-size:0.65em;\'>{c["role"]}</div></div>""", unsafe_allow_html=True)
    st.markdown("---")
    _,col_b,_ = st.columns(3)
    with col_b:
        if st.button("🚀  PLAY NOW  —  FREE", use_container_width=True):
            st.session_state.page = "age_gate"; st.rerun()

def page_age_gate():
    st.markdown("<h1>🔞 Age Verification</h1>", unsafe_allow_html=True)
    _,c2,_ = st.columns([1,2,1])
    with c2:
        st.markdown("""<div style=\'background:#1a003a;border:2px solid #FFD700;border-radius:18px;padding:28px;text-align:center;\'>
        <div style=\'font-size:3em;\'>🎂</div><h3 style=\'color:#FFD700;\'>How old are you?</h3></div>""", unsafe_allow_html=True)
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
            format_func=lambda k: f"{CHARACTERS[k][\'emoji\']} {CHARACTERS[k][\'name\']} — {CHARACTERS[k][\'role\']}")
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
        <div style=\'background:linear-gradient(135deg,{ch["color"]}22,#1a003a);border:3px solid {ch["color"]};border-radius:20px;padding:28px;text-align:center;\'>
        <div style=\'font-size:5em;\'>{ch["emoji"]}</div>
        <h2 style=\'color:{ch["color"]};margin:8px 0;\'>{username if username else "???"}</h2>
        <div style=\'color:#A1C9F4;\'>{ch["role"]} · {gender}</div>
        {"<div style=\\"color:#FFD700;font-size:1.1em;margin-top:8px;\\">👑 SUPREME LEADER 👑</div>" if is_dr else ""}
        <hr style=\'border-color:{ch["color"]}44;\'/>
        <div style=\'text-align:left;\'>
        Skin: {skin} | Hair: {hair} ({hair_c})<br>Outfit: {outfit} | Aura: <span style=\'color:{aura};\'>■</span><br>
        {"🪶 Wings " if has_wings else ""}{"🦄 Horns " if has_horns else ""}{"✨ Glow Eyes" if glow_eyes else ""}
        </div></div>""", unsafe_allow_html=True)
        if is_dr: st.success("👑 You are Supreme Leader: FLY ✈ + TELEPORT ⚡ + PHASE WALLS 👻 + REALITY CONTROL 🌍")
        st.markdown("""<div style=\'background:#1a003a;border:1px solid #7C3AED;border-radius:12px;padding:12px;margin-top:12px;\'>
        <b style=\'color:#A1C9F4;\'>📦 Your Room:</b><br>
        <span style=\'color:#909094;font-size:0.9em;\'>🖥 Gaming PC | 💻 Gaming Laptop | 🛏 King Bed | 🚿 Bathroom | 📺 PS5 | 📱 Phone | 🔫 Gun | 🔒 Lock</span></div>""", unsafe_allow_html=True)
        if st.button("🚀 Enter the Circus!", use_container_width=True):
            if not username.strip(): st.error("❌ Please enter a name!")
            else:
                st.session_state.username = username.strip()
                st.session_state.gender = gender.split(" ")[0].lower()
                st.session_state.platform = "PC" if "PC" in platform else "PS5"
                st.session_state.character = selected_char
                st.session_state.logged_in = True
                st.session_state.page = "game"
                rid = f"room_{username.lower().replace(\' \',\'_\')}"
                st.session_state.my_room_id = rid
                st.session_state.rooms[rid] = {"name":f"🏠 {username}\'s Room","zone":"throne_room" if is_dr else "circus_tent",
                    "players":[username],"private":True,"code":gen_code(),"locked":False,"max":8,"owner":username}
                st.rerun()

def page_game():
    user = st.session_state.username
    char = CHARACTERS.get(st.session_state.character, CHARACTERS["custom"])
    zone = ZONES.get(st.session_state.current_zone, ZONES["circus_tent"])
    dr = is_dino()
    with st.sidebar:
        st.markdown(f"""<div style=\'background:linear-gradient(135deg,{char["color"]}33,#1a003a);border:2px solid {char["color"]};border-radius:14px;padding:12px;text-align:center;\'>
        <div style=\'font-size:2.5em;\'>{char["emoji"]}</div>
        <b style=\'color:{char["color"]};font-size:1.1em;\'>{user}</b><br>
        <span style=\'color:#909094;font-size:0.85em;\'>{char["role"]}</span>
        {"<br><span style=\\"color:#FFD700;\\">👑 Supreme Leader</span>" if dr else ""}
        </div>""", unsafe_allow_html=True)
        st.progress(st.session_state.energy/100, text=f"⚡ Energy: {st.session_state.energy}%")
        st.progress(st.session_state.hunger/100, text=f"🍔 Hunger: {st.session_state.hunger}%")
        st.progress(st.session_state.thirst/100, text=f"💧 Thirst: {st.session_state.thirst}%")
        st.markdown(f"""<div style=\'background:{zone["color"]}22;border:1px solid {zone["color"]};border-radius:10px;padding:8px;text-align:center;\'>
        <span style=\'font-size:1.5em;\'>{zone["emoji"]}</span> <b style=\'color:#fbfbff;\'>{zone["name"]}</b></div>""", unsafe_allow_html=True)
        if dr:
            for p in ["✈ Fly","⚡ Teleport","👻 Phase Walls","🌍 Reality Control"]:
                if st.button(p, key=f"pw_{p}", use_container_width=True):
                    st.session_state.action_log.append(f"⚡ {user} uses {p}!"); st.toast(f"⚡ {p} activated!")
        if st.button("🚪 Log Out", use_container_width=True):
            st.session_state.page = "store"; st.session_state.logged_in = False; st.rerun()

    tab_world,tab_room,tab_chat,tab_rooms,tab_lb = st.tabs(["🌍 World","🏠 My Room","💬 Chat & Calls","🎪 Rooms","🏆 Leaderboard"])

    with tab_world:
        st.markdown(f"<h2>🌍 {zone[\'emoji\']} {zone[\'name\']}</h2>", unsafe_allow_html=True)
        zone_cols = st.columns(7)
        for i,(zid,z) in enumerate(ZONES.items()):
            with zone_cols[i]:
                active = zid == st.session_state.current_zone
                st.markdown(f"""<div style=\'background:{z["color"]}{"44" if active else "15"};border:2px solid {"#FFD700" if active else z["color"]};border-radius:12px;padding:8px;text-align:center;\'>
                <div style=\'font-size:1.8em;\'>{z["emoji"]}</div>
                <div style=\'color:#fbfbff;font-size:0.75em;font-weight:bold;\'>{z["name"]}</div>
                {"<div style=\\"color:#FFD700;font-size:0.7em;\\">● HERE</div>" if active else ""}
                </div>""", unsafe_allow_html=True)
                if not active:
                    if st.button("Go", key=f"zone_{zid}", use_container_width=True):
                        st.session_state.current_zone = zid
                        st.session_state.action_log.append(f"{'⚡' if dr else '🚶'} {user} {'teleported' if dr else 'traveled'} to {z[\'name\']}!")
                        st.rerun()
        st.markdown("---")
        st.markdown(f"### {zone[\'emoji\']} NPCs in {zone[\'name\']}")
        if zone["npcs"]:
            npc_cols = st.columns(len(zone["npcs"]))
            for i,npc in enumerate(zone["npcs"]):
                with npc_cols[i]:
                    ch_data = next((c for c in CHARACTERS.values() if c["name"]==npc),None)
                    color = ch_data["color"] if ch_data else "#A1C9F4"
                    emoji = ch_data["emoji"] if ch_data else "🤖"
                    dialogue = random.choice(NPC_DIALOGUES.get(npc,["..."]))
                    st.markdown(f"""<div style=\'background:{color}22;border:2px solid {color};border-radius:14px;padding:14px;\'>
                    <div style=\'font-size:2em;\'>{emoji}</div><b style=\'color:{color};\'>{npc}</b><br>
                    <span style=\'color:#fbfbff;font-style:italic;\'>&quot;{dialogue}&quot;</span></div>""", unsafe_allow_html=True)
                    if st.button(f"Talk to {npc}", key=f"talk_{npc}_{i}", use_container_width=True):
                        reply = random.choice(NPC_DIALOGUES.get(npc,["..."]))
                        st.session_state.chat_messages.append({"sender":npc,"msg":reply,"time":time.strftime("%H:%M"),"npc":True})
                        st.toast(f"{emoji} {npc}: {reply[:50]}")
        if st.session_state.action_log:
            st.markdown("---")
            st.markdown("**📜 Action Log**")
            for entry in reversed(st.session_state.action_log[-8:]):
                st.markdown(f"<span style=\'color:#909094;font-size:0.85em;\'>{entry}</span>", unsafe_allow_html=True)

    with tab_room:
        st.markdown("<h2>🏠 Your Room</h2>", unsafe_allow_html=True)
        lc,bc = st.columns(2)
        with lc:
            locked = st.session_state.room_locked
            st.markdown(f"<div style=\'color:{'#f04438' if locked else '#17b26a'};font-size:1.1em;font-weight:bold;\'>{'🔒 LOCKED' if locked else '🔓 Unlocked'}</div>", unsafe_allow_html=True)
            if locked:
                if st.button("🔓 Unlock Room", use_container_width=True): st.session_state.room_locked = False; st.rerun()
            else:
                if st.button("🔒 Lock Room", use_container_width=True): st.session_state.room_locked = True; st.rerun()
        with bc:
            if st.button("🚿 Bathroom" if not st.session_state.in_bathroom else "🚪 Leave Bathroom", use_container_width=True):
                st.session_state.in_bathroom = not st.session_state.in_bathroom; st.rerun()
        if st.session_state.in_bathroom:
            st.markdown("""<div style=\'background:#0a1a2a;border:2px solid #00BCD4;border-radius:14px;padding:18px;\'>
            <h3 style=\'color:#00BCD4;\'>🚿 Bathroom</h3>
            <span style=\'color:#909094;\'>Shower 🚿 · Sink 🪥 · Mirror 🪞 · Toilet 🚽</span></div>""", unsafe_allow_html=True)
        else:
            r1,r2 = st.columns(2)
            items_l = [("🖥 Gaming PC","RTX 9090 · 128GB RAM","Gaming only","#A1C9F4"),("🛏 King Bed","Neon underglow · runes","Sleep to restore energy","#8DE5A1"),("📺 PS5 Screen","77-inch curved OLED","Play PS5 games","#003087")]
            items_r = [("💻 Gaming Laptop","RGB hinge","Gaming + Chat + Calls","#FFB482"),("📱 Smartphone","Always in inventory","Messages · Calls · Apps","#FF9F9B"),("🔫 Sidearm","Pistol (no bazooka)","Combat in battle zones","#D0BBFF")]
            with r1:
                for label,desc,use,color in items_l:
                    st.markdown(f"""<div style=\'background:{color}15;border:2px solid {color};border-radius:12px;padding:14px;margin-bottom:10px;\'>
                    <b style=\'color:{color};\'>{label}</b><br><span style=\'color:#909094;font-size:0.85em;\'>{desc}</span><br>
                    <span style=\'color:#fbfbff;font-size:0.85em;\'>Use: {use}</span></div>""", unsafe_allow_html=True)
            with r2:
                for label,desc,use,color in items_r:
                    st.markdown(f"""<div style=\'background:{color}15;border:2px solid {color};border-radius:12px;padding:14px;margin-bottom:10px;\'>
                    <b style=\'color:{color};\'>{label}</b><br><span style=\'color:#909094;font-size:0.85em;\'>{desc}</span><br>
                    <span style=\'color:#fbfbff;font-size:0.85em;\'>Use: {use}</span></div>""", unsafe_allow_html=True)
            st.markdown("### ⚡ Actions")
            actions = [("😴 Sleep","sleep","+50 energy","energy",50),("🍔 Eat","eat","+30 hunger","hunger",30),("💧 Drink","drink","+20 thirst","thirst",20),("🚬 Smoke","smoke","Cosmetic 💨",None,0),("💨 Vape","vape","Cosmetic ☁",None,0),("🍺 Alcohol","alcohol","Cosmetic 🥴",None,0)]
            ac1,ac2,ac3 = st.columns(3)
            action_cols = [ac1,ac2,ac3,ac1,ac2,ac3]
            for (label,aid,effect,stat,val),col in zip(actions,action_cols):
                with col:
                    if st.button(f"{label}\\n{effect}", key=f"act_{aid}", use_container_width=True):
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
                    st.markdown("<span style=\'color:#909094;\'>No messages yet. Say something!</span>", unsafe_allow_html=True)
                for msg in st.session_state.chat_messages[-20:]:
                    name = msg["sender"]; is_me = name==user; is_npc = msg.get("npc",False)
                    color = "#FFD700" if name in ["Dino Raptor","Dino_Raptor"] else ("#A1C9F4" if is_me else ("#FF8A80" if is_npc else "#8DE5A1"))
                    align = "right" if is_me else "left"
                    st.markdown(f"""<div style=\'text-align:{align};margin:4px 0;\'>
                    <span style=\'color:{color};font-size:0.85em;font-weight:bold;\'>{name}</span>
                    <span style=\'color:#909094;font-size:0.7em;\'> {msg["time"]}</span><br>
                    <span style=\'background:#1a003a;padding:4px 10px;border-radius:10px;color:#fbfbff;font-size:0.9em;display:inline-block;\'>{msg["msg"]}</span></div>""", unsafe_allow_html=True)
            msg_in = st.text_input("Type a message...", key="chat_input", placeholder="Type here...")
            _,sc2 = st.columns([3,1])
            with sc2:
                if st.button("Send 📤", use_container_width=True):
                    if msg_in.strip():
                        st.session_state.chat_messages.append({"sender":user,"msg":filter_message(msg_in.strip()),"time":time.strftime("%H:%M"),"npc":False}); st.rerun()
        with ct2:
            st.markdown("""<div style=\'background:#1a003a;border:2px solid #7C3AED;border-radius:12px;padding:12px;\'>
            <b style=\'color:#A1C9F4;\'>📱 Phone App</b><br>
            <span style=\'color:#909094;font-size:0.85em;\'>• 💬 Berichten<br>• 📞 Bellen<br>• 🎥 Video Bellen<br>• 🎙 Voice Chat<br>• 📡 Push-to-Talk</span></div>""", unsafe_allow_html=True)
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
            st.markdown("""<div style=\'background:#1a003a;border:1px solid #17b26a;border-radius:10px;padding:10px;margin-top:8px;\'>
            <span style=\'color:#17b26a;font-size:0.8em;\'>🚫 Filter actief:</span><br>
            <span style=\'color:#909094;font-size:0.75em;\'>Schelden → ⭐ · Middelvinger → 👋</span></div>""", unsafe_allow_html=True)

    with tab_rooms:
        st.markdown("<h2>🎪 Game Rooms</h2>", unsafe_allow_html=True)
        rc1,rc2 = st.columns([2,1])
        with rc1:
            st.markdown("**🌍 Public Rooms**")
            for rid,room in st.session_state.rooms.items():
                if not room["private"]:
                    z = ZONES.get(room["zone"],{}); pc=len(room["players"]); pm=room["max"]
                    st.markdown(f"""<div style=\'background:#1a003a;border:2px solid #7C3AED;border-radius:12px;padding:14px;margin-bottom:8px;\'>
                    <b style=\'color:#fbfbff;\'>{room["name"]}</b><span style=\'float:right;color:#A1C9F4;\'>{pc}/{pm}</span><br>
                    <span style=\'background:{z.get("color","#7C3AED")}33;color:{z.get("color","#A1C9F4")};border-radius:6px;padding:2px 8px;font-size:0.8em;\'>{z.get("emoji","🌍")} {z.get("name","Zone")}</span>
                    {"&nbsp;<span style=\"color:#17b26a;font-size:0.8em;\">🔓 Open</span>" if not room.get("locked") else "<span style=\"color:#f04438;font-size:0.8em;\">🔒 Locked</span>"}
                    </div>""", unsafe_allow_html=True)
                    if not room.get("locked") or dr:
                        if st.button(f"Join {room[\'name\']}", key=f"join_{rid}"):
                            if user not in room["players"]: room["players"].append(user)
                            st.session_state.current_room=rid; st.session_state.current_zone=room["zone"]
                            st.toast(f"✅ Joined {room[\'name\']}!"); st.rerun()
        with rc2:
            st.markdown("**🔒 Create Private Room**")
            rname = st.text_input("Room name", placeholder="My Secret Room", key="new_room_name")
            rzone = st.selectbox("Zone", list(ZONES.keys()), format_func=lambda k: f"{ZONES[k][\'emoji\']} {ZONES[k][\'name\']}", key="new_room_zone")
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
                            st.success(f"✅ Joined {room[\'name\']}!"); st.rerun()
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
            st.markdown(f"""<div style=\'background:{"#2d1a00" if is_me_lb else "#1a0030"};border:2px solid {"#FFD700" if is_me_lb else "#7C3AED"};border-radius:12px;padding:12px;margin-bottom:6px;display:flex;align-items:center;\'>
            <span style=\'font-size:1.5em;margin-right:10px;\'>{medal}</span>
            <span style=\'font-size:1.3em;margin-right:8px;\'>{player["char"]}</span>
            <b style=\'color:{"#FFD700" if is_me_lb else "#fbfbff"};flex:1;\'>{player["name"]}</b>
            <span style=\'color:#A1C9F4;\'>{player["badge"]}</span>
            <span style=\'color:#FFD700;font-family:Creepster,cursive;font-size:1.2em;margin-left:16px;\'>{player["score"]:,} pts</span></div>""", unsafe_allow_html=True)
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
'''

REQUIREMENTS = """streamlit>=1.32.0
"""

README = """# 🐉 Dino-Raptor-Blue-Killer
## Amazing Digital Circus — Online Game

### 🚀 Deploy on Streamlit Community Cloud (FREE)

1. Go to https://github.com and create a new repository called `dino-raptor-blue-killer`
2. Upload these files:
   - `app.py`
   - `requirements.txt`
3. Go to https://share.streamlit.io
4. Click **New app**
5. Select your repository: `dino-raptor-blue-killer`
6. Main file path: `app.py`
7. Click **Deploy** — it's FREE!

### 🌐 Your permanent URL will be:
`https://YOUR-GITHUB-USERNAME-dino-raptor-blue-killer-app-XXXXX.streamlit.app`

### Or search the web for:
`dino-raptor-blue-killer`

### 🎮 How to play:
- **PC:** Open the URL in any browser
- **PS5:** Open PS5 browser → paste the URL
- **Chrome/Edge:** Type URL in address bar

### 👑 Supreme Leader:
Enter name **Dino Raptor** to get all powers!

### 📋 Features:
- Age gate (13+)
- 8 characters + custom creator
- 7 world zones
- Private rooms with secret codes
- Chat, calls, video
- Own room with PC, laptop, bed, bathroom, PS5, gun
- Sleep, eat, drink, smoke, vape, alcohol actions
- Word filter (no swearing, no middle fingers)
- Leaderboard
- NPC dialogue
"""

# Write files
with open("app.py", "w", encoding="utf-8") as f:
    f.write(APP_CODE)

with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write(REQUIREMENTS)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(README)

# Verify
app_size = os.path.getsize("app.py")
req_size = os.path.getsize("requirements.txt")
readme_size = os.path.getsize("README.md")

print("=" * 60)
print("  📦 STREAMLIT COMMUNITY CLOUD EXPORT — DONE!")
print("=" * 60)
print(f"  ✅ app.py          — {app_size:,} bytes")
print(f"  ✅ requirements.txt — {req_size:,} bytes")
print(f"  ✅ README.md        — {readme_size:,} bytes")
print()
print("  🚀 HOW TO DEPLOY (FREE):")
print("  ─────────────────────────────────────────────")
print("  1. Go to github.com → New repository")
print("     Name: dino-raptor-blue-killer")
print("  2. Upload: app.py + requirements.txt")
print("  3. Go to share.streamlit.io → New app")
print("  4. Select repo → Main file: app.py → Deploy!")
print()
print("  🌐 Your free permanent URL:")
print("  https://[name]-dino-raptor-blue-killer-app.streamlit.app")
print()
print("  🎮 PC: Open URL in browser")
print("  🎮 PS5: PS5 browser → paste URL")
print("  🎮 Chrome: Type URL → Enter → play!")
print()
print("  👑 Type 'Dino Raptor' as name → Supreme Leader!")
print("=" * 60)

export_info = {
    "files": ["app.py", "requirements.txt", "README.md"],
    "deploy_url": "https://share.streamlit.io",
    "github_repo_name": "dino-raptor-blue-killer",
    "main_file": "app.py",
    "search_name": "dino-raptor-blue-killer",
    "age_rating": "13+",
    "platforms": ["PC", "PS5", "Browser"],
    "supreme_leader_name": "Dino Raptor",
}
print("\n📋 export_info ready for downstream use.")
