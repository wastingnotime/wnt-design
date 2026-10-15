#!/usr/bin/env python3
"""Render the committed WNT identity masters; no font installation required."""
from pathlib import Path
import hashlib
import json
import subprocess
import xml.etree.ElementTree as ET
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / 'assets/identity/v1.0.0'
OUT = KIT / 'exports'
PROOF = ROOT / 'docs/identity'
GREEN, INK, PAPER = '#9cffaa', '#101813', '#fff8f3'
NS = '{http://www.w3.org/2000/svg}'

def master(name):
    root = ET.parse(KIT / 'masters' / f'{name}.svg').getroot()
    w = float(root.attrib['viewBox'].split()[2])
    body = ''.join(ET.tostring(e, encoding='unicode') for e in root if e.tag != NS+'title')
    return body, w

MARK, _ = master('mark')
WORD, WORD_W = master('wordmark')
INITIALS, INITIALS_W = master('initials')

def mark(x, y, width, color):
    return f'<g fill="{color}" transform="translate({x} {y}) scale({width/128})">{MARK}</g>'

def word(x, y, width, color, initials=False):
    body, natural = (INITIALS, INITIALS_W) if initials else (WORD, WORD_W)
    return f'<g fill="{color}" transform="translate({x} {y}) scale({width/natural})">{body}</g>'

def rect(x,y,w,h,color):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>'

def label(x,y,text,size=20,color=INK):
    return f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="{size}" fill="{color}">{text}</text>'

def svg(w,h,body,title='Wasting No Time — Forward W, identity v1.0.0'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><title>{title}</title>{body}</svg>\n'

def render(source, destination, size=None):
    cmd = ['rsvg-convert', '-o', str(destination)]
    if size:
        cmd += ['-w',str(size),'-h',str(size)]
    subprocess.run(cmd+[str(source)], check=True)

def save(name,w,h,body,png=False):
    path=OUT/f'{name}.svg'
    path.write_text(svg(w,h,body))
    if png:
        render(path,path.with_suffix('.png'))
    return path

def luminance(color):
    rgb=[int(color[i:i+2],16)/255 for i in (1,3,5)]
    rgb=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in rgb]
    return sum(v*c for v,c in zip(rgb,(.2126,.7152,.0722)))

def contrast(a,b):
    x,y=sorted([luminance(a),luminance(b)])
    return (y+.05)/(x+.05)

def main():
    OUT.mkdir(parents=True,exist_ok=True); PROOF.mkdir(parents=True,exist_ok=True)
    for name,color in [('green',GREEN),('dark',INK),('white','#ffffff'),('black','#000000')]:
        save('mark-'+name,128,96,mark(0,0,128,color))
    for name,bg,fg,accent in [('dark',INK,PAPER,GREEN),('light',PAPER,INK,INK),('mono-dark',None,INK,INK),('mono-white',None,'#ffffff','#ffffff')]:
        body=rect(0,0,640,128,bg) if bg else ''
        body+=mark(16,16,128,accent)+word(168,20,440,fg)
        save('lockup-'+name,640,128,body)
    avatar=save('avatar',800,800,rect(0,0,800,800,INK)+mark(120,190,560,GREEN),True)
    save('apple-touch-icon',180,180,rect(0,0,180,180,INK)+mark(27,42.75,126,GREEN),True)
    favicon=save('favicon',128,128,rect(0,0,128,128,INK)+mark(0,16,128,GREEN))
    for size in (16,32,48):
        render(favicon, OUT/f'favicon-{size}.png',size)
    # Pillow's ICO writer accepts explicit images, preserving native renders at each size.
    images=[Image.open(OUT/f'favicon-{s}.png').convert('RGBA') for s in (16,32,48)]
    images[-1].save(OUT/'favicon.ico',sizes=[(16,16),(32,32),(48,48)],append_images=images[:-1])
    save('social',1200,630,rect(0,0,1200,630,INK)+mark(120,180,340,GREEN)+word(510,255,590,PAPER),True)
    # All content fits within the conservative 1235×338 centered inner safe area.
    banner_body=rect(0,0,2560,1440,INK)+mark(765,615,280,GREEN)+word(1115,650,680,PAPER)
    save('youtube-banner',2560,1440,banner_body,True)
    save('video-watermark',150,150,mark(15,30,120,'#ffffff'),True)
    save('video-watermark-dark',150,150,mark(15,30,120,INK),True)
    save('thumbnail-signature',320,96,mark(8,12,96,'#ffffff')+word(132,5,160,'#ffffff',True))
    save('end-card',1920,1080,rect(0,0,1920,1080,INK)+mark(745,846,112,GREEN)+word(887,856,288,PAPER),True)
    # Review sheet is a local specimen, not a consumer UI implementation.
    body=rect(0,0,1400,1120,PAPER)+label(56,60,'WNT / Forward W',36)+label(56,96,'Selected direction B · identity v1.0.0',20)
    body+=rect(56,130,620,340,INK)+mark(180,155,380,GREEN)
    body+=mark(820,155,380,INK)
    body+=rect(56,500,1288,120,INK)+mark(76,512,128,GREEN)+word(240,520,440,PAPER)
    body+=label(56,680,'AVATARS · square / circular',18)
    body+=rect(56,704,104,104,INK)+mark(71.6,728.7,72.8,GREEN)
    body+='<defs><clipPath id="circle"><circle cx="232" cy="756" r="52"/></clipPath></defs>'
    body+='<g clip-path="url(#circle)">'+rect(180,704,104,104,INK)+mark(195.6,728.7,72.8,GREEN)+'</g>'
    body+=label(344,680,'FAVICONS · 16 / 32 / 48 px',16)
    for x,s in [(344,16),(390,32),(452,48)]:
        data=__import__('base64').b64encode((OUT/f'favicon-{s}.png').read_bytes()).decode()
        body+=f'<image x="{x}" y="720" width="{s}" height="{s}" href="data:image/png;base64,{data}"/>'
    body+=label(680,680,'MARK · white / dark monochrome',16)
    body+=rect(680,704,160,104,INK)+mark(696,708,128,'#ffffff')+mark(880,708,128,INK)
    body+=label(56,876,'PRODUCT ENDORSEMENT · specimen only',18)
    body+=label(56,935,'Sliding Tasks',38,'#b63820')+label(56,970,'Product identity leads.',18,'#645f5a')
    body+=mark(56,1000,24,'#645f5a')+label(88,1017,'made by WNT',14,'#645f5a')
    body+=mark(300,1000,24,'#645f5a')+label(332,1017,'feito por WNT',14,'#645f5a')
    body+=label(870,935,'WNT channels',28)+label(870,970,'One mark. One asset version.',18)
    body+=label(56,1080,'Same geometry in every export · no gradients · no font dependencies in production SVGs',18)
    (PROOF/'v1.0.0-specimen.svg').write_text(svg(1400,1120,body,'WNT identity v1.0.0 — local specimen'))
    render(PROOF/'v1.0.0-specimen.svg',PROOF/'v1.0.0-specimen.png')
    # Crop proofs use vector clips, retaining the exact banner artwork.
    crops=[('TV',0,0,2560,1440),('Desktop center strip (illustrative)',0,508.75,2560,422.5),('Scaled minimum safe area',508.125,508.75,1543.75,422.5),('Conservative inner safe area',662.5,551,1235,338)]
    proof=label(40,45,'YouTube banner / crop proof',28)
    y=80
    for i,(name,x,cy,w,h) in enumerate(crops):
        scale=1200/w
        proof+=label(40,y+22,name,18)
        proof+=f'<svg x="40" y="{y+40}" width="1200" height="{h*scale}" viewBox="{x} {cy} {w} {h}" overflow="hidden">{banner_body}</svg>'
        y+=h*scale+90
    (PROOF/'v1.0.0-banner-crops.svg').write_text(svg(1280,int(y),rect(0,0,1280,int(y),PAPER)+proof,'WNT banner crop construction proof'))
    render(PROOF/'v1.0.0-banner-crops.svg',PROOF/'v1.0.0-banner-crops.png')
    pairs=[(GREEN,INK),(INK,PAPER),('#ffffff',INK),('#645f5a',PAPER),(GREEN,PAPER)]
    manifest={
        'version':'1.0.0','mark':'forward-w','selected_direction':'B',
        'selection_date':'2026-10-15','parent_url':'https://wastingnotime.org/',
        'geometry_source':'masters/mark.svg','wordmark_source':'masters/wordmark.svg',
        'colors':{'green':GREEN,'ink':INK,'paper':PAPER},
        'contrast':[{'foreground':a,'background':b,'ratio':round(contrast(a,b),4)} for a,b in pairs],
        'tools':{'renderer':subprocess.check_output(['rsvg-convert','--version'],text=True).strip(),'pillow':Image.__version__},
        'files':[]}
    for p in sorted(KIT.rglob('*')):
        if p.is_file() and p.name!='manifest.json':
            item={'path':str(p.relative_to(KIT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
            if p.suffix in ('.png','.ico'):
                with Image.open(p) as im: item['pixels']=list(im.size)
            manifest['files'].append(item)
    (KIT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'exported':len(manifest['files']),'contrast':manifest['contrast']},indent=2))

if __name__=='__main__':
    main()
