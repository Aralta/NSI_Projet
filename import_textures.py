import pygame

zz = 0
aa= 1
ab = 2
ac = 3
ad = 4
ae = 5
af = 6
ag = 7
ah = 8
ai = 9
aj = 10
ak = 11
al = 12
am = 13
an = 14
ao = 15
ap = 16
aq = 17
ar = 18
aS = 19
at = 20
au = 21
av = 22
aw = 23
ax = 24
ay = 25
az = 26
ba = 27
bb = 28
bc = 29
bd = 30
be = 31
bf = 32
bg = 33
bh = 34
bi = 35
bj = 36
bk = 37
bl = 38
bm = 39
bn = 40
bo = 41
bp = 42
bq = 43
br = 44
bs = 45
bt = 46
bu = 47
bv = 48
bw = 49
bx = 50
by = 51
bz = 52
ca = 53
cb = 54
cc = 55
cd = 56
ce = 57
cf = 58
cg = 59
ch = 60
ci = 61
cj = 62
ck = 63
cl = 64
cm = 65
cn = 66
co = 67

TEXTURES ={ 
    zz: pygame.image.load("./Textures/herbe.png"), 

#texture pour lac (eau)
    bg: pygame.image.load("./Textures/lac/eau.png"),   
    bi: pygame.image.load("./Textures/lac/eau_sup_gauche.png"),
    bj: pygame.image.load("./Textures/lac/eau_cote_sup.png"),
    bk: pygame.image.load("./Textures/lac/eau_sup_droit.png"),
    bh: pygame.image.load("./Textures/lac/eau_cote_droit.png"),
    be: pygame.image.load("./Textures/lac/eau_inf_droit.png"),
    bd: pygame.image.load("./Textures/lac/eau_cote_inf.png"),
    bc: pygame.image.load("./Textures/lac/eau_inf_gauche.png"),
    bf: pygame.image.load("./Textures/lac/eau_cote_gauche.png"),    

#texture maison
    aa: pygame.image.load("./Textures/maison/aa.png"),
    ab: pygame.image.load("./Textures/maison/ab.png"),
    ac: pygame.image.load("./Textures/maison/ac.png"),
    ad: pygame.image.load("./Textures/maison/ad.png"),
    ae: pygame.image.load("./Textures/maison/ae.png"),
    af: pygame.image.load("./Textures/maison/af.png"),
    ag: pygame.image.load("./Textures/maison/ag.png"),
    ah: pygame.image.load("./Textures/maison/ah.png"),
    ai: pygame.image.load("./Textures/maison/ai.png"),
    aj: pygame.image.load("./Textures/maison/aj.png"),
    ak: pygame.image.load("./Textures/maison/ak.png"),
    al: pygame.image.load("./Textures/maison/al.png"),
    am: pygame.image.load("./Textures/maison/am.png"),
    an: pygame.image.load("./Textures/maison/an.png"),
    ao: pygame.image.load("./Textures/maison/ao.png"),
    ap: pygame.image.load("./Textures/maison/ap.png"),
    aq: pygame.image.load("./Textures/maison/aq.png"),
    ar: pygame.image.load("./Textures/maison/ar.png"),
    aS: pygame.image.load("./Textures/maison/as.png"),
    at: pygame.image.load("./Textures/maison/at.png"),
    au: pygame.image.load("./Textures/maison/au.png"),
    av: pygame.image.load("./Textures/maison/av.png"),
    aw: pygame.image.load("./Textures/maison/aw.png"),
    ax: pygame.image.load("./Textures/maison/ax.png"),
    ay: pygame.image.load("./Textures/maison/ay.png"),
    az: pygame.image.load("./Textures/maison/az.png"),
    ba: pygame.image.load("./Textures/maison/ba.png"),
    bb: pygame.image.load("./Textures/maison/bb.png"),




#chemin
    bl: pygame.image.load("./Textures/chemin/bl.png"),
    bm: pygame.image.load("./Textures/chemin/bm.png"),
    bn: pygame.image.load("./Textures/chemin/bn.png"),
    bo: pygame.image.load("./Textures/chemin/bo.png"),
    bp: pygame.image.load("./Textures/chemin/bp.png"),
    bq: pygame.image.load("./Textures/chemin/bq.png"),
    br: pygame.image.load("./Textures/chemin/br.png"),
    bs: pygame.image.load("./Textures/chemin/bs.png"),
    bt: pygame.image.load("./Textures/chemin/bt.png"),
   # bu: pygame.image.load("./Textures/chemin/bu.png"),
  #  bv: pygame.image.load("./Textures/chemin/bv.png"),
 #   bw: pygame.image.load("./Textures/chemin/bw.png"),
  #  bx: pygame.image.load("./Textures/chemin/bx.png"),

#texture toit maison 2
 #   by: pygame.image.load("./Textures/toit-maison2/by.png"),
  #  bz: pygame.image.load("./Textures/toit-maison2/bz.png"),
   # ca: pygame.image.load("./Textures/toit-maison2/ca.png"),
    #cb: pygame.image.load("./Textures/toit-maison2/cb.png"),
   # cc: pygame.image.load("./Textures/toit-maison2/cc.png"),
   # cd: pygame.image.load("./Textures/toit-maison2/cd.png"),
   # ce: pygame.image.load("./Textures/toit-maison2/ce.png"),
   # cf: pygame.image.load("./Textures/toit-maison2/cf.png"),
    #cg: pygame.image.load("./Textures/toit-maison2/cg.png"),
   # ch: pygame.image.load("./Textures/toit-maison2/ch.png"),
   # ci: pygame.image.load("./Textures/toit-maison2/ci.png"),
   # cj: pygame.image.load("./Textures/toit-maison2/cj.png"),
    #ck: pygame.image.load("./Textures/toit-maison2/ck.png"),
    #cl: pygame.image.load("./Textures/toit-maison2/cl.png"),
    #cm: pygame.image.load("./Textures/toit-maison2/cm.png"),
    #cn: pygame.image.load("./Textures/toit-maison2/cn.png"),
    #co: pygame.image.load("./Textures/toit-maison2/co.png"),
    #ar: pygame.image.load("./Textures/toit-maison2/ar.png"),
    #aS: pygame.image.load("./Textures/toit-maison2/as.png"),
    #at: pygame.image.load("./Textures/toit-maison2/at.png"),
    #au: pygame.image.load("./Textures/toit-maison2/au.png"),
    #av: pygame.image.load("./Textures/toit-maison2/av.png"),
    #aw: pygame.image.load("./Textures/toit-maison2/aw.png"),
    #ax: pygame.image.load("./Textures/toit-maison2/ax.png"),
    #ay: pygame.image.load("./Textures/toit-maison2/ay.png"),
    #az: pygame.image.load("./Textures/toit-maison2/az.png"),
    #ba: pygame.image.load("./Textures/toit-maison2/ba.png"),
    #bb: pygame.image.load("./Textures/toit-maison2/bb.png"),







#    i: pygame.image.load("./Textures/chemin/   .png"),
#    j: pygame.image.load("./Textures/chemin/   .png"),
#    k: pygame.image.load
#    l: pygame.image.load
#    m: pygame.image.load



    

}