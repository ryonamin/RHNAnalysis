# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 9.0 for Linux x86 (64-bit) (November 20, 2012)
# Date: Thu 27 Dec 2018 15:48:58



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
g1p = Parameter(name = 'g1p',
                nature = 'external',
                type = 'real',
                value = 0.2,
                texname = '\\text{g1p}',
                lhablock = 'BLINPUTS',
                lhacode = [ 1 ])

a1 = Parameter(name = 'a1',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{a1}',
               lhablock = 'BLINPUTS',
               lhacode = [ 2 ])

b1 = Parameter(name = 'b1',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{b1}',
               lhablock = 'BLINPUTS',
               lhacode = [ 3 ])

Sa = Parameter(name = 'Sa',
               nature = 'external',
               type = 'real',
               value = 0.01,
               texname = '\\text{Sa}',
               lhablock = 'BLINPUTS',
               lhacode = [ 4 ])

cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

VNl1x1 = Parameter(name = 'VNl1x1',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{VNl1x1}',
                   lhablock = 'NUMIXING',
                   lhacode = [ 1, 1 ])

VNl1x2 = Parameter(name = 'VNl1x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{VNl1x2}',
                   lhablock = 'NUMIXING',
                   lhacode = [ 1, 2 ])

VNl1x3 = Parameter(name = 'VNl1x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{VNl1x3}',
                   lhablock = 'NUMIXING',
                   lhacode = [ 1, 3 ])

VNl2x1 = Parameter(name = 'VNl2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{VNl2x1}',
                   lhablock = 'NUMIXING',
                   lhacode = [ 2, 1 ])

VNl2x2 = Parameter(name = 'VNl2x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{VNl2x2}',
                   lhablock = 'NUMIXING',
                   lhacode = [ 2, 2 ])

VNl2x3 = Parameter(name = 'VNl2x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{VNl2x3}',
                   lhablock = 'NUMIXING',
                   lhacode = [ 2, 3 ])

VNl3x1 = Parameter(name = 'VNl3x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{VNl3x1}',
                   lhablock = 'NUMIXING',
                   lhacode = [ 3, 1 ])

VNl3x2 = Parameter(name = 'VNl3x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{VNl3x2}',
                   lhablock = 'NUMIXING',
                   lhacode = [ 3, 2 ])

VNl3x3 = Parameter(name = 'VNl3x3',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{VNl3x3}',
                   lhablock = 'NUMIXING',
                   lhacode = [ 3, 3 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 80.379,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])

MZp = Parameter(name = 'MZp',
                nature = 'external',
                type = 'real',
                value = 3000,
                texname = '\\text{MZp}',
                lhablock = 'MASS',
                lhacode = [ 9900032 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MN1 = Parameter(name = 'MN1',
                nature = 'external',
                type = 'real',
                value = 100,
                texname = '\\text{MN1}',
                lhablock = 'MASS',
                lhacode = [ 9910012 ])

MN2 = Parameter(name = 'MN2',
                nature = 'external',
                type = 'real',
                value = 200,
                texname = '\\text{MN2}',
                lhablock = 'MASS',
                lhacode = [ 9910014 ])

MN3 = Parameter(name = 'MN3',
                nature = 'external',
                type = 'real',
                value = 300,
                texname = '\\text{MN3}',
                lhablock = 'MASS',
                lhacode = [ 9910016 ])

MH1 = Parameter(name = 'MH1',
                nature = 'external',
                type = 'real',
                value = 125.18,
                texname = '\\text{MH1}',
                lhablock = 'MASS',
                lhacode = [ 25 ])

MH2 = Parameter(name = 'MH2',
                nature = 'external',
                type = 'real',
                value = 450,
                texname = '\\text{MH2}',
                lhablock = 'MASS',
                lhacode = [ 9900035 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WZp = Parameter(name = 'WZp',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{WZp}',
                lhablock = 'DECAY',
                lhacode = [ 9900032 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WN1 = Parameter(name = 'WN1',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WN1}',
                lhablock = 'DECAY',
                lhacode = [ 9910012 ])

WN2 = Parameter(name = 'WN2',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WN2}',
                lhablock = 'DECAY',
                lhacode = [ 9910014 ])

WN3 = Parameter(name = 'WN3',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WN3}',
                lhablock = 'DECAY',
                lhacode = [ 9910016 ])

WH1 = Parameter(name = 'WH1',
                nature = 'external',
                type = 'real',
                value = 1.5,
                texname = '\\text{WH1}',
                lhablock = 'DECAY',
                lhacode = [ 25 ])

WH2 = Parameter(name = 'WH2',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{WH2}',
                lhablock = 'DECAY',
                lhacode = [ 9900035 ])

gt = Parameter(name = 'gt',
               nature = 'internal',
               type = 'real',
               value = 'a1*g1p',
               texname = '\\text{gt}')

Ca = Parameter(name = 'Ca',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - Sa**2)',
               texname = '\\text{Ca}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '0.231',
                texname = '\\text{sw2}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

Sp2num = Parameter(name = 'Sp2num',
                   nature = 'internal',
                   type = 'real',
                   value = '2*gt*cmath.sqrt(ee**2/cw**2 + ee**2/sw**2)',
                   texname = '\\text{Sp2num}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam1 = Parameter(name = 'lam1',
                 nature = 'internal',
                 type = 'real',
                 value = '(Ca**2*MH1**2)/(2.*vev**2) + (MH2**2*Sa**2)/(2.*vev**2)',
                 texname = '\\text{lam1}')

x = Parameter(name = 'x',
              nature = 'internal',
              type = 'real',
              value = '(MZp*cmath.sqrt(1 - (gt**2*vev**2)/(4*MZp**2 - (g1**2 + gw**2)*vev**2)))/(2.*b1*g1p)',
              texname = 'x')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

C2gNum = Parameter(name = 'C2gNum',
                   nature = 'internal',
                   type = 'real',
                   value = 'ee**2/cw**2 + gt**2 + ee**2/sw**2 - (16*b1**2*g1p**2*x**2)/vev**2',
                   texname = '\\text{C2gNum}')

Cn = Parameter(name = 'Cn',
               nature = 'internal',
               type = 'real',
               value = 'ee**2/cw**2 + gt**2 + ee**2/sw**2 + (16*b1**2*g1p**2*x**2)/vev**2',
               texname = '\\text{Cn}')

Cp2num = Parameter(name = 'Cp2num',
                   nature = 'internal',
                   type = 'real',
                   value = '-(ee**2/cw**2) + gt**2 - ee**2/sw**2 + (16*b1**2*g1p**2*x**2)/vev**2',
                   texname = '\\text{Cp2num}')

Dn = Parameter(name = 'Dn',
               nature = 'internal',
               type = 'real',
               value = '64*b1**2*g1p**2*(ee**2/cw**2 + ee**2/sw**2)*vev**2*x**2',
               texname = '\\text{Dn}')

S2gNum = Parameter(name = 'S2gNum',
                   nature = 'internal',
                   type = 'real',
                   value = '(8*b1*g1p*gt*x)/vev',
                   texname = '\\text{S2gNum}')

lam2 = Parameter(name = 'lam2',
                 nature = 'internal',
                 type = 'real',
                 value = '(Ca**2*MH2**2)/(2.*x**2) + (MH1**2*Sa**2)/(2.*x**2)',
                 texname = '\\text{lam2}')

lam3 = Parameter(name = 'lam3',
                 nature = 'internal',
                 type = 'real',
                 value = '(Ca*(-MH1**2 + MH2**2)*Sa)/(vev*x)',
                 texname = '\\text{lam3}')

mu2H1 = Parameter(name = 'mu2H1',
                  nature = 'internal',
                  type = 'real',
                  value = 'lam1*vev**2 + (lam3*x**2)/2.',
                  texname = 'm^2')

mu2H2 = Parameter(name = 'mu2H2',
                  nature = 'internal',
                  type = 'real',
                  value = '(lam3*vev**2)/2. + lam2*x**2',
                  texname = '\\mu ^2')

sg = Parameter(name = 'sg',
               nature = 'internal',
               type = 'real',
               value = '-cmath.sin(cmath.asin(S2gNum/cmath.sqrt(C2gNum**2 + S2gNum**2))/2.)',
               texname = '\\text{sg}')

Sp = Parameter(name = 'Sp',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sin(cmath.asin(Sp2num/cmath.sqrt(Cp2num**2 + Sp2num**2))/2.)',
               texname = '\\text{Sp}')

cg = Parameter(name = 'cg',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sg**2)',
               texname = '\\text{cg}')

Cp = Parameter(name = 'Cp',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - Sp**2)',
               texname = '\\text{Cp}')

