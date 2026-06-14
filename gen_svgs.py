#!/usr/bin/env python3
"""Generate professional product SVG illustrations for Patitas Pet Shop."""
import os

os.makedirs('/home/user/Pet-Shop/assets/images', exist_ok=True)

def write_svg(filename, content):
    path = f'/home/user/Pet-Shop/assets/images/{filename}.svg'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  ✓ {filename}.svg')


def food_bag(bg1, bg2, brand, line2, accent, w=800, h=600):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{bg1}"/>
      <stop offset="100%" style="stop-color:{bg2}"/>
    </linearGradient>
    <linearGradient id="bag" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:rgba(255,255,255,0.28)"/>
      <stop offset="100%" style="stop-color:rgba(255,255,255,0.09)"/>
    </linearGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#bg)"/>
  <!-- ambient glow -->
  <ellipse cx="{w//2}" cy="{h//2}" rx="{int(w*.55)}" ry="{int(h*.55)}" fill="rgba(255,255,255,0.04)"/>
  <!-- shadow -->
  <ellipse cx="{w//2}" cy="{int(h*.89)}" rx="190" ry="18" fill="rgba(0,0,0,0.18)"/>
  <!-- bag body -->
  <rect x="{int(w*.27)}" y="{int(h*.22)}" width="{int(w*.46)}" height="{int(h*.62)}" rx="20" fill="url(#bag)" stroke="rgba(255,255,255,0.28)" stroke-width="1.5"/>
  <!-- top fold -->
  <path d="M{int(w*.30)} {int(h*.22)} L{int(w*.70)} {int(h*.22)} L{int(w*.66)} {int(h*.10)} L{int(w*.34)} {int(h*.10)} Z" fill="rgba(255,255,255,0.18)" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
  <!-- colour band -->
  <rect x="{int(w*.27)}" y="{int(h*.46)}" width="{int(w*.46)}" height="{int(h*.16)}" fill="{accent}" opacity="0.88"/>
  <!-- paw on band -->
  <g transform="translate({int(w*.33)},{int(h*.535)})" fill="rgba(255,255,255,0.30)">
    <ellipse cx="0" cy="9" rx="13" ry="11"/>
    <circle cx="-15" cy="-2" r="6"/>
    <circle cx="-6" cy="-11" r="6"/>
    <circle cx="6" cy="-11" r="6"/>
    <circle cx="15" cy="-2" r="6"/>
  </g>
  <!-- brand text -->
  <text x="{w//2}" y="{int(h*.545)}" text-anchor="middle" font-size="30" font-weight="800" font-family="Poppins,Arial,sans-serif" fill="white">{brand}</text>
  <!-- product line -->
  <text x="{w//2}" y="{int(h*.578)}" text-anchor="middle" font-size="15" font-weight="500" font-family="Poppins,Arial,sans-serif" fill="rgba(255,255,255,0.82)">{line2}</text>
  <!-- weight tag -->
  <rect x="{int(w*.42)}" y="{int(h*.76)}" width="{int(w*.16)}" height="30" rx="15" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.38)" stroke-width="1.5"/>
  <text x="{w//2}" y="{int(h*.80)}" text-anchor="middle" font-size="14" font-weight="600" font-family="Poppins,Arial,sans-serif" fill="white">15 kg</text>
</svg>'''


def rascador():
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#6B2A0A"/><stop offset="100%" style="stop-color:#D4520A"/>
    </linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <ellipse cx="400" cy="310" rx="360" ry="280" fill="rgba(255,255,255,0.03)"/>
  <!-- shadow -->
  <ellipse cx="400" cy="530" rx="155" ry="17" fill="rgba(0,0,0,0.2)"/>
  <!-- base platform -->
  <rect x="260" y="490" width="280" height="28" rx="9" fill="rgba(255,255,255,0.25)" stroke="rgba(255,255,255,0.35)" stroke-width="1.5"/>
  <!-- lower platform -->
  <rect x="250" y="415" width="300" height="28" rx="9" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.28)" stroke-width="1.5"/>
  <!-- mid platform -->
  <rect x="275" y="290" width="250" height="28" rx="9" fill="rgba(255,255,255,0.22)" stroke="rgba(255,255,255,0.3)" stroke-width="1.5"/>
  <!-- top platform / house -->
  <rect x="250" y="88" width="300" height="36" rx="10" fill="rgba(255,255,255,0.3)" stroke="rgba(255,255,255,0.4)" stroke-width="1.5"/>
  <!-- house walls -->
  <rect x="285" y="88" width="230" height="100" rx="0" fill="rgba(255,255,255,0.12)" stroke="rgba(255,255,255,0.22)" stroke-width="1"/>
  <!-- house roof -->
  <polygon points="280,88 520,88 400,40" fill="rgba(255,255,255,0.18)" stroke="rgba(255,255,255,0.28)" stroke-width="1.5"/>
  <!-- main post -->
  <rect x="365" y="118" width="70" height="380" rx="12" fill="rgba(255,255,255,0.14)" stroke="rgba(255,255,255,0.22)" stroke-width="1.5"/>
  <!-- sisal texture -->
  <g stroke="rgba(255,255,255,0.07)" stroke-width="2">
    <line x1="378" y1="120" x2="378" y2="498"/>
    <line x1="390" y1="120" x2="390" y2="498"/>
    <line x1="402" y1="120" x2="402" y2="498"/>
    <line x1="414" y1="120" x2="414" y2="498"/>
    <line x1="424" y1="120" x2="424" y2="498"/>
  </g>
  <!-- cat silhouette on top house -->
  <g fill="rgba(255,255,255,0.65)" transform="translate(346,28)">
    <ellipse cx="54" cy="20" rx="24" ry="20"/>
    <circle cx="54" cy="-7" r="15"/>
    <polygon points="40,-20 46,-34 52,-20"/>
    <polygon points="56,-20 62,-34 68,-20"/>
  </g>
  <!-- label -->
  <text x="400" y="570" text-anchor="middle" font-size="18" font-weight="700" font-family="Poppins,Arial,sans-serif" fill="rgba(255,255,255,0.88)">Rascador Torre Sisal · 120 cm</text>
</svg>'''


def cama():
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a2a5c"/><stop offset="100%" style="stop-color:#2471a3"/>
    </linearGradient>
    <radialGradient id="cushion" cx="45%" cy="38%">
      <stop offset="0%" style="stop-color:rgba(255,255,255,0.38)"/>
      <stop offset="100%" style="stop-color:rgba(255,255,255,0.10)"/>
    </radialGradient>
  </defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <!-- ambient -->
  <ellipse cx="400" cy="320" rx="350" ry="280" fill="rgba(255,255,255,0.03)"/>
  <!-- shadow -->
  <ellipse cx="400" cy="518" rx="210" ry="22" fill="rgba(0,0,0,0.18)"/>
  <!-- outer rim/bolster -->
  <ellipse cx="400" cy="370" rx="238" ry="136" fill="rgba(255,255,255,0.18)" stroke="rgba(255,255,255,0.28)" stroke-width="2"/>
  <!-- bolster top arc (raised edge) -->
  <path d="M172 330 Q400 230 628 330" stroke="rgba(255,255,255,0.30)" stroke-width="30" fill="none" stroke-linecap="round"/>
  <!-- inner cushion -->
  <ellipse cx="400" cy="385" rx="196" ry="104" fill="url(#cushion)" stroke="rgba(255,255,255,0.22)" stroke-width="1.5"/>
  <!-- quilted centre dip -->
  <ellipse cx="400" cy="390" rx="125" ry="62" fill="rgba(255,255,255,0.07)"/>
  <!-- sleeping dog silhouette -->
  <g fill="rgba(255,255,255,0.55)">
    <!-- curled body -->
    <ellipse cx="395" cy="380" rx="88" ry="46"/>
    <!-- head -->
    <circle cx="488" cy="352" r="30"/>
    <!-- muzzle -->
    <ellipse cx="514" cy="366" rx="18" ry="14"/>
    <!-- ear flop -->
    <ellipse cx="474" cy="330" rx="12" ry="20" transform="rotate(-25,474,330)"/>
    <!-- paw -->
    <ellipse cx="318" cy="404" rx="28" ry="12" transform="rotate(-8,318,404)"/>
  </g>
  <!-- Zzz -->
  <g fill="rgba(255,255,255,0.30)" font-size="26" font-weight="700" font-family="Poppins,Arial,sans-serif">
    <text x="560" y="300">Z</text>
    <text x="588" y="274">Z</text>
    <text x="614" y="252">Z</text>
  </g>
  <!-- label -->
  <text x="400" y="562" text-anchor="middle" font-size="18" font-weight="700" font-family="Poppins,Arial,sans-serif" fill="rgba(255,255,255,0.88)">Cama Premium · Tallas M · L · XL</text>
</svg>'''


def piedras():
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4a1570"/><stop offset="100%" style="stop-color:#8e44ad"/>
    </linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <ellipse cx="400" cy="310" rx="360" ry="280" fill="rgba(255,255,255,0.03)"/>
  <!-- litter tray -->
  <path d="M148 310 L198 472 L602 472 L652 310 Z" fill="rgba(255,255,255,0.14)" stroke="rgba(255,255,255,0.25)" stroke-width="1.5"/>
  <!-- tray rim -->
  <rect x="138" y="292" width="524" height="28" rx="9" fill="rgba(255,255,255,0.22)" stroke="rgba(255,255,255,0.32)" stroke-width="1.5"/>
  <!-- litter granules -->
  <g fill="rgba(255,255,255,0.45)">
    <ellipse cx="240" cy="386" rx="20" ry="13" transform="rotate(12,240,386)"/>
    <ellipse cx="295" cy="418" rx="16" ry="10" transform="rotate(-8,295,418)"/>
    <ellipse cx="348" cy="374" rx="22" ry="14" transform="rotate(5,348,374)"/>
    <ellipse cx="408" cy="402" rx="18" ry="11" transform="rotate(-16,408,402)"/>
    <ellipse cx="462" cy="382" rx="17" ry="11" transform="rotate(10,462,382)"/>
    <ellipse cx="516" cy="422" rx="20" ry="12" transform="rotate(-4,516,422)"/>
    <ellipse cx="270" cy="440" rx="14" ry="9" transform="rotate(8,270,440)"/>
    <ellipse cx="380" cy="448" rx="18" ry="10" transform="rotate(-12,380,448)"/>
    <ellipse cx="444" cy="440" rx="15" ry="9" transform="rotate(18,444,440)"/>
    <ellipse cx="325" cy="398" rx="12" ry="8" transform="rotate(-6,325,398)"/>
    <ellipse cx="490" cy="404" rx="16" ry="10" transform="rotate(9,490,404)"/>
    <ellipse cx="554" cy="418" rx="14" ry="9" transform="rotate(-11,554,418)"/>
    <ellipse cx="210" cy="420" rx="12" ry="8" transform="rotate(14,210,420)"/>
    <ellipse cx="575" cy="390" rx="13" ry="8" transform="rotate(-7,575,390)"/>
  </g>
  <!-- product badge -->
  <rect x="272" y="166" width="256" height="100" rx="18" fill="rgba(255,255,255,0.16)" stroke="rgba(255,255,255,0.28)" stroke-width="1.5"/>
  <text x="400" y="210" text-anchor="middle" font-size="24" font-weight="800" font-family="Poppins,Arial,sans-serif" fill="white">Piedras Sanitarias</text>
  <text x="400" y="238" text-anchor="middle" font-size="14" font-weight="500" font-family="Poppins,Arial,sans-serif" fill="rgba(255,255,255,0.78)">Premium · Control de Olores · 4 kg</text>
  <!-- cat silhouette peeking -->
  <g fill="rgba(255,255,255,0.22)" transform="translate(540,290)">
    <circle cx="60" cy="0" r="38"/>
    <polygon points="38,-38 46,-60 54,-38"/>
    <polygon points="66,-38 74,-60 82,-38"/>
    <ellipse cx="44" cy="8" rx="8" ry="5"/>
    <ellipse cx="76" cy="8" rx="8" ry="5"/>
  </g>
</svg>'''


def juguetes():
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a4a1a"/><stop offset="100%" style="stop-color:#27ae60"/>
    </linearGradient>
    <radialGradient id="ball" cx="38%" cy="32%">
      <stop offset="0%" style="stop-color:rgba(255,230,60,0.9)"/>
      <stop offset="55%" style="stop-color:rgba(200,160,0,0.8)"/>
      <stop offset="100%" style="stop-color:rgba(140,100,0,0.7)"/>
    </radialGradient>
  </defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <ellipse cx="400" cy="310" rx="360" ry="290" fill="rgba(255,255,255,0.03)"/>
  <!-- shadow -->
  <ellipse cx="330" cy="512" rx="150" ry="16" fill="rgba(0,0,0,0.18)"/>
  <!-- main tennis ball -->
  <circle cx="320" cy="305" r="162" fill="url(#ball)" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
  <!-- seam lines -->
  <path d="M192 188 Q258 268 224 350 Q190 435 264 510" stroke="white" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.65"/>
  <path d="M448 188 Q382 268 416 350 Q450 435 376 510" stroke="white" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.65"/>
  <!-- bone (top right) -->
  <g fill="rgba(255,255,255,0.50)" transform="translate(530,90)">
    <rect x="22" y="14" width="96" height="22" rx="11"/>
    <circle cx="20" cy="14" r="16"/>
    <circle cx="20" cy="36" r="16"/>
    <circle cx="118" cy="14" r="16"/>
    <circle cx="118" cy="36" r="16"/>
  </g>
  <!-- rope toy -->
  <path d="M582 320 Q630 268 650 320 Q670 372 622 404" stroke="rgba(255,255,255,0.48)" stroke-width="14" fill="none" stroke-linecap="round"/>
  <path d="M622 404 Q575 436 565 390 Q555 344 600 334" stroke="rgba(255,255,255,0.48)" stroke-width="14" fill="none" stroke-linecap="round"/>
  <!-- stars -->
  <g fill="rgba(255,255,255,0.28)" font-size="24" font-family="Arial">
    <text x="140" y="190">&#9733;</text>
    <text x="630" y="178">&#9733;</text>
    <text x="665" y="468">&#9733;</text>
  </g>
  <!-- label -->
  <text x="400" y="564" text-anchor="middle" font-size="18" font-weight="700" font-family="Poppins,Arial,sans-serif" fill="rgba(255,255,255,0.90)">Juguetes para Mascotas</text>
</svg>'''


def correas():
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#5c0a0a"/><stop offset="100%" style="stop-color:#c0392b"/>
    </linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <ellipse cx="400" cy="310" rx="360" ry="280" fill="rgba(255,255,255,0.03)"/>
  <!-- collar ring -->
  <circle cx="350" cy="240" r="130" fill="none" stroke="rgba(255,255,255,0.32)" stroke-width="30"/>
  <!-- collar buckle at top -->
  <rect x="322" y="98" width="56" height="28" rx="6" fill="rgba(255,255,255,0.48)" stroke="rgba(255,255,255,0.55)" stroke-width="1.5"/>
  <line x1="350" y1="98" x2="350" y2="126" stroke="rgba(255,255,255,0.80)" stroke-width="3.5"/>
  <!-- collar tag -->
  <line x1="350" y1="370" x2="350" y2="418" stroke="rgba(255,255,255,0.38)" stroke-width="3"/>
  <ellipse cx="350" cy="442" rx="28" ry="28" fill="rgba(255,255,255,0.22)" stroke="rgba(255,255,255,0.38)" stroke-width="2"/>
  <text x="350" y="450" text-anchor="middle" font-size="14" font-weight="800" font-family="Poppins,Arial,sans-serif" fill="rgba(255,255,255,0.78)">ID</text>
  <!-- leash line -->
  <path d="M478 240 Q570 160 638 200 Q690 228 670 310 Q650 380 592 408" stroke="rgba(255,255,255,0.42)" stroke-width="13" fill="none" stroke-linecap="round"/>
  <!-- handle loop -->
  <path d="M562 440 Q530 398 588 372 Q648 348 656 408 Q660 460 600 468 Q548 476 548 438 Z" fill="none" stroke="rgba(255,255,255,0.40)" stroke-width="13" stroke-linejoin="round"/>
  <!-- harness ring (small) -->
  <circle cx="478" cy="240" r="14" fill="none" stroke="rgba(255,255,255,0.55)" stroke-width="6"/>
  <!-- label -->
  <text x="210" y="540" text-anchor="middle" font-size="18" font-weight="700" font-family="Poppins,Arial,sans-serif" fill="rgba(255,255,255,0.88)">Correas y Collares</text>
  <text x="210" y="565" text-anchor="middle" font-size="14" font-weight="400" font-family="Poppins,Arial,sans-serif" fill="rgba(255,255,255,0.58)">Paseos seguros y felices</text>
</svg>'''


def higiene():
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0a4a3e"/><stop offset="100%" style="stop-color:#1abc9c"/>
    </linearGradient>
    <linearGradient id="bottle" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:rgba(255,255,255,0.38)"/>
      <stop offset="100%" style="stop-color:rgba(255,255,255,0.11)"/>
    </linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <ellipse cx="400" cy="310" rx="360" ry="280" fill="rgba(255,255,255,0.03)"/>
  <!-- shadows -->
  <ellipse cx="305" cy="515" rx="102" ry="13" fill="rgba(0,0,0,0.14)"/>
  <ellipse cx="490" cy="515" rx="70" ry="10" fill="rgba(0,0,0,0.12)"/>
  <!-- === shampoo bottle === -->
  <!-- pump cap -->
  <rect x="270" y="135" width="70" height="65" rx="10" fill="rgba(255,255,255,0.28)" stroke="rgba(255,255,255,0.38)" stroke-width="1.5"/>
  <!-- pump tube -->
  <rect x="300" y="82" width="20" height="60" rx="7" fill="rgba(255,255,255,0.32)" stroke="rgba(255,255,255,0.40)" stroke-width="1.5"/>
  <!-- pump head -->
  <rect x="286" y="80" width="48" height="14" rx="5" fill="rgba(255,255,255,0.38)"/>
  <!-- bottle body -->
  <rect x="236" y="198" width="138" height="300" rx="34" fill="url(#bottle)" stroke="rgba(255,255,255,0.32)" stroke-width="1.5"/>
  <!-- label area -->
  <rect x="248" y="258" width="114" height="110" rx="10" fill="rgba(255,255,255,0.18)" stroke="rgba(255,255,255,0.28)" stroke-width="1"/>
  <text x="305" y="300" text-anchor="middle" font-size="15" font-weight="800" font-family="Poppins,Arial,sans-serif" fill="white">PET</text>
  <text x="305" y="320" text-anchor="middle" font-size="15" font-weight="800" font-family="Poppins,Arial,sans-serif" fill="white">SHAMPOO</text>
  <text x="305" y="340" text-anchor="middle" font-size="11" font-weight="400" font-family="Poppins,Arial,sans-serif" fill="rgba(255,255,255,0.7)">500 ml</text>
  <!-- === comb/brush === -->
  <!-- handle -->
  <rect x="444" y="248" width="38" height="200" rx="12" fill="rgba(255,255,255,0.20)" stroke="rgba(255,255,255,0.30)" stroke-width="1.5"/>
  <!-- bristle base -->
  <rect x="430" y="432" width="66" height="24" rx="5" fill="rgba(255,255,255,0.28)" stroke="rgba(255,255,255,0.35)" stroke-width="1.2"/>
  <!-- bristles -->
  <g stroke="rgba(255,255,255,0.55)" stroke-width="3" stroke-linecap="round">
    <line x1="440" y1="456" x2="440" y2="496"/>
    <line x1="450" y1="456" x2="450" y2="498"/>
    <line x1="460" y1="456" x2="460" y2="496"/>
    <line x1="470" y1="456" x2="470" y2="498"/>
    <line x1="480" y1="456" x2="480" y2="496"/>
    <line x1="490" y1="456" x2="490" y2="498"/>
  </g>
  <!-- soap bubbles -->
  <g fill="none" stroke="rgba(255,255,255,0.22)" stroke-width="2">
    <circle cx="580" cy="200" r="34"/>
    <circle cx="626" cy="148" r="20"/>
    <circle cx="590" cy="286" r="25"/>
    <circle cx="638" cy="238" r="15"/>
    <circle cx="168" cy="228" r="28"/>
    <circle cx="128" cy="180" r="17"/>
    <circle cx="185" cy="315" r="20"/>
    <circle cx="145" cy="280" r="12"/>
  </g>
  <!-- label -->
  <text x="400" y="562" text-anchor="middle" font-size="18" font-weight="700" font-family="Poppins,Arial,sans-serif" fill="rgba(255,255,255,0.90)">Higiene y Cuidado</text>
</svg>'''


def hero():
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="700" viewBox="0 0 1200 700">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#031a0d"/>
      <stop offset="50%" style="stop-color:#0a5c35"/>
      <stop offset="100%" style="stop-color:#1a8a50"/>
    </linearGradient>
    <radialGradient id="glow" cx="30%" cy="55%" r="65%">
      <stop offset="0%" style="stop-color:rgba(37,211,102,0.18)"/>
      <stop offset="100%" style="stop-color:rgba(37,211,102,0)"/>
    </radialGradient>
  </defs>
  <rect width="1200" height="700" fill="url(#bg)"/>
  <rect width="1200" height="700" fill="url(#glow)"/>
  <!-- large background paw marks -->
  <g fill="rgba(255,255,255,0.04)">
    <ellipse cx="140" cy="200" rx="44" ry="36"/>
    <circle cx="94"  cy="152" r="17"/>
    <circle cx="116" cy="134" r="17"/>
    <circle cx="142" cy="130" r="17"/>
    <circle cx="168" cy="136" r="17"/>
    <ellipse cx="950" cy="510" rx="54" ry="44"/>
    <circle cx="884" cy="448" r="21"/>
    <circle cx="912" cy="422" r="21"/>
    <circle cx="946" cy="416" r="21"/>
    <circle cx="980" cy="424" r="21"/>
    <ellipse cx="1080" cy="155" rx="38" ry="31"/>
    <circle cx="1036" cy="114" r="15"/>
    <circle cx="1056" cy="98"  r="15"/>
    <circle cx="1080" cy="94"  r="15"/>
    <circle cx="1104" cy="102" r="15"/>
  </g>
  <!-- dog silhouette (right) -->
  <g fill="rgba(255,255,255,0.055)" transform="translate(680,140)">
    <ellipse cx="220" cy="290" rx="168" ry="128"/>
    <circle cx="98" cy="186" r="84"/>
    <ellipse cx="56" cy="216" rx="38" ry="30"/>
    <ellipse cx="62" cy="122" rx="32" ry="54" transform="rotate(-20,62,122)"/>
    <ellipse cx="142" cy="116" rx="32" ry="54" transform="rotate(12,142,116)"/>
    <path d="M388 272 Q448 210 428 146" stroke="rgba(255,255,255,0.055)" stroke-width="32" fill="none" stroke-linecap="round"/>
    <rect x="118" y="388" width="46" height="94" rx="22"/>
    <rect x="182" y="388" width="46" height="94" rx="22"/>
    <rect x="268" y="388" width="46" height="94" rx="22"/>
    <rect x="326" y="388" width="46" height="94" rx="22"/>
  </g>
  <!-- cat silhouette (left) -->
  <g fill="rgba(255,255,255,0.045)" transform="translate(40,190)">
    <ellipse cx="108" cy="208" rx="86" ry="108"/>
    <circle cx="108" cy="92" r="58"/>
    <polygon points="70,56 80,10 106,48"/>
    <polygon points="110,48 136,10 146,58"/>
    <path d="M194 296 Q238 232 214 162" stroke="rgba(255,255,255,0.045)" stroke-width="22" fill="none" stroke-linecap="round"/>
  </g>
  <!-- bokeh -->
  <g fill="rgba(255,255,255,0.05)">
    <circle cx="310" cy="100" r="82"/>
    <circle cx="820" cy="610" r="102"/>
    <circle cx="1120" cy="360" r="62"/>
    <circle cx="90"  cy="560" r="72"/>
  </g>
</svg>'''


def about():
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="700" viewBox="0 0 800 700">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#031209"/>
      <stop offset="100%" style="stop-color:#0d6e3f"/>
    </linearGradient>
  </defs>
  <rect width="800" height="700" fill="url(#bg)"/>
  <!-- shelf lines -->
  <g stroke="rgba(255,255,255,0.10)" stroke-width="2.5" fill="none">
    <line x1="70" y1="200" x2="730" y2="200"/>
    <line x1="70" y1="330" x2="730" y2="330"/>
    <line x1="70" y1="460" x2="730" y2="460"/>
    <line x1="245" y1="178" x2="245" y2="480"/>
    <line x1="420" y1="178" x2="420" y2="480"/>
    <line x1="595" y1="178" x2="595" y2="480"/>
    <line x1="70"  y1="570" x2="730" y2="570"/>
  </g>
  <!-- product silhouettes on shelves -->
  <g fill="rgba(255,255,255,0.09)" stroke="rgba(255,255,255,0.16)" stroke-width="1">
    <rect x="88"  y="144" width="72" height="56" rx="5"/>
    <rect x="172" y="148" width="58" height="52" rx="5"/>
    <rect x="264" y="142" width="82" height="58" rx="5"/>
    <rect x="358" y="147" width="52" height="53" rx="5"/>
    <rect x="438" y="144" width="72" height="56" rx="5"/>
    <rect x="522" y="148" width="62" height="52" rx="5"/>
    <rect x="614" y="142" width="78" height="58" rx="5"/>
    <rect x="84"  y="274" width="66" height="56" rx="5"/>
    <rect x="162" y="278" width="72" height="52" rx="5"/>
    <rect x="260" y="270" width="78" height="60" rx="5"/>
    <rect x="352" y="275" width="56" height="55" rx="5"/>
    <rect x="432" y="272" width="82" height="58" rx="5"/>
    <rect x="526" y="278" width="52" height="52" rx="5"/>
    <rect x="608" y="270" width="72" height="60" rx="5"/>
  </g>
  <!-- paw logo centre -->
  <g fill="rgba(255,255,255,0.12)" transform="translate(282,470)">
    <ellipse cx="118" cy="96" rx="72" ry="58"/>
    <circle cx="32"  cy="40" r="27"/>
    <circle cx="72"  cy="14" r="27"/>
    <circle cx="118" cy="8"  r="27"/>
    <circle cx="163" cy="14" r="27"/>
    <circle cx="200" cy="42" r="27"/>
  </g>
  <text x="400" y="624" text-anchor="middle" font-size="22" font-weight="700" font-family="Poppins,Arial,sans-serif" fill="rgba(255,255,255,0.68)">Patitas Pet Shop</text>
  <text x="400" y="652" text-anchor="middle" font-size="15" font-weight="400" font-family="Poppins,Arial,sans-serif" fill="rgba(255,255,255,0.40)">+8 años de experiencia</text>
</svg>'''


def cta():
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="600" viewBox="0 0 1200 600">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#020d06"/>
      <stop offset="100%" style="stop-color:#052412"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="600" fill="url(#bg)"/>
  <!-- subtle paw pattern -->
  <g fill="rgba(255,255,255,0.03)">
    <ellipse cx="200" cy="300" rx="62" ry="50"/>
    <circle cx="138" cy="238" r="23"/>
    <circle cx="163" cy="218" r="23"/>
    <circle cx="196" cy="212" r="23"/>
    <circle cx="230" cy="220" r="23"/>
    <circle cx="254" cy="244" r="23"/>
    <ellipse cx="900" cy="400" rx="56" ry="45"/>
    <circle cx="842" cy="344" r="21"/>
    <circle cx="864" cy="326" r="21"/>
    <circle cx="896" cy="320" r="21"/>
    <circle cx="927" cy="328" r="21"/>
    <circle cx="950" cy="352" r="21"/>
  </g>
  <circle cx="600" cy="300" r="200" fill="rgba(37,211,102,0.04)"/>
  <circle cx="600" cy="300" r="320" fill="rgba(37,211,102,0.02)"/>
</svg>'''


print("Generating improved SVG illustrations…")

# Food bags
write_svg('prod-royal-canin',   food_bag('#6B3A08', '#B8860B', 'ROYAL CANIN', 'Adulto · Todas las razas', 'rgba(160,108,0,0.90)'))
write_svg('prod-pro-plan',      food_bag('#0d2e4a', '#1a6896', 'PRO PLAN',    'Adulto · Performance',     'rgba(22,92,138,0.90)'))
write_svg('prod-excellent',     food_bag('#0d3a1a', '#1a8a3a', 'EXCELLENT',   'Adulto · Balanceado',      'rgba(20,120,50,0.90)'))
write_svg('cat-alimento-perros',food_bag('#6B3A08', '#B8860B', 'ALIMENTOS',   'para Perros',              'rgba(160,108,0,0.90)'))
write_svg('cat-alimento-gatos', food_bag('#4a0a6a', '#8e44ad', 'ALIMENTOS',   'para Gatos',               'rgba(130,50,170,0.90)'))
write_svg('promo-cachorro',     food_bag('#5a1a0a', '#c0390a', 'ROYAL CANIN', 'Cachorro · 10 kg',         'rgba(180,45,10,0.90)'))

# Accessories
write_svg('prod-piedras',       piedras())
write_svg('prod-rascador',      rascador())
write_svg('prod-cama',          cama())
write_svg('cat-juguetes',       juguetes())
write_svg('cat-camas',          cama())
write_svg('cat-correas',        correas())
write_svg('cat-higiene',        higiene())
write_svg('promo-higiene-gatos',higiene())
write_svg('promo-juguetes',     juguetes())

# Backgrounds
write_svg('hero',               hero())
write_svg('about',              about())
write_svg('cta',                cta())

print(f"\nDone — all SVGs updated.")
