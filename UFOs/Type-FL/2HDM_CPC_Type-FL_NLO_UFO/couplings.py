# This file was automatically created by FeynRules 2.3.36
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Tue 18 Aug 2020 00:12:31


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(complex(0,1)*I1a33)',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '-(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '(cb*cw*ee*sa)/(2.*sw) - (ca*cw*ee*sb)/(2.*sw) + (cb*ee*sa*sw)/(2.*cw) - (ca*ee*sb*sw)/(2.*cw)',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-(cb*cw*ee*sa)/(2.*sw) + (ca*cw*ee*sb)/(2.*sw) - (cb*ee*sa*sw)/(2.*cw) + (ca*ee*sb*sw)/(2.*cw)',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-(ca*cb*cw*ee)/(2.*sw) - (cw*ee*sa*sb)/(2.*sw) - (ca*cb*ee*sw)/(2.*cw) - (ee*sa*sb*sw)/(2.*cw)',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '(ca*cb*cw*ee)/(2.*sw) + (cw*ee*sa*sb)/(2.*sw) + (ca*cb*ee*sw)/(2.*cw) + (ee*sa*sb*sw)/(2.*cw)',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '(cb**2*cw*ee*complex(0,1))/(2.*sw) + (cw*ee*complex(0,1)*sb**2)/(2.*sw) - (cb**2*ee*complex(0,1)*sw)/(2.*cw) - (ee*complex(0,1)*sb**2*sw)/(2.*cw)',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-(cb**2*cw*ee*complex(0,1))/(2.*sw) - (cw*ee*complex(0,1)*sb**2)/(2.*sw) + (cb**2*ee*complex(0,1)*sw)/(2.*cw) + (ee*complex(0,1)*sb**2*sw)/(2.*cw)',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '(cb**2*cw*ee**2*complex(0,1))/sw + (cw*ee**2*complex(0,1)*sb**2)/sw - (cb**2*ee**2*complex(0,1)*sw)/cw - (ee**2*complex(0,1)*sb**2*sw)/cw',
                  order = {'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = 'ca**2*ee**2*complex(0,1) + ee**2*complex(0,1)*sa**2 + (ca**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*sa**2)/(2.*sw**2) + (ca**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*sa**2*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)*I2a33',
                 order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-(cb**2*ee**2*complex(0,1)) - ee**2*complex(0,1)*sb**2 + (cb**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*sb**2)/(2.*sw**2) + (cb**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*sb**2*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = 'cb**2*ee**2*complex(0,1) + ee**2*complex(0,1)*sb**2 + (cb**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*sb**2)/(2.*sw**2) + (cb**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*sb**2*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_112 = Coupling(name = 'GC_112',
                  value = '-(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '3*ca**2*cb*complex(0,1)*lam1*sa*vev - 2*ca**2*cb*complex(0,1)*lam3*sa*vev - 2*ca**2*cb*complex(0,1)*lam4*sa*vev - 2*ca**2*cb*complex(0,1)*lam5*sa*vev + cb*complex(0,1)*lam3*sa**3*vev + cb*complex(0,1)*lam4*sa**3*vev + cb*complex(0,1)*lam5*sa**3*vev - ca**3*complex(0,1)*lam3*sb*vev - ca**3*complex(0,1)*lam4*sb*vev - ca**3*complex(0,1)*lam5*sb*vev - 3*ca*complex(0,1)*lam2*sa**2*sb*vev + 2*ca*complex(0,1)*lam3*sa**2*sb*vev + 2*ca*complex(0,1)*lam4*sa**2*sb*vev + 2*ca*complex(0,1)*lam5*sa**2*sb*vev',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '3*ca**2*cb*complex(0,1)*lam3*sa*vev + 3*ca**2*cb*complex(0,1)*lam4*sa*vev + 3*ca**2*cb*complex(0,1)*lam5*sa*vev + 3*cb*complex(0,1)*lam1*sa**3*vev - 3*ca**3*complex(0,1)*lam2*sb*vev - 3*ca*complex(0,1)*lam3*sa**2*sb*vev - 3*ca*complex(0,1)*lam4*sa**2*sb*vev - 3*ca*complex(0,1)*lam5*sa**2*sb*vev',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '-3*ca**3*cb*complex(0,1)*lam1*vev - 3*ca*cb*complex(0,1)*lam3*sa**2*vev - 3*ca*cb*complex(0,1)*lam4*sa**2*vev - 3*ca*cb*complex(0,1)*lam5*sa**2*vev - 3*ca**2*complex(0,1)*lam3*sa*sb*vev - 3*ca**2*complex(0,1)*lam4*sa*sb*vev - 3*ca**2*complex(0,1)*lam5*sa*sb*vev - 3*complex(0,1)*lam2*sa**3*sb*vev',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-(ca**3*cb*complex(0,1)*lam3*vev) - ca**3*cb*complex(0,1)*lam4*vev - ca**3*cb*complex(0,1)*lam5*vev - 3*ca*cb*complex(0,1)*lam1*sa**2*vev + 2*ca*cb*complex(0,1)*lam3*sa**2*vev + 2*ca*cb*complex(0,1)*lam4*sa**2*vev + 2*ca*cb*complex(0,1)*lam5*sa**2*vev - 3*ca**2*complex(0,1)*lam2*sa*sb*vev + 2*ca**2*complex(0,1)*lam3*sa*sb*vev + 2*ca**2*complex(0,1)*lam4*sa*sb*vev + 2*ca**2*complex(0,1)*lam5*sa*sb*vev - complex(0,1)*lam3*sa**3*sb*vev - complex(0,1)*lam4*sa**3*sb*vev - complex(0,1)*lam5*sa**3*sb*vev',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '-(cb**2*ee**2*complex(0,1)*vev)/(2.*cw) - (ee**2*complex(0,1)*sb**2*vev)/(2.*cw)',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = 'cb**3*complex(0,1)*lam1*sa*vev - ca*cb**2*complex(0,1)*lam3*sb*vev - ca*cb**2*complex(0,1)*lam4*sb*vev - ca*cb**2*complex(0,1)*lam5*sb*vev + cb*complex(0,1)*lam3*sa*sb**2*vev + cb*complex(0,1)*lam4*sa*sb**2*vev + cb*complex(0,1)*lam5*sa*sb**2*vev - ca*complex(0,1)*lam2*sb**3*vev',
                  order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*I3a33',
                 order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = 'cb**3*complex(0,1)*lam3*sa*vev - ca*cb**2*complex(0,1)*lam2*sb*vev + ca*cb**2*complex(0,1)*lam4*sb*vev + ca*cb**2*complex(0,1)*lam5*sb*vev + cb*complex(0,1)*lam1*sa*sb**2*vev - cb*complex(0,1)*lam4*sa*sb**2*vev - cb*complex(0,1)*lam5*sa*sb**2*vev - ca*complex(0,1)*lam3*sb**3*vev',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '-(cb**3*complex(0,1)*lam4*sa*vev)/2. - (cb**3*complex(0,1)*lam5*sa*vev)/2. + ca*cb**2*complex(0,1)*lam1*sb*vev - ca*cb**2*complex(0,1)*lam3*sb*vev - (ca*cb**2*complex(0,1)*lam4*sb*vev)/2. - (ca*cb**2*complex(0,1)*lam5*sb*vev)/2. - cb*complex(0,1)*lam2*sa*sb**2*vev + cb*complex(0,1)*lam3*sa*sb**2*vev + (cb*complex(0,1)*lam4*sa*sb**2*vev)/2. + (cb*complex(0,1)*lam5*sa*sb**2*vev)/2. + (ca*complex(0,1)*lam4*sb**3*vev)/2. + (ca*complex(0,1)*lam5*sb**3*vev)/2.',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '-(cb**3*complex(0,1)*lam5*sa*vev) + ca*cb**2*complex(0,1)*lam1*sb*vev - ca*cb**2*complex(0,1)*lam3*sb*vev - ca*cb**2*complex(0,1)*lam4*sb*vev - cb*complex(0,1)*lam2*sa*sb**2*vev + cb*complex(0,1)*lam3*sa*sb**2*vev + cb*complex(0,1)*lam4*sa*sb**2*vev + ca*complex(0,1)*lam5*sb**3*vev',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = 'cb**3*complex(0,1)*lam3*sa*vev + cb**3*complex(0,1)*lam4*sa*vev - cb**3*complex(0,1)*lam5*sa*vev - ca*cb**2*complex(0,1)*lam2*sb*vev + 2*ca*cb**2*complex(0,1)*lam5*sb*vev + cb*complex(0,1)*lam1*sa*sb**2*vev - 2*cb*complex(0,1)*lam5*sa*sb**2*vev - ca*complex(0,1)*lam3*sb**3*vev - ca*complex(0,1)*lam4*sb**3*vev + ca*complex(0,1)*lam5*sb**3*vev',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-(ca*cb**3*complex(0,1)*lam1*vev) - cb**2*complex(0,1)*lam3*sa*sb*vev - cb**2*complex(0,1)*lam4*sa*sb*vev - cb**2*complex(0,1)*lam5*sa*sb*vev - ca*cb*complex(0,1)*lam3*sb**2*vev - ca*cb*complex(0,1)*lam4*sb**2*vev - ca*cb*complex(0,1)*lam5*sb**2*vev - complex(0,1)*lam2*sa*sb**3*vev',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '-(ca*cb**3*complex(0,1)*lam3*vev) - cb**2*complex(0,1)*lam2*sa*sb*vev + cb**2*complex(0,1)*lam4*sa*sb*vev + cb**2*complex(0,1)*lam5*sa*sb*vev - ca*cb*complex(0,1)*lam1*sb**2*vev + ca*cb*complex(0,1)*lam4*sb**2*vev + ca*cb*complex(0,1)*lam5*sb**2*vev - complex(0,1)*lam3*sa*sb**3*vev',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '-(ca*cb**3*complex(0,1)*lam4*vev)/2. - (ca*cb**3*complex(0,1)*lam5*vev)/2. - cb**2*complex(0,1)*lam1*sa*sb*vev + cb**2*complex(0,1)*lam3*sa*sb*vev + (cb**2*complex(0,1)*lam4*sa*sb*vev)/2. + (cb**2*complex(0,1)*lam5*sa*sb*vev)/2. - ca*cb*complex(0,1)*lam2*sb**2*vev + ca*cb*complex(0,1)*lam3*sb**2*vev + (ca*cb*complex(0,1)*lam4*sb**2*vev)/2. + (ca*cb*complex(0,1)*lam5*sb**2*vev)/2. - (complex(0,1)*lam4*sa*sb**3*vev)/2. - (complex(0,1)*lam5*sa*sb**3*vev)/2.',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '-(ca*cb**3*complex(0,1)*lam5*vev) - cb**2*complex(0,1)*lam1*sa*sb*vev + cb**2*complex(0,1)*lam3*sa*sb*vev + cb**2*complex(0,1)*lam4*sa*sb*vev - ca*cb*complex(0,1)*lam2*sb**2*vev + ca*cb*complex(0,1)*lam3*sb**2*vev + ca*cb*complex(0,1)*lam4*sb**2*vev - complex(0,1)*lam5*sa*sb**3*vev',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '-(ca*cb**3*complex(0,1)*lam3*vev) - ca*cb**3*complex(0,1)*lam4*vev + ca*cb**3*complex(0,1)*lam5*vev - cb**2*complex(0,1)*lam2*sa*sb*vev + 2*cb**2*complex(0,1)*lam5*sa*sb*vev - ca*cb*complex(0,1)*lam1*sb**2*vev + 2*ca*cb*complex(0,1)*lam5*sb**2*vev - complex(0,1)*lam3*sa*sb**3*vev - complex(0,1)*lam4*sa*sb**3*vev + complex(0,1)*lam5*sa*sb**3*vev',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(cb**4*lam4*vev)/2. - (cb**4*lam5*vev)/2. + cb**2*lam4*sb**2*vev - cb**2*lam5*sb**2*vev + (lam4*sb**4*vev)/2. - (lam5*sb**4*vev)/2.',
                  order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(complex(0,1)*I4a33)',
                 order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '-(cb**4*lam4*vev)/2. + (cb**4*lam5*vev)/2. - cb**2*lam4*sb**2*vev + cb**2*lam5*sb**2*vev - (lam4*sb**4*vev)/2. + (lam5*sb**4*vev)/2.',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '-(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '-(cb*ee**2*complex(0,1)*sa*vev)/(2.*sw**2) + (ca*ee**2*complex(0,1)*sb*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '(ca*cb*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sa*sb*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '(cb**2*ee**2*complex(0,1)*vev)/(2.*sw) + (ee**2*complex(0,1)*sb**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '-(cb*ee**2*complex(0,1)*sa*vev) + ca*ee**2*complex(0,1)*sb*vev - (cb*cw**2*ee**2*complex(0,1)*sa*vev)/(2.*sw**2) + (ca*cw**2*ee**2*complex(0,1)*sb*vev)/(2.*sw**2) - (cb*ee**2*complex(0,1)*sa*sw**2*vev)/(2.*cw**2) + (ca*ee**2*complex(0,1)*sb*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = 'ca*cb*ee**2*complex(0,1)*vev + ee**2*complex(0,1)*sa*sb*vev + (ca*cb*cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*sa*sb*vev)/(2.*sw**2) + (ca*cb*ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2) + (ee**2*complex(0,1)*sa*sb*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-3*ca**3*complex(0,1)*lam2*sa + 3*ca**3*complex(0,1)*lam3*sa + 3*ca**3*complex(0,1)*lam4*sa + 3*ca**3*complex(0,1)*lam5*sa + 3*ca*complex(0,1)*lam1*sa**3 - 3*ca*complex(0,1)*lam3*sa**3 - 3*ca*complex(0,1)*lam4*sa**3 - 3*ca*complex(0,1)*lam5*sa**3',
                 order = {'QED':2})

GC_140 = Coupling(name = 'GC_140',
                  value = '-(yb/cmath.sqrt(2))',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '-((ca*complex(0,1)*yb)/(cb*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '(complex(0,1)*sa*yb)/(cb*cmath.sqrt(2))',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '(sb*yb)/(cb*cmath.sqrt(2))',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = 'yt/cmath.sqrt(2)',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '-((ca*complex(0,1)*yt)/(sb*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '(cb*yt)/(sb*cmath.sqrt(2))',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((complex(0,1)*sa*yt)/(sb*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '-(complex(0,1)*ytau)',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '-(ytau/cmath.sqrt(2))',
                  order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '3*ca**3*complex(0,1)*lam1*sa - 3*ca**3*complex(0,1)*lam3*sa - 3*ca**3*complex(0,1)*lam4*sa - 3*ca**3*complex(0,1)*lam5*sa - 3*ca*complex(0,1)*lam2*sa**3 + 3*ca*complex(0,1)*lam3*sa**3 + 3*ca*complex(0,1)*lam4*sa**3 + 3*ca*complex(0,1)*lam5*sa**3',
                 order = {'QED':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '-((ca*complex(0,1)*ytau)/(sb*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '-((cb*complex(0,1)*ytau)/sb)',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '-((cb*ytau)/(sb*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '-((complex(0,1)*sa*ytau)/(sb*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '-3*ca**4*complex(0,1)*lam2 - 6*ca**2*complex(0,1)*lam3*sa**2 - 6*ca**2*complex(0,1)*lam4*sa**2 - 6*ca**2*complex(0,1)*lam5*sa**2 - 3*complex(0,1)*lam1*sa**4',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '-3*ca**4*complex(0,1)*lam1 - 6*ca**2*complex(0,1)*lam3*sa**2 - 6*ca**2*complex(0,1)*lam4*sa**2 - 6*ca**2*complex(0,1)*lam5*sa**2 - 3*complex(0,1)*lam2*sa**4',
                 order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '-(ca**4*complex(0,1)*lam3) - ca**4*complex(0,1)*lam4 - ca**4*complex(0,1)*lam5 - 3*ca**2*complex(0,1)*lam1*sa**2 - 3*ca**2*complex(0,1)*lam2*sa**2 + 4*ca**2*complex(0,1)*lam3*sa**2 + 4*ca**2*complex(0,1)*lam4*sa**2 + 4*ca**2*complex(0,1)*lam5*sa**2 - complex(0,1)*lam3*sa**4 - complex(0,1)*lam4*sa**4 - complex(0,1)*lam5*sa**4',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(cb*complex(0,1)*I2a33)/sb',
                 order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '(cb*complex(0,1)*I3a33)/sb',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(complex(0,1)*I1a33*sb)/cb',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(complex(0,1)*I4a33*sb)/cb',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '(cb*ee**2*complex(0,1)*sa)/(2.*cw) - (ca*ee**2*complex(0,1)*sb)/(2.*cw)',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '-(cb*ee**2*complex(0,1)*sa)/(2.*cw) + (ca*ee**2*complex(0,1)*sb)/(2.*cw)',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(ca*cb*ee**2*complex(0,1))/(2.*cw) - (ee**2*complex(0,1)*sa*sb)/(2.*cw)',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '-(cb**2*ee*complex(0,1)) - ee*complex(0,1)*sb**2',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '2*cb**2*ee**2*complex(0,1) + 2*ee**2*complex(0,1)*sb**2',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '-(cb**2*ee**2)/(2.*cw) - (ee**2*sb**2)/(2.*cw)',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(cb**2*ee**2)/(2.*cw) + (ee**2*sb**2)/(2.*cw)',
                 order = {'QED':2})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-(ca*cb**2*complex(0,1)*lam2*sa) + ca*cb**2*complex(0,1)*lam3*sa + ca**2*cb*complex(0,1)*lam4*sb + ca**2*cb*complex(0,1)*lam5*sb - cb*complex(0,1)*lam4*sa**2*sb - cb*complex(0,1)*lam5*sa**2*sb + ca*complex(0,1)*lam1*sa*sb**2 - ca*complex(0,1)*lam3*sa*sb**2',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = 'ca*cb**2*complex(0,1)*lam1*sa - ca*cb**2*complex(0,1)*lam3*sa - ca**2*cb*complex(0,1)*lam4*sb - ca**2*cb*complex(0,1)*lam5*sb + cb*complex(0,1)*lam4*sa**2*sb + cb*complex(0,1)*lam5*sa**2*sb - ca*complex(0,1)*lam2*sa*sb**2 + ca*complex(0,1)*lam3*sa*sb**2',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = 'ca*cb**2*complex(0,1)*lam4*sa + ca*cb**2*complex(0,1)*lam5*sa - ca**2*cb*complex(0,1)*lam2*sb + ca**2*cb*complex(0,1)*lam3*sb + cb*complex(0,1)*lam1*sa**2*sb - cb*complex(0,1)*lam3*sa**2*sb - ca*complex(0,1)*lam4*sa*sb**2 - ca*complex(0,1)*lam5*sa*sb**2',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = 'ca*cb**2*complex(0,1)*lam1*sa - ca*cb**2*complex(0,1)*lam3*sa - ca*cb**2*complex(0,1)*lam4*sa + ca*cb**2*complex(0,1)*lam5*sa - 2*ca**2*cb*complex(0,1)*lam5*sb + 2*cb*complex(0,1)*lam5*sa**2*sb - ca*complex(0,1)*lam2*sa*sb**2 + ca*complex(0,1)*lam3*sa*sb**2 + ca*complex(0,1)*lam4*sa*sb**2 - ca*complex(0,1)*lam5*sa*sb**2',
                 order = {'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '-(ca*cb**2*complex(0,1)*lam2*sa) + ca*cb**2*complex(0,1)*lam3*sa + ca*cb**2*complex(0,1)*lam4*sa - ca*cb**2*complex(0,1)*lam5*sa + 2*ca**2*cb*complex(0,1)*lam5*sb - 2*cb*complex(0,1)*lam5*sa**2*sb + ca*complex(0,1)*lam1*sa*sb**2 - ca*complex(0,1)*lam3*sa*sb**2 - ca*complex(0,1)*lam4*sa*sb**2 + ca*complex(0,1)*lam5*sa*sb**2',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '-(ca*cb**2*complex(0,1)*lam4*sa) - ca*cb**2*complex(0,1)*lam5*sa + ca**2*cb*complex(0,1)*lam1*sb - ca**2*cb*complex(0,1)*lam3*sb - cb*complex(0,1)*lam2*sa**2*sb + cb*complex(0,1)*lam3*sa**2*sb + ca*complex(0,1)*lam4*sa*sb**2 + ca*complex(0,1)*lam5*sa*sb**2',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '2*ca*cb**2*complex(0,1)*lam5*sa - ca**2*cb*complex(0,1)*lam2*sb + ca**2*cb*complex(0,1)*lam3*sb + ca**2*cb*complex(0,1)*lam4*sb - ca**2*cb*complex(0,1)*lam5*sb + cb*complex(0,1)*lam1*sa**2*sb - cb*complex(0,1)*lam3*sa**2*sb - cb*complex(0,1)*lam4*sa**2*sb + cb*complex(0,1)*lam5*sa**2*sb - 2*ca*complex(0,1)*lam5*sa*sb**2',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '-2*ca*cb**2*complex(0,1)*lam5*sa + ca**2*cb*complex(0,1)*lam1*sb - ca**2*cb*complex(0,1)*lam3*sb - ca**2*cb*complex(0,1)*lam4*sb + ca**2*cb*complex(0,1)*lam5*sb - cb*complex(0,1)*lam2*sa**2*sb + cb*complex(0,1)*lam3*sa**2*sb + cb*complex(0,1)*lam4*sa**2*sb - cb*complex(0,1)*lam5*sa**2*sb + 2*ca*complex(0,1)*lam5*sa*sb**2',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '-(ca**2*cb**2*complex(0,1)*lam2) - cb**2*complex(0,1)*lam3*sa**2 - 2*ca*cb*complex(0,1)*lam4*sa*sb - 2*ca*cb*complex(0,1)*lam5*sa*sb - ca**2*complex(0,1)*lam3*sb**2 - complex(0,1)*lam1*sa**2*sb**2',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '-(ca**2*cb**2*complex(0,1)*lam2) - cb**2*complex(0,1)*lam3*sa**2 - cb**2*complex(0,1)*lam4*sa**2 + cb**2*complex(0,1)*lam5*sa**2 - 4*ca*cb*complex(0,1)*lam5*sa*sb - ca**2*complex(0,1)*lam3*sb**2 - ca**2*complex(0,1)*lam4*sb**2 + ca**2*complex(0,1)*lam5*sb**2 - complex(0,1)*lam1*sa**2*sb**2',
                 order = {'QED':2})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-(ca**2*cb**2*complex(0,1)*lam1) - cb**2*complex(0,1)*lam3*sa**2 - 2*ca*cb*complex(0,1)*lam4*sa*sb - 2*ca*cb*complex(0,1)*lam5*sa*sb - ca**2*complex(0,1)*lam3*sb**2 - complex(0,1)*lam2*sa**2*sb**2',
                 order = {'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '-(ca**2*cb**2*complex(0,1)*lam1) - cb**2*complex(0,1)*lam3*sa**2 - cb**2*complex(0,1)*lam4*sa**2 + cb**2*complex(0,1)*lam5*sa**2 - 4*ca*cb*complex(0,1)*lam5*sa*sb - ca**2*complex(0,1)*lam3*sb**2 - ca**2*complex(0,1)*lam4*sb**2 + ca**2*complex(0,1)*lam5*sb**2 - complex(0,1)*lam2*sa**2*sb**2',
                 order = {'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '-(ca**2*cb**2*complex(0,1)*lam3) - cb**2*complex(0,1)*lam2*sa**2 + 2*ca*cb*complex(0,1)*lam4*sa*sb + 2*ca*cb*complex(0,1)*lam5*sa*sb - ca**2*complex(0,1)*lam1*sb**2 - complex(0,1)*lam3*sa**2*sb**2',
                 order = {'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '-(ca**2*cb**2*complex(0,1)*lam3) - cb**2*complex(0,1)*lam1*sa**2 + 2*ca*cb*complex(0,1)*lam4*sa*sb + 2*ca*cb*complex(0,1)*lam5*sa*sb - ca**2*complex(0,1)*lam2*sb**2 - complex(0,1)*lam3*sa**2*sb**2',
                 order = {'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '-(ca**2*cb**2*complex(0,1)*lam4)/2. - (ca**2*cb**2*complex(0,1)*lam5)/2. + (cb**2*complex(0,1)*lam4*sa**2)/2. + (cb**2*complex(0,1)*lam5*sa**2)/2. - ca*cb*complex(0,1)*lam1*sa*sb - ca*cb*complex(0,1)*lam2*sa*sb + 2*ca*cb*complex(0,1)*lam3*sa*sb + (ca**2*complex(0,1)*lam4*sb**2)/2. + (ca**2*complex(0,1)*lam5*sb**2)/2. - (complex(0,1)*lam4*sa**2*sb**2)/2. - (complex(0,1)*lam5*sa**2*sb**2)/2.',
                 order = {'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '-(ca**2*cb**2*complex(0,1)*lam5) + cb**2*complex(0,1)*lam5*sa**2 - ca*cb*complex(0,1)*lam1*sa*sb - ca*cb*complex(0,1)*lam2*sa*sb + 2*ca*cb*complex(0,1)*lam3*sa*sb + 2*ca*cb*complex(0,1)*lam4*sa*sb - 2*ca*cb*complex(0,1)*lam5*sa*sb + ca**2*complex(0,1)*lam5*sb**2 - complex(0,1)*lam5*sa**2*sb**2',
                 order = {'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '-(ca**2*cb**2*complex(0,1)*lam3) - ca**2*cb**2*complex(0,1)*lam4 + ca**2*cb**2*complex(0,1)*lam5 - cb**2*complex(0,1)*lam2*sa**2 + 4*ca*cb*complex(0,1)*lam5*sa*sb - ca**2*complex(0,1)*lam1*sb**2 - complex(0,1)*lam3*sa**2*sb**2 - complex(0,1)*lam4*sa**2*sb**2 + complex(0,1)*lam5*sa**2*sb**2',
                 order = {'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(ca**2*cb**2*complex(0,1)*lam3) - ca**2*cb**2*complex(0,1)*lam4 + ca**2*cb**2*complex(0,1)*lam5 - cb**2*complex(0,1)*lam1*sa**2 + 4*ca*cb*complex(0,1)*lam5*sa*sb - ca**2*complex(0,1)*lam2*sb**2 - complex(0,1)*lam3*sa**2*sb**2 - complex(0,1)*lam4*sa**2*sb**2 + complex(0,1)*lam5*sa**2*sb**2',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '-(cb**3*lam4*sa)/2. + (cb**3*lam5*sa)/2. + (ca*cb**2*lam4*sb)/2. - (ca*cb**2*lam5*sb)/2. - (cb*lam4*sa*sb**2)/2. + (cb*lam5*sa*sb**2)/2. + (ca*lam4*sb**3)/2. - (ca*lam5*sb**3)/2.',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '(cb**3*lam4*sa)/2. - (cb**3*lam5*sa)/2. - (ca*cb**2*lam4*sb)/2. + (ca*cb**2*lam5*sb)/2. + (cb*lam4*sa*sb**2)/2. - (cb*lam5*sa*sb**2)/2. - (ca*lam4*sb**3)/2. + (ca*lam5*sb**3)/2.',
                 order = {'QED':2})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '-(cb**3*complex(0,1)*lam2*sb) + cb**3*complex(0,1)*lam3*sb + cb**3*complex(0,1)*lam4*sb + cb**3*complex(0,1)*lam5*sb + cb*complex(0,1)*lam1*sb**3 - cb*complex(0,1)*lam3*sb**3 - cb*complex(0,1)*lam4*sb**3 - cb*complex(0,1)*lam5*sb**3',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = 'cb**3*complex(0,1)*lam1*sb - cb**3*complex(0,1)*lam3*sb - cb**3*complex(0,1)*lam4*sb - cb**3*complex(0,1)*lam5*sb - cb*complex(0,1)*lam2*sb**3 + cb*complex(0,1)*lam3*sb**3 + cb*complex(0,1)*lam4*sb**3 + cb*complex(0,1)*lam5*sb**3',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-2*cb**3*complex(0,1)*lam2*sb + 2*cb**3*complex(0,1)*lam3*sb + 2*cb**3*complex(0,1)*lam4*sb + 2*cb**3*complex(0,1)*lam5*sb + 2*cb*complex(0,1)*lam1*sb**3 - 2*cb*complex(0,1)*lam3*sb**3 - 2*cb*complex(0,1)*lam4*sb**3 - 2*cb*complex(0,1)*lam5*sb**3',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '2*cb**3*complex(0,1)*lam1*sb - 2*cb**3*complex(0,1)*lam3*sb - 2*cb**3*complex(0,1)*lam4*sb - 2*cb**3*complex(0,1)*lam5*sb - 2*cb*complex(0,1)*lam2*sb**3 + 2*cb*complex(0,1)*lam3*sb**3 + 2*cb*complex(0,1)*lam4*sb**3 + 2*cb*complex(0,1)*lam5*sb**3',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-3*cb**3*complex(0,1)*lam2*sb + 3*cb**3*complex(0,1)*lam3*sb + 3*cb**3*complex(0,1)*lam4*sb + 3*cb**3*complex(0,1)*lam5*sb + 3*cb*complex(0,1)*lam1*sb**3 - 3*cb*complex(0,1)*lam3*sb**3 - 3*cb*complex(0,1)*lam4*sb**3 - 3*cb*complex(0,1)*lam5*sb**3',
                 order = {'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '3*cb**3*complex(0,1)*lam1*sb - 3*cb**3*complex(0,1)*lam3*sb - 3*cb**3*complex(0,1)*lam4*sb - 3*cb**3*complex(0,1)*lam5*sb - 3*cb*complex(0,1)*lam2*sb**3 + 3*cb*complex(0,1)*lam3*sb**3 + 3*cb*complex(0,1)*lam4*sb**3 + 3*cb*complex(0,1)*lam5*sb**3',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '(ca*cb**3*lam4)/2. - (ca*cb**3*lam5)/2. + (cb**2*lam4*sa*sb)/2. - (cb**2*lam5*sa*sb)/2. + (ca*cb*lam4*sb**2)/2. - (ca*cb*lam5*sb**2)/2. + (lam4*sa*sb**3)/2. - (lam5*sa*sb**3)/2.',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '-(ca*cb**3*lam4)/2. + (ca*cb**3*lam5)/2. - (cb**2*lam4*sa*sb)/2. + (cb**2*lam5*sa*sb)/2. - (ca*cb*lam4*sb**2)/2. + (ca*cb*lam5*sb**2)/2. - (lam4*sa*sb**3)/2. + (lam5*sa*sb**3)/2.',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '-(cb**4*complex(0,1)*lam2) - 2*cb**2*complex(0,1)*lam3*sb**2 - 2*cb**2*complex(0,1)*lam4*sb**2 - 2*cb**2*complex(0,1)*lam5*sb**2 - complex(0,1)*lam1*sb**4',
                 order = {'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '-2*cb**4*complex(0,1)*lam2 - 4*cb**2*complex(0,1)*lam3*sb**2 - 4*cb**2*complex(0,1)*lam4*sb**2 - 4*cb**2*complex(0,1)*lam5*sb**2 - 2*complex(0,1)*lam1*sb**4',
                 order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '-3*cb**4*complex(0,1)*lam2 - 6*cb**2*complex(0,1)*lam3*sb**2 - 6*cb**2*complex(0,1)*lam4*sb**2 - 6*cb**2*complex(0,1)*lam5*sb**2 - 3*complex(0,1)*lam1*sb**4',
                 order = {'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(cb**4*complex(0,1)*lam1) - 2*cb**2*complex(0,1)*lam3*sb**2 - 2*cb**2*complex(0,1)*lam4*sb**2 - 2*cb**2*complex(0,1)*lam5*sb**2 - complex(0,1)*lam2*sb**4',
                 order = {'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '-2*cb**4*complex(0,1)*lam1 - 4*cb**2*complex(0,1)*lam3*sb**2 - 4*cb**2*complex(0,1)*lam4*sb**2 - 4*cb**2*complex(0,1)*lam5*sb**2 - 2*complex(0,1)*lam2*sb**4',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '-3*cb**4*complex(0,1)*lam1 - 6*cb**2*complex(0,1)*lam3*sb**2 - 6*cb**2*complex(0,1)*lam4*sb**2 - 6*cb**2*complex(0,1)*lam5*sb**2 - 3*complex(0,1)*lam2*sb**4',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '-(cb**4*complex(0,1)*lam3) - cb**2*complex(0,1)*lam1*sb**2 - cb**2*complex(0,1)*lam2*sb**2 + 2*cb**2*complex(0,1)*lam4*sb**2 + 2*cb**2*complex(0,1)*lam5*sb**2 - complex(0,1)*lam3*sb**4',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '-(cb**4*complex(0,1)*lam3) - cb**4*complex(0,1)*lam4 - 2*cb**2*complex(0,1)*lam1*sb**2 - 2*cb**2*complex(0,1)*lam2*sb**2 + 2*cb**2*complex(0,1)*lam3*sb**2 + 2*cb**2*complex(0,1)*lam4*sb**2 + 4*cb**2*complex(0,1)*lam5*sb**2 - complex(0,1)*lam3*sb**4 - complex(0,1)*lam4*sb**4',
                 order = {'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = '-(cb**4*complex(0,1)*lam4)/2. - (cb**4*complex(0,1)*lam5)/2. - cb**2*complex(0,1)*lam1*sb**2 - cb**2*complex(0,1)*lam2*sb**2 + 2*cb**2*complex(0,1)*lam3*sb**2 + cb**2*complex(0,1)*lam4*sb**2 + cb**2*complex(0,1)*lam5*sb**2 - (complex(0,1)*lam4*sb**4)/2. - (complex(0,1)*lam5*sb**4)/2.',
                 order = {'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(cb**4*complex(0,1)*lam3) - cb**4*complex(0,1)*lam4 - cb**4*complex(0,1)*lam5 - 3*cb**2*complex(0,1)*lam1*sb**2 - 3*cb**2*complex(0,1)*lam2*sb**2 + 4*cb**2*complex(0,1)*lam3*sb**2 + 4*cb**2*complex(0,1)*lam4*sb**2 + 4*cb**2*complex(0,1)*lam5*sb**2 - complex(0,1)*lam3*sb**4 - complex(0,1)*lam4*sb**4 - complex(0,1)*lam5*sb**4',
                 order = {'QED':2})

GC_68 = Coupling(name = 'GC_68',
                 value = '-2*cb**4*complex(0,1)*lam5 - 2*cb**2*complex(0,1)*lam1*sb**2 - 2*cb**2*complex(0,1)*lam2*sb**2 + 4*cb**2*complex(0,1)*lam3*sb**2 + 4*cb**2*complex(0,1)*lam4*sb**2 - 2*complex(0,1)*lam5*sb**4',
                 order = {'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '(ca**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sa**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '-G',
                order = {'QCD':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '(cb**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sb**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '(cb*ee*complex(0,1)*sa)/(2.*sw) - (ca*ee*complex(0,1)*sb)/(2.*sw)',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '-(cb*ee*complex(0,1)*sa)/(2.*sw) + (ca*ee*complex(0,1)*sb)/(2.*sw)',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(cb*ee**2*complex(0,1)*sa)/(2.*sw) - (ca*ee**2*complex(0,1)*sb)/(2.*sw)',
                 order = {'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(cb*ee**2*complex(0,1)*sa)/(2.*sw) + (ca*ee**2*complex(0,1)*sb)/(2.*sw)',
                 order = {'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '-(ca*cb*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sa*sb)/(2.*sw)',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '(ca*cb*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sa*sb)/(2.*sw)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '(ca*cb*ee**2*complex(0,1))/(2.*sw) + (ee**2*complex(0,1)*sa*sb)/(2.*sw)',
                 order = {'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '-(cb**2*ee)/(2.*sw) - (ee*sb**2)/(2.*sw)',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '(cb**2*ee)/(2.*sw) + (ee*sb**2)/(2.*sw)',
                 order = {'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(cb**2*ee**2)/(2.*sw) - (ee**2*sb**2)/(2.*sw)',
                 order = {'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '(cb**2*ee**2)/(2.*sw) + (ee**2*sb**2)/(2.*sw)',
                 order = {'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '(2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '(-2*cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_9 = Coupling(name = 'GC_9',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '-((cw*ee*complex(0,1))/sw)',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '(cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_95 = Coupling(name = 'GC_95',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

