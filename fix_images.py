#!/usr/bin/env python3
"""
Generate local SVG images for Patitas Pet Shop and update index.html.
SVG is pure text/XML — no image libraries required.
"""
import os
import re

# 1. Create assets/images directory
os.makedirs('/home/user/Pet-Shop/assets/images', exist_ok=True)


def make_svg(filename, bg1, bg2, emoji, label, sublabel='', w=800, h=600):
    mid_y   = int(h * 0.44)
    lbl_y   = int(h * 0.725)
    sub_y   = int(h * 0.835)
    fs_em   = int(min(w, h) * 0.22)
    fs_lbl  = int(min(w, h) * 0.065)
    fs_sub  = int(min(w, h) * 0.043)

    sub_tag = ''
    if sublabel:
        sub_tag = (f'\n  <text x="{w//2}" y="{sub_y}" text-anchor="middle"'
                   f' font-size="{fs_sub}" font-weight="400"'
                   f' font-family="Poppins,Arial,sans-serif"'
                   f' fill="rgba(255,255,255,0.82)">{sublabel}</text>')

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">\n'
        f'  <defs>\n'
        f'    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">\n'
        f'      <stop offset="0%"   style="stop-color:{bg1};stop-opacity:1"/>\n'
        f'      <stop offset="100%" style="stop-color:{bg2};stop-opacity:1"/>\n'
        f'    </linearGradient>\n'
        f'    <radialGradient id="glow" cx="50%" cy="45%" r="55%">\n'
        f'      <stop offset="0%"   style="stop-color:rgba(255,255,255,0.15);stop-opacity:1"/>\n'
        f'      <stop offset="100%" style="stop-color:rgba(255,255,255,0);stop-opacity:1"/>\n'
        f'    </radialGradient>\n'
        f'  </defs>\n'
        f'  <rect width="{w}" height="{h}" fill="url(#bg)"/>\n'
        f'  <!-- Decorative circles -->\n'
        f'  <circle cx="{int(w*0.12)}" cy="{int(h*0.15)}" r="{int(min(w,h)*0.08)}" fill="rgba(255,255,255,0.08)"/>\n'
        f'  <circle cx="{int(w*0.88)}" cy="{int(h*0.85)}" r="{int(min(w,h)*0.12)}" fill="rgba(255,255,255,0.08)"/>\n'
        f'  <circle cx="{int(w*0.85)}" cy="{int(h*0.12)}" r="{int(min(w,h)*0.06)}" fill="rgba(255,255,255,0.06)"/>\n'
        f'  <circle cx="{int(w*0.15)}" cy="{int(h*0.85)}" r="{int(min(w,h)*0.09)}" fill="rgba(255,255,255,0.06)"/>\n'
        f'  <circle cx="{w//2}" cy="{h//2}" r="{int(min(w,h)*0.25)}" fill="rgba(255,255,255,0.05)"/>\n'
        f'  <!-- Glow -->\n'
        f'  <ellipse cx="{w//2}" cy="{h//2}" rx="{w//2}" ry="{h//2}" fill="url(#glow)"/>\n'
        f'  <!-- Emoji -->\n'
        f'  <text x="{w//2}" y="{mid_y}" text-anchor="middle" dominant-baseline="middle"'
        f' font-size="{fs_em}" font-family="Apple Color Emoji,Segoe UI Emoji,Noto Color Emoji,sans-serif">{emoji}</text>\n'
        f'  <!-- Label -->\n'
        f'  <text x="{w//2}" y="{lbl_y}" text-anchor="middle"'
        f' font-size="{fs_lbl}" font-weight="700"'
        f' font-family="Poppins,Arial,sans-serif" fill="white" opacity="0.95">{label}</text>{sub_tag}\n'
        f'</svg>'
    )

    path = f'/home/user/Pet-Shop/assets/images/{filename}.svg'
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(svg)
    return path


# ── Image definitions ────────────────────────────────────────────────────────
images = [
    # (filename,  bg1,       bg2,       emoji, label,                  sublabel)
    ('hero',               '#0a5c35', '#25D366', '\U0001f43e', 'Patitas Pet Shop',        'Tu mascota, nuestra pasión'),
    ('prod-royal-canin',   '#8B5E0A', '#D4A017', '\U0001f415', 'Royal Canin Adulto',      'Alimento Premium 15 kg'),
    ('prod-pro-plan',      '#1a4a6e', '#2980b9', '\U0001f415', 'Pro Plan Adulto',         'Alimento Premium 15 kg'),
    ('prod-excellent',     '#1d6b3b', '#2ecc71', '\U0001f415', 'Excellent Adulto',        'Alimento Balanceado 15 kg'),
    ('prod-piedras',       '#5b2680', '#9b59b6', '\U0001f431', 'Piedras Sanitarias',      'Premium 4 kg'),
    ('prod-rascador',      '#8B3A0A', '#e67e22', '\U0001f408', 'Rascador para Gatos',     'Torre Sisal 120 cm'),
    ('prod-cama',          '#1a3a5c', '#2471a3', '\U0001f415', 'Cama Premium Perros',     'Tallas M · L · XL'),
    ('cat-alimento-perros','#7a4a0a', '#D4A017', '\U0001f436', 'Alimentos para Perros',   'Todas las marcas y razas'),
    ('cat-alimento-gatos', '#5b1a7a', '#9b59b6', '\U0001f431', 'Alimentos para Gatos',   'Nutrición completa'),
    ('cat-juguetes',       '#1a6e35', '#2ecc71', '\U0001f3be', 'Juguetes',                'Diversión garantizada'),
    ('cat-camas',          '#1a2a5c', '#2980b9', '\U0001f6cf️', 'Camas y Descanso', 'Comodidad para tu mascota'),
    ('cat-correas',        '#5c2a0a', '#c0392b', '\U0001f9ae', 'Correas y Collares',      'Paseos seguros y felices'),
    ('cat-higiene',        '#0a5c4e', '#1abc9c', '\U0001f6c1', 'Higiene y Cuidado',       'Salud para tu mascota'),
    ('promo-cachorro',     '#6b1a1a', '#e74c3c', '\U0001f436', 'Royal Canin Cachorro',    'Oferta −20% · 10 kg'),
    ('promo-higiene-gatos','#0a4a3e', '#16a085', '\U0001f431', 'Kit Higiene Gatos',       'Super Oferta −30%'),
    ('promo-juguetes',     '#1a5c25', '#f39c12', '\U0001f3be', 'Pack Juguetes',           'Oferta −15% · Set x5'),
    ('gallery-1',          '#1a5c35', '#27ae60', '\U0001f415', 'Perro Feliz',             ''),
    ('gallery-2',          '#8B3A0A', '#d35400', '\U0001f415', 'Dos Perros Jugando',      ''),
    ('gallery-3',          '#5b1a7a', '#8e44ad', '\U0001f408', 'Gato Tierno',             ''),
    ('gallery-4',          '#1a2a5c', '#2471a3', '\U0001f415', 'Perros Corriendo',        ''),
    ('gallery-5',          '#1a5c3a', '#1e8449', '\U0001f415', 'Perro Jugando',           ''),
    ('gallery-6',          '#7a4a0a', '#e67e22', '\U0001f436', 'Cachorro Adorable',       ''),
    ('about',              '#0a3d1f', '#0d6e3f', '\U0001f43e', 'Patitas Pet Shop',        '+8 años de experiencia'),
    ('cta',                '#062413', '#0a5c35', '\U0001f43e', 'Consultános',        'por WhatsApp'),
]

print("Generating SVG files…")
for img in images:
    make_svg(*img)
    print(f"  ✓ {img[0]}.svg")

# ── Alt text → local path mapping ────────────────────────────────────────────
alt_to_src = {
    'Perro y gato felices':              'assets/images/hero.svg',
    'Royal Canin Adulto':                'assets/images/prod-royal-canin.svg',
    'Pro Plan Adulto':                   'assets/images/prod-pro-plan.svg',
    'Excellent Adulto':                  'assets/images/prod-excellent.svg',
    'Piedras Sanitarias Premium':        'assets/images/prod-piedras.svg',
    'Rascador para Gatos':               'assets/images/prod-rascador.svg',
    'Cama Premium para Perros':          'assets/images/prod-cama.svg',
    'Alimentos para Perros':             'assets/images/cat-alimento-perros.svg',
    'Alimentos para Gatos':              'assets/images/cat-alimento-gatos.svg',
    'Juguetes':                          'assets/images/cat-juguetes.svg',
    'Camas':                             'assets/images/cat-camas.svg',
    'Correas':                           'assets/images/cat-correas.svg',
    'Higiene':                           'assets/images/cat-higiene.svg',
    'Royal Canin Cachorro':              'assets/images/promo-cachorro.svg',
    'Kit Higiene Gatos':                 'assets/images/promo-higiene-gatos.svg',
    'Pack Juguetes':                     'assets/images/promo-juguetes.svg',
    'Perro feliz':                       'assets/images/gallery-1.svg',
    'Dos perros jugando':                'assets/images/gallery-2.svg',
    'Gato tierno':                       'assets/images/gallery-3.svg',
    'Perros corriendo':                  'assets/images/gallery-4.svg',
    'Perro jugando':                     'assets/images/gallery-5.svg',
    'Cachorro adorable':                 'assets/images/gallery-6.svg',
    'Mascota feliz con producto Patitas':'assets/images/about.svg',
    'Mascota feliz':                     'assets/images/cta.svg',
}

# ── Read and patch HTML ───────────────────────────────────────────────────────
html_path = '/home/user/Pet-Shop/index.html'
with open(html_path, 'r', encoding='utf-8') as fh:
    html = fh.read()

print("\nUpdating HTML image references…")
found = 0
for alt_text, new_src in alt_to_src.items():
    esc = re.escape(alt_text)

    # Case A: src appears BEFORE alt in the same <img> tag
    pat_a = re.compile(
        r'(<img\s[^>]*?)src="[^"]*"([^>]*?alt="' + esc + r'"[^>]*?>)',
        re.DOTALL
    )
    new_html, n = re.subn(pat_a, rf'\1src="{new_src}"\2', html)

    if n == 0:
        # Case B: alt appears BEFORE src
        pat_b = re.compile(
            r'(<img\s[^>]*?alt="' + esc + r'"[^>]*?)src="[^"]*"([^>]*?>)',
            re.DOTALL
        )
        new_html, n = re.subn(pat_b, rf'\1src="{new_src}"\2', html)

    if n > 0:
        html = new_html
        found += 1
        print(f"  ✓  {alt_text}")
    else:
        print(f"  ✗  NOT FOUND: {alt_text}")

with open(html_path, 'w', encoding='utf-8') as fh:
    fh.write(html)

print(f"\nDone — {found}/{len(alt_to_src)} images updated in index.html")
