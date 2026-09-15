from pathlib import Path
from PIL import Image
from io import BytesIO
import base64,html,json

import argparse
parser=argparse.ArgumentParser(description='Compose SVGs from archived outputs; no inference or augmentation.')
parser.add_argument('--source-dir',type=Path,required=True,help='Folder with polar-diagnostic.png, roi-detail.png, lens-input.png and chip-input.jpeg')
args=parser.parse_args()
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/images'
SRC=args.source_dir
LOC=args.source_dir
INK='#243a37';MUTED='#526a65';TEAL='#157c78';BLUE='#227bb2';RED='#ba4936';GOLD='#b76b16'

class SVG:
 def __init__(self,w,h,title):
  self.w,self.h=w,h;self.parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{html.escape(title)}</title><defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#f3f6f3"/><stop offset="1" stop-color="#e6efeb"/></linearGradient></defs><rect width="100%" height="100%" fill="url(#bg)"/><g font-family="Segoe UI, Arial, sans-serif" fill="{INK}">']
 def text(self,x,y,lines,size=28,color=INK,weight=400,anchor='start',lineheight=1.3):
  if isinstance(lines,str):lines=[lines]
  for n,line in enumerate(lines):self.parts.append(f'<text x="{x}" y="{y+n*size*lineheight}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{color}">{html.escape(line)}</text>')
 def rect(self,x,y,w,h,color=TEAL,dash=False,fill='none',radius=0,stroke=3):
  self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{color}" stroke-width="{stroke}"'+(' stroke-dasharray="10 7"' if dash else '')+'/>')
 def path(self,points,color=MUTED,width=2,dash=False):
  self.parts.append(f'<polyline points="'+ ' '.join(f'{x},{y}' for x,y in points)+f'" fill="none" stroke="{color}" stroke-width="{width}"'+(' stroke-dasharray="8 6"' if dash else '')+'/>')
 def arrow(self,x1,y1,x2,y2,color=MUTED):
  self.path([(x1,y1),(x2,y2)],color,2.5)
  import math
  a=math.atan2(y2-y1,x2-x1)
  self.path([(x2-12*math.cos(a-.45),y2-12*math.sin(a-.45)),(x2,y2),(x2-12*math.cos(a+.45),y2-12*math.sin(a+.45))],color,2.5)
 def image(self,im,x,y,w,h):
  b=BytesIO();im.save(b,format='PNG');s=base64.b64encode(b.getvalue()).decode()
  self.parts.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="none" href="data:image/png;base64,{s}"/>')
 def circle(self,x,y,r,color=RED,width=3):self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{color}" stroke-width="{width}"/>')
 def save(self,name):
  (OUT/name).write_text(''.join(self.parts)+'</g></svg>\n',encoding='utf-8')

polar=Image.open(SRC/'polar-diagnostic.png').convert('RGB')
detail=Image.open(SRC/'roi-detail.png').convert('RGB')
# Crop only axes/white margins from the archived, paired experimental panels.
# No intensity, color-map, fitted background, or response values are altered.
P=polar.crop((105,48,676,540));B=polar.crop((1452,48,2022,540));R=polar.crop((779,647,1348,1139))
local=[detail.crop((x,300,x+242,733)) for x in [124,881,1636]]
manifest={'polar':{'input':[105,48,676,540],'robust_background':[1452,48,2022,540],'robust_residual_score':[779,647,1348,1139]},'local':[[x,300,x+242,733] for x in [124,881,1636]],'note':'Paired source panels preserve their pixels and original colormaps. The local signed defect layer is alpha-weighted, not the unweighted residual.'}
(SRC/'panel-crops.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')

def polar_panel(s,im,x,y,w,h,title,mark=True):
 s.text(x,y-20,title,28,weight=600);s.image(im,x,y,w,h)
 if mark:
  # The same polar-domain scratch region is indicated in input/background/score.
  s.rect(x+w*.585,y+h*.445,w*.073,h*.265,GOLD,stroke=3)
  s.text(x+w*.685,y+h*.50,'A',30,GOLD,600)

s=SVG(1440,1180,'Spatial intrinsic-structure decomposition and cross-focus research direction')
s.text(40,54,'Polar–Fourier intrinsic structure',36,weight=600)
s.text(40,94,'Archived single-layer prototype outputs · real inspection images',24,MUTED)
s.text(40,149,'Polar unfolding → robust harmonic fit → reconstruction and local response',26,TEAL)
for x,im,title in [(40,P,'Polar input'),(520,B,'Reconstructed background'),(1000,R,'Robust residual score')]:polar_panel(s,im,x,215,400,344,title)
s.arrow(453,390,504,390);s.arrow(933,390,984,390)
s.text(40,596,'A marks the same polar location; normal structure is retained while localized responses remain.',23,MUTED)
s.text(40,652,'Image-space detail',30,weight=600)
for x,im,title in [(40,local[0],'Original image crop'),(520,local[1],'Robust background'),(1000,local[2],'Signed defect layer')]:
 s.text(x,695,title,27,weight=600);s.image(im,x+114,720,173,310)
s.text(40,1062,'Mechanism foundation → cross-focus feature analysis and joint perception',28,TEAL,600)
s.text(40,1105,'Compare response strength and shape against normal focus evolution; persistence alone is insufficient.',23,MUTED)
s.text(40,1148,'Cross-focus crops and measured trajectories are pending source material; no synthetic curve is shown.',22,MUTED)
s.save('polar-fourier-research.svg')

s=SVG(720,1700,'Polar–Fourier spatial decomposition, mobile overview')
s.text(28,50,['Polar–Fourier','intrinsic structure'],35,weight=600)
s.text(28,148,'Archived single-layer outputs',27,MUTED)
polar_panel(s,P,28,224,310,267,'Polar input')
polar_panel(s,B,382,224,310,267,'Reconstruction')
polar_panel(s,R,28,570,310,267,'Residual score')
s.text(382,606,['A: same polar','location.'],30,GOLD,600)
s.text(382,700,['Normal structure','is retained; local','responses remain.'],27,MUTED)
s.text(28,906,'Image-space detail',32,weight=600)
for x,im,title in [(28,local[0],['Original','crop']),(269,local[1],['Robust','background']),(510,local[2],['Signed','defect layer'])]:
 s.text(x,966,title,28,weight=600);s.image(im,x,1040,182,326)
s.text(28,1434,'Next: cross-focus joint perception',30,TEAL,600)
s.text(28,1488,['Response strength and shape relative to normal','focus evolution; persistence alone is insufficient.'],27,MUTED)
s.text(28,1605,['Measured focus crops and trajectories pending.','No synthetic curve is shown.'],26,MUTED)
s.save('polar-fourier-research-mobile.svg')

lens=Image.open(LOC/'lens-input.png').convert('RGB')
chip=Image.open(LOC/'chip-input.jpeg').convert('RGB').resize((900,752),Image.Resampling.LANCZOS)
# Replot the box coordinates visible in the archived image27 output.
# Full-image and crop coordinates remain coupled by this exact crop transform.
outer=(316,290,583,462);inner=(339,312,560,439)
crop=(290,265,610,485);aoi=chip.crop(crop)

def lens_view(s,x,y,size,final=False):
 s.image(lens,x,y,size,size)
 if final:
  cx,cy,r=x+405/768*size,y+418/768*size,214/768*size
  s.circle(cx,cy,r,RED,3);s.path([(cx-9,cy),(cx+9,cy)],RED,3);s.path([(cx,cy-9),(cx,cy+9)],RED,3)
 else:s.rect(x+size*.235,y+size*.23,size*.59,size*.61,TEAL,True,stroke=3)

def chip_view(s,x,y,w,h,show_inner=False,aoi_view=False,outer_dash=False):
 s.image(aoi if aoi_view else chip,x,y,w,h)
 srcw,srch=(320,220) if aoi_view else (900,752)
 ox,oy=(crop[0],crop[1]) if aoi_view else (0,0)
 for box,col,dashed in [(outer,BLUE,outer_dash)]+([(inner,RED,False)] if show_inner else []):
  l,t,r,b=box;s.rect(x+(l-ox)/srcw*w,y+(t-oy)/srch*h,(r-l)/srcw*w,(b-t)/srch*h,col,dashed,stroke=3)

s=SVG(1440,1220,'Florence-2 semantic grounding and geometry-constrained localization')
s.text(40,54,'Semantic grounding + geometric localization',36,weight=600)
s.text(40,96,'Archived inspection examples · explanatory overlays',24,MUTED)
s.text(40,159,'Lens · semantic candidate → boundary verification → center and circle',30,TEAL,600)
s.rect(40,207,282,184,TEAL,fill='#f2f7f5',radius=12,stroke=1)
s.text(60,239,['“the entire outer','circular camera lens','module, including','the outer ring”'],24,TEAL,500)
s.text(60,366,'Florence-2 prompt',22,TEAL)
lens_view(s,382,202,320)
s.path([(322,300),(430,300)],TEAL,2.5);s.arrow(430,300,457,277,TEAL)
s.text(382,557,'Candidate outline (schematic)',22,MUTED)
s.arrow(720,367,1050,367)
s.text(750,289,['Edges + radial structure','Circular consistency'],25,MUTED)
s.text(750,420,['Geometric refinement','follows semantic grounding'],23,MUTED)
lens_view(s,1070,202,320,True)
s.text(1070,557,'Recorded circle + center',22,MUTED)
s.path([(40,596),(1400,596)],'#c5d6cf',1)
s.text(40,654,'Chip · outer localization → AOI crop → inner refinement → map back',30,BLUE,600)
s.text(40,708,['“central black rectangular','image sensor window”'],25,BLUE,500)
chip_view(s,40,805,300,251)
s.arrow(180,753,180,900,BLUE)
s.text(40,1094,'1 · Outer ROI',25,BLUE,600)
s.arrow(356,923,392,923,BLUE)
s.text(410,708,['“most inner small flat black','rectangular sensor screen”'],24,RED,500)
chip_view(s,410,843,300,206,True,True)
s.arrow(550,752,550,885,RED)
s.text(410,1094,'2 · AOI + inner ROI',25,RED,600)
s.arrow(725,943,1050,943,RED)
s.text(755,835,['Containment + margins','Center / aspect ratio','Boundary & texture checks'],23,MUTED)
s.text(755,1002,['Restore original-image','coordinates'],23,RED)
chip_view(s,1070,805,300,251,True)
s.arrow(1050,943,1180,943,RED)
s.text(1070,1094,'3 · Mapped result',25,weight=600)
s.text(40,1165,'Blue: outer ROI · Red: final inner ROI / lens geometry · Prompt excerpts retain their recorded wording.',22,MUTED)
s.save('semantic-geometric-localization.svg')

s=SVG(720,2140,'Semantic grounding and two-stage localization, mobile overview')
s.text(28,50,['Semantic grounding +','geometric localization'],34,weight=600)
s.text(28,150,'Archived examples · explanatory overlays',25,MUTED)
s.text(28,219,'Lens',32,TEAL,600)
s.text(28,264,['“the entire outer circular camera lens module,','including the outer ring”'],27,TEAL)
lens_view(s,28,380,300);lens_view(s,390,380,300,True)
s.arrow(180,326,180,449,TEAL)
s.arrow(339,530,378,530)
s.text(28,725,['Candidate outline','(schematic)'],27,MUTED)
s.text(390,725,['Recorded circle','and center'],27,RED)
s.text(28,841,['Edges + radial / circular constraints','refine the semantic candidate.'],28,MUTED)
s.path([(28,932),(692,932)],'#c5d6cf',1)
s.text(28,997,'Chip · two-stage localization',32,BLUE,600)
s.text(28,1052,['“central black rectangular','image sensor window”'],28,BLUE)
chip_view(s,28,1167,310,259)
s.arrow(200,1114,200,1265,BLUE)
s.text(28,1475,'1 · Outer ROI',28,BLUE,600)
s.arrow(356,1295,386,1295,BLUE)
chip_view(s,397,1210,295,203,True,True)
s.text(397,1475,'2 · AOI + inner ROI',26,RED,600)
s.text(28,1550,['“most inner small flat black','rectangular sensor screen”'],28,RED)
s.path([(405,1585),(704,1585),(704,1327)],RED,2);s.arrow(704,1327,647,1327,RED)
s.text(28,1660,['Containment, margins, aspect ratio,','boundary and texture checks.'],28,MUTED)
chip_view(s,400,1750,292,244,True)
s.text(28,1790,['Map refined ROI','back to original','image coordinates.'],28,RED)
s.arrow(225,1910,382,1910,RED)
s.text(400,2040,'3 · Mapped result',28,weight=600)
s.text(28,2110,'Blue: outer ROI · Red: final inner ROI / circle',26,MUTED)
s.save('semantic-geometric-localization-mobile.svg')
print('Four source-based SVG panels built; no synthetic image content or curves.')
