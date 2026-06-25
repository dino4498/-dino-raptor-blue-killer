import streamlit as st

st.set_page_config(page_title="Dino-Raptor-Blue-Killer", page_icon="dragon", layout="wide", initial_sidebar_state="collapsed")

GAME_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dino-Raptor-Blue-Killer</title>
<style>
* { margin:0; padding:0; box-sizing:border-box; }
html, body { width:100%; height:100%; overflow:hidden; background:#05000f; color:#fbfbff; font-family:'Segoe UI',sans-serif; }
canvas { display:block; cursor:pointer; }
#hud { position:fixed; top:8px; left:8px; background:rgba(0,0,0,0.75); border:1px solid #ffd400; border-radius:8px; padding:6px 12px; font-size:13px; pointer-events:none; z-index:10; }
#zoneLabel { position:fixed; top:8px; left:50%; transform:translateX(-50%); background:rgba(0,0,0,0.8); border:1px solid #A1C9F4; border-radius:20px; padding:4px 18px; font-size:13px; font-weight:bold; pointer-events:none; z-index:10; }
#minimap { position:fixed; top:8px; right:8px; background:rgba(0,0,0,0.85); border:1px solid #A1C9F4; border-radius:8px; padding:5px; z-index:10; pointer-events:none; }
#controls { position:fixed; bottom:8px; right:8px; background:rgba(0,0,0,0.7); border:1px solid #444; border-radius:8px; padding:8px 10px; font-size:10px; color:#909094; pointer-events:none; z-index:10; line-height:1.6; }
#chatBox { position:fixed; bottom:8px; left:8px; width:300px; background:rgba(0,0,0,0.88); border:1px solid #A1C9F4; border-radius:8px; z-index:10; }
#chatLog { height:110px; overflow-y:auto; padding:6px 8px; font-size:11px; }
#chatInput { display:flex; border-top:1px solid #333; }
#chatInput input { flex:1; background:transparent; border:none; color:#fbfbff; padding:5px 8px; font-size:12px; outline:none; }
#chatInput button { background:#ffd400; color:#05000f; border:none; padding:5px 10px; cursor:pointer; font-weight:bold; border-radius:0 0 8px 0; }
#powerBar { position:fixed; top:50px; left:8px; display:none; z-index:10; }
#powerBar button { display:block; margin-bottom:4px; background:rgba(255,212,0,0.18); border:1px solid #ffd400; color:#ffd400; padding:4px 12px; border-radius:6px; cursor:pointer; font-size:11px; }
#powerBar button:hover { background:#ffd400; color:#05000f; }
#interactHint { position:fixed; bottom:160px; left:50%; transform:translateX(-50%); background:rgba(0,0,0,0.85); border:1px solid #8DE5A1; border-radius:20px; padding:5px 18px; font-size:13px; display:none; z-index:10; pointer-events:none; color:#8DE5A1; }
#dialogBox { position:fixed; bottom:170px; left:50%; transform:translateX(-50%); background:#0d0d1a; border:2px solid #ffd400; border-radius:12px; padding:14px 20px; max-width:400px; display:none; z-index:50; }
#dialogBox .speaker { color:#ffd400; font-weight:bold; margin-bottom:6px; font-size:14px; }
#dialogBox .text { color:#fbfbff; font-size:13px; line-height:1.5; }
#dialogBox button { margin-top:10px; background:#ffd400; color:#05000f; border:none; padding:5px 16px; border-radius:6px; cursor:pointer; font-weight:bold; }
#overlay { position:fixed; top:0; left:0; width:100%; height:100%; background:#05000f; display:flex; flex-direction:column; align-items:center; justify-content:center; z-index:200; overflow-y:auto; }
#overlay h1 { font-size:2.6em; color:#ffd400; text-shadow:0 0 30px #ffd400; margin-bottom:6px; text-align:center; }
#overlay p { color:#A1C9F4; margin-bottom:16px; font-size:1em; text-align:center; }
.form-group { margin-bottom:12px; width:320px; }
.form-group label { display:block; margin-bottom:4px; color:#A1C9F4; font-size:12px; }
.form-group input, .form-group select { width:100%; background:#1a1a2e; border:1px solid #555; color:#fbfbff; padding:8px; border-radius:8px; font-size:13px; }
.char-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:6px; width:480px; margin-bottom:14px; }
.char-card { background:#1a1a2e; border:2px solid #333; border-radius:8px; padding:8px 4px; text-align:center; cursor:pointer; transition:all 0.15s; font-size:10px; }
.char-card:hover,.char-card.selected { border-color:#ffd400; background:#2a2a3e; transform:scale(1.05); }
.char-card .emoji { font-size:1.8em; }
.big-btn { background:linear-gradient(135deg,#ffd400,#ff8c00); color:#05000f; border:none; padding:12px 32px; border-radius:10px; font-size:1.1em; font-weight:bold; cursor:pointer; margin-top:8px; }
#roomMenu { position:fixed; top:50%; left:50%; transform:translate(-50%,-50%); background:#0d0d1a; border:2px solid #ffd400; border-radius:12px; padding:18px; width:360px; display:none; z-index:100; }
#roomMenu h3 { color:#ffd400; margin-bottom:10px; text-align:center; }
#roomMenu input, #roomMenu select { width:100%; background:#1a1a2e; border:1px solid #555; color:#fbfbff; padding:6px; border-radius:6px; margin-bottom:7px; font-size:12px; }
#roomMenu button { width:100%; padding:7px; border:none; border-radius:6px; cursor:pointer; font-size:12px; font-weight:bold; margin-bottom:5px; }
.btn-gold{background:#ffd400;color:#05000f;}
.btn-red{background:#f04438;color:#fff;}
.btn-blue{background:#1F77B4;color:#fff;}
#roomCodeDisplay { position:fixed; top:50%; left:50%; transform:translate(-50%,-50%); background:#0d0d1a; border:2px solid #8DE5A1; border-radius:12px; padding:22px; text-align:center; display:none; z-index:150; }
#roomCodeDisplay .code { font-size:2.4em; color:#ffd400; font-weight:bold; letter-spacing:8px; margin:12px 0; }
#roomCodeDisplay button { background:#8DE5A1; color:#05000f; border:none; padding:8px 20px; border-radius:8px; cursor:pointer; font-weight:bold; }
#focusHint { position:fixed; top:50%; left:50%; transform:translate(-50%,-50%); background:rgba(0,0,0,0.9); border:2px solid #ffd400; border-radius:12px; padding:20px 30px; text-align:center; z-index:300; display:none; }
#focusHint h2 { color:#ffd400; margin-bottom:8px; }
#focusHint p { color:#fbfbff; font-size:13px; }
#floorIndicator { position:fixed; left:50%; top:50%; transform:translate(-50%,-50%); background:rgba(0,0,0,0.9); border:2px solid #A1C9F4; border-radius:10px; padding:12px 24px; font-size:1.2em; color:#A1C9F4; display:none; z-index:20; pointer-events:none; }
</style>
</head>
<body>
<div id="focusHint"><h2>Click to play!</h2><p>Click the screen so keys work.</p></div>
<div id="hud"><span id="hudName">Dino Raptor</span> | <span id="hudZone">Throne Room</span> | <span id="hudFloor">Floor 1</span> | <span id="hudPlayers">4 players</span></div>
<div id="zoneLabel">THRONE ROOM</div>
<div id="powerBar">
  <button onclick="toggleFly()">FLY [F]</button>
  <button onclick="doTP()">TP [T]</button>
  <button onclick="togglePhase()">PHASE [P]</button>
  <button onclick="doReality()">SHIFT [R]</button>
</div>
<div id="interactHint">Press E to talk</div>
<div id="floorIndicator"></div>
<div id="dialogBox">
  <div class="speaker" id="dialogSpeaker"></div>
  <div class="text" id="dialogText"></div>
  <button onclick="closeDialog()">Continue</button>
</div>
<div id="chatBox">
  <div id="chatLog"></div>
  <div id="chatInput">
    <input type="text" id="chatMsg" placeholder="Chat (Enter to send)" maxlength="120" onkeydown="if(event.key==='Enter'){event.stopPropagation();sendChat();}">
    <button onclick="sendChat()">Send</button>
  </div>
</div>
<div id="minimap"><canvas id="minimapCanvas" width="120" height="80"></canvas><div style="font-size:9px;color:#909094;text-align:center;margin-top:2px;" id="mmLabel">Floor 1</div></div>
<div id="controls">WASD/Arrows=Move | SPACE=Jump<br>E=Talk | H=Actions | M=Rooms<br>Q=Floor up | Z=Floor down<br>F=Fly T=TP P=Phase R=Reality</div>
<div id="roomMenu">
  <h3>Multiplayer Rooms</h3>
  <div id="roomList"></div>
  <hr style="border-color:#333;margin:8px 0;">
  <input type="text" id="newRoomName" placeholder="Room name...">
  <select id="newRoomZone">
    <option value="throne">Throne Room</option>
    <option value="void">The Void</option>
    <option value="moon">Moon</option>
    <option value="sun">Sun Zone</option>
    <option value="beach">Beach</option>
    <option value="fairground">Fairground</option>
    <option value="circus">Circus Tent</option>
  </select>
  <label style="color:#A1C9F4;font-size:12px;display:flex;align-items:center;gap:6px;margin-bottom:8px;"><input type="checkbox" id="privateRoom"> Private room (with code)</label>
  <button class="btn-gold" onclick="createRoom()">Create room</button>
  <input type="text" id="joinCode" placeholder="Join with code (6 chars)...">
  <button class="btn-blue" onclick="joinWithCode()">Join with code</button>
  <button class="btn-red" onclick="closeRoomMenu()">Close</button>
</div>
<div id="roomCodeDisplay">
  <h3 style="color:#8DE5A1;">Your private code</h3>
  <p style="color:#A1C9F4;font-size:12px;">Share only with friends!</p>
  <div class="code" id="generatedCode">XXXXXX</div>
  <button onclick="document.getElementById('roomCodeDisplay').style.display='none'">Got it!</button>
</div>
<div id="overlay">
  <div id="ageScreen" style="display:flex;flex-direction:column;align-items:center;">
    <h1>DINO-RAPTOR-BLUE-KILLER</h1>
    <p>The Amazing Digital Circus - Online World</p>
    <div class="form-group"><label>Your age:</label><input type="number" id="ageInput" placeholder="How old are you?" min="1" max="120"></div>
    <button class="big-btn" onclick="checkAge()">ENTER THE CIRCUS</button>
  </div>
  <div id="charScreen" style="display:none;flex-direction:column;align-items:center;">
    <h1 style="font-size:2em;color:#ffd400;margin-bottom:6px;">Choose Your Character</h1>
    <p>Or create your own below!</p>
    <div class="char-grid" id="charGrid"></div>
    <div style="width:480px;background:#1a1a2e;border:1px solid #555;border-radius:10px;padding:12px;margin-bottom:12px;">
      <div style="color:#ffd400;font-weight:bold;margin-bottom:8px;">Create own character</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
        <div class="form-group" style="margin:0;"><label>Name:</label><input type="text" id="customName" placeholder="Your name..."></div>
        <div class="form-group" style="margin:0;"><label>Gender:</label>
          <select id="customGender"><option value="male">Boy</option><option value="female">Girl</option><option value="nonbinary">Non-binary</option></select>
        </div>
        <div class="form-group" style="margin:0;"><label>Skin:</label>
          <select id="customSkin">
            <option value="#FDBCB4">Light</option><option value="#E8956D">Medium</option>
            <option value="#8D5524">Dark</option><option value="#7EC8E3">Blue</option>
            <option value="#90EE90">Green</option><option value="#FFD700">Gold</option>
          </select>
        </div>
        <div class="form-group" style="margin:0;"><label>Hair:</label>
          <select id="customHair">
            <option value="#1a1a1a">Black</option><option value="#FFD700">Gold</option>
            <option value="#8B0000">Red</option><option value="#4169E1">Blue</option>
            <option value="#9400D3">Purple</option><option value="#FF69B4">Pink</option>
          </select>
        </div>
      </div>
    </div>
    <button class="big-btn" onclick="startGame()">PLAY!</button>
  </div>
</div>
<canvas id="gameCanvas"></canvas>
<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
resizeCanvas();
window.addEventListener('resize', resizeCanvas);
canvas.setAttribute('tabindex', '0');
canvas.style.outline = 'none';
let hasFocus = false;
function requestFocus() { canvas.focus(); hasFocus = true; document.getElementById('focusHint').style.display = 'none'; }
canvas.addEventListener('click', requestFocus);
canvas.addEventListener('mousedown', requestFocus);
document.addEventListener('click', function() { if (document.getElementById('overlay').style.display === 'none') canvas.focus(); });
function showFocusHint() {
  const hint = document.getElementById('focusHint');
  hint.style.display = 'block';
  setTimeout(function() { hint.style.display = 'none'; }, 4000);
}
const CHARACTERS = [
  { id:'dino_raptor', name:'Dino Raptor', emoji:'DR', color:'#FFD700', secondary:'#9400D3', isLeader:true,  gender:'male' },
  { id:'pomni',       name:'Pomni',       emoji:'PO', color:'#A1C9F4', secondary:'#D0BBFF', isLeader:false, gender:'female' },
  { id:'ragatha',     name:'Ragatha',     emoji:'RA', color:'#FFB482', secondary:'#FF9F9B', isLeader:false, gender:'female' },
  { id:'jax',         name:'Jax',         emoji:'JX', color:'#8DE5A1', secondary:'#555555', isLeader:false, gender:'male' },
  { id:'gangle',      name:'Gangle',      emoji:'GA', color:'#D0BBFF', secondary:'#FFD700', isLeader:false, gender:'female' },
  { id:'zooble',      name:'Zooble',      emoji:'ZO', color:'#FF9F9B', secondary:'#8DE5A1', isLeader:false, gender:'female' },
  { id:'kinger',      name:'Kinger',      emoji:'KI', color:'#FFD700', secondary:'#8C564B', isLeader:false, gender:'male' },
  { id:'bubble',      name:'Bubble',      emoji:'BU', color:'#A1C9F4', secondary:'#D0BBFF', isLeader:false, gender:'nonbinary' },
];
const NPC_LINES = {
  pomni:   ['Wait... where am I?!','I want to go HOME!','This circus is a nightmare...','Is Dino Raptor the boss now?'],
  ragatha: ['Everything will be okay!','Have you tried smiling?','I make wool art!','Dino Raptor is actually pretty cool!'],
  jax:     ['Ugh. You again.','What do you want?','...boring.','Whatever.'],
  gangle:  ['*moves like a puppet*','My masks fell off...','Are you really talking to me?','*tears*'],
  zooble:  ['Leave me alone.','My wheel fell off AGAIN.','...okay. Hi.','I do not want to be here.'],
  kinger:  ['THE WALLS ARE CLOSING IN','I have 47 emergency plans!','*chess sounds*','Do not trust the carpets.'],
  bubble:  ['Bloop!','Bloooop~','Bloop bloop!','...bloop?'],
};
const ZONES = [
  { id:'void',       name:'THE VOID',    sky:'#0a0010', floor:'#1a0030', accent:'#9400D3', ambient:'#200040' },
  { id:'moon',       name:'MOON',        sky:'#0d0d1a', floor:'#c0c0d8', accent:'#A1C9F4', ambient:'#0a0a20' },
  { id:'sun',        name:'SUN ZONE',    sky:'#1a0a00', floor:'#8B4513', accent:'#FFD700', ambient:'#3a1a00' },
  { id:'beach',      name:'BEACH',       sky:'#003d7a', floor:'#F4D03F', accent:'#00BFFF', ambient:'#005599' },
  { id:'fairground', name:'FAIRGROUND',  sky:'#0a0020', floor:'#228B22', accent:'#FF69B4', ambient:'#1a0030' },
  { id:'circus',     name:'CIRCUS TENT', sky:'#1a0005', floor:'#8B4513', accent:'#FF0000', ambient:'#2a000a' },
  { id:'throne',     name:'THRONE ROOM', sky:'#05000f', floor:'#1a1a2e', accent:'#FFD700', ambient:'#0d0020' },
];
const FLOOR_NAMES = ['Basement','Ground Floor','Upper Floor','Rooftop'];
const PLATFORMS_BY_FLOOR = {
  0: [
    { x:80,   w:340, h:18, label:'Dungeon',      color:'#3a1a00', accent:'#8B4513' },
    { x:500,  w:280, h:18, label:'Storage',      color:'#0a1a00', accent:'#228B22' },
    { x:860,  w:320, h:18, label:'Void Portal',  color:'#0a0020', accent:'#9400D3' },
    { x:1260, w:260, h:18, label:'Secret Vault', color:'#1a0010', accent:'#f04438' },
    { x:1600, w:300, h:18, label:'Sewer',        color:'#001a00', accent:'#8DE5A1' },
  ],
  1: [
    { x:80,   w:460, h:18, label:'Main Hall',   color:'#0d0d1a', accent:'#FFD700' },
    { x:620,  w:280, h:18, label:'Kitchen',     color:'#1a1a00', accent:'#FFA500' },
    { x:980,  w:260, h:18, label:'Living Room', color:'#0d0d20', accent:'#A1C9F4' },
    { x:1320, w:180, h:18, label:'Bathroom',    color:'#002233', accent:'#00BFFF' },
    { x:1580, w:340, h:18, label:'Game Room',   color:'#001a20', accent:'#8DE5A1' },
  ],
  2: [
    { x:80,   w:440, h:18, label:'DR Bedroom',   color:'#0d0010', accent:'#FFD700' },
    { x:600,  w:280, h:18, label:'Pomni Room',   color:'#001433', accent:'#A1C9F4' },
    { x:960,  w:280, h:18, label:'Ragatha Room', color:'#1a0a00', accent:'#FFB482' },
    { x:1320, w:260, h:18, label:'Jax Room',     color:'#001a00', accent:'#8DE5A1' },
    { x:1660, w:200, h:18, label:'Bathroom 2',   color:'#002233', accent:'#00BFFF' },
  ],
  3: [
    { x:80, w:1800, h:18, label:'Rooftop', color:'#000510', accent:'#A1C9F4' },
  ],
};
const ROOM_ITEMS = {
  'DR Bedroom':   ['[BED]','[PC]','[LAPTOP]','[PS5]','[GUN]','[PHONE]'],
  'Main Hall':    ['[THRONE]','[PILLAR]','[CHAIR]'],
  'Kitchen':      ['[PAN]','[FRIDGE]','[CHAIR]'],
  'Living Room':  ['[SOFA]','[TV]','[GAMEPAD]'],
  'Bathroom':     ['[TOILET]','[SHOWER]','[SINK]'],
  'Bathroom 2':   ['[TOILET]','[SHOWER]','[SINK]'],
  'Game Room':    ['[PC]','[LAPTOP]','[GAMEPAD]'],
  'Pomni Room':   ['[BED]','[PEN]','[WINDOW]'],
  'Ragatha Room': ['[BED]','[YARN]','[PAINT]'],
  'Jax Room':     ['[BED]','[GYM]','[MIRROR]'],
  'Dungeon':      ['[CHAINS]','[TORCH]','[SKULL]'],
  'Storage':      ['[BOX]','[BARREL]'],
  'Void Portal':  ['[VORTEX]','[STARS]'],
  'Secret Vault': ['[LOCK]','[GEM]','[GOLD]'],
  'Sewer':        ['[RAT]','[WATER]'],
  'Rooftop':      ['[STARS]','[SCOPE]','[LIGHT]','[MOON]'],
};
const WORLD_W = 2000;
const CHAR_W = 28;
const CHAR_H = 46;
const GRAVITY = 0.55;
const JUMP_VEL = -12;
const WALK_SPD = 3.5;
let player = {
  x:300, y:0, vx:0, vy:0, w:CHAR_W, h:CHAR_H,
  onGround:false, character:CHARACTERS[0], name:'Dino Raptor',
  gender:'male', skinColor:'#FFD700', hairColor:'#9400D3',
  floor:1, flying:false, phasing:false,
  breastOffset:0, breastVel:0, dir:1, isLeader:true,
};
let camera = { x:0 };
let keys = {};
let gameStarted = false;
let frameCount = 0;
let currentZoneIdx = 6;
let selectedChar = 0;
let nearNPC = null;
let dialogOpen = false;
let npcs = [];
let otherPlayers = [];
const keysDown = function(e) {
  keys[e.key.toLowerCase()] = true;
  keys[e.code] = true;
  if (e.key === 'Tab') { e.preventDefault(); document.getElementById('chatMsg').focus(); return; }
  if (document.activeElement === document.getElementById('chatMsg')) return;
  e.preventDefault();
  if (e.key === 'f' || e.key === 'F') toggleFly();
  if (e.key === 't' || e.key === 'T') doTP();
  if (e.key === 'p' || e.key === 'P') togglePhase();
  if (e.key === 'r' || e.key === 'R') doReality();
  if (e.key === 'm' || e.key === 'M') toggleRoomMenu();
  if (e.key === 'e' || e.key === 'E') tryInteract();
  if (e.key === 'h' || e.key === 'H') doRoomAction();
  if (e.key === 'q' || e.key === 'Q') changeFloor(1);
  if (e.key === 'z' || e.key === 'Z') changeFloor(-1);
};
const keysUp = function(e) { keys[e.key.toLowerCase()] = false; keys[e.code] = false; };
canvas.addEventListener('keydown', keysDown);
canvas.addEventListener('keyup', keysUp);
document.addEventListener('keydown', function(e) {
  if (!gameStarted) return;
  if (document.activeElement === document.getElementById('chatMsg')) return;
  keysDown(e);
});
document.addEventListener('keyup', keysUp);
function initCharGrid() {
  const grid = document.getElementById('charGrid');
  grid.innerHTML = '';
  CHARACTERS.forEach(function(c, i) {
    const card = document.createElement('div');
    card.className = 'char-card' + (i === 0 ? ' selected' : '');
    card.innerHTML = '<div class="emoji" style="background:' + c.color + ';width:36px;height:36px;border-radius:50%;line-height:36px;margin:0 auto 4px;color:#05000f;font-weight:bold;">' + c.emoji + '</div><div style="font-weight:bold;color:' + c.color + ';font-size:11px;">' + c.name + '</div><div style="color:#909094;font-size:9px;">' + (c.isLeader ? 'LEADER' : c.gender) + '</div>';
    card.onclick = function() {
      document.querySelectorAll('.char-card').forEach(function(x) { x.classList.remove('selected'); });
      card.classList.add('selected');
      selectedChar = i;
    };
    grid.appendChild(card);
  });
}
function checkAge() {
  const age = parseInt(document.getElementById('ageInput').value);
  if (!age || age < 13) { alert('You must be at least 13 years old!'); return; }
  document.getElementById('ageScreen').style.display = 'none';
  document.getElementById('charScreen').style.display = 'flex';
  initCharGrid();
}
function startGame() {
  const nameVal = document.getElementById('customName').value.trim();
  const name = nameVal || CHARACTERS[selectedChar].name;
  const gender = document.getElementById('customGender').value;
  const skin = document.getElementById('customSkin').value;
  const hair = document.getElementById('customHair').value;
  const base = CHARACTERS[selectedChar];
  const isLeader = name.toLowerCase().replace(/[^a-z0-9]/g,'').indexOf('dinoraptor') >= 0 || name.toLowerCase() === 'dino raptor' || base.isLeader;
  player.character = Object.assign({}, base, { isLeader: isLeader });
  player.name = name; player.gender = gender; player.skinColor = skin; player.hairColor = hair; player.isLeader = isLeader;
  document.getElementById('overlay').style.display = 'none';
  document.getElementById('hudName').textContent = (isLeader ? '[LEADER] ' : '') + name;
  if (isLeader) document.getElementById('powerBar').style.display = 'block';
  gameStarted = true;
  initNPCs(); initOtherPlayers(); placePlayerOnFloor(); requestFocus(); showFocusHint(); gameLoop();
  setTimeout(function() {
    addChat('System', 'Welcome to the Amazing Digital Circus!', '#ffd400');
    addChat('System', 'WASD/Arrows=Move | SPACE=Jump | E=Talk | H=Action | M=Rooms', '#909094');
    addChat('System', 'Q=Floor up | Z=Floor down | F=Fly | T=TP | P=Phase | R=Reality', '#909094');
  }, 400);
}
function getGroundY() { return canvas.height - 80; }
function placePlayerOnFloor() { player.y = getGroundY() - player.h; player.vy = 0; player.onGround = true; }
function initNPCs() {
  npcs = CHARACTERS.filter(function(c) { return c.id !== 'dino_raptor'; }).map(function(c, i) {
    return { character:c, x:200+i*230, y:0, vx:(Math.random()-0.5)*1.2, vy:0, dir:1, onGround:true, floor:1, walkTimer:0, dialogIdx:0, breastOffset:0, breastVel:0, bobPhase:i*0.7 };
  });
  npcs.forEach(function(n) { n.y = getGroundY() - CHAR_H; });
}
function initOtherPlayers() {
  otherPlayers = [
    { name:'CoolPlayer99', x:600,  y:0, character:CHARACTERS[2], dir:1,  breastOffset:0, breastVel:0, floor:1 },
    { name:'PS5User',      x:900,  y:0, character:CHARACTERS[4], dir:-1, breastOffset:0, breastVel:0, floor:1 },
    { name:'VoidWalker',   x:1200, y:0, character:CHARACTERS[3], dir:1,  breastOffset:0, breastVel:0, floor:1 },
  ];
  otherPlayers.forEach(function(op) { op.y = getGroundY() - CHAR_H; });
}
function updatePlayer() {
  if (!gameStarted || dialogOpen) return;
  const groundY = getGroundY();
  const left  = keys['arrowleft']  || keys['a'] || keys['keya'];
  const right = keys['arrowright'] || keys['d'] || keys['keyd'];
  const up    = keys['arrowup']    || keys['w'] || keys['keyw'] || keys[' '] || keys['space'];
  if (left)       { player.vx = -WALK_SPD; player.dir = -1; }
  else if (right) { player.vx = WALK_SPD; player.dir = 1; }
  else player.vx *= 0.75;
  if (player.flying && player.isLeader) {
    const flyUp   = keys['arrowup']   || keys['w'] || keys['keyw'];
    const flyDown = keys['arrowdown'] || keys['s'] || keys['keys'];
    if (flyUp)        player.vy = -5;
    else if (flyDown) player.vy = 4;
    else player.vy *= 0.6;
    player.vy = Math.max(-7, Math.min(7, player.vy));
  } else {
    if (up && player.onGround) { player.vy = JUMP_VEL; player.onGround = false; }
    player.vy += GRAVITY;
  }
  player.x += player.vx; player.y += player.vy;
  if (player.y + player.h >= groundY) { player.y = groundY - player.h; player.vy = 0; player.onGround = true; }
  if (player.x < 0) player.x = 0;
  if (player.x + player.w > WORLD_W) player.x = WORLD_W - player.w;
  if (player.gender === 'female' || player.character.gender === 'female') {
    const spd = Math.abs(player.vx) + Math.abs(player.vy) * 0.3;
    player.breastVel += (0 - player.breastOffset) * 0.28 - player.breastVel * 0.35 + spd * 0.12 * (Math.random()-0.5);
    player.breastOffset = Math.max(-4.5, Math.min(4.5, player.breastOffset + player.breastVel));
  }
  camera.x = Math.max(0, Math.min(WORLD_W - canvas.width, player.x - canvas.width * 0.4));
  currentZoneIdx = Math.min(ZONES.length - 1, Math.floor(player.x / (WORLD_W / ZONES.length)));
  const zone = ZONES[currentZoneIdx];
  document.getElementById('zoneLabel').textContent = zone.name;
  document.getElementById('hudZone').textContent = zone.name;
  document.getElementById('hudFloor').textContent = 'Floor ' + player.floor + ' - ' + FLOOR_NAMES[player.floor];
}
function updateNPCs() {
  const groundY = getGroundY();
  nearNPC = null;
  npcs.forEach(function(npc) {
    npc.walkTimer++;
    if (npc.walkTimer > 100 + Math.random()*80) { npc.vx = (Math.random()-0.5)*1.6; npc.dir = npc.vx >= 0 ? 1 : -1; npc.walkTimer = 0; }
    if (npc.character.id === 'bubble') {
      npc.bobPhase += 0.025; npc.x += npc.vx * 0.5;
      npc.y = groundY - CHAR_H - 30 + Math.sin(npc.bobPhase) * 22;
    } else {
      npc.vy += GRAVITY; npc.x += npc.vx; npc.y += npc.vy;
      if (npc.y + CHAR_H >= groundY) { npc.y = groundY - CHAR_H; npc.vy = 0; npc.onGround = true; }
    }
    if (npc.x < 20) { npc.x = 20; npc.vx = Math.abs(npc.vx); npc.dir = 1; }
    if (npc.x > WORLD_W - 50) { npc.x = WORLD_W - 50; npc.vx = -Math.abs(npc.vx); npc.dir = -1; }
    if (npc.character.gender === 'female') {
      const spd = Math.abs(npc.vx);
      npc.breastVel += (0 - npc.breastOffset) * 0.28 - npc.breastVel * 0.35 + spd * 0.15 * (Math.random()-0.5);
      npc.breastOffset = Math.max(-4.5, Math.min(4.5, npc.breastOffset + npc.breastVel));
    }
    if (npc.floor !== player.floor) return;
    const dx = (npc.x + CHAR_W/2) - (player.x + player.w/2);
    const dy = (npc.y + CHAR_H/2) - (player.y + player.h/2);
    if (Math.sqrt(dx*dx + dy*dy) < 72) nearNPC = npc;
  });
  otherPlayers.forEach(function(op) {
    op.x += op.dir * 0.9;
    if (op.x > WORLD_W - 60) op.dir = -1;
    if (op.x < 60) op.dir = 1;
    op.y = groundY - CHAR_H;
    if (op.character.gender === 'female') {
      op.breastVel = (op.breastVel||0) + (0-(op.breastOffset||0))*0.28 - (op.breastVel||0)*0.35 + 0.9*0.1*(Math.random()-0.5);
      op.breastOffset = Math.max(-4, Math.min(4, (op.breastOffset||0) + op.breastVel));
    }
  });
  document.getElementById('interactHint').style.display = (nearNPC && nearNPC.floor === player.floor) ? 'block' : 'none';
  document.getElementById('hudPlayers').textContent = (1 + otherPlayers.length) + ' players';
}
function drawChar(cx, cy, ch, name, dir, bOff, isPlayer, cSkin, cHair) {
  const W = CHAR_W, H = CHAR_H;
  if (cx + W < -20 || cx - 40 > canvas.width + 20) return;
  ctx.save();
  ctx.translate(cx + W/2, cy + H/2);
  if (dir < 0) ctx.scale(-1,1);
  const ox = -W/2, oy2 = -H/2;
  const skin = cSkin || ch.color;
  const hair = cHair || ch.secondary;
  ctx.fillStyle = 'rgba(0,0,0,0.3)';
  ctx.beginPath(); ctx.ellipse(0, H/2+3, W*0.7, 5, 0, 0, Math.PI*2); ctx.fill();
  ctx.fillStyle = hair;
  ctx.fillRect(ox+3,  oy2+H-14, 9, 14);
  ctx.fillRect(ox+W-12, oy2+H-14, 9, 14);
  ctx.fillStyle = '#333333';
  ctx.fillRect(ox+1,    oy2+H-4, 12, 5);
  ctx.fillRect(ox+W-13, oy2+H-4, 12, 5);
  ctx.fillStyle = skin;
  ctx.fillRect(ox+4, oy2+H*0.42, W-8, H*0.38);
  ctx.fillStyle = skin;
  ctx.fillRect(ox-5, oy2+H*0.43, 8, H*0.28);
  ctx.fillRect(ox+W-3, oy2+H*0.43, 8, H*0.28);
  ctx.fillStyle = skin;
  ctx.beginPath(); ctx.arc(ox-1,   oy2+H*0.43+H*0.28, 5, 0, Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.arc(ox+W+1, oy2+H*0.43+H*0.28, 5, 0, Math.PI*2); ctx.fill();
  if (ch.gender === 'female' || ch.gender === 'nonbinary') {
    const bo = bOff || 0;
    ctx.fillStyle = skin;
    ctx.beginPath(); ctx.arc(ox+8,    oy2+H*0.5+bo,  5.5, 0, Math.PI*2); ctx.fill();
    ctx.beginPath(); ctx.arc(ox+W-8,  oy2+H*0.5-bo, 5.5, 0, Math.PI*2); ctx.fill();
    ctx.strokeStyle = 'rgba(0,0,0,0.25)'; ctx.lineWidth = 0.8;
    ctx.beginPath(); ctx.arc(ox+8,   oy2+H*0.5+bo,  5.5, 0, Math.PI*2); ctx.stroke();
    ctx.beginPath(); ctx.arc(ox+W-8, oy2+H*0.5-bo, 5.5, 0, Math.PI*2); ctx.stroke();
  }
  ctx.fillStyle = skin;
  ctx.fillRect(ox+W/2-4, oy2+H*0.3, 8, H*0.12);
  ctx.fillStyle = skin;
  ctx.beginPath(); ctx.arc(0, oy2+H*0.22, 13, 0, Math.PI*2); ctx.fill();
  ctx.strokeStyle = 'rgba(0,0,0,0.2)'; ctx.lineWidth = 1; ctx.stroke();
  ctx.fillStyle = hair;
  ctx.beginPath(); ctx.arc(0, oy2+H*0.22, 13, Math.PI, 0); ctx.fill();
  if (ch.gender === 'female') { ctx.fillRect(-13, oy2+H*0.22-6, 5, 16); ctx.fillRect(8, oy2+H*0.22-6, 5, 16); }
  ctx.fillStyle = '#fbfbff';
  ctx.beginPath(); ctx.arc(-4.5, oy2+H*0.2, 4, 0, Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.arc(4.5,  oy2+H*0.2, 4, 0, Math.PI*2); ctx.fill();
  ctx.fillStyle = '#1a1a2e';
  ctx.beginPath(); ctx.arc(-4.5, oy2+H*0.2, 2, 0, Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.arc(4.5,  oy2+H*0.2, 2, 0, Math.PI*2); ctx.fill();
  ctx.fillStyle = '#ffffff';
  ctx.beginPath(); ctx.arc(-3.5, oy2+H*0.19, 0.8, 0, Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.arc(5.5,  oy2+H*0.19, 0.8, 0, Math.PI*2); ctx.fill();
  ctx.strokeStyle = '#555555'; ctx.lineWidth = 1.2;
  ctx.beginPath();
  if (ch.id === 'jax') { ctx.moveTo(-4, oy2+H*0.28); ctx.lineTo(4, oy2+H*0.28); }
  else { ctx.arc(0, oy2+H*0.25, 3.5, 0.2, Math.PI-0.2); }
  ctx.stroke();
  if (ch.isLeader || ch.id === 'dino_raptor') {
    ctx.restore(); ctx.save();
    ctx.translate(cx+W/2, cy+H/2);
    if (dir < 0) ctx.scale(-1,1);
    ctx.shadowColor = '#FFD700'; ctx.shadowBlur = 22;
    ctx.strokeStyle = '#FFD700'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.arc(0, 0, H*0.6, 0, Math.PI*2); ctx.stroke();
    ctx.shadowBlur = 0;
    ctx.fillStyle = '#9400D3'; ctx.globalAlpha = 0.75;
    ctx.beginPath();
    ctx.moveTo(ox+2, oy2+H*0.44); ctx.lineTo(ox-28, oy2+H*0.3); ctx.lineTo(ox-10, oy2+H*0.6);
    ctx.closePath(); ctx.fill();
    ctx.beginPath();
    ctx.moveTo(ox+W-2, oy2+H*0.44); ctx.lineTo(ox+W+28, oy2+H*0.3); ctx.lineTo(ox+W+10, oy2+H*0.6);
    ctx.closePath(); ctx.fill();
    ctx.globalAlpha = 1;
    ctx.fillStyle = '#FFD700';
    const ty = oy2+H*0.09;
    ctx.beginPath();
    ctx.moveTo(-11,ty+1); ctx.lineTo(-11,ty-10); ctx.lineTo(-5,ty-5); ctx.lineTo(0,ty-12);
    ctx.lineTo(5,ty-5); ctx.lineTo(11,ty-10); ctx.lineTo(11,ty+1);
    ctx.closePath(); ctx.fill();
    ctx.strokeStyle = '#FF8C00'; ctx.lineWidth = 1; ctx.stroke();
    var gems = [[-7,ty-7,'#f04438'],[0,ty-11,'#A1C9F4'],[7,ty-7,'#8DE5A1']];
    gems.forEach(function(g) { ctx.fillStyle=g[2]; ctx.beginPath(); ctx.arc(g[0],g[1],2,0,Math.PI*2); ctx.fill(); });
    ctx.fillStyle = '#555555';
    ctx.beginPath(); ctx.moveTo(-8,ty-8); ctx.lineTo(-12,ty-22); ctx.lineTo(-4,ty-10); ctx.closePath(); ctx.fill();
    ctx.beginPath(); ctx.moveTo(8,ty-8);  ctx.lineTo(12,ty-22);  ctx.lineTo(4,ty-10);  ctx.closePath(); ctx.fill();
  }
  if (ch.id === 'pomni') {
    const hy = oy2+H*0.09;
    ctx.fillStyle = '#A1C9F4';
    ctx.beginPath(); ctx.moveTo(-11,hy); ctx.lineTo(-4,hy-16); ctx.lineTo(3,hy); ctx.closePath(); ctx.fill();
    ctx.fillStyle = '#D0BBFF';
    ctx.beginPath(); ctx.moveTo(3,hy); ctx.lineTo(10,hy-16); ctx.lineTo(17,hy); ctx.closePath(); ctx.fill();
    ctx.fillStyle = '#ffd400';
    ctx.beginPath(); ctx.arc(-4,hy-17,3.5,0,Math.PI*2); ctx.fill();
    ctx.beginPath(); ctx.arc(10,hy-17,3.5,0,Math.PI*2); ctx.fill();
  }
  if (ch.id === 'jax') {
    ctx.fillStyle = '#8DE5A1';
    ctx.beginPath(); ctx.ellipse(-6,oy2+H*0.05,4,13,-0.2,0,Math.PI*2); ctx.fill();
    ctx.beginPath(); ctx.ellipse(6, oy2+H*0.05,4,13, 0.2,0,Math.PI*2); ctx.fill();
    ctx.fillStyle = '#FF9F9B';
    ctx.beginPath(); ctx.ellipse(-6,oy2+H*0.04,2,8,-0.2,0,Math.PI*2); ctx.fill();
    ctx.beginPath(); ctx.ellipse(6, oy2+H*0.04,2,8, 0.2,0,Math.PI*2); ctx.fill();
  }
  if (ch.id === 'kinger') {
    ctx.fillStyle = '#FFD700';
    ctx.fillRect(-8,oy2+H*0.07,16,10); ctx.fillRect(-3,oy2+H*0.04,6,8);
    ctx.fillRect(-7,oy2+H*0.04,4,3);   ctx.fillRect(3,oy2+H*0.04,4,3);
    ctx.strokeStyle = '#8C564B'; ctx.lineWidth = 1.2;
    ctx.strokeRect(-8,oy2+H*0.07,16,10);
  }
  if (ch.id === 'bubble') {
    ctx.restore(); ctx.save();
    ctx.translate(cx+W/2, cy+H/2);
    ctx.globalAlpha = 0.8;
    const grad = ctx.createRadialGradient(-5,oy2+H*0.12,2, 0,oy2+H*0.22,18);
    grad.addColorStop(0,'#ffffff'); grad.addColorStop(0.5,'#A1C9F4'); grad.addColorStop(1,'#D0BBFF');
    ctx.fillStyle = grad;
    ctx.beginPath(); ctx.arc(0,oy2+H*0.22,18,0,Math.PI*2); ctx.fill();
    ctx.globalAlpha = 1;
  }
  ctx.restore();
  const scx = cx+W/2, scy = cy-14;
  const tag = (ch.isLeader ? '[DR] ' : ch.emoji+' ') + name;
  ctx.font = isPlayer ? 'bold 11px Segoe UI' : '10px Segoe UI';
  const tw = ctx.measureText(tag).width + 8;
  ctx.fillStyle = 'rgba(0,0,0,0.72)';
  ctx.fillRect(scx-tw/2, scy-13, tw, 15);
  ctx.fillStyle = isPlayer ? '#ffd400' : '#fbfbff';
  ctx.textAlign = 'center';
  ctx.fillText(tag, scx, scy-1);
  ctx.textAlign = 'left';
}
function drawWorld() {
  const zone = ZONES[currentZoneIdx];
  const gY = getGroundY();
  const skyGrad = ctx.createLinearGradient(0,0,0,canvas.height);
  skyGrad.addColorStop(0, zone.sky); skyGrad.addColorStop(0.65, zone.ambient); skyGrad.addColorStop(1, zone.floor);
  ctx.fillStyle = skyGrad; ctx.fillRect(0,0,canvas.width,canvas.height);
  if (zone.id === 'void' || zone.id === 'moon' || zone.id === 'throne') {
    ctx.fillStyle = '#ffffff';
    for (var si = 0; si < 90; si++) {
      const sx = ((si*137.5 - camera.x*0.04) % canvas.width + canvas.width) % canvas.width;
      const sy = (si*71) % (canvas.height*0.55);
      const ss = 0.4 + (si%3)*0.5;
      ctx.globalAlpha = 0.5 + 0.5*Math.sin(frameCount*0.04+si);
      ctx.beginPath(); ctx.arc(sx,sy,ss,0,Math.PI*2); ctx.fill();
    }
    ctx.globalAlpha = 1;
  }
  if (zone.id === 'void') {
    ctx.strokeStyle = 'rgba(148,0,211,0.25)'; ctx.lineWidth = 1;
    const gOff = camera.x * 0.5 % 80;
    for (var gxi = -(gOff%80); gxi < canvas.width+80; gxi += 80) { ctx.beginPath(); ctx.moveTo(gxi,0); ctx.lineTo(gxi,canvas.height); ctx.stroke(); }
    for (var gyi = 0; gyi < canvas.height; gyi += 80) { ctx.beginPath(); ctx.moveTo(0,gyi); ctx.lineTo(canvas.width,gyi); ctx.stroke(); }
  }
  if (zone.id === 'moon') {
    ctx.fillStyle = '#1F77B4'; ctx.shadowColor='#1F77B4'; ctx.shadowBlur=22;
    ctx.beginPath(); ctx.arc(canvas.width*0.12, 75, 42, 0, Math.PI*2); ctx.fill();
    ctx.shadowBlur = 0;
    [[280,gY-8,38],[700,gY-6,28],[1300,gY-10,46]].forEach(function(c) {
      ctx.fillStyle = '#b0b0c8';
      ctx.beginPath(); ctx.ellipse(c[0]-camera.x, c[1], c[2], c[2]*0.28, 0, 0, Math.PI*2); ctx.fill();
    });
  }
  if (zone.id === 'sun') {
    ctx.fillStyle='#FF8C00'; ctx.shadowColor='#FFD700'; ctx.shadowBlur=60;
    ctx.beginPath(); ctx.arc(canvas.width*0.5, 55, 52, 0, Math.PI*2); ctx.fill();
    ctx.shadowBlur = 0;
    ctx.strokeStyle='#FFD700'; ctx.lineWidth=3; ctx.globalAlpha=0.5;
    for (var ri = 0; ri < 16; ri++) {
      const ang = ri/16*Math.PI*2 + frameCount*0.004;
      ctx.beginPath();
      ctx.moveTo(canvas.width*0.5+Math.cos(ang)*58, 55+Math.sin(ang)*58);
      ctx.lineTo(canvas.width*0.5+Math.cos(ang)*88, 55+Math.sin(ang)*88);
      ctx.stroke();
    }
    ctx.globalAlpha = 1;
  }
  if (zone.id === 'beach') {
    ctx.fillStyle='#0066AA'; ctx.fillRect(0, canvas.height*0.35, canvas.width, canvas.height*0.65);
    ctx.strokeStyle='#00BFFF'; ctx.lineWidth=2;
    for (var wi = 0; wi < 5; wi++) {
      ctx.beginPath();
      const wy = canvas.height*0.37+wi*22;
      for (var wx = 0; wx <= canvas.width; wx += 5) {
        const wOff = Math.sin((wx+camera.x*0.25+wi*55+frameCount*0.6)*0.03)*7;
        if (wx === 0) ctx.moveTo(wx, wy+wOff); else ctx.lineTo(wx, wy+wOff);
      }
      ctx.stroke();
    }
    ctx.fillStyle='#FFD700'; ctx.shadowColor='#FFD700'; ctx.shadowBlur=28;
    ctx.beginPath(); ctx.arc(canvas.width*0.82, 72, 38, 0, Math.PI*2); ctx.fill();
    ctx.shadowBlur = 0;
  }
  if (zone.id === 'fairground') {
    const fwCx = 900-camera.x, fwCy = gY-170, fwR = 80;
    ctx.strokeStyle='#FF69B4'; ctx.lineWidth=3;
    ctx.beginPath(); ctx.arc(fwCx, fwCy, fwR, 0, Math.PI*2); ctx.stroke();
    for (var fi = 0; fi < 8; fi++) {
      const ang = fi/8*Math.PI*2+frameCount*0.006;
      const fsx = fwCx+Math.cos(ang)*fwR, fsy = fwCy+Math.sin(ang)*fwR;
      ctx.fillStyle = ['#FF69B4','#FFD700','#A1C9F4','#8DE5A1'][fi%4];
      ctx.beginPath(); ctx.arc(fsx,fsy,8,0,Math.PI*2); ctx.fill();
    }
    for (var li = 0; li < 24; li++) {
      const lx = li*55-(camera.x*0.1%55)+28;
      ctx.fillStyle = ['#FFD700','#FF69B4','#A1C9F4','#8DE5A1'][li%4];
      ctx.beginPath(); ctx.arc(lx,28,5,0,Math.PI*2); ctx.fill();
    }
  }
  if (zone.id === 'throne') {
    ctx.fillStyle = '#1a1a2e';
    for (var twi = 0; twi < 18; twi++) {
      const twx = twi*115-(camera.x*0.1%115);
      ctx.fillRect(twx,28,78,60); ctx.fillRect(twx+8,8,22,26); ctx.fillRect(twx+48,8,22,26);
    }
    for (var oi = 0; oi < 7; oi++) {
      const ox2 = oi*170+80-(camera.x*0.06%170);
      const oy3 = 90+Math.sin(frameCount*0.03+oi*1.1)*28;
      const oc2 = ['#9400D3','#FFD700','#A1C9F4'][oi%3];
      ctx.fillStyle=oc2; ctx.shadowColor=oc2; ctx.shadowBlur=14;
      ctx.beginPath(); ctx.arc(ox2,oy3,10,0,Math.PI*2); ctx.fill(); ctx.shadowBlur=0;
    }
  }
  const platforms = PLATFORMS_BY_FLOOR[player.floor] || [];
  const platformY = gY - 140;
  platforms.forEach(function(room) {
    const rx = room.x - camera.x;
    if (rx+room.w < -20 || rx > canvas.width+20) return;
    ctx.fillStyle = room.color || '#1a1a2e';
    ctx.fillRect(rx, platformY, room.w, room.h);
    ctx.strokeStyle = room.accent || '#FFD700'; ctx.lineWidth = 2.5;
    ctx.strokeRect(rx, platformY, room.w, room.h);
    ctx.fillStyle = room.accent || '#FFD700'; ctx.font = 'bold 11px Segoe UI'; ctx.textAlign = 'center';
    ctx.fillText(room.label, rx+room.w/2, platformY-6);
    ctx.textAlign = 'left';
    const items = ROOM_ITEMS[room.label] || [];
    items.forEach(function(item, ii) {
      ctx.font = '10px Segoe UI'; ctx.fillStyle = '#909094';
      ctx.fillText(item, rx+6+ii*52, platformY-20);
    });
  });
  ctx.fillStyle = zone.floor; ctx.fillRect(0, gY, canvas.width, canvas.height-gY);
  ctx.strokeStyle = zone.accent || '#555555'; ctx.lineWidth = 2.5;
  ctx.beginPath(); ctx.moveTo(0,gY); ctx.lineTo(canvas.width,gY); ctx.stroke();
  ctx.font = 'bold 13px Segoe UI';
  if (player.floor < 3) { ctx.fillStyle='#A1C9F4'; ctx.fillText('UP: ' + FLOOR_NAMES[player.floor+1] + ' [Q]', 18, canvas.height-48); }
  if (player.floor > 0) { ctx.fillStyle='#8DE5A1'; ctx.fillText('DOWN: ' + FLOOR_NAMES[player.floor-1] + ' [Z]', 18, canvas.height-28); }
}
function drawMinimap() {
  const mm = document.getElementById('minimapCanvas');
  const mc = mm.getContext('2d');
  mc.fillStyle = '#0a0a1a'; mc.fillRect(0,0,120,80);
  mc.strokeStyle = '#333333'; mc.lineWidth = 1; mc.strokeRect(0,0,120,80);
  ZONES.forEach(function(z,i) { mc.fillStyle=z.accent+'33'; mc.fillRect(i*120/7,0,120/7,80); });
  mc.strokeStyle='#555555'; mc.lineWidth=1; mc.beginPath(); mc.moveTo(0,70); mc.lineTo(120,70); mc.stroke();
  npcs.filter(function(n) { return n.floor===player.floor; }).forEach(function(n) {
    mc.fillStyle=n.character.color; mc.beginPath(); mc.arc(n.x/WORLD_W*120,68,2.5,0,Math.PI*2); mc.fill();
  });
  otherPlayers.forEach(function(op) {
    mc.fillStyle='#A1C9F4'; mc.beginPath(); mc.arc(op.x/WORLD_W*120,68,2.5,0,Math.PI*2); mc.fill();
  });
  mc.fillStyle='#ffd400'; mc.fillRect(player.x/WORLD_W*120-3,63,6,7);
  mc.strokeStyle='rgba(255,212,0,0.4)'; mc.lineWidth=1;
  mc.strokeRect(camera.x/WORLD_W*120, 0, canvas.width/WORLD_W*120, 80);
  document.getElementById('mmLabel').textContent = 'Floor '+player.floor+' - '+ZONES[currentZoneIdx].name.substring(0,8);
}
function render() {
  ctx.clearRect(0,0,canvas.width,canvas.height);
  drawWorld();
  npcs.filter(function(n) { return n.floor===player.floor; }).forEach(function(n) {
    drawChar(n.x-camera.x, n.y, n.character, n.character.name, n.dir, n.breastOffset, false, null, null);
  });
  otherPlayers.filter(function(op) { return (op.floor||1)===player.floor; }).forEach(function(op) {
    drawChar(op.x-camera.x, op.y, op.character, op.name, op.dir, op.breastOffset||0, false, null, null);
  });
  drawChar(player.x-camera.x, player.y, player.character, player.name, player.dir, player.breastOffset, true, player.skinColor, player.hairColor);
  if (player.flying) {
    ctx.strokeStyle='#ffd400'; ctx.lineWidth=1.5; ctx.globalAlpha=0.35;
    for (var ti = 1; ti <= 6; ti++) {
      ctx.beginPath(); ctx.arc(player.x-camera.x+player.w/2-ti*10*player.dir, player.y+player.h/2+(Math.random()-0.5)*8, 3-ti*0.4,0,Math.PI*2); ctx.stroke();
    }
    ctx.globalAlpha = 1;
  }
  if (nearNPC && nearNPC.floor===player.floor) {
    ctx.strokeStyle='#8DE5A1'; ctx.lineWidth=2; ctx.setLineDash([4,3]);
    ctx.beginPath(); ctx.arc(nearNPC.x-camera.x+CHAR_W/2, nearNPC.y+CHAR_H/2, CHAR_H*0.7, 0, Math.PI*2); ctx.stroke();
    ctx.setLineDash([]);
  }
  drawMinimap();
}
function gameLoop() { frameCount++; updatePlayer(); updateNPCs(); render(); requestAnimationFrame(gameLoop); }
function toggleFly() {
  if (!player.isLeader) return;
  player.flying = !player.flying;
  if (player.flying) player.vy = -6;
  addChat('System', player.flying ? 'Dino Raptor is flying!' : 'Landed.', '#ffd400');
}
function doTP() {
  if (!player.isLeader) return;
  player.x = 100+Math.random()*(WORLD_W-200); player.y = getGroundY()-player.h;
  addChat('System','Dino Raptor teleported!','#ffd400');
}
function togglePhase() {
  if (!player.isLeader) return;
  player.phasing = !player.phasing;
  addChat('System', player.phasing ? 'Phase mode ON' : 'Phase mode OFF', '#ffd400');
}
function doReality() {
  if (!player.isLeader) return;
  currentZoneIdx = (currentZoneIdx+1) % ZONES.length;
  addChat('System','Reality shift: '+ZONES[currentZoneIdx].name,'#ffd400');
}
function changeFloor(delta) {
  const nf = player.floor+delta;
  if (nf < 0 || nf > 3) { addChat('System','No floor there!','#f04438'); return; }
  player.floor = nf; placePlayerOnFloor();
  const ind = document.getElementById('floorIndicator');
  ind.textContent = 'Floor: ' + FLOOR_NAMES[player.floor];
  ind.style.display = 'block';
  setTimeout(function() { ind.style.display='none'; }, 1800);
  addChat('System','Floor '+player.floor+' - '+FLOOR_NAMES[player.floor],'#A1C9F4');
}
function tryInteract() {
  if (!nearNPC || nearNPC.floor!==player.floor || dialogOpen) return;
  const lines = NPC_LINES[nearNPC.character.id] || ['...'];
  const line = lines[nearNPC.dialogIdx % lines.length];
  nearNPC.dialogIdx++;
  document.getElementById('dialogSpeaker').textContent = nearNPC.character.name;
  document.getElementById('dialogText').textContent = line;
  document.getElementById('dialogBox').style.display = 'block';
  dialogOpen = true;
}
function closeDialog() { document.getElementById('dialogBox').style.display='none'; dialogOpen=false; canvas.focus(); }
const ROOM_ACTIONS = ['Went to sleep','Ate a burger','Drank water','Smoked','Vaped','Drank a beer','Played PS5','Used the laptop','Used the gaming PC','Took a shower','Checked the phone','Practiced with gun'];
function doRoomAction() {
  const act = ROOM_ACTIONS[Math.floor(Math.random()*ROOM_ACTIONS.length)];
  addChat(player.name, act, player.isLeader ? '#ffd400' : '#fbfbff');
}
const BLOCKED = ['fuck','shit','bitch','cunt','cock','dick','nigga','nigger','kut','klootzak','godverdomme','tering','kanker','hoer'];
function filterMsg(msg) {
  let out = msg;
  BLOCKED.forEach(function(w) { out = out.replace(new RegExp(w,'gi'),'*'.repeat(w.length)); });
  return out;
}
function addChat(sender, msg, color) {
  const log = document.getElementById('chatLog');
  const el = document.createElement('div'); el.style.marginBottom = '2px';
  const sc = color || '#A1C9F4';
  el.innerHTML = '<span style="color:' + sc + ';font-weight:bold">' + sender + ':</span> <span style="color:#fbfbff">' + msg + '</span>';
  log.appendChild(el); log.scrollTop = log.scrollHeight;
}
function sendChat() {
  const inp = document.getElementById('chatMsg');
  const raw = inp.value.trim(); if (!raw) return;
  addChat(player.name, filterMsg(raw), player.isLeader ? '#ffd400' : '#fbfbff');
  inp.value = ''; canvas.focus();
  setTimeout(function() {
    const on = npcs.filter(function(n) { return n.floor===player.floor; });
    if (!on.length) return;
    const npc = on[Math.floor(Math.random()*on.length)];
    const lines = NPC_LINES[npc.character.id] || ['...'];
    addChat(npc.character.name, lines[Math.floor(Math.random()*lines.length)], npc.character.color);
  }, 1000+Math.random()*1500);
}
var rooms = [
  { id:'r1', name:'Throne Room HQ',  zone:'throne',     players:3, max:16, priv:false },
  { id:'r2', name:'Beach Party',      zone:'beach',      players:7, max:16, priv:false },
  { id:'r3', name:'Void Club',        zone:'void',       players:2, max:8,  priv:true, code:'I1XTKU' },
  { id:'r4', name:'Kermis Madness',   zone:'fairground', players:5, max:16, priv:false },
];
function toggleRoomMenu() {
  const menu = document.getElementById('roomMenu');
  const vis = menu.style.display === 'block';
  menu.style.display = vis ? 'none' : 'block';
  if (!vis) renderRoomList();
}
function closeRoomMenu() { document.getElementById('roomMenu').style.display='none'; canvas.focus(); }
function renderRoomList() {
  const list = document.getElementById('roomList'); list.innerHTML = '';
  rooms.filter(function(r) { return !r.priv; }).forEach(function(r) {
    const d = document.createElement('div');
    d.style.cssText = 'background:#1a1a2e;border-radius:6px;padding:5px 9px;margin-bottom:5px;cursor:pointer;font-size:12px;border:1px solid #333;';
    d.textContent = r.name + ' (' + r.players + '/' + r.max + ')';
    d.onclick = function() { joinRoom(r); closeRoomMenu(); };
    list.appendChild(d);
  });
}
function createRoom() {
  const name = document.getElementById('newRoomName').value.trim() || 'My Room';
  const zone = document.getElementById('newRoomZone').value;
  const priv = document.getElementById('privateRoom').checked;
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  const code = priv ? Array.from({length:6},function(){return chars[Math.floor(Math.random()*chars.length)];}).join('') : null;
  rooms.push({ id:'r'+Date.now(), name:name, zone:zone, players:1, max:16, priv:priv, code:code });
  if (priv && code) {
    document.getElementById('generatedCode').textContent = code;
    document.getElementById('roomCodeDisplay').style.display = 'block';
  }
  addChat('System','Room "'+name+'" created!','#8DE5A1');
  closeRoomMenu();
}
function joinWithCode() {
  const code = document.getElementById('joinCode').value.trim().toUpperCase();
  const room = rooms.find(function(r) { return r.code===code; });
  if (room) { joinRoom(room); closeRoomMenu(); }
  else addChat('System','Wrong code! Ask the host.','#f04438');
}
function joinRoom(r) {
  addChat('System','Joined: '+r.name,'#8DE5A1');
  document.getElementById('hudPlayers').textContent = (r.players+1)+' players';
}
setInterval(function() {
  if (!gameStarted) return;
  const on = npcs.filter(function(n) { return n.floor===player.floor; });
  if (!on.length) return;
  const n = on[Math.floor(Math.random()*on.length)];
  const lines = NPC_LINES[n.character.id] || ['...'];
  addChat(n.character.name, lines[Math.floor(Math.random()*lines.length)], n.character.color);
}, 9000);
</script>
</body>
</html>
'''


st.markdown('''<style>
  .main .block-container { padding:0 !important; max-width:100% !important; }
  header { display:none !important; }
  footer { display:none !important; }
  #MainMenu { display:none !important; }
</style>''', unsafe_allow_html=True)

st.components.v1.html(GAME_HTML, height=780, scrolling=False)
