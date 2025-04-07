# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Mon 7 Apr 2025 23:36:35



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

rhod1x1 = Parameter(name = 'rhod1x1',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhod1x1}',
                    lhablock = 'RHODO',
                    lhacode = [ 1, 1 ])

rhod1x2 = Parameter(name = 'rhod1x2',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhod1x2}',
                    lhablock = 'RHODO',
                    lhacode = [ 1, 2 ])

rhod1x3 = Parameter(name = 'rhod1x3',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhod1x3}',
                    lhablock = 'RHODO',
                    lhacode = [ 1, 3 ])

rhod2x1 = Parameter(name = 'rhod2x1',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhod2x1}',
                    lhablock = 'RHODO',
                    lhacode = [ 2, 1 ])

rhod2x2 = Parameter(name = 'rhod2x2',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhod2x2}',
                    lhablock = 'RHODO',
                    lhacode = [ 2, 2 ])

rhod2x3 = Parameter(name = 'rhod2x3',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhod2x3}',
                    lhablock = 'RHODO',
                    lhacode = [ 2, 3 ])

rhod3x1 = Parameter(name = 'rhod3x1',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhod3x1}',
                    lhablock = 'RHODO',
                    lhacode = [ 3, 1 ])

rhod3x2 = Parameter(name = 'rhod3x2',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhod3x2}',
                    lhablock = 'RHODO',
                    lhacode = [ 3, 2 ])

rhod3x3 = Parameter(name = 'rhod3x3',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhod3x3}',
                    lhablock = 'RHODO',
                    lhacode = [ 3, 3 ])

rhol1x1 = Parameter(name = 'rhol1x1',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhol1x1}',
                    lhablock = 'RHOLEP',
                    lhacode = [ 1, 1 ])

rhol1x2 = Parameter(name = 'rhol1x2',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhol1x2}',
                    lhablock = 'RHOLEP',
                    lhacode = [ 1, 2 ])

rhol1x3 = Parameter(name = 'rhol1x3',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhol1x3}',
                    lhablock = 'RHOLEP',
                    lhacode = [ 1, 3 ])

rhol2x1 = Parameter(name = 'rhol2x1',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhol2x1}',
                    lhablock = 'RHOLEP',
                    lhacode = [ 2, 1 ])

rhol2x2 = Parameter(name = 'rhol2x2',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhol2x2}',
                    lhablock = 'RHOLEP',
                    lhacode = [ 2, 2 ])

rhol2x3 = Parameter(name = 'rhol2x3',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhol2x3}',
                    lhablock = 'RHOLEP',
                    lhacode = [ 2, 3 ])

rhol3x1 = Parameter(name = 'rhol3x1',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhol3x1}',
                    lhablock = 'RHOLEP',
                    lhacode = [ 3, 1 ])

rhol3x2 = Parameter(name = 'rhol3x2',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhol3x2}',
                    lhablock = 'RHOLEP',
                    lhacode = [ 3, 2 ])

rhol3x3 = Parameter(name = 'rhol3x3',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhol3x3}',
                    lhablock = 'RHOLEP',
                    lhacode = [ 3, 3 ])

rhou1x1 = Parameter(name = 'rhou1x1',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhou1x1}',
                    lhablock = 'RHOUP',
                    lhacode = [ 1, 1 ])

rhou1x2 = Parameter(name = 'rhou1x2',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhou1x2}',
                    lhablock = 'RHOUP',
                    lhacode = [ 1, 2 ])

rhou1x3 = Parameter(name = 'rhou1x3',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhou1x3}',
                    lhablock = 'RHOUP',
                    lhacode = [ 1, 3 ])

rhou2x1 = Parameter(name = 'rhou2x1',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhou2x1}',
                    lhablock = 'RHOUP',
                    lhacode = [ 2, 1 ])

rhou2x2 = Parameter(name = 'rhou2x2',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhou2x2}',
                    lhablock = 'RHOUP',
                    lhacode = [ 2, 2 ])

rhou2x3 = Parameter(name = 'rhou2x3',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhou2x3}',
                    lhablock = 'RHOUP',
                    lhacode = [ 2, 3 ])

rhou3x1 = Parameter(name = 'rhou3x1',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhou3x1}',
                    lhablock = 'RHOUP',
                    lhacode = [ 3, 1 ])

rhou3x2 = Parameter(name = 'rhou3x2',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhou3x2}',
                    lhablock = 'RHOUP',
                    lhacode = [ 3, 2 ])

rhou3x3 = Parameter(name = 'rhou3x3',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{rhou3x3}',
                    lhablock = 'RHOUP',
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

yd1hat1x2 = Parameter(name = 'yd1hat1x2',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhod1x2*sb)',
                      texname = '\\text{yd1hat1x2}')

yd1hat1x3 = Parameter(name = 'yd1hat1x3',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhod1x3*sb)',
                      texname = '\\text{yd1hat1x3}')

yd1hat2x1 = Parameter(name = 'yd1hat2x1',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhod2x1*sb)',
                      texname = '\\text{yd1hat2x1}')

yd1hat2x3 = Parameter(name = 'yd1hat2x3',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhod2x3*sb)',
                      texname = '\\text{yd1hat2x3}')

yd1hat3x1 = Parameter(name = 'yd1hat3x1',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhod3x1*sb)',
                      texname = '\\text{yd1hat3x1}')

yd1hat3x2 = Parameter(name = 'yd1hat3x2',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhod3x2*sb)',
                      texname = '\\text{yd1hat3x2}')

yd2hat1x2 = Parameter(name = 'yd2hat1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhod1x2',
                      texname = '\\text{yd2hat1x2}')

yd2hat1x3 = Parameter(name = 'yd2hat1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhod1x3',
                      texname = '\\text{yd2hat1x3}')

yd2hat2x1 = Parameter(name = 'yd2hat2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhod2x1',
                      texname = '\\text{yd2hat2x1}')

yd2hat2x3 = Parameter(name = 'yd2hat2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhod2x3',
                      texname = '\\text{yd2hat2x3}')

yd2hat3x1 = Parameter(name = 'yd2hat3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhod3x1',
                      texname = '\\text{yd2hat3x1}')

yd2hat3x2 = Parameter(name = 'yd2hat3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhod3x2',
                      texname = '\\text{yd2hat3x2}')

yl1hat1x2 = Parameter(name = 'yl1hat1x2',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhol1x2*sb)',
                      texname = '\\text{yl1hat1x2}')

yl1hat1x3 = Parameter(name = 'yl1hat1x3',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhol1x3*sb)',
                      texname = '\\text{yl1hat1x3}')

yl1hat2x1 = Parameter(name = 'yl1hat2x1',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhol2x1*sb)',
                      texname = '\\text{yl1hat2x1}')

yl1hat2x3 = Parameter(name = 'yl1hat2x3',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhol2x3*sb)',
                      texname = '\\text{yl1hat2x3}')

yl1hat3x1 = Parameter(name = 'yl1hat3x1',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhol3x1*sb)',
                      texname = '\\text{yl1hat3x1}')

yl1hat3x2 = Parameter(name = 'yl1hat3x2',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhol3x2*sb)',
                      texname = '\\text{yl1hat3x2}')

yl2hat1x2 = Parameter(name = 'yl2hat1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhol1x2',
                      texname = '\\text{yl2hat1x2}')

yl2hat1x3 = Parameter(name = 'yl2hat1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhol1x3',
                      texname = '\\text{yl2hat1x3}')

yl2hat2x1 = Parameter(name = 'yl2hat2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhol2x1',
                      texname = '\\text{yl2hat2x1}')

yl2hat2x3 = Parameter(name = 'yl2hat2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhol2x3',
                      texname = '\\text{yl2hat2x3}')

yl2hat3x1 = Parameter(name = 'yl2hat3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhol3x1',
                      texname = '\\text{yl2hat3x1}')

yl2hat3x2 = Parameter(name = 'yl2hat3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhol3x2',
                      texname = '\\text{yl2hat3x2}')

yu1hat1x2 = Parameter(name = 'yu1hat1x2',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhou1x2*sb)',
                      texname = '\\text{yu1hat1x2}')

yu1hat1x3 = Parameter(name = 'yu1hat1x3',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhou1x3*sb)',
                      texname = '\\text{yu1hat1x3}')

yu1hat2x1 = Parameter(name = 'yu1hat2x1',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhou2x1*sb)',
                      texname = '\\text{yu1hat2x1}')

yu1hat2x3 = Parameter(name = 'yu1hat2x3',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhou2x3*sb)',
                      texname = '\\text{yu1hat2x3}')

yu1hat3x1 = Parameter(name = 'yu1hat3x1',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhou3x1*sb)',
                      texname = '\\text{yu1hat3x1}')

yu1hat3x2 = Parameter(name = 'yu1hat3x2',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhou3x2*sb)',
                      texname = '\\text{yu1hat3x2}')

yu2hat1x2 = Parameter(name = 'yu2hat1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhou1x2',
                      texname = '\\text{yu2hat1x2}')

yu2hat1x3 = Parameter(name = 'yu2hat1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhou1x3',
                      texname = '\\text{yu2hat1x3}')

yu2hat2x1 = Parameter(name = 'yu2hat2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhou2x1',
                      texname = '\\text{yu2hat2x1}')

yu2hat2x3 = Parameter(name = 'yu2hat2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhou2x3',
                      texname = '\\text{yu2hat2x3}')

yu2hat3x1 = Parameter(name = 'yu2hat3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhou3x1',
                      texname = '\\text{yu2hat3x1}')

yu2hat3x2 = Parameter(name = 'yu2hat3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhou3x2',
                      texname = '\\text{yu2hat3x2}')

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

yd1hat1x1 = Parameter(name = 'yd1hat1x1',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhod1x1*sb) + cb*ydo',
                      texname = '\\text{yd1hat1x1}')

yd1hat2x2 = Parameter(name = 'yd1hat2x2',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhod2x2*sb) + cb*ys',
                      texname = '\\text{yd1hat2x2}')

yd1hat3x3 = Parameter(name = 'yd1hat3x3',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhod3x3*sb) + cb*yb',
                      texname = '\\text{yd1hat3x3}')

yd2hat1x1 = Parameter(name = 'yd2hat1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhod1x1 + sb*ydo',
                      texname = '\\text{yd2hat1x1}')

yd2hat2x2 = Parameter(name = 'yd2hat2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhod2x2 + sb*ys',
                      texname = '\\text{yd2hat2x2}')

yd2hat3x3 = Parameter(name = 'yd2hat3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhod3x3 + sb*yb',
                      texname = '\\text{yd2hat3x3}')

yl1hat1x1 = Parameter(name = 'yl1hat1x1',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhol1x1*sb) + cb*ye',
                      texname = '\\text{yl1hat1x1}')

yl1hat2x2 = Parameter(name = 'yl1hat2x2',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhol2x2*sb) + cb*ym',
                      texname = '\\text{yl1hat2x2}')

yl1hat3x3 = Parameter(name = 'yl1hat3x3',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhol3x3*sb) + cb*ytau',
                      texname = '\\text{yl1hat3x3}')

yl2hat1x1 = Parameter(name = 'yl2hat1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhol1x1 + sb*ye',
                      texname = '\\text{yl2hat1x1}')

yl2hat2x2 = Parameter(name = 'yl2hat2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhol2x2 + sb*ym',
                      texname = '\\text{yl2hat2x2}')

yl2hat3x3 = Parameter(name = 'yl2hat3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhol3x3 + sb*ytau',
                      texname = '\\text{yl2hat3x3}')

yu1hat1x1 = Parameter(name = 'yu1hat1x1',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhou1x1*sb) + cb*yup',
                      texname = '\\text{yu1hat1x1}')

yu1hat2x2 = Parameter(name = 'yu1hat2x2',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhou2x2*sb) + cb*yc',
                      texname = '\\text{yu1hat2x2}')

yu1hat3x3 = Parameter(name = 'yu1hat3x3',
                      nature = 'internal',
                      type = 'real',
                      value = '-(rhou3x3*sb) + cb*yt',
                      texname = '\\text{yu1hat3x3}')

yu2hat1x1 = Parameter(name = 'yu2hat1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhou1x1 + sb*yup',
                      texname = '\\text{yu2hat1x1}')

yu2hat2x2 = Parameter(name = 'yu2hat2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhou2x2 + sb*yc',
                      texname = '\\text{yu2hat2x2}')

yu2hat3x3 = Parameter(name = 'yu2hat3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'cb*rhou3x3 + sb*yt',
                      texname = '\\text{yu2hat3x3}')

I1a11 = Parameter(name = 'I1a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd1hat1x1*complexconjugate(CKM1x1) + yd1hat2x1*complexconjugate(CKM1x2)',
                  texname = '\\text{I1a11}')

I1a12 = Parameter(name = 'I1a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd1hat1x1*complexconjugate(CKM2x1) + yd1hat2x1*complexconjugate(CKM2x2)',
                  texname = '\\text{I1a12}')

I1a13 = Parameter(name = 'I1a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd1hat3x1',
                  texname = '\\text{I1a13}')

I1a21 = Parameter(name = 'I1a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd1hat1x2*complexconjugate(CKM1x1) + yd1hat2x2*complexconjugate(CKM1x2)',
                  texname = '\\text{I1a21}')

I1a22 = Parameter(name = 'I1a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd1hat1x2*complexconjugate(CKM2x1) + yd1hat2x2*complexconjugate(CKM2x2)',
                  texname = '\\text{I1a22}')

I1a23 = Parameter(name = 'I1a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd1hat3x2',
                  texname = '\\text{I1a23}')

I1a31 = Parameter(name = 'I1a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd1hat1x3*complexconjugate(CKM1x1) + yd1hat2x3*complexconjugate(CKM1x2)',
                  texname = '\\text{I1a31}')

I1a32 = Parameter(name = 'I1a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd1hat1x3*complexconjugate(CKM2x1) + yd1hat2x3*complexconjugate(CKM2x2)',
                  texname = '\\text{I1a32}')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd1hat3x3',
                  texname = '\\text{I1a33}')

I2a11 = Parameter(name = 'I2a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd2hat1x1*complexconjugate(CKM1x1) + yd2hat2x1*complexconjugate(CKM1x2)',
                  texname = '\\text{I2a11}')

I2a12 = Parameter(name = 'I2a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd2hat1x1*complexconjugate(CKM2x1) + yd2hat2x1*complexconjugate(CKM2x2)',
                  texname = '\\text{I2a12}')

I2a13 = Parameter(name = 'I2a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd2hat3x1',
                  texname = '\\text{I2a13}')

I2a21 = Parameter(name = 'I2a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd2hat1x2*complexconjugate(CKM1x1) + yd2hat2x2*complexconjugate(CKM1x2)',
                  texname = '\\text{I2a21}')

I2a22 = Parameter(name = 'I2a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd2hat1x2*complexconjugate(CKM2x1) + yd2hat2x2*complexconjugate(CKM2x2)',
                  texname = '\\text{I2a22}')

I2a23 = Parameter(name = 'I2a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd2hat3x2',
                  texname = '\\text{I2a23}')

I2a31 = Parameter(name = 'I2a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd2hat1x3*complexconjugate(CKM1x1) + yd2hat2x3*complexconjugate(CKM1x2)',
                  texname = '\\text{I2a31}')

I2a32 = Parameter(name = 'I2a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd2hat1x3*complexconjugate(CKM2x1) + yd2hat2x3*complexconjugate(CKM2x2)',
                  texname = '\\text{I2a32}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd2hat3x3',
                  texname = '\\text{I2a33}')

I3a11 = Parameter(name = 'I3a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu1hat1x1*complexconjugate(CKM1x1) + yu1hat2x1*complexconjugate(CKM2x1)',
                  texname = '\\text{I3a11}')

I3a12 = Parameter(name = 'I3a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu1hat1x2*complexconjugate(CKM1x1) + yu1hat2x2*complexconjugate(CKM2x1)',
                  texname = '\\text{I3a12}')

I3a13 = Parameter(name = 'I3a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu1hat1x3*complexconjugate(CKM1x1) + yu1hat2x3*complexconjugate(CKM2x1)',
                  texname = '\\text{I3a13}')

I3a21 = Parameter(name = 'I3a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu1hat1x1*complexconjugate(CKM1x2) + yu1hat2x1*complexconjugate(CKM2x2)',
                  texname = '\\text{I3a21}')

I3a22 = Parameter(name = 'I3a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu1hat1x2*complexconjugate(CKM1x2) + yu1hat2x2*complexconjugate(CKM2x2)',
                  texname = '\\text{I3a22}')

I3a23 = Parameter(name = 'I3a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu1hat1x3*complexconjugate(CKM1x2) + yu1hat2x3*complexconjugate(CKM2x2)',
                  texname = '\\text{I3a23}')

I3a31 = Parameter(name = 'I3a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu1hat3x1',
                  texname = '\\text{I3a31}')

I3a32 = Parameter(name = 'I3a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu1hat3x2',
                  texname = '\\text{I3a32}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu1hat3x3',
                  texname = '\\text{I3a33}')

I4a11 = Parameter(name = 'I4a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu2hat1x1*complexconjugate(CKM1x1) + yu2hat2x1*complexconjugate(CKM2x1)',
                  texname = '\\text{I4a11}')

I4a12 = Parameter(name = 'I4a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu2hat1x2*complexconjugate(CKM1x1) + yu2hat2x2*complexconjugate(CKM2x1)',
                  texname = '\\text{I4a12}')

I4a13 = Parameter(name = 'I4a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu2hat1x3*complexconjugate(CKM1x1) + yu2hat2x3*complexconjugate(CKM2x1)',
                  texname = '\\text{I4a13}')

I4a21 = Parameter(name = 'I4a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu2hat1x1*complexconjugate(CKM1x2) + yu2hat2x1*complexconjugate(CKM2x2)',
                  texname = '\\text{I4a21}')

I4a22 = Parameter(name = 'I4a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu2hat1x2*complexconjugate(CKM1x2) + yu2hat2x2*complexconjugate(CKM2x2)',
                  texname = '\\text{I4a22}')

I4a23 = Parameter(name = 'I4a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu2hat1x3*complexconjugate(CKM1x2) + yu2hat2x3*complexconjugate(CKM2x2)',
                  texname = '\\text{I4a23}')

I4a31 = Parameter(name = 'I4a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu2hat3x1',
                  texname = '\\text{I4a31}')

I4a32 = Parameter(name = 'I4a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu2hat3x2',
                  texname = '\\text{I4a32}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu2hat3x3',
                  texname = '\\text{I4a33}')

I5a11 = Parameter(name = 'I5a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yu1hat1x1 + CKM2x1*yu1hat2x1',
                  texname = '\\text{I5a11}')

I5a12 = Parameter(name = 'I5a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yu1hat1x1 + CKM2x2*yu1hat2x1',
                  texname = '\\text{I5a12}')

I5a13 = Parameter(name = 'I5a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu1hat3x1',
                  texname = '\\text{I5a13}')

I5a21 = Parameter(name = 'I5a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yu1hat1x2 + CKM2x1*yu1hat2x2',
                  texname = '\\text{I5a21}')

I5a22 = Parameter(name = 'I5a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yu1hat1x2 + CKM2x2*yu1hat2x2',
                  texname = '\\text{I5a22}')

I5a23 = Parameter(name = 'I5a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu1hat3x2',
                  texname = '\\text{I5a23}')

I5a31 = Parameter(name = 'I5a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yu1hat1x3 + CKM2x1*yu1hat2x3',
                  texname = '\\text{I5a31}')

I5a32 = Parameter(name = 'I5a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yu1hat1x3 + CKM2x2*yu1hat2x3',
                  texname = '\\text{I5a32}')

I5a33 = Parameter(name = 'I5a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu1hat3x3',
                  texname = '\\text{I5a33}')

I6a11 = Parameter(name = 'I6a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yu2hat1x1 + CKM2x1*yu2hat2x1',
                  texname = '\\text{I6a11}')

I6a12 = Parameter(name = 'I6a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yu2hat1x1 + CKM2x2*yu2hat2x1',
                  texname = '\\text{I6a12}')

I6a13 = Parameter(name = 'I6a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu2hat3x1',
                  texname = '\\text{I6a13}')

I6a21 = Parameter(name = 'I6a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yu2hat1x2 + CKM2x1*yu2hat2x2',
                  texname = '\\text{I6a21}')

I6a22 = Parameter(name = 'I6a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yu2hat1x2 + CKM2x2*yu2hat2x2',
                  texname = '\\text{I6a22}')

I6a23 = Parameter(name = 'I6a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu2hat3x2',
                  texname = '\\text{I6a23}')

I6a31 = Parameter(name = 'I6a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yu2hat1x3 + CKM2x1*yu2hat2x3',
                  texname = '\\text{I6a31}')

I6a32 = Parameter(name = 'I6a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yu2hat1x3 + CKM2x2*yu2hat2x3',
                  texname = '\\text{I6a32}')

I6a33 = Parameter(name = 'I6a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yu2hat3x3',
                  texname = '\\text{I6a33}')

I7a11 = Parameter(name = 'I7a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yd1hat1x1 + CKM1x2*yd1hat2x1',
                  texname = '\\text{I7a11}')

I7a12 = Parameter(name = 'I7a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yd1hat1x2 + CKM1x2*yd1hat2x2',
                  texname = '\\text{I7a12}')

I7a13 = Parameter(name = 'I7a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yd1hat1x3 + CKM1x2*yd1hat2x3',
                  texname = '\\text{I7a13}')

I7a21 = Parameter(name = 'I7a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yd1hat1x1 + CKM2x2*yd1hat2x1',
                  texname = '\\text{I7a21}')

I7a22 = Parameter(name = 'I7a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yd1hat1x2 + CKM2x2*yd1hat2x2',
                  texname = '\\text{I7a22}')

I7a23 = Parameter(name = 'I7a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yd1hat1x3 + CKM2x2*yd1hat2x3',
                  texname = '\\text{I7a23}')

I7a31 = Parameter(name = 'I7a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd1hat3x1',
                  texname = '\\text{I7a31}')

I7a32 = Parameter(name = 'I7a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd1hat3x2',
                  texname = '\\text{I7a32}')

I7a33 = Parameter(name = 'I7a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd1hat3x3',
                  texname = '\\text{I7a33}')

I8a11 = Parameter(name = 'I8a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yd2hat1x1 + CKM1x2*yd2hat2x1',
                  texname = '\\text{I8a11}')

I8a12 = Parameter(name = 'I8a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yd2hat1x2 + CKM1x2*yd2hat2x2',
                  texname = '\\text{I8a12}')

I8a13 = Parameter(name = 'I8a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yd2hat1x3 + CKM1x2*yd2hat2x3',
                  texname = '\\text{I8a13}')

I8a21 = Parameter(name = 'I8a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yd2hat1x1 + CKM2x2*yd2hat2x1',
                  texname = '\\text{I8a21}')

I8a22 = Parameter(name = 'I8a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yd2hat1x2 + CKM2x2*yd2hat2x2',
                  texname = '\\text{I8a22}')

I8a23 = Parameter(name = 'I8a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yd2hat1x3 + CKM2x2*yd2hat2x3',
                  texname = '\\text{I8a23}')

I8a31 = Parameter(name = 'I8a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd2hat3x1',
                  texname = '\\text{I8a31}')

I8a32 = Parameter(name = 'I8a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd2hat3x2',
                  texname = '\\text{I8a32}')

I8a33 = Parameter(name = 'I8a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd2hat3x3',
                  texname = '\\text{I8a33}')

