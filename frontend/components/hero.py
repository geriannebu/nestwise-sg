import base64
from pathlib import Path

import streamlit.components.v1 as components

def _get_logo_src() -> str:
    candidates = [
        Path("assets/nestwise_logo.jpeg"),
        Path("assets/nestwise_logo.png"),
        Path("frontend/assets/nestwise_logo.jpeg"),
        Path("frontend/assets/nestwise_logo.png"),
    ]
    for p in candidates:
        if p.exists():
            mime = "image/png" if p.suffix.lower() == ".png" else "image/jpeg"
            return f"data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"
    return ""


def render_hero() -> None:
    logo_src = _get_logo_src()
    logo_tag = (
        f"<img class=\'logo-img\' src=\'{logo_src}\' alt=\'NestWise\' />"
        if logo_src else "<span class=\'logo-mono\'>N</span>"
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:100%;font-family:'DM Sans',-apple-system,sans-serif;background:transparent;color:#0f172a;overflow:hidden}}
.hero{{position:relative;width:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:40px 32px 56px;background:radial-gradient(ellipse 65% 50% at 50% 0%,rgba(199,244,233,0.70) 0%,transparent 60%),#f7fbfa}}
.logo-wrap{{position:relative;width:110px;height:110px;margin:0 auto 14px;animation:logo-in 0.7s cubic-bezier(0.22,1,0.36,1) both}}
.logo-wrap::before{{content:'';position:absolute;inset:-5px;border-radius:50%;background:conic-gradient(from 0deg,rgba(10,163,138,0.55),rgba(52,209,180,0.15),rgba(10,163,138,0.55));animation:spin 7s linear infinite}}
.logo-wrap::after{{content:'';position:absolute;inset:-2px;border-radius:50%;background:#f7fbfa}}
.logo-circle{{position:relative;z-index:1;width:100%;height:100%;border-radius:50%;background:linear-gradient(145deg,#e6f8f4,#fff);overflow:hidden;display:grid;place-items:center;box-shadow:0 8px 28px rgba(10,163,138,0.16)}}
.logo-img{{width:82%;height:82%;object-fit:contain;mix-blend-mode:multiply;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)}}
.logo-mono{{font-size:36px;font-weight:800;color:#0aa38a}}
@keyframes logo-in{{from{{opacity:0;transform:scale(0.75) translateY(16px)}}to{{opacity:1;transform:scale(1) translateY(0)}}}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.wordmark{{font-size:13px;font-weight:800;letter-spacing:0.07em;text-transform:uppercase;color:#0aa38a;margin-bottom:18px;opacity:0;animation:fadeup 0.5s 0.3s ease both;animation-fill-mode:forwards}}
.title{{font-size:clamp(38px,5.5vw,72px);line-height:0.94;letter-spacing:-0.055em;font-weight:800;color:#0b132d;max-width:820px;margin:0 auto 14px;opacity:0;animation:fadeup 0.6s 0.15s ease both;animation-fill-mode:forwards}}
.accent{{background:linear-gradient(135deg,#0aa38a 0%,#34d1b4 100%);-webkit-background-clip:text;background-clip:text;color:transparent}}
.sub{{font-size:clamp(14px,1.8vw,17px);line-height:1.7;font-weight:500;color:#5f6c7b;max-width:560px;margin:0 auto 28px;opacity:0;animation:fadeup 0.6s 0.22s ease both;animation-fill-mode:forwards}}
.ticker-wrap{{position:relative;width:100%;max-width:620px;margin:0 auto 28px;height:58px;overflow:hidden;opacity:0;animation:fadeup 0.6s 0.3s ease both;animation-fill-mode:forwards}}
.ticker-track{{display:flex;flex-direction:column;animation:tick 9s ease-in-out infinite}}
.ticker-item{{height:58px;display:flex;align-items:center;justify-content:center;gap:14px;flex-shrink:0}}
.ticker-num{{font-size:30px;font-weight:800;letter-spacing:-0.04em;background:linear-gradient(135deg,#0aa38a,#34d1b4);-webkit-background-clip:text;background-clip:text;color:transparent;line-height:1}}
.ticker-label{{font-size:13px;font-weight:600;color:#6b7280;text-align:left;line-height:1.35;max-width:180px}}
.ticker-div{{width:1px;height:28px;background:rgba(10,163,138,0.20);flex-shrink:0}}
@keyframes tick{{0%,26%{{transform:translateY(0)}}33%,59%{{transform:translateY(-58px)}}66%,92%{{transform:translateY(-116px)}}100%{{transform:translateY(0)}}}}
.chips{{display:flex;flex-wrap:wrap;gap:9px;justify-content:center;margin-bottom:28px;opacity:0;animation:fadeup 0.6s 0.36s ease both;animation-fill-mode:forwards}}
.chip{{display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:999px;background:rgba(255,255,255,0.84);border:1px solid rgba(15,23,42,0.09);box-shadow:0 4px 14px rgba(15,23,42,0.05);color:#334155;font-size:12.5px;font-weight:700;white-space:nowrap}}
.cta-row{{display:flex;flex-wrap:wrap;gap:11px;align-items:center;justify-content:center;opacity:0;animation:fadeup 0.6s 0.42s ease both;animation-fill-mode:forwards}}
.cta-primary{{display:inline-flex;align-items:center;gap:9px;padding:14px 28px;border-radius:999px;background:linear-gradient(135deg,#0aa38a 0%,#34d1b4 100%);color:#fff;text-decoration:none;font-size:14px;font-weight:800;letter-spacing:-0.01em;box-shadow:0 10px 32px rgba(10,163,138,0.30);transition:transform 0.17s ease,box-shadow 0.17s ease;cursor:pointer;border:none}}
.cta-primary:hover{{transform:translateY(-2px);box-shadow:0 16px 40px rgba(10,163,138,0.38)}}
.cta-ghost{{display:inline-flex;align-items:center;gap:7px;padding:12px 20px;border-radius:999px;background:rgba(255,255,255,0.86);border:1px solid rgba(15,23,42,0.09);color:#374151;font-size:13px;font-weight:700;box-shadow:0 4px 14px rgba(15,23,42,0.05)}}
.scroll-hint{{position:absolute;bottom:16px;left:50%;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:4px;color:#9ca3af;font-size:10px;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;pointer-events:none;opacity:0;animation:fadeup 0.5s 1.1s ease both,bob 2.6s 1.8s ease-in-out infinite;animation-fill-mode:forwards}}
@keyframes fadeup{{from{{opacity:0;transform:translateY(18px)}}to{{opacity:1;transform:translateY(0)}}}}
@keyframes bob{{0%,100%{{transform:translateX(-50%) translateY(0)}}50%{{transform:translateX(-50%) translateY(6px)}}}}
</style>
</head>
<body>
<div class="hero">
  <div class="logo-wrap"><div class="logo-circle">{logo_tag}</div></div>
  <div class="wordmark">NestWise SG</div>
  <div class="title">Find the <span class="accent">fair&nbsp;price</span><br>of your dream flat</div>
  <div class="sub">Compare asking prices against modelled fair value and recent transacted benchmarks — then explore the neighbourhood around every option.</div>
  <div class="ticker-wrap">
    <div class="ticker-track">
      <div class="ticker-item"><span class="ticker-num">23</span><div class="ticker-div"></div><span class="ticker-label">HDB towns analysed across Singapore</span></div>
      <div class="ticker-item"><span class="ticker-num">S$0</span><div class="ticker-div"></div><span class="ticker-label">Cost to find your fair price estimate</span></div>
      <div class="ticker-item"><span class="ticker-num">6+</span><div class="ticker-div"></div><span class="ticker-label">Amenity layers mapped around every flat</span></div>
      <div class="ticker-item"><span class="ticker-num">23</span><div class="ticker-div"></div><span class="ticker-label">HDB towns analysed across Singapore</span></div>
    </div>
  </div>
  <div class="chips">
    <span class="chip">🔍 Price analysis</span>
    <span class="chip">🗺️ Town matching</span>
    <span class="chip">📍 Amenity map</span>
    <span class="chip">⚖️ Flat comparison</span>
  </div>
  <div class="cta-row">
    <a class="cta-primary" id="cta" href="#">Start your search <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M8 3v10M3 8l5 5 5-5" stroke="white" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
    <div class="cta-ghost"><svg width="13" height="13" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6.5" stroke="#9ca3af" stroke-width="1.4"/><path d="M8 5v3.5l2 2" stroke="#9ca3af" stroke-width="1.4" stroke-linecap="round"/></svg>Takes about 2 minutes</div>
  </div>
  <div class="scroll-hint"><span>Scroll</span><svg width="13" height="13" viewBox="0 0 20 20" fill="none"><path d="M10 4v12M5 11l5 5 5-5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
</div>
<script>
(function(){{
  var cta=document.getElementById('cta');
  if(cta){{
    cta.addEventListener('click',function(e){{
      e.preventDefault();
      try{{
        var t=window.parent.document.getElementById('nw-form-anchor');
        if(t){{t.scrollIntoView({{behavior:'smooth',block:'start'}})}}
        else{{window.parent.scrollBy({{top:window.parent.innerHeight*0.92,behavior:'smooth'}})}}
      }}catch(err){{window.parent.scrollBy({{top:700,behavior:'smooth'}})}}
    }});
  }}
  function resize(){{
    var h=document.documentElement.getBoundingClientRect().height;
    window.parent.postMessage({{type:'streamlit:setFrameHeight',height:Math.ceil(h)}},'*');
  }}
  resize();
  window.addEventListener('load',resize);
  if(document.fonts&&document.fonts.ready){{document.fonts.ready.then(resize);}}
  setTimeout(resize,200);
  setTimeout(resize,600);
}})();
</script>
</body>
</html>"""

    components.html(html, height=700, scrolling=False)
