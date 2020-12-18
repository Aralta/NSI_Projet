from import_textures import *

GRID1 = [
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,av,aw,ax,ay,az,ba,bb,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,ao,ap,aq,ar,aS,at,au,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,ah,ai,aj,ak,al,am,an,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,aa,ab,ac,ad,ae,af,ag,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,bo,bp,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,bl,bm,bn,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,bo],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,bl],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,bi,bj,bj,bj,bj,bj,bj,bj],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,bf,bg,bg,bg,bg,bg,bg,bg],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,bf,bg,bg,bg,bg,bg,bg,bg],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,bf,bg,bg,bg,bg,bg,bg,bg],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,bf,bg,bg,bg,bg,bg,bg,bg],
    [zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,zz,bc,bd,bd,bd,bd,bd,bd,bd],

]

TILESIZE = 40
MAPWIDTH = 40
MAPHEIGHT = 23
DISPLAYWEIDTH = TILESIZE*MAPWIDTH
DISPLAYHEIGHT = TILESIZE*MAPHEIGHT

COLLISION_AREA1 = pygame.Rect ((100,40),(280,160))
COLLISION_AREA2 = pygame.Rect ((1270,660),(320,240))


#de grille 1 à 2
PASSAGE1_AREA = pygame.Rect((1560,400),(40,80))