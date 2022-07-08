# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.1 for Mac OS X ARM (64-bit) (January 28, 2022)
# Date: Fri 8 Jul 2022 20:52:01



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 91.188,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

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

tb = Parameter(name = 'tb',
               nature = 'external',
               type = 'real',
               value = 5.,
               texname = 't_{\\beta }',
               lhablock = 'THDMBLOCK',
               lhacode = [ 1 ])

cba = Parameter(name = 'cba',
                nature = 'external',
                type = 'real',
                value = 0.01,
                texname = 'c_{\\beta -\\alpha }',
                lhablock = 'THDMBLOCK',
                lhacode = [ 2 ])

m122 = Parameter(name = 'm122',
                 nature = 'external',
                 type = 'real',
                 value = 90000.,
                 texname = '\\text{m}_{12}^2',
                 lhablock = 'THDMBLOCK',
                 lhacode = [ 3 ])

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

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MHL = Parameter(name = 'MHL',
                nature = 'external',
                type = 'real',
                value = 125,
                texname = '\\text{MHL}',
                lhablock = 'MASS',
                lhacode = [ 25 ])

MHH = Parameter(name = 'MHH',
                nature = 'external',
                type = 'real',
                value = 400,
                texname = '\\text{MHH}',
                lhablock = 'MASS',
                lhacode = [ 135 ])

MHA = Parameter(name = 'MHA',
                nature = 'external',
                type = 'real',
                value = 500,
                texname = '\\text{MHA}',
                lhablock = 'MASS',
                lhacode = [ 136 ])

MHp = Parameter(name = 'MHp',
                nature = 'external',
                type = 'real',
                value = 600,
                texname = '\\text{MHp}',
                lhablock = 'MASS',
                lhacode = [ 137 ])

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

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WHL = Parameter(name = 'WHL',
                nature = 'external',
                type = 'real',
                value = 0.00407,
                texname = '\\text{WHL}',
                lhablock = 'DECAY',
                lhacode = [ 25 ])

WHH = Parameter(name = 'WHH',
                nature = 'external',
                type = 'real',
                value = 0.0107,
                texname = '\\text{WHH}',
                lhablock = 'DECAY',
                lhacode = [ 135 ])

WHA = Parameter(name = 'WHA',
                nature = 'external',
                type = 'real',
                value = 0.0107,
                texname = '\\text{WHA}',
                lhablock = 'DECAY',
                lhacode = [ 136 ])

WHp = Parameter(name = 'WHp',
                nature = 'external',
                type = 'real',
                value = 0.0207,
                texname = '\\text{WHp}',
                lhablock = 'DECAY',
                lhacode = [ 137 ])

beta = Parameter(name = 'beta',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.atan(tb)',
                 texname = '\\beta')

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

sba = Parameter(name = 'sba',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(1 - cba**2)',
                texname = 's_{\\beta -\\alpha }')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

alpha = Parameter(name = 'alpha',
                  nature = 'internal',
                  type = 'real',
                  value = 'beta - cmath.acos(cba)',
                  texname = '\\alpha')

cb = Parameter(name = 'cb',
               nature = 'internal',
               type = 'real',
               value = 'cmath.cos(beta)',
               texname = 'c_{\\beta }')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

sb = Parameter(name = 'sb',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sin(beta)',
               texname = 's_{\\beta }')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

ca = Parameter(name = 'ca',
               nature = 'internal',
               type = 'real',
               value = 'cb*cba + sb*sba',
               texname = 'c_{\\alpha }')

m112 = Parameter(name = 'm112',
                 nature = 'internal',
                 type = 'real',
                 value = '(m122*sb)/cb + (MHL**2*sba*(cba*sb - cb*sba))/(2.*cb) - (cba*MHH**2*(cb*cba + sb*sba))/(2.*cb)',
                 texname = '\\text{m112}')

m222 = Parameter(name = 'm222',
                 nature = 'internal',
                 type = 'real',
                 value = '(cb*m122)/sb + (cba*MHH**2*(-(cba*sb) + cb*sba))/(2.*sb) - (MHL**2*sba*(cb*cba + sb*sba))/(2.*sb)',
                 texname = '\\text{m222}')

MM2 = Parameter(name = 'MM2',
                nature = 'internal',
                type = 'real',
                value = 'm122/(cb*sb)',
                texname = '\\text{MM2}')

sa = Parameter(name = 'sa',
               nature = 'internal',
               type = 'real',
               value = 'cba*sb - cb*sba',
               texname = 's_{\\alpha }')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

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
                 value = '(-(m122*sb) + cb*(MHH**2 + (-MHH**2 + MHL**2)*(cba*sb - cb*sba)**2))/(cb**3*vev**2)',
                 texname = '\\text{lam1}')

lam2 = Parameter(name = 'lam2',
                 nature = 'internal',
                 type = 'real',
                 value = '(-(cb*m122) + sb*(MHL**2 + (MHH**2 - MHL**2)*(cba*sb - cb*sba)**2))/(sb**3*vev**2)',
                 texname = '\\text{lam2}')

lam3 = Parameter(name = 'lam3',
                 nature = 'internal',
                 type = 'real',
                 value = '(-m122 + 2*cb*MHp**2*sb + (MHH**2 - MHL**2)*(cba*sb - cb*sba)*(cb*cba + sb*sba))/(cb*sb*vev**2)',
                 texname = '\\text{lam3}')

lam4 = Parameter(name = 'lam4',
                 nature = 'internal',
                 type = 'real',
                 value = '(m122 + cb*(MHA**2 - 2*MHp**2)*sb)/(cb*sb*vev**2)',
                 texname = '\\text{lam4}')

lam5 = Parameter(name = 'lam5',
                 nature = 'internal',
                 type = 'real',
                 value = '(m122 - cb*MHA**2*sb)/(cb*sb*vev**2)',
                 texname = '\\text{lam5}')

vev1 = Parameter(name = 'vev1',
                 nature = 'internal',
                 type = 'real',
                 value = 'cb*vev',
                 texname = '\\text{vev1}')

vev2 = Parameter(name = 'vev2',
                 nature = 'internal',
                 type = 'real',
                 value = 'sb*vev',
                 texname = '\\text{vev2}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

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

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I1a33}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I2a33}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I3a33}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I4a33}')

