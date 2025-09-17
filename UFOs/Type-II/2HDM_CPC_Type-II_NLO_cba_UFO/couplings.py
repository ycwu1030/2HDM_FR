# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.1 for Mac OS X ARM (64-bit) (January 28, 2022)
# Date: Fri 8 Jul 2022 20:52:02


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(complex(0,1)*I1a33)',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(-2*cb**4*cba**2*complex(0,1)*MHA**2)/vev**2 - (cb**4*cba**4*complex(0,1)*MHH**2)/vev**2 - (cb**2*cba**2*complex(0,1)*MHL**2)/vev**2 + (cb**4*cba**4*complex(0,1)*MHL**2)/vev**2 + (2*cb**3*cba**2*complex(0,1)*m122)/(sb*vev**2) + (4*cb*cba**2*complex(0,1)*m122*sb)/vev**2 - (4*cb**2*cba**2*complex(0,1)*MHA**2*sb**2)/vev**2 - (cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 - (cb**2*cba**4*complex(0,1)*MHH**2*sb**2)/vev**2 + (cb**2*cba**4*complex(0,1)*MHL**2*sb**2)/vev**2 + (2*cba**2*complex(0,1)*m122*sb**3)/(cb*vev**2) - (2*cba**2*complex(0,1)*MHA**2*sb**4)/vev**2 - (2*cb**2*cba*complex(0,1)*m122*sba)/vev**2 - (2*cb**4*cba*complex(0,1)*m122*sba)/(sb**2*vev**2) + (cb**5*cba**3*complex(0,1)*MHH**2*sba)/(sb*vev**2) + (2*cb**3*cba*complex(0,1)*MHL**2*sba)/(sb*vev**2) - (cb**5*cba**3*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (cb**3*cba**3*complex(0,1)*MHH**2*sb*sba)/vev**2 - (cb**3*cba**3*complex(0,1)*MHL**2*sb*sba)/vev**2 + (2*cba*complex(0,1)*m122*sb**2*sba)/vev**2 - (2*cba*complex(0,1)*MHH**2*sb**3*sba)/(cb*vev**2) + (cb*cba**3*complex(0,1)*MHH**2*sb**3*sba)/vev**2 - (cb*cba**3*complex(0,1)*MHL**2*sb**3*sba)/vev**2 + (2*cba*complex(0,1)*m122*sb**4*sba)/(cb**2*vev**2) + (cba**3*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) - (cba**3*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) - (3*cb**4*cba**2*complex(0,1)*MHH**2*sba**2)/vev**2 + (3*cb**4*cba**2*complex(0,1)*MHL**2*sba**2)/vev**2 + (cb**5*complex(0,1)*m122*sba**2)/(sb**3*vev**2) - (cb**4*complex(0,1)*MHL**2*sba**2)/(sb**2*vev**2) - (2*cb*complex(0,1)*m122*sb*sba**2)/vev**2 - (5*cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 + (5*cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 - (complex(0,1)*MHH**2*sb**4*sba**2)/(cb**2*vev**2) - (cba**2*complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 + (cba**2*complex(0,1)*MHL**2*sb**4*sba**2)/vev**2 + (complex(0,1)*m122*sb**5*sba**2)/(cb**3*vev**2) + (cba**2*complex(0,1)*MHH**2*sb**6*sba**2)/(cb**2*vev**2) - (cba**2*complex(0,1)*MHL**2*sb**6*sba**2)/(cb**2*vev**2) + (4*cb**5*cba*complex(0,1)*MHH**2*sba**3)/(sb*vev**2) - (4*cb**5*cba*complex(0,1)*MHL**2*sba**3)/(sb*vev**2) + (4*cb**3*cba*complex(0,1)*MHH**2*sb*sba**3)/vev**2 - (4*cb**3*cba*complex(0,1)*MHL**2*sb*sba**3)/vev**2 - (2*cb*cba*complex(0,1)*MHH**2*sb**3*sba**3)/vev**2 + (2*cb*cba*complex(0,1)*MHL**2*sb**3*sba**3)/vev**2 - (2*cba*complex(0,1)*MHH**2*sb**5*sba**3)/(cb*vev**2) + (2*cba*complex(0,1)*MHL**2*sb**5*sba**3)/(cb*vev**2) - (cb**6*complex(0,1)*MHH**2*sba**4)/(sb**2*vev**2) + (cb**6*complex(0,1)*MHL**2*sba**4)/(sb**2*vev**2) + (2*cb**2*complex(0,1)*MHH**2*sb**2*sba**4)/vev**2 - (2*cb**2*complex(0,1)*MHL**2*sb**2*sba**4)/vev**2 + (complex(0,1)*MHH**2*sb**4*sba**4)/vev**2 - (complex(0,1)*MHL**2*sb**4*sba**4)/vev**2',
                  order = {'QED':2})

GC_101 = Coupling(name = 'GC_101',
                  value = '-((cb**4*cba**4*complex(0,1)*MHH**2)/vev**2) - (cb**2*cba**2*complex(0,1)*MHL**2)/vev**2 + (cb**4*cba**4*complex(0,1)*MHL**2)/vev**2 - (2*cb**4*cba**2*complex(0,1)*MHp**2)/vev**2 + (2*cb**3*cba**2*complex(0,1)*m122)/(sb*vev**2) + (4*cb*cba**2*complex(0,1)*m122*sb)/vev**2 - (cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 - (cb**2*cba**4*complex(0,1)*MHH**2*sb**2)/vev**2 + (cb**2*cba**4*complex(0,1)*MHL**2*sb**2)/vev**2 - (4*cb**2*cba**2*complex(0,1)*MHp**2*sb**2)/vev**2 + (2*cba**2*complex(0,1)*m122*sb**3)/(cb*vev**2) - (2*cba**2*complex(0,1)*MHp**2*sb**4)/vev**2 - (2*cb**2*cba*complex(0,1)*m122*sba)/vev**2 - (2*cb**4*cba*complex(0,1)*m122*sba)/(sb**2*vev**2) + (cb**5*cba**3*complex(0,1)*MHH**2*sba)/(sb*vev**2) + (2*cb**3*cba*complex(0,1)*MHL**2*sba)/(sb*vev**2) - (cb**5*cba**3*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (cb**3*cba**3*complex(0,1)*MHH**2*sb*sba)/vev**2 - (cb**3*cba**3*complex(0,1)*MHL**2*sb*sba)/vev**2 + (2*cba*complex(0,1)*m122*sb**2*sba)/vev**2 - (2*cba*complex(0,1)*MHH**2*sb**3*sba)/(cb*vev**2) + (cb*cba**3*complex(0,1)*MHH**2*sb**3*sba)/vev**2 - (cb*cba**3*complex(0,1)*MHL**2*sb**3*sba)/vev**2 + (2*cba*complex(0,1)*m122*sb**4*sba)/(cb**2*vev**2) + (cba**3*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) - (cba**3*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) - (3*cb**4*cba**2*complex(0,1)*MHH**2*sba**2)/vev**2 + (3*cb**4*cba**2*complex(0,1)*MHL**2*sba**2)/vev**2 + (cb**5*complex(0,1)*m122*sba**2)/(sb**3*vev**2) - (cb**4*complex(0,1)*MHL**2*sba**2)/(sb**2*vev**2) - (2*cb*complex(0,1)*m122*sb*sba**2)/vev**2 - (5*cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 + (5*cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 - (complex(0,1)*MHH**2*sb**4*sba**2)/(cb**2*vev**2) - (cba**2*complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 + (cba**2*complex(0,1)*MHL**2*sb**4*sba**2)/vev**2 + (complex(0,1)*m122*sb**5*sba**2)/(cb**3*vev**2) + (cba**2*complex(0,1)*MHH**2*sb**6*sba**2)/(cb**2*vev**2) - (cba**2*complex(0,1)*MHL**2*sb**6*sba**2)/(cb**2*vev**2) + (4*cb**5*cba*complex(0,1)*MHH**2*sba**3)/(sb*vev**2) - (4*cb**5*cba*complex(0,1)*MHL**2*sba**3)/(sb*vev**2) + (4*cb**3*cba*complex(0,1)*MHH**2*sb*sba**3)/vev**2 - (4*cb**3*cba*complex(0,1)*MHL**2*sb*sba**3)/vev**2 - (2*cb*cba*complex(0,1)*MHH**2*sb**3*sba**3)/vev**2 + (2*cb*cba*complex(0,1)*MHL**2*sb**3*sba**3)/vev**2 - (2*cba*complex(0,1)*MHH**2*sb**5*sba**3)/(cb*vev**2) + (2*cba*complex(0,1)*MHL**2*sb**5*sba**3)/(cb*vev**2) - (cb**6*complex(0,1)*MHH**2*sba**4)/(sb**2*vev**2) + (cb**6*complex(0,1)*MHL**2*sba**4)/(sb**2*vev**2) + (2*cb**2*complex(0,1)*MHH**2*sb**2*sba**4)/vev**2 - (2*cb**2*complex(0,1)*MHL**2*sb**2*sba**4)/vev**2 + (complex(0,1)*MHH**2*sb**4*sba**4)/vev**2 - (complex(0,1)*MHL**2*sb**4*sba**4)/vev**2',
                  order = {'QED':2})

GC_102 = Coupling(name = 'GC_102',
                  value = '(3*cb*cba**4*complex(0,1)*MHH**2*sb)/vev**2 - (3*cb**3*cba**6*complex(0,1)*MHH**2*sb)/vev**2 - (3*cb*cba**4*complex(0,1)*MHL**2*sb)/vev**2 + (3*cb**3*cba**6*complex(0,1)*MHL**2*sb)/vev**2 - (3*cb*cba**6*complex(0,1)*MHH**2*sb**3)/vev**2 + (3*cb*cba**6*complex(0,1)*MHL**2*sb**3)/vev**2 - (3*cb**2*cba**3*complex(0,1)*MHH**2*sba)/vev**2 + (6*cb**4*cba**5*complex(0,1)*MHH**2*sba)/vev**2 + (9*cb**2*cba**3*complex(0,1)*MHL**2*sba)/vev**2 - (6*cb**4*cba**5*complex(0,1)*MHL**2*sba)/vev**2 - (6*cb**3*cba**3*complex(0,1)*m122*sba)/(sb*vev**2) - (12*cb*cba**3*complex(0,1)*m122*sb*sba)/vev**2 + (9*cba**3*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (3*cba**3*complex(0,1)*MHL**2*sb**2*sba)/vev**2 - (6*cba**3*complex(0,1)*m122*sb**3*sba)/(cb*vev**2) - (6*cba**5*complex(0,1)*MHH**2*sb**4*sba)/vev**2 + (6*cba**5*complex(0,1)*MHL**2*sb**4*sba)/vev**2 + (9*cb**2*cba**2*complex(0,1)*m122*sba**2)/vev**2 + (9*cb**4*cba**2*complex(0,1)*m122*sba**2)/(sb**2*vev**2) - (3*cb**5*cba**4*complex(0,1)*MHH**2*sba**2)/(sb*vev**2) - (9*cb**3*cba**2*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) + (3*cb**5*cba**4*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) - (9*cb*cba**2*complex(0,1)*MHH**2*sb*sba**2)/vev**2 + (3*cb**3*cba**4*complex(0,1)*MHH**2*sb*sba**2)/vev**2 + (9*cb*cba**2*complex(0,1)*MHL**2*sb*sba**2)/vev**2 - (3*cb**3*cba**4*complex(0,1)*MHL**2*sb*sba**2)/vev**2 - (9*cba**2*complex(0,1)*m122*sb**2*sba**2)/vev**2 + (9*cba**2*complex(0,1)*MHH**2*sb**3*sba**2)/(cb*vev**2) - (9*cba**2*complex(0,1)*m122*sb**4*sba**2)/(cb**2*vev**2) - (6*cba**4*complex(0,1)*MHH**2*sb**5*sba**2)/(cb*vev**2) + (6*cba**4*complex(0,1)*MHL**2*sb**5*sba**2)/(cb*vev**2) + (9*cb**4*cba**3*complex(0,1)*MHH**2*sba**3)/vev**2 - (9*cb**2*cba*complex(0,1)*MHL**2*sba**3)/vev**2 - (9*cb**4*cba**3*complex(0,1)*MHL**2*sba**3)/vev**2 - (3*cb**5*cba*complex(0,1)*m122*sba**3)/(sb**3*vev**2) + (3*cb**4*cba*complex(0,1)*MHL**2*sba**3)/(sb**2*vev**2) + (6*cb**3*cba*complex(0,1)*m122*sba**3)/(sb*vev**2) + (18*cb*cba*complex(0,1)*m122*sb*sba**3)/vev**2 - (9*cba*complex(0,1)*MHH**2*sb**2*sba**3)/vev**2 + (15*cb**2*cba**3*complex(0,1)*MHH**2*sb**2*sba**3)/vev**2 - (15*cb**2*cba**3*complex(0,1)*MHL**2*sb**2*sba**3)/vev**2 + (6*cba*complex(0,1)*m122*sb**3*sba**3)/(cb*vev**2) + (3*cba*complex(0,1)*MHH**2*sb**4*sba**3)/(cb**2*vev**2) + (3*cba**3*complex(0,1)*MHH**2*sb**4*sba**3)/vev**2 - (3*cba**3*complex(0,1)*MHL**2*sb**4*sba**3)/vev**2 - (3*cba*complex(0,1)*m122*sb**5*sba**3)/(cb**3*vev**2) - (3*cba**3*complex(0,1)*MHH**2*sb**6*sba**3)/(cb**2*vev**2) + (3*cba**3*complex(0,1)*MHL**2*sb**6*sba**3)/(cb**2*vev**2) - (3*cb**2*complex(0,1)*m122*sba**4)/vev**2 - (3*cb**4*complex(0,1)*m122*sba**4)/(sb**2*vev**2) - (12*cb**5*cba**2*complex(0,1)*MHH**2*sba**4)/(sb*vev**2) + (3*cb**3*complex(0,1)*MHL**2*sba**4)/(sb*vev**2) + (12*cb**5*cba**2*complex(0,1)*MHL**2*sba**4)/(sb*vev**2) - (3*cb**3*cba**2*complex(0,1)*MHH**2*sb*sba**4)/vev**2 + (3*cb**3*cba**2*complex(0,1)*MHL**2*sb*sba**4)/vev**2 + (3*complex(0,1)*m122*sb**2*sba**4)/vev**2 - (3*complex(0,1)*MHH**2*sb**3*sba**4)/(cb*vev**2) + (15*cb*cba**2*complex(0,1)*MHH**2*sb**3*sba**4)/vev**2 - (15*cb*cba**2*complex(0,1)*MHL**2*sb**3*sba**4)/vev**2 + (3*complex(0,1)*m122*sb**4*sba**4)/(cb**2*vev**2) + (6*cba**2*complex(0,1)*MHH**2*sb**5*sba**4)/(cb*vev**2) - (6*cba**2*complex(0,1)*MHL**2*sb**5*sba**4)/(cb*vev**2) - (9*cb**4*cba*complex(0,1)*MHH**2*sba**5)/vev**2 + (9*cb**4*cba*complex(0,1)*MHL**2*sba**5)/vev**2 + (3*cb**6*cba*complex(0,1)*MHH**2*sba**5)/(sb**2*vev**2) - (3*cb**6*cba*complex(0,1)*MHL**2*sba**5)/(sb**2*vev**2) - (15*cb**2*cba*complex(0,1)*MHH**2*sb**2*sba**5)/vev**2 + (15*cb**2*cba*complex(0,1)*MHL**2*sb**2*sba**5)/vev**2 - (3*cba*complex(0,1)*MHH**2*sb**4*sba**5)/vev**2 + (3*cba*complex(0,1)*MHL**2*sb**4*sba**5)/vev**2 + (3*cb**5*complex(0,1)*MHH**2*sba**6)/(sb*vev**2) - (3*cb**5*complex(0,1)*MHL**2*sba**6)/(sb*vev**2) + (3*cb**3*complex(0,1)*MHH**2*sb*sba**6)/vev**2 - (3*cb**3*complex(0,1)*MHL**2*sb*sba**6)/vev**2',
                  order = {'QED':2})

GC_103 = Coupling(name = 'GC_103',
                  value = '(-3*cb**4*cba**6*complex(0,1)*MHH**2)/vev**2 + (3*cb**4*cba**6*complex(0,1)*MHL**2)/vev**2 + (3*cb**5*cba**4*complex(0,1)*m122)/(sb**3*vev**2) - (3*cb**4*cba**4*complex(0,1)*MHL**2)/(sb**2*vev**2) - (6*cb*cba**4*complex(0,1)*m122*sb)/vev**2 - (6*cb**2*cba**6*complex(0,1)*MHH**2*sb**2)/vev**2 + (6*cb**2*cba**6*complex(0,1)*MHL**2*sb**2)/vev**2 - (3*cba**4*complex(0,1)*MHH**2*sb**4)/(cb**2*vev**2) + (3*cba**4*complex(0,1)*m122*sb**5)/(cb**3*vev**2) + (3*cba**6*complex(0,1)*MHH**2*sb**6)/(cb**2*vev**2) - (3*cba**6*complex(0,1)*MHL**2*sb**6)/(cb**2*vev**2) + (12*cb**2*cba**3*complex(0,1)*m122*sba)/vev**2 + (12*cb**4*cba**3*complex(0,1)*m122*sba)/(sb**2*vev**2) + (6*cb**5*cba**5*complex(0,1)*MHH**2*sba)/(sb*vev**2) - (12*cb**3*cba**3*complex(0,1)*MHL**2*sba)/(sb*vev**2) - (6*cb**5*cba**5*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (6*cb**3*cba**5*complex(0,1)*MHH**2*sb*sba)/vev**2 - (6*cb**3*cba**5*complex(0,1)*MHL**2*sb*sba)/vev**2 - (12*cba**3*complex(0,1)*m122*sb**2*sba)/vev**2 + (12*cba**3*complex(0,1)*MHH**2*sb**3*sba)/(cb*vev**2) - (18*cb*cba**5*complex(0,1)*MHH**2*sb**3*sba)/vev**2 + (18*cb*cba**5*complex(0,1)*MHL**2*sb**3*sba)/vev**2 - (12*cba**3*complex(0,1)*m122*sb**4*sba)/(cb**2*vev**2) - (18*cba**5*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) + (18*cba**5*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) + (6*cb**4*cba**4*complex(0,1)*MHH**2*sba**2)/vev**2 - (18*cb**2*cba**2*complex(0,1)*MHL**2*sba**2)/vev**2 - (6*cb**4*cba**4*complex(0,1)*MHL**2*sba**2)/vev**2 - (3*cb**6*cba**4*complex(0,1)*MHH**2*sba**2)/(sb**2*vev**2) + (3*cb**6*cba**4*complex(0,1)*MHL**2*sba**2)/(sb**2*vev**2) + (12*cb**3*cba**2*complex(0,1)*m122*sba**2)/(sb*vev**2) + (24*cb*cba**2*complex(0,1)*m122*sb*sba**2)/vev**2 - (18*cba**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 + (36*cb**2*cba**4*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (36*cb**2*cba**4*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 + (12*cba**2*complex(0,1)*m122*sb**3*sba**2)/(cb*vev**2) + (27*cba**4*complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 - (27*cba**4*complex(0,1)*MHL**2*sb**4*sba**2)/vev**2 - (6*cb**5*cba**3*complex(0,1)*MHH**2*sba**3)/(sb*vev**2) + (6*cb**5*cba**3*complex(0,1)*MHL**2*sba**3)/(sb*vev**2) + (12*cb*cba*complex(0,1)*MHH**2*sb*sba**3)/vev**2 - (18*cb**3*cba**3*complex(0,1)*MHH**2*sb*sba**3)/vev**2 - (12*cb*cba*complex(0,1)*MHL**2*sb*sba**3)/vev**2 + (18*cb**3*cba**3*complex(0,1)*MHL**2*sb*sba**3)/vev**2 - (18*cb*cba**3*complex(0,1)*MHH**2*sb**3*sba**3)/vev**2 + (18*cb*cba**3*complex(0,1)*MHL**2*sb**3*sba**3)/vev**2 - (6*cba**3*complex(0,1)*MHH**2*sb**5*sba**3)/(cb*vev**2) + (6*cba**3*complex(0,1)*MHL**2*sb**5*sba**3)/(cb*vev**2) - (3*cb**2*complex(0,1)*MHH**2*sba**4)/vev**2 + (15*cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba**4)/vev**2 - (3*complex(0,1)*MHL**2*sb**2*sba**4)/vev**2 - (15*cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba**4)/vev**2 + (15*cba**2*complex(0,1)*MHH**2*sb**4*sba**4)/vev**2 - (15*cba**2*complex(0,1)*MHL**2*sb**4*sba**4)/vev**2 - (12*cb**3*cba*complex(0,1)*MHH**2*sb*sba**5)/vev**2 + (12*cb**3*cba*complex(0,1)*MHL**2*sb*sba**5)/vev**2 - (12*cb*cba*complex(0,1)*MHH**2*sb**3*sba**5)/vev**2 + (12*cb*cba*complex(0,1)*MHL**2*sb**3*sba**5)/vev**2 + (3*cb**4*complex(0,1)*MHH**2*sba**6)/vev**2 - (3*cb**4*complex(0,1)*MHL**2*sba**6)/vev**2 + (3*cb**2*complex(0,1)*MHH**2*sb**2*sba**6)/vev**2 - (3*cb**2*complex(0,1)*MHL**2*sb**2*sba**6)/vev**2',
                  order = {'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '(3*cb**2*cba**4*complex(0,1)*m122)/vev**2 + (3*cb**4*cba**4*complex(0,1)*m122)/(sb**2*vev**2) - (3*cb**3*cba**4*complex(0,1)*MHL**2)/(sb*vev**2) - (3*cba**4*complex(0,1)*m122*sb**2)/vev**2 + (3*cba**4*complex(0,1)*MHH**2*sb**3)/(cb*vev**2) - (3*cb*cba**6*complex(0,1)*MHH**2*sb**3)/vev**2 + (3*cb*cba**6*complex(0,1)*MHL**2*sb**3)/vev**2 - (3*cba**4*complex(0,1)*m122*sb**4)/(cb**2*vev**2) - (3*cba**6*complex(0,1)*MHH**2*sb**5)/(cb*vev**2) + (3*cba**6*complex(0,1)*MHL**2*sb**5)/(cb*vev**2) + (3*cb**4*cba**5*complex(0,1)*MHH**2*sba)/vev**2 - (9*cb**2*cba**3*complex(0,1)*MHL**2*sba)/vev**2 - (3*cb**4*cba**5*complex(0,1)*MHL**2*sba)/vev**2 - (3*cb**5*cba**3*complex(0,1)*m122*sba)/(sb**3*vev**2) + (3*cb**4*cba**3*complex(0,1)*MHL**2*sba)/(sb**2*vev**2) + (6*cb**3*cba**3*complex(0,1)*m122*sba)/(sb*vev**2) + (18*cb*cba**3*complex(0,1)*m122*sb*sba)/vev**2 - (9*cba**3*complex(0,1)*MHH**2*sb**2*sba)/vev**2 + (15*cb**2*cba**5*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (15*cb**2*cba**5*complex(0,1)*MHL**2*sb**2*sba)/vev**2 + (6*cba**3*complex(0,1)*m122*sb**3*sba)/(cb*vev**2) + (3*cba**3*complex(0,1)*MHH**2*sb**4*sba)/(cb**2*vev**2) + (9*cba**5*complex(0,1)*MHH**2*sb**4*sba)/vev**2 - (9*cba**5*complex(0,1)*MHL**2*sb**4*sba)/vev**2 - (3*cba**3*complex(0,1)*m122*sb**5*sba)/(cb**3*vev**2) - (3*cba**5*complex(0,1)*MHH**2*sb**6*sba)/(cb**2*vev**2) + (3*cba**5*complex(0,1)*MHL**2*sb**6*sba)/(cb**2*vev**2) - (9*cb**2*cba**2*complex(0,1)*m122*sba**2)/vev**2 - (9*cb**4*cba**2*complex(0,1)*m122*sba**2)/(sb**2*vev**2) - (6*cb**5*cba**4*complex(0,1)*MHH**2*sba**2)/(sb*vev**2) + (9*cb**3*cba**2*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) + (6*cb**5*cba**4*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) + (9*cb*cba**2*complex(0,1)*MHH**2*sb*sba**2)/vev**2 - (15*cb**3*cba**4*complex(0,1)*MHH**2*sb*sba**2)/vev**2 - (9*cb*cba**2*complex(0,1)*MHL**2*sb*sba**2)/vev**2 + (15*cb**3*cba**4*complex(0,1)*MHL**2*sb*sba**2)/vev**2 + (9*cba**2*complex(0,1)*m122*sb**2*sba**2)/vev**2 - (9*cba**2*complex(0,1)*MHH**2*sb**3*sba**2)/(cb*vev**2) + (3*cb*cba**4*complex(0,1)*MHH**2*sb**3*sba**2)/vev**2 - (3*cb*cba**4*complex(0,1)*MHL**2*sb**3*sba**2)/vev**2 + (9*cba**2*complex(0,1)*m122*sb**4*sba**2)/(cb**2*vev**2) + (12*cba**4*complex(0,1)*MHH**2*sb**5*sba**2)/(cb*vev**2) - (12*cba**4*complex(0,1)*MHL**2*sb**5*sba**2)/(cb*vev**2) - (3*cb**2*cba*complex(0,1)*MHH**2*sba**3)/vev**2 - (3*cb**4*cba**3*complex(0,1)*MHH**2*sba**3)/vev**2 + (9*cb**2*cba*complex(0,1)*MHL**2*sba**3)/vev**2 + (3*cb**4*cba**3*complex(0,1)*MHL**2*sba**3)/vev**2 + (3*cb**6*cba**3*complex(0,1)*MHH**2*sba**3)/(sb**2*vev**2) - (3*cb**6*cba**3*complex(0,1)*MHL**2*sba**3)/(sb**2*vev**2) - (6*cb**3*cba*complex(0,1)*m122*sba**3)/(sb*vev**2) - (12*cb*cba*complex(0,1)*m122*sb*sba**3)/vev**2 + (9*cba*complex(0,1)*MHH**2*sb**2*sba**3)/vev**2 - (15*cb**2*cba**3*complex(0,1)*MHH**2*sb**2*sba**3)/vev**2 - (3*cba*complex(0,1)*MHL**2*sb**2*sba**3)/vev**2 + (15*cb**2*cba**3*complex(0,1)*MHL**2*sb**2*sba**3)/vev**2 - (6*cba*complex(0,1)*m122*sb**3*sba**3)/(cb*vev**2) - (9*cba**3*complex(0,1)*MHH**2*sb**4*sba**3)/vev**2 + (9*cba**3*complex(0,1)*MHL**2*sb**4*sba**3)/vev**2 + (6*cb**5*cba**2*complex(0,1)*MHH**2*sba**4)/(sb*vev**2) - (6*cb**5*cba**2*complex(0,1)*MHL**2*sba**4)/(sb*vev**2) - (3*cb*complex(0,1)*MHH**2*sb*sba**4)/vev**2 + (3*cb*complex(0,1)*MHL**2*sb*sba**4)/vev**2 - (3*cb*cba**2*complex(0,1)*MHH**2*sb**3*sba**4)/vev**2 + (3*cb*cba**2*complex(0,1)*MHL**2*sb**3*sba**4)/vev**2 + (3*cba**2*complex(0,1)*MHH**2*sb**5*sba**4)/(cb*vev**2) - (3*cba**2*complex(0,1)*MHL**2*sb**5*sba**4)/(cb*vev**2) + (6*cb**4*cba*complex(0,1)*MHH**2*sba**5)/vev**2 - (6*cb**4*cba*complex(0,1)*MHL**2*sba**5)/vev**2 - (6*cba*complex(0,1)*MHH**2*sb**4*sba**5)/vev**2 + (6*cba*complex(0,1)*MHL**2*sb**4*sba**5)/vev**2 + (3*cb**3*complex(0,1)*MHH**2*sb*sba**6)/vev**2 - (3*cb**3*complex(0,1)*MHL**2*sb*sba**6)/vev**2 + (3*cb*complex(0,1)*MHH**2*sb**3*sba**6)/vev**2 - (3*cb*complex(0,1)*MHL**2*sb**3*sba**6)/vev**2',
                  order = {'QED':2})

GC_105 = Coupling(name = 'GC_105',
                  value = '-((cb**4*cba**6*complex(0,1)*MHH**2)/vev**2) - (3*cb**2*cba**4*complex(0,1)*MHL**2)/vev**2 + (cb**4*cba**6*complex(0,1)*MHL**2)/vev**2 + (2*cb**3*cba**4*complex(0,1)*m122)/(sb*vev**2) + (4*cb*cba**4*complex(0,1)*m122*sb)/vev**2 - (3*cba**4*complex(0,1)*MHH**2*sb**2)/vev**2 + (cb**2*cba**6*complex(0,1)*MHH**2*sb**2)/vev**2 - (cb**2*cba**6*complex(0,1)*MHL**2*sb**2)/vev**2 + (2*cba**4*complex(0,1)*m122*sb**3)/(cb*vev**2) + (2*cba**6*complex(0,1)*MHH**2*sb**4)/vev**2 - (2*cba**6*complex(0,1)*MHL**2*sb**4)/vev**2 - (6*cb**2*cba**3*complex(0,1)*m122*sba)/vev**2 - (6*cb**4*cba**3*complex(0,1)*m122*sba)/(sb**2*vev**2) + (cb**5*cba**5*complex(0,1)*MHH**2*sba)/(sb*vev**2) + (6*cb**3*cba**3*complex(0,1)*MHL**2*sba)/(sb*vev**2) - (cb**5*cba**5*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (6*cb*cba**3*complex(0,1)*MHH**2*sb*sba)/vev**2 - (5*cb**3*cba**5*complex(0,1)*MHH**2*sb*sba)/vev**2 - (6*cb*cba**3*complex(0,1)*MHL**2*sb*sba)/vev**2 + (5*cb**3*cba**5*complex(0,1)*MHL**2*sb*sba)/vev**2 + (6*cba**3*complex(0,1)*m122*sb**2*sba)/vev**2 - (6*cba**3*complex(0,1)*MHH**2*sb**3*sba)/(cb*vev**2) - (cb*cba**5*complex(0,1)*MHH**2*sb**3*sba)/vev**2 + (cb*cba**5*complex(0,1)*MHL**2*sb**3*sba)/vev**2 + (6*cba**3*complex(0,1)*m122*sb**4*sba)/(cb**2*vev**2) + (5*cba**5*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) - (5*cba**5*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) - (3*cb**2*cba**2*complex(0,1)*MHH**2*sba**2)/vev**2 - (cb**4*cba**4*complex(0,1)*MHH**2*sba**2)/vev**2 + (12*cb**2*cba**2*complex(0,1)*MHL**2*sba**2)/vev**2 + (cb**4*cba**4*complex(0,1)*MHL**2*sba**2)/vev**2 + (3*cb**5*cba**2*complex(0,1)*m122*sba**2)/(sb**3*vev**2) - (3*cb**4*cba**2*complex(0,1)*MHL**2*sba**2)/(sb**2*vev**2) - (8*cb**3*cba**2*complex(0,1)*m122*sba**2)/(sb*vev**2) - (22*cb*cba**2*complex(0,1)*m122*sb*sba**2)/vev**2 + (12*cba**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (14*cb**2*cba**4*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (3*cba**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 + (14*cb**2*cba**4*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 - (8*cba**2*complex(0,1)*m122*sb**3*sba**2)/(cb*vev**2) - (3*cba**2*complex(0,1)*MHH**2*sb**4*sba**2)/(cb**2*vev**2) - (10*cba**4*complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 + (10*cba**4*complex(0,1)*MHL**2*sb**4*sba**2)/vev**2 + (3*cba**2*complex(0,1)*m122*sb**5*sba**2)/(cb**3*vev**2) + (3*cba**4*complex(0,1)*MHH**2*sb**6*sba**2)/(cb**2*vev**2) - (3*cba**4*complex(0,1)*MHL**2*sb**6*sba**2)/(cb**2*vev**2) + (6*cb**2*cba*complex(0,1)*m122*sba**3)/vev**2 + (6*cb**4*cba*complex(0,1)*m122*sba**3)/(sb**2*vev**2) + (8*cb**5*cba**3*complex(0,1)*MHH**2*sba**3)/(sb*vev**2) - (6*cb**3*cba*complex(0,1)*MHL**2*sba**3)/(sb*vev**2) - (8*cb**5*cba**3*complex(0,1)*MHL**2*sba**3)/(sb*vev**2) - (6*cb*cba*complex(0,1)*MHH**2*sb*sba**3)/vev**2 + (8*cb**3*cba**3*complex(0,1)*MHH**2*sb*sba**3)/vev**2 + (6*cb*cba*complex(0,1)*MHL**2*sb*sba**3)/vev**2 - (8*cb**3*cba**3*complex(0,1)*MHL**2*sb*sba**3)/vev**2 - (6*cba*complex(0,1)*m122*sb**2*sba**3)/vev**2 + (6*cba*complex(0,1)*MHH**2*sb**3*sba**3)/(cb*vev**2) - (8*cb*cba**3*complex(0,1)*MHH**2*sb**3*sba**3)/vev**2 + (8*cb*cba**3*complex(0,1)*MHL**2*sb**3*sba**3)/vev**2 - (6*cba*complex(0,1)*m122*sb**4*sba**3)/(cb**2*vev**2) - (8*cba**3*complex(0,1)*MHH**2*sb**5*sba**3)/(cb*vev**2) + (8*cba**3*complex(0,1)*MHL**2*sb**5*sba**3)/(cb*vev**2) + (10*cb**4*cba**2*complex(0,1)*MHH**2*sba**4)/vev**2 - (3*cb**2*complex(0,1)*MHL**2*sba**4)/vev**2 - (10*cb**4*cba**2*complex(0,1)*MHL**2*sba**4)/vev**2 - (3*cb**6*cba**2*complex(0,1)*MHH**2*sba**4)/(sb**2*vev**2) + (3*cb**6*cba**2*complex(0,1)*MHL**2*sba**4)/(sb**2*vev**2) + (2*cb**3*complex(0,1)*m122*sba**4)/(sb*vev**2) + (4*cb*complex(0,1)*m122*sb*sba**4)/vev**2 - (3*complex(0,1)*MHH**2*sb**2*sba**4)/vev**2 + (14*cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba**4)/vev**2 - (14*cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba**4)/vev**2 + (2*complex(0,1)*m122*sb**3*sba**4)/(cb*vev**2) + (cba**2*complex(0,1)*MHH**2*sb**4*sba**4)/vev**2 - (cba**2*complex(0,1)*MHL**2*sb**4*sba**4)/vev**2 - (5*cb**5*cba*complex(0,1)*MHH**2*sba**5)/(sb*vev**2) + (5*cb**5*cba*complex(0,1)*MHL**2*sba**5)/(sb*vev**2) + (cb**3*cba*complex(0,1)*MHH**2*sb*sba**5)/vev**2 - (cb**3*cba*complex(0,1)*MHL**2*sb*sba**5)/vev**2 + (5*cb*cba*complex(0,1)*MHH**2*sb**3*sba**5)/vev**2 - (5*cb*cba*complex(0,1)*MHL**2*sb**3*sba**5)/vev**2 - (cba*complex(0,1)*MHH**2*sb**5*sba**5)/(cb*vev**2) + (cba*complex(0,1)*MHL**2*sb**5*sba**5)/(cb*vev**2) - (2*cb**4*complex(0,1)*MHH**2*sba**6)/vev**2 + (2*cb**4*complex(0,1)*MHL**2*sba**6)/vev**2 - (cb**2*complex(0,1)*MHH**2*sb**2*sba**6)/vev**2 + (cb**2*complex(0,1)*MHL**2*sb**2*sba**6)/vev**2 + (complex(0,1)*MHH**2*sb**4*sba**6)/vev**2 - (complex(0,1)*MHL**2*sb**4*sba**6)/vev**2',
                  order = {'QED':2})

GC_106 = Coupling(name = 'GC_106',
                  value = '(-3*cb**2*cba**4*complex(0,1)*MHH**2)/vev**2 - (3*cb**2*cba**6*complex(0,1)*MHH**2*sb**2)/vev**2 - (3*cba**4*complex(0,1)*MHL**2*sb**2)/vev**2 + (3*cb**2*cba**6*complex(0,1)*MHL**2*sb**2)/vev**2 - (3*cba**6*complex(0,1)*MHH**2*sb**4)/vev**2 + (3*cba**6*complex(0,1)*MHL**2*sb**4)/vev**2 - (12*cb*cba**3*complex(0,1)*MHH**2*sb*sba)/vev**2 + (12*cb**3*cba**5*complex(0,1)*MHH**2*sb*sba)/vev**2 + (12*cb*cba**3*complex(0,1)*MHL**2*sb*sba)/vev**2 - (12*cb**3*cba**5*complex(0,1)*MHL**2*sb*sba)/vev**2 + (12*cb*cba**5*complex(0,1)*MHH**2*sb**3*sba)/vev**2 - (12*cb*cba**5*complex(0,1)*MHL**2*sb**3*sba)/vev**2 - (15*cb**4*cba**4*complex(0,1)*MHH**2*sba**2)/vev**2 - (18*cb**2*cba**2*complex(0,1)*MHL**2*sba**2)/vev**2 + (15*cb**4*cba**4*complex(0,1)*MHL**2*sba**2)/vev**2 + (12*cb**3*cba**2*complex(0,1)*m122*sba**2)/(sb*vev**2) + (24*cb*cba**2*complex(0,1)*m122*sb*sba**2)/vev**2 - (18*cba**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (15*cb**2*cba**4*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 + (15*cb**2*cba**4*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 + (12*cba**2*complex(0,1)*m122*sb**3*sba**2)/(cb*vev**2) - (12*cb**2*cba*complex(0,1)*m122*sba**3)/vev**2 - (12*cb**4*cba*complex(0,1)*m122*sba**3)/(sb**2*vev**2) + (6*cb**5*cba**3*complex(0,1)*MHH**2*sba**3)/(sb*vev**2) + (12*cb**3*cba*complex(0,1)*MHL**2*sba**3)/(sb*vev**2) - (6*cb**5*cba**3*complex(0,1)*MHL**2*sba**3)/(sb*vev**2) + (18*cb**3*cba**3*complex(0,1)*MHH**2*sb*sba**3)/vev**2 - (18*cb**3*cba**3*complex(0,1)*MHL**2*sb*sba**3)/vev**2 + (12*cba*complex(0,1)*m122*sb**2*sba**3)/vev**2 - (12*cba*complex(0,1)*MHH**2*sb**3*sba**3)/(cb*vev**2) + (18*cb*cba**3*complex(0,1)*MHH**2*sb**3*sba**3)/vev**2 - (18*cb*cba**3*complex(0,1)*MHL**2*sb**3*sba**3)/vev**2 + (12*cba*complex(0,1)*m122*sb**4*sba**3)/(cb**2*vev**2) + (6*cba**3*complex(0,1)*MHH**2*sb**5*sba**3)/(cb*vev**2) - (6*cba**3*complex(0,1)*MHL**2*sb**5*sba**3)/(cb*vev**2) - (27*cb**4*cba**2*complex(0,1)*MHH**2*sba**4)/vev**2 + (27*cb**4*cba**2*complex(0,1)*MHL**2*sba**4)/vev**2 + (3*cb**5*complex(0,1)*m122*sba**4)/(sb**3*vev**2) - (3*cb**4*complex(0,1)*MHL**2*sba**4)/(sb**2*vev**2) - (6*cb*complex(0,1)*m122*sb*sba**4)/vev**2 - (36*cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba**4)/vev**2 + (36*cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba**4)/vev**2 - (3*complex(0,1)*MHH**2*sb**4*sba**4)/(cb**2*vev**2) - (6*cba**2*complex(0,1)*MHH**2*sb**4*sba**4)/vev**2 + (6*cba**2*complex(0,1)*MHL**2*sb**4*sba**4)/vev**2 + (3*complex(0,1)*m122*sb**5*sba**4)/(cb**3*vev**2) + (3*cba**2*complex(0,1)*MHH**2*sb**6*sba**4)/(cb**2*vev**2) - (3*cba**2*complex(0,1)*MHL**2*sb**6*sba**4)/(cb**2*vev**2) + (18*cb**5*cba*complex(0,1)*MHH**2*sba**5)/(sb*vev**2) - (18*cb**5*cba*complex(0,1)*MHL**2*sba**5)/(sb*vev**2) + (18*cb**3*cba*complex(0,1)*MHH**2*sb*sba**5)/vev**2 - (18*cb**3*cba*complex(0,1)*MHL**2*sb*sba**5)/vev**2 - (6*cb*cba*complex(0,1)*MHH**2*sb**3*sba**5)/vev**2 + (6*cb*cba*complex(0,1)*MHL**2*sb**3*sba**5)/vev**2 - (6*cba*complex(0,1)*MHH**2*sb**5*sba**5)/(cb*vev**2) + (6*cba*complex(0,1)*MHL**2*sb**5*sba**5)/(cb*vev**2) - (3*cb**6*complex(0,1)*MHH**2*sba**6)/(sb**2*vev**2) + (3*cb**6*complex(0,1)*MHL**2*sba**6)/(sb**2*vev**2) + (6*cb**2*complex(0,1)*MHH**2*sb**2*sba**6)/vev**2 - (6*cb**2*complex(0,1)*MHL**2*sb**2*sba**6)/vev**2 + (3*complex(0,1)*MHH**2*sb**4*sba**6)/vev**2 - (3*complex(0,1)*MHL**2*sb**4*sba**6)/vev**2',
                  order = {'QED':2})

GC_107 = Coupling(name = 'GC_107',
                  value = '(cb**4*MHA**2)/vev - (cb**4*MHp**2)/vev + (2*cb**2*MHA**2*sb**2)/vev - (2*cb**2*MHp**2*sb**2)/vev + (MHA**2*sb**4)/vev - (MHp**2*sb**4)/vev',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-((cb**4*MHA**2)/vev) + (cb**4*MHp**2)/vev - (2*cb**2*MHA**2*sb**2)/vev + (2*cb**2*MHp**2*sb**2)/vev - (MHA**2*sb**4)/vev + (MHp**2*sb**4)/vev',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '(-2*cb**4*cba*complex(0,1)*MHA**2)/vev - (cb**4*cba**3*complex(0,1)*MHH**2)/vev - (cb**2*cba*complex(0,1)*MHL**2)/vev + (cb**4*cba**3*complex(0,1)*MHL**2)/vev + (2*cb**3*cba*complex(0,1)*m122)/(sb*vev) + (4*cb*cba*complex(0,1)*m122*sb)/vev - (4*cb**2*cba*complex(0,1)*MHA**2*sb**2)/vev - (cba*complex(0,1)*MHH**2*sb**2)/vev - (cb**2*cba**3*complex(0,1)*MHH**2*sb**2)/vev + (cb**2*cba**3*complex(0,1)*MHL**2*sb**2)/vev + (2*cba*complex(0,1)*m122*sb**3)/(cb*vev) - (2*cba*complex(0,1)*MHA**2*sb**4)/vev - (cb**2*complex(0,1)*m122*sba)/vev - (cb**4*complex(0,1)*m122*sba)/(sb**2*vev) + (cb**5*cba**2*complex(0,1)*MHH**2*sba)/(sb*vev) + (cb**3*complex(0,1)*MHL**2*sba)/(sb*vev) - (cb**5*cba**2*complex(0,1)*MHL**2*sba)/(sb*vev) + (cb**3*cba**2*complex(0,1)*MHH**2*sb*sba)/vev - (cb**3*cba**2*complex(0,1)*MHL**2*sb*sba)/vev + (complex(0,1)*m122*sb**2*sba)/vev - (complex(0,1)*MHH**2*sb**3*sba)/(cb*vev) + (complex(0,1)*m122*sb**4*sba)/(cb**2*vev) - (cb**4*cba*complex(0,1)*MHH**2*sba**2)/vev + (cb**4*cba*complex(0,1)*MHL**2*sba**2)/vev - (cb**2*cba*complex(0,1)*MHH**2*sb**2*sba**2)/vev + (cb**2*cba*complex(0,1)*MHL**2*sb**2*sba**2)/vev + (cb**5*complex(0,1)*MHH**2*sba**3)/(sb*vev) - (cb**5*complex(0,1)*MHL**2*sba**3)/(sb*vev) + (cb**3*complex(0,1)*MHH**2*sb*sba**3)/vev - (cb**3*complex(0,1)*MHL**2*sb*sba**3)/vev',
                  order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)*I2a33',
                 order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-((cb**4*cba**3*complex(0,1)*MHH**2)/vev) - (cb**2*cba*complex(0,1)*MHL**2)/vev + (cb**4*cba**3*complex(0,1)*MHL**2)/vev - (2*cb**4*cba*complex(0,1)*MHp**2)/vev + (2*cb**3*cba*complex(0,1)*m122)/(sb*vev) + (4*cb*cba*complex(0,1)*m122*sb)/vev - (cba*complex(0,1)*MHH**2*sb**2)/vev - (cb**2*cba**3*complex(0,1)*MHH**2*sb**2)/vev + (cb**2*cba**3*complex(0,1)*MHL**2*sb**2)/vev - (4*cb**2*cba*complex(0,1)*MHp**2*sb**2)/vev + (2*cba*complex(0,1)*m122*sb**3)/(cb*vev) - (2*cba*complex(0,1)*MHp**2*sb**4)/vev - (cb**2*complex(0,1)*m122*sba)/vev - (cb**4*complex(0,1)*m122*sba)/(sb**2*vev) + (cb**5*cba**2*complex(0,1)*MHH**2*sba)/(sb*vev) + (cb**3*complex(0,1)*MHL**2*sba)/(sb*vev) - (cb**5*cba**2*complex(0,1)*MHL**2*sba)/(sb*vev) + (cb**3*cba**2*complex(0,1)*MHH**2*sb*sba)/vev - (cb**3*cba**2*complex(0,1)*MHL**2*sb*sba)/vev + (complex(0,1)*m122*sb**2*sba)/vev - (complex(0,1)*MHH**2*sb**3*sba)/(cb*vev) + (complex(0,1)*m122*sb**4*sba)/(cb**2*vev) - (cb**4*cba*complex(0,1)*MHH**2*sba**2)/vev + (cb**4*cba*complex(0,1)*MHL**2*sba**2)/vev - (cb**2*cba*complex(0,1)*MHH**2*sb**2*sba**2)/vev + (cb**2*cba*complex(0,1)*MHL**2*sb**2*sba**2)/vev + (cb**5*complex(0,1)*MHH**2*sba**3)/(sb*vev) - (cb**5*complex(0,1)*MHL**2*sba**3)/(sb*vev) + (cb**3*complex(0,1)*MHH**2*sb*sba**3)/vev - (cb**3*complex(0,1)*MHL**2*sb*sba**3)/vev',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '(cb*cba*complex(0,1)*MHH**2*sb)/vev - (cb**3*cba**3*complex(0,1)*MHH**2*sb)/vev - (cb*cba*complex(0,1)*MHL**2*sb)/vev + (cb**3*cba**3*complex(0,1)*MHL**2*sb)/vev - (cb*cba**3*complex(0,1)*MHH**2*sb**3)/vev + (cb*cba**3*complex(0,1)*MHL**2*sb**3)/vev - (cb**2*complex(0,1)*MHH**2*sba)/vev + (cb**4*cba**2*complex(0,1)*MHH**2*sba)/vev - (cb**4*cba**2*complex(0,1)*MHL**2*sba)/vev + (cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba)/vev - (complex(0,1)*MHL**2*sb**2*sba)/vev - (cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba)/vev - (cb**3*cba*complex(0,1)*MHH**2*sb*sba**2)/vev + (cb**3*cba*complex(0,1)*MHL**2*sb*sba**2)/vev - (cb*cba*complex(0,1)*MHH**2*sb**3*sba**2)/vev + (cb*cba*complex(0,1)*MHL**2*sb**3*sba**2)/vev + (cb**4*complex(0,1)*MHH**2*sba**3)/vev - (cb**4*complex(0,1)*MHL**2*sba**3)/vev + (cb**2*complex(0,1)*MHH**2*sb**2*sba**3)/vev - (cb**2*complex(0,1)*MHL**2*sb**2*sba**3)/vev',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '(cb*cba*complex(0,1)*MHH**2*sb)/vev - (cb**3*cba**3*complex(0,1)*MHH**2*sb)/vev - (cb*cba*complex(0,1)*MHL**2*sb)/vev + (cb**3*cba**3*complex(0,1)*MHL**2*sb)/vev - (cb*cba**3*complex(0,1)*MHH**2*sb**3)/vev + (cb*cba**3*complex(0,1)*MHL**2*sb**3)/vev - (cb**4*complex(0,1)*MHA**2*sba)/vev + (cb**4*cba**2*complex(0,1)*MHH**2*sba)/vev + (cb**2*complex(0,1)*MHL**2*sba)/vev - (cb**4*cba**2*complex(0,1)*MHL**2*sba)/vev - (2*cb**2*complex(0,1)*MHA**2*sb**2*sba)/vev + (complex(0,1)*MHH**2*sb**2*sba)/vev + (cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba)/vev - (cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba)/vev - (complex(0,1)*MHA**2*sb**4*sba)/vev - (cb**3*cba*complex(0,1)*MHH**2*sb*sba**2)/vev + (cb**3*cba*complex(0,1)*MHL**2*sb*sba**2)/vev - (cb*cba*complex(0,1)*MHH**2*sb**3*sba**2)/vev + (cb*cba*complex(0,1)*MHL**2*sb**3*sba**2)/vev + (cb**4*complex(0,1)*MHH**2*sba**3)/vev - (cb**4*complex(0,1)*MHL**2*sba**3)/vev + (cb**2*complex(0,1)*MHH**2*sb**2*sba**3)/vev - (cb**2*complex(0,1)*MHL**2*sb**2*sba**3)/vev',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '(cb*cba*complex(0,1)*MHH**2*sb)/vev - (cb**3*cba**3*complex(0,1)*MHH**2*sb)/vev - (cb*cba*complex(0,1)*MHL**2*sb)/vev + (cb**3*cba**3*complex(0,1)*MHL**2*sb)/vev - (cb*cba**3*complex(0,1)*MHH**2*sb**3)/vev + (cb*cba**3*complex(0,1)*MHL**2*sb**3)/vev + (cb**4*cba**2*complex(0,1)*MHH**2*sba)/vev + (cb**2*complex(0,1)*MHL**2*sba)/vev - (cb**4*cba**2*complex(0,1)*MHL**2*sba)/vev - (cb**4*complex(0,1)*MHp**2*sba)/vev + (complex(0,1)*MHH**2*sb**2*sba)/vev + (cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba)/vev - (cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba)/vev - (2*cb**2*complex(0,1)*MHp**2*sb**2*sba)/vev - (complex(0,1)*MHp**2*sb**4*sba)/vev - (cb**3*cba*complex(0,1)*MHH**2*sb*sba**2)/vev + (cb**3*cba*complex(0,1)*MHL**2*sb*sba**2)/vev - (cb*cba*complex(0,1)*MHH**2*sb**3*sba**2)/vev + (cb*cba*complex(0,1)*MHL**2*sb**3*sba**2)/vev + (cb**4*complex(0,1)*MHH**2*sba**3)/vev - (cb**4*complex(0,1)*MHL**2*sba**3)/vev + (cb**2*complex(0,1)*MHH**2*sb**2*sba**3)/vev - (cb**2*complex(0,1)*MHL**2*sb**2*sba**3)/vev',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-((cb**2*cba*complex(0,1)*MHH**2)/vev) - (cb**2*cba**3*complex(0,1)*MHH**2*sb**2)/vev - (cba*complex(0,1)*MHL**2*sb**2)/vev + (cb**2*cba**3*complex(0,1)*MHL**2*sb**2)/vev - (cba**3*complex(0,1)*MHH**2*sb**4)/vev + (cba**3*complex(0,1)*MHL**2*sb**4)/vev - (cb*complex(0,1)*MHH**2*sb*sba)/vev + (cb**3*cba**2*complex(0,1)*MHH**2*sb*sba)/vev + (cb*complex(0,1)*MHL**2*sb*sba)/vev - (cb**3*cba**2*complex(0,1)*MHL**2*sb*sba)/vev + (cb*cba**2*complex(0,1)*MHH**2*sb**3*sba)/vev - (cb*cba**2*complex(0,1)*MHL**2*sb**3*sba)/vev - (cb**2*cba*complex(0,1)*MHH**2*sb**2*sba**2)/vev + (cb**2*cba*complex(0,1)*MHL**2*sb**2*sba**2)/vev - (cba*complex(0,1)*MHH**2*sb**4*sba**2)/vev + (cba*complex(0,1)*MHL**2*sb**4*sba**2)/vev + (cb**3*complex(0,1)*MHH**2*sb*sba**3)/vev - (cb**3*complex(0,1)*MHL**2*sb*sba**3)/vev + (cb*complex(0,1)*MHH**2*sb**3*sba**3)/vev - (cb*complex(0,1)*MHL**2*sb**3*sba**3)/vev',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '(cb**4*cba*complex(0,1)*MHA**2)/vev - (cb**2*cba*complex(0,1)*MHL**2)/vev + (2*cb**2*cba*complex(0,1)*MHA**2*sb**2)/vev - (cba*complex(0,1)*MHH**2*sb**2)/vev + (cb**2*cba**3*complex(0,1)*MHH**2*sb**2)/vev - (cb**2*cba**3*complex(0,1)*MHL**2*sb**2)/vev + (cba*complex(0,1)*MHA**2*sb**4)/vev + (cba**3*complex(0,1)*MHH**2*sb**4)/vev - (cba**3*complex(0,1)*MHL**2*sb**4)/vev + (cb*complex(0,1)*MHH**2*sb*sba)/vev - (cb**3*cba**2*complex(0,1)*MHH**2*sb*sba)/vev - (cb*complex(0,1)*MHL**2*sb*sba)/vev + (cb**3*cba**2*complex(0,1)*MHL**2*sb*sba)/vev - (cb*cba**2*complex(0,1)*MHH**2*sb**3*sba)/vev + (cb*cba**2*complex(0,1)*MHL**2*sb**3*sba)/vev + (cb**2*cba*complex(0,1)*MHH**2*sb**2*sba**2)/vev - (cb**2*cba*complex(0,1)*MHL**2*sb**2*sba**2)/vev + (cba*complex(0,1)*MHH**2*sb**4*sba**2)/vev - (cba*complex(0,1)*MHL**2*sb**4*sba**2)/vev - (cb**3*complex(0,1)*MHH**2*sb*sba**3)/vev + (cb**3*complex(0,1)*MHL**2*sb*sba**3)/vev - (cb*complex(0,1)*MHH**2*sb**3*sba**3)/vev + (cb*complex(0,1)*MHL**2*sb**3*sba**3)/vev',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '-((cb**2*cba*complex(0,1)*MHL**2)/vev) + (cb**4*cba*complex(0,1)*MHp**2)/vev - (cba*complex(0,1)*MHH**2*sb**2)/vev + (cb**2*cba**3*complex(0,1)*MHH**2*sb**2)/vev - (cb**2*cba**3*complex(0,1)*MHL**2*sb**2)/vev + (2*cb**2*cba*complex(0,1)*MHp**2*sb**2)/vev + (cba**3*complex(0,1)*MHH**2*sb**4)/vev - (cba**3*complex(0,1)*MHL**2*sb**4)/vev + (cba*complex(0,1)*MHp**2*sb**4)/vev + (cb*complex(0,1)*MHH**2*sb*sba)/vev - (cb**3*cba**2*complex(0,1)*MHH**2*sb*sba)/vev - (cb*complex(0,1)*MHL**2*sb*sba)/vev + (cb**3*cba**2*complex(0,1)*MHL**2*sb*sba)/vev - (cb*cba**2*complex(0,1)*MHH**2*sb**3*sba)/vev + (cb*cba**2*complex(0,1)*MHL**2*sb**3*sba)/vev + (cb**2*cba*complex(0,1)*MHH**2*sb**2*sba**2)/vev - (cb**2*cba*complex(0,1)*MHL**2*sb**2*sba**2)/vev + (cba*complex(0,1)*MHH**2*sb**4*sba**2)/vev - (cba*complex(0,1)*MHL**2*sb**4*sba**2)/vev - (cb**3*complex(0,1)*MHH**2*sb*sba**3)/vev + (cb**3*complex(0,1)*MHL**2*sb*sba**3)/vev - (cb*complex(0,1)*MHH**2*sb**3*sba**3)/vev + (cb*complex(0,1)*MHL**2*sb**3*sba**3)/vev',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '(cb**2*cba*complex(0,1)*m122)/vev + (cb**4*cba*complex(0,1)*m122)/(sb**2*vev) - (cb**3*cba*complex(0,1)*MHL**2)/(sb*vev) - (cba*complex(0,1)*m122*sb**2)/vev + (cba*complex(0,1)*MHH**2*sb**3)/(cb*vev) - (cb*cba**3*complex(0,1)*MHH**2*sb**3)/vev + (cb*cba**3*complex(0,1)*MHL**2*sb**3)/vev - (cba*complex(0,1)*m122*sb**4)/(cb**2*vev) - (cba**3*complex(0,1)*MHH**2*sb**5)/(cb*vev) + (cba**3*complex(0,1)*MHL**2*sb**5)/(cb*vev) - (2*cb**4*complex(0,1)*MHA**2*sba)/vev - (cb**2*complex(0,1)*MHL**2*sba)/vev + (2*cb**3*complex(0,1)*m122*sba)/(sb*vev) + (4*cb*complex(0,1)*m122*sb*sba)/vev - (4*cb**2*complex(0,1)*MHA**2*sb**2*sba)/vev - (complex(0,1)*MHH**2*sb**2*sba)/vev + (cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba)/vev - (cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba)/vev + (2*complex(0,1)*m122*sb**3*sba)/(cb*vev) - (2*complex(0,1)*MHA**2*sb**4*sba)/vev + (cba**2*complex(0,1)*MHH**2*sb**4*sba)/vev - (cba**2*complex(0,1)*MHL**2*sb**4*sba)/vev - (cb*cba*complex(0,1)*MHH**2*sb**3*sba**2)/vev + (cb*cba*complex(0,1)*MHL**2*sb**3*sba**2)/vev - (cba*complex(0,1)*MHH**2*sb**5*sba**2)/(cb*vev) + (cba*complex(0,1)*MHL**2*sb**5*sba**2)/(cb*vev) + (cb**2*complex(0,1)*MHH**2*sb**2*sba**3)/vev - (cb**2*complex(0,1)*MHL**2*sb**2*sba**3)/vev + (complex(0,1)*MHH**2*sb**4*sba**3)/vev - (complex(0,1)*MHL**2*sb**4*sba**3)/vev',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '(cb**2*cba*complex(0,1)*m122)/vev + (cb**4*cba*complex(0,1)*m122)/(sb**2*vev) - (cb**3*cba*complex(0,1)*MHL**2)/(sb*vev) - (cba*complex(0,1)*m122*sb**2)/vev + (cba*complex(0,1)*MHH**2*sb**3)/(cb*vev) - (cb*cba**3*complex(0,1)*MHH**2*sb**3)/vev + (cb*cba**3*complex(0,1)*MHL**2*sb**3)/vev - (cba*complex(0,1)*m122*sb**4)/(cb**2*vev) - (cba**3*complex(0,1)*MHH**2*sb**5)/(cb*vev) + (cba**3*complex(0,1)*MHL**2*sb**5)/(cb*vev) - (cb**2*complex(0,1)*MHL**2*sba)/vev - (2*cb**4*complex(0,1)*MHp**2*sba)/vev + (2*cb**3*complex(0,1)*m122*sba)/(sb*vev) + (4*cb*complex(0,1)*m122*sb*sba)/vev - (complex(0,1)*MHH**2*sb**2*sba)/vev + (cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba)/vev - (cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba)/vev - (4*cb**2*complex(0,1)*MHp**2*sb**2*sba)/vev + (2*complex(0,1)*m122*sb**3*sba)/(cb*vev) + (cba**2*complex(0,1)*MHH**2*sb**4*sba)/vev - (cba**2*complex(0,1)*MHL**2*sb**4*sba)/vev - (2*complex(0,1)*MHp**2*sb**4*sba)/vev - (cb*cba*complex(0,1)*MHH**2*sb**3*sba**2)/vev + (cb*cba*complex(0,1)*MHL**2*sb**3*sba**2)/vev - (cba*complex(0,1)*MHH**2*sb**5*sba**2)/(cb*vev) + (cba*complex(0,1)*MHL**2*sb**5*sba**2)/(cb*vev) + (cb**2*complex(0,1)*MHH**2*sb**2*sba**3)/vev - (cb**2*complex(0,1)*MHL**2*sb**2*sba**3)/vev + (complex(0,1)*MHH**2*sb**4*sba**3)/vev - (complex(0,1)*MHL**2*sb**4*sba**3)/vev',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '(-3*cb**2*cba**3*complex(0,1)*MHH**2)/vev - (3*cb**2*cba**5*complex(0,1)*MHH**2*sb**2)/vev - (3*cba**3*complex(0,1)*MHL**2*sb**2)/vev + (3*cb**2*cba**5*complex(0,1)*MHL**2*sb**2)/vev - (3*cba**5*complex(0,1)*MHH**2*sb**4)/vev + (3*cba**5*complex(0,1)*MHL**2*sb**4)/vev - (9*cb*cba**2*complex(0,1)*MHH**2*sb*sba)/vev + (9*cb**3*cba**4*complex(0,1)*MHH**2*sb*sba)/vev + (9*cb*cba**2*complex(0,1)*MHL**2*sb*sba)/vev - (9*cb**3*cba**4*complex(0,1)*MHL**2*sb*sba)/vev + (9*cb*cba**4*complex(0,1)*MHH**2*sb**3*sba)/vev - (9*cb*cba**4*complex(0,1)*MHL**2*sb**3*sba)/vev - (9*cb**4*cba**3*complex(0,1)*MHH**2*sba**2)/vev - (9*cb**2*cba*complex(0,1)*MHL**2*sba**2)/vev + (9*cb**4*cba**3*complex(0,1)*MHL**2*sba**2)/vev + (6*cb**3*cba*complex(0,1)*m122*sba**2)/(sb*vev) + (12*cb*cba*complex(0,1)*m122*sb*sba**2)/vev - (9*cba*complex(0,1)*MHH**2*sb**2*sba**2)/vev - (12*cb**2*cba**3*complex(0,1)*MHH**2*sb**2*sba**2)/vev + (12*cb**2*cba**3*complex(0,1)*MHL**2*sb**2*sba**2)/vev + (6*cba*complex(0,1)*m122*sb**3*sba**2)/(cb*vev) - (3*cba**3*complex(0,1)*MHH**2*sb**4*sba**2)/vev + (3*cba**3*complex(0,1)*MHL**2*sb**4*sba**2)/vev - (3*cb**2*complex(0,1)*m122*sba**3)/vev - (3*cb**4*complex(0,1)*m122*sba**3)/(sb**2*vev) + (3*cb**5*cba**2*complex(0,1)*MHH**2*sba**3)/(sb*vev) + (3*cb**3*complex(0,1)*MHL**2*sba**3)/(sb*vev) - (3*cb**5*cba**2*complex(0,1)*MHL**2*sba**3)/(sb*vev) + (12*cb**3*cba**2*complex(0,1)*MHH**2*sb*sba**3)/vev - (12*cb**3*cba**2*complex(0,1)*MHL**2*sb*sba**3)/vev + (3*complex(0,1)*m122*sb**2*sba**3)/vev - (3*complex(0,1)*MHH**2*sb**3*sba**3)/(cb*vev) + (9*cb*cba**2*complex(0,1)*MHH**2*sb**3*sba**3)/vev - (9*cb*cba**2*complex(0,1)*MHL**2*sb**3*sba**3)/vev + (3*complex(0,1)*m122*sb**4*sba**3)/(cb**2*vev) - (9*cb**4*cba*complex(0,1)*MHH**2*sba**4)/vev + (9*cb**4*cba*complex(0,1)*MHL**2*sba**4)/vev - (9*cb**2*cba*complex(0,1)*MHH**2*sb**2*sba**4)/vev + (9*cb**2*cba*complex(0,1)*MHL**2*sb**2*sba**4)/vev + (3*cb**5*complex(0,1)*MHH**2*sba**5)/(sb*vev) - (3*cb**5*complex(0,1)*MHL**2*sba**5)/(sb*vev) + (3*cb**3*complex(0,1)*MHH**2*sb*sba**5)/vev - (3*cb**3*complex(0,1)*MHL**2*sb*sba**5)/vev',
                  order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*I3a33',
                 order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '(3*cb**2*cba**3*complex(0,1)*m122)/vev + (3*cb**4*cba**3*complex(0,1)*m122)/(sb**2*vev) - (3*cb**3*cba**3*complex(0,1)*MHL**2)/(sb*vev) - (3*cba**3*complex(0,1)*m122*sb**2)/vev + (3*cba**3*complex(0,1)*MHH**2*sb**3)/(cb*vev) - (3*cb*cba**5*complex(0,1)*MHH**2*sb**3)/vev + (3*cb*cba**5*complex(0,1)*MHL**2*sb**3)/vev - (3*cba**3*complex(0,1)*m122*sb**4)/(cb**2*vev) - (3*cba**5*complex(0,1)*MHH**2*sb**5)/(cb*vev) + (3*cba**5*complex(0,1)*MHL**2*sb**5)/(cb*vev) - (9*cb**2*cba**2*complex(0,1)*MHL**2*sba)/vev + (6*cb**3*cba**2*complex(0,1)*m122*sba)/(sb*vev) + (12*cb*cba**2*complex(0,1)*m122*sb*sba)/vev - (9*cba**2*complex(0,1)*MHH**2*sb**2*sba)/vev + (9*cb**2*cba**4*complex(0,1)*MHH**2*sb**2*sba)/vev - (9*cb**2*cba**4*complex(0,1)*MHL**2*sb**2*sba)/vev + (6*cba**2*complex(0,1)*m122*sb**3*sba)/(cb*vev) + (9*cba**4*complex(0,1)*MHH**2*sb**4*sba)/vev - (9*cba**4*complex(0,1)*MHL**2*sb**4*sba)/vev + (9*cb*cba*complex(0,1)*MHH**2*sb*sba**2)/vev - (9*cb**3*cba**3*complex(0,1)*MHH**2*sb*sba**2)/vev - (9*cb*cba*complex(0,1)*MHL**2*sb*sba**2)/vev + (9*cb**3*cba**3*complex(0,1)*MHL**2*sb*sba**2)/vev - (12*cb*cba**3*complex(0,1)*MHH**2*sb**3*sba**2)/vev + (12*cb*cba**3*complex(0,1)*MHL**2*sb**3*sba**2)/vev - (3*cba**3*complex(0,1)*MHH**2*sb**5*sba**2)/(cb*vev) + (3*cba**3*complex(0,1)*MHL**2*sb**5*sba**2)/(cb*vev) - (3*cb**2*complex(0,1)*MHH**2*sba**3)/vev + (3*cb**4*cba**2*complex(0,1)*MHH**2*sba**3)/vev - (3*cb**4*cba**2*complex(0,1)*MHL**2*sba**3)/vev + (12*cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba**3)/vev - (3*complex(0,1)*MHL**2*sb**2*sba**3)/vev - (12*cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba**3)/vev + (9*cba**2*complex(0,1)*MHH**2*sb**4*sba**3)/vev - (9*cba**2*complex(0,1)*MHL**2*sb**4*sba**3)/vev - (9*cb**3*cba*complex(0,1)*MHH**2*sb*sba**4)/vev + (9*cb**3*cba*complex(0,1)*MHL**2*sb*sba**4)/vev - (9*cb*cba*complex(0,1)*MHH**2*sb**3*sba**4)/vev + (9*cb*cba*complex(0,1)*MHL**2*sb**3*sba**4)/vev + (3*cb**4*complex(0,1)*MHH**2*sba**5)/vev - (3*cb**4*complex(0,1)*MHL**2*sba**5)/vev + (3*cb**2*complex(0,1)*MHH**2*sb**2*sba**5)/vev - (3*cb**2*complex(0,1)*MHL**2*sb**2*sba**5)/vev',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '-((cb**4*cba**5*complex(0,1)*MHH**2)/vev) - (3*cb**2*cba**3*complex(0,1)*MHL**2)/vev + (cb**4*cba**5*complex(0,1)*MHL**2)/vev + (2*cb**3*cba**3*complex(0,1)*m122)/(sb*vev) + (4*cb*cba**3*complex(0,1)*m122*sb)/vev - (3*cba**3*complex(0,1)*MHH**2*sb**2)/vev + (cb**2*cba**5*complex(0,1)*MHH**2*sb**2)/vev - (cb**2*cba**5*complex(0,1)*MHL**2*sb**2)/vev + (2*cba**3*complex(0,1)*m122*sb**3)/(cb*vev) + (2*cba**5*complex(0,1)*MHH**2*sb**4)/vev - (2*cba**5*complex(0,1)*MHL**2*sb**4)/vev - (3*cb**2*cba**2*complex(0,1)*m122*sba)/vev - (3*cb**4*cba**2*complex(0,1)*m122*sba)/(sb**2*vev) + (cb**5*cba**4*complex(0,1)*MHH**2*sba)/(sb*vev) + (3*cb**3*cba**2*complex(0,1)*MHL**2*sba)/(sb*vev) - (cb**5*cba**4*complex(0,1)*MHL**2*sba)/(sb*vev) + (6*cb*cba**2*complex(0,1)*MHH**2*sb*sba)/vev - (5*cb**3*cba**4*complex(0,1)*MHH**2*sb*sba)/vev - (6*cb*cba**2*complex(0,1)*MHL**2*sb*sba)/vev + (5*cb**3*cba**4*complex(0,1)*MHL**2*sb*sba)/vev + (3*cba**2*complex(0,1)*m122*sb**2*sba)/vev - (3*cba**2*complex(0,1)*MHH**2*sb**3*sba)/(cb*vev) - (4*cb*cba**4*complex(0,1)*MHH**2*sb**3*sba)/vev + (4*cb*cba**4*complex(0,1)*MHL**2*sb**3*sba)/vev + (3*cba**2*complex(0,1)*m122*sb**4*sba)/(cb**2*vev) + (2*cba**4*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev) - (2*cba**4*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev) - (3*cb**2*cba*complex(0,1)*MHH**2*sba**2)/vev + (3*cb**4*cba**3*complex(0,1)*MHH**2*sba**2)/vev + (6*cb**2*cba*complex(0,1)*MHL**2*sba**2)/vev - (3*cb**4*cba**3*complex(0,1)*MHL**2*sba**2)/vev - (4*cb**3*cba*complex(0,1)*m122*sba**2)/(sb*vev) - (8*cb*cba*complex(0,1)*m122*sb*sba**2)/vev + (6*cba*complex(0,1)*MHH**2*sb**2*sba**2)/vev - (3*cba*complex(0,1)*MHL**2*sb**2*sba**2)/vev - (4*cba*complex(0,1)*m122*sb**3*sba**2)/(cb*vev) - (3*cba**3*complex(0,1)*MHH**2*sb**4*sba**2)/vev + (3*cba**3*complex(0,1)*MHL**2*sb**4*sba**2)/vev + (cb**5*cba**2*complex(0,1)*MHH**2*sba**3)/(sb*vev) - (cb**5*cba**2*complex(0,1)*MHL**2*sba**3)/(sb*vev) - (3*cb*complex(0,1)*MHH**2*sb*sba**3)/vev - (2*cb**3*cba**2*complex(0,1)*MHH**2*sb*sba**3)/vev + (3*cb*complex(0,1)*MHL**2*sb*sba**3)/vev + (2*cb**3*cba**2*complex(0,1)*MHL**2*sb*sba**3)/vev - (cb*cba**2*complex(0,1)*MHH**2*sb**3*sba**3)/vev + (cb*cba**2*complex(0,1)*MHL**2*sb**3*sba**3)/vev + (2*cba**2*complex(0,1)*MHH**2*sb**5*sba**3)/(cb*vev) - (2*cba**2*complex(0,1)*MHL**2*sb**5*sba**3)/(cb*vev) + (4*cb**4*cba*complex(0,1)*MHH**2*sba**4)/vev - (4*cb**4*cba*complex(0,1)*MHL**2*sba**4)/vev - (cb**2*cba*complex(0,1)*MHH**2*sb**2*sba**4)/vev + (cb**2*cba*complex(0,1)*MHL**2*sb**2*sba**4)/vev - (5*cba*complex(0,1)*MHH**2*sb**4*sba**4)/vev + (5*cba*complex(0,1)*MHL**2*sb**4*sba**4)/vev + (3*cb**3*complex(0,1)*MHH**2*sb*sba**5)/vev - (3*cb**3*complex(0,1)*MHL**2*sb*sba**5)/vev + (3*cb*complex(0,1)*MHH**2*sb**3*sba**5)/vev - (3*cb*complex(0,1)*MHL**2*sb**3*sba**5)/vev',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '(3*cb*cba**3*complex(0,1)*MHH**2*sb)/vev - (3*cb**3*cba**5*complex(0,1)*MHH**2*sb)/vev - (3*cb*cba**3*complex(0,1)*MHL**2*sb)/vev + (3*cb**3*cba**5*complex(0,1)*MHL**2*sb)/vev - (3*cb*cba**5*complex(0,1)*MHH**2*sb**3)/vev + (3*cb*cba**5*complex(0,1)*MHL**2*sb**3)/vev - (3*cb**2*cba**2*complex(0,1)*MHH**2*sba)/vev + (5*cb**4*cba**4*complex(0,1)*MHH**2*sba)/vev + (6*cb**2*cba**2*complex(0,1)*MHL**2*sba)/vev - (5*cb**4*cba**4*complex(0,1)*MHL**2*sba)/vev - (4*cb**3*cba**2*complex(0,1)*m122*sba)/(sb*vev) - (8*cb*cba**2*complex(0,1)*m122*sb*sba)/vev + (6*cba**2*complex(0,1)*MHH**2*sb**2*sba)/vev + (cb**2*cba**4*complex(0,1)*MHH**2*sb**2*sba)/vev - (3*cba**2*complex(0,1)*MHL**2*sb**2*sba)/vev - (cb**2*cba**4*complex(0,1)*MHL**2*sb**2*sba)/vev - (4*cba**2*complex(0,1)*m122*sb**3*sba)/(cb*vev) - (4*cba**4*complex(0,1)*MHH**2*sb**4*sba)/vev + (4*cba**4*complex(0,1)*MHL**2*sb**4*sba)/vev + (3*cb**2*cba*complex(0,1)*m122*sba**2)/vev + (3*cb**4*cba*complex(0,1)*m122*sba**2)/(sb**2*vev) - (2*cb**5*cba**3*complex(0,1)*MHH**2*sba**2)/(sb*vev) - (3*cb**3*cba*complex(0,1)*MHL**2*sba**2)/(sb*vev) + (2*cb**5*cba**3*complex(0,1)*MHL**2*sba**2)/(sb*vev) - (6*cb*cba*complex(0,1)*MHH**2*sb*sba**2)/vev + (cb**3*cba**3*complex(0,1)*MHH**2*sb*sba**2)/vev + (6*cb*cba*complex(0,1)*MHL**2*sb*sba**2)/vev - (cb**3*cba**3*complex(0,1)*MHL**2*sb*sba**2)/vev - (3*cba*complex(0,1)*m122*sb**2*sba**2)/vev + (3*cba*complex(0,1)*MHH**2*sb**3*sba**2)/(cb*vev) + (2*cb*cba**3*complex(0,1)*MHH**2*sb**3*sba**2)/vev - (2*cb*cba**3*complex(0,1)*MHL**2*sb**3*sba**2)/vev - (3*cba*complex(0,1)*m122*sb**4*sba**2)/(cb**2*vev) - (cba**3*complex(0,1)*MHH**2*sb**5*sba**2)/(cb*vev) + (cba**3*complex(0,1)*MHL**2*sb**5*sba**2)/(cb*vev) + (3*cb**4*cba**2*complex(0,1)*MHH**2*sba**3)/vev - (3*cb**2*complex(0,1)*MHL**2*sba**3)/vev - (3*cb**4*cba**2*complex(0,1)*MHL**2*sba**3)/vev + (2*cb**3*complex(0,1)*m122*sba**3)/(sb*vev) + (4*cb*complex(0,1)*m122*sb*sba**3)/vev - (3*complex(0,1)*MHH**2*sb**2*sba**3)/vev + (2*complex(0,1)*m122*sb**3*sba**3)/(cb*vev) - (3*cba**2*complex(0,1)*MHH**2*sb**4*sba**3)/vev + (3*cba**2*complex(0,1)*MHL**2*sb**4*sba**3)/vev - (2*cb**5*cba*complex(0,1)*MHH**2*sba**4)/(sb*vev) + (2*cb**5*cba*complex(0,1)*MHL**2*sba**4)/(sb*vev) + (4*cb**3*cba*complex(0,1)*MHH**2*sb*sba**4)/vev - (4*cb**3*cba*complex(0,1)*MHL**2*sb*sba**4)/vev + (5*cb*cba*complex(0,1)*MHH**2*sb**3*sba**4)/vev - (5*cb*cba*complex(0,1)*MHL**2*sb**3*sba**4)/vev - (cba*complex(0,1)*MHH**2*sb**5*sba**4)/(cb*vev) + (cba*complex(0,1)*MHL**2*sb**5*sba**4)/(cb*vev) - (2*cb**4*complex(0,1)*MHH**2*sba**5)/vev + (2*cb**4*complex(0,1)*MHL**2*sba**5)/vev - (cb**2*complex(0,1)*MHH**2*sb**2*sba**5)/vev + (cb**2*complex(0,1)*MHL**2*sb**2*sba**5)/vev + (complex(0,1)*MHH**2*sb**4*sba**5)/vev - (complex(0,1)*MHL**2*sb**4*sba**5)/vev',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '-0.5*(cb**2*ee**2*complex(0,1)*vev)/cw - (ee**2*complex(0,1)*sb**2*vev)/(2.*cw)',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-0.25*(cb**2*ee**2*vev)/sw**2 - (ee**2*sb**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '(cb**2*ee**2*vev)/(4.*sw**2) + (ee**2*sb**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '-0.25*(cb**2*cba*ee**2*complex(0,1)*vev)/sw**2 - (cba*ee**2*complex(0,1)*sb**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '(cb**2*cba*ee**2*complex(0,1)*vev)/(2.*sw**2) + (cba*ee**2*complex(0,1)*sb**2*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '(cb**2*ee**2*complex(0,1)*vev)/(4.*cw) + (ee**2*complex(0,1)*sb**2*vev)/(4.*cw) - (cb**2*cw*ee**2*complex(0,1)*vev)/(4.*sw**2) - (cw*ee**2*complex(0,1)*sb**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(cb**2*ee**2*complex(0,1)*vev)/(4.*cw) + (ee**2*complex(0,1)*sb**2*vev)/(4.*cw) + (cb**2*cw*ee**2*complex(0,1)*vev)/(4.*sw**2) + (cw*ee**2*complex(0,1)*sb**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(complex(0,1)*I4a33)',
                 order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '-0.25*(cb**2*ee**2*complex(0,1)*sba*vev)/sw**2 - (ee**2*complex(0,1)*sb**2*sba*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '(cb**2*ee**2*complex(0,1)*sba*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sb**2*sba*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '-0.5*(cb**2*ee**2*complex(0,1)*vev)/sw - (ee**2*complex(0,1)*sb**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '(cb**2*ee**2*complex(0,1)*vev)/(2.*sw) + (ee**2*complex(0,1)*sb**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '-0.5*(cb**2*cba*ee**2*complex(0,1)*vev) - (cba*ee**2*complex(0,1)*sb**2*vev)/2. - (cb**2*cba*cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (cba*cw**2*ee**2*complex(0,1)*sb**2*vev)/(4.*sw**2) - (cb**2*cba*ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2) - (cba*ee**2*complex(0,1)*sb**2*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = 'cb**2*cba*ee**2*complex(0,1)*vev + cba*ee**2*complex(0,1)*sb**2*vev + (cb**2*cba*cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (cba*cw**2*ee**2*complex(0,1)*sb**2*vev)/(2.*sw**2) + (cb**2*cba*ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2) + (cba*ee**2*complex(0,1)*sb**2*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '-0.5*(cb**2*ee**2*complex(0,1)*sba*vev) - (ee**2*complex(0,1)*sb**2*sba*vev)/2. - (cb**2*cw**2*ee**2*complex(0,1)*sba*vev)/(4.*sw**2) - (cw**2*ee**2*complex(0,1)*sb**2*sba*vev)/(4.*sw**2) - (cb**2*ee**2*complex(0,1)*sba*sw**2*vev)/(4.*cw**2) - (ee**2*complex(0,1)*sb**2*sba*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = 'cb**2*ee**2*complex(0,1)*sba*vev + ee**2*complex(0,1)*sb**2*sba*vev + (cb**2*cw**2*ee**2*complex(0,1)*sba*vev)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*sb**2*sba*vev)/(2.*sw**2) + (cb**2*ee**2*complex(0,1)*sba*sw**2*vev)/(2.*cw**2) + (ee**2*complex(0,1)*sb**2*sba*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '-(yb/cmath.sqrt(2))',
                  order = {'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = 'yb/cmath.sqrt(2)',
                  order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '(cb*complex(0,1)*I2a33)/sb',
                 order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '-((sb*yb)/(cb*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(sb*yb)/(cb*cmath.sqrt(2))',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '(cba*complex(0,1)*sb*yb)/(cb*cmath.sqrt(2)) - (complex(0,1)*sba*yb)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((cba*complex(0,1)*yb)/cmath.sqrt(2)) - (complex(0,1)*sb*sba*yb)/(cb*cmath.sqrt(2))',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '-(yt/cmath.sqrt(2))',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = 'yt/cmath.sqrt(2)',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '-((cb*yt)/(sb*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '(cb*yt)/(sb*cmath.sqrt(2))',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '-((cb*cba*complex(0,1)*yt)/(sb*cmath.sqrt(2))) - (complex(0,1)*sba*yt)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '-((cba*complex(0,1)*yt)/cmath.sqrt(2)) + (cb*complex(0,1)*sba*yt)/(sb*cmath.sqrt(2))',
                  order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '(cb*complex(0,1)*I3a33)/sb',
                 order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '-(complex(0,1)*ytau)',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '-(ytau/cmath.sqrt(2))',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = 'ytau/cmath.sqrt(2)',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '(complex(0,1)*sb*ytau)/cb',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '-((sb*ytau)/(cb*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '(sb*ytau)/(cb*cmath.sqrt(2))',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '(cba*complex(0,1)*sb*ytau)/(cb*cmath.sqrt(2)) - (complex(0,1)*sba*ytau)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '-((cba*complex(0,1)*ytau)/cmath.sqrt(2)) - (complex(0,1)*sb*sba*ytau)/(cb*cmath.sqrt(2))',
                  order = {'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '(complex(0,1)*I1a33*sb)/cb',
                 order = {'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '(complex(0,1)*I4a33*sb)/cb',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '-(cb**2*ee*complex(0,1)) - ee*complex(0,1)*sb**2',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '2*cb**2*ee**2*complex(0,1) + 2*ee**2*complex(0,1)*sb**2',
                 order = {'QED':2})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '-0.5*(cb**2*ee**2)/cw - (ee**2*sb**2)/(2.*cw)',
                 order = {'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '(cb**2*ee**2)/(2.*cw) + (ee**2*sb**2)/(2.*cw)',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '-0.5*(cb**2*cba*ee**2*complex(0,1))/cw - (cba*ee**2*complex(0,1)*sb**2)/(2.*cw)',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '-0.5*(cb**2*ee**2*complex(0,1)*sba)/cw - (ee**2*complex(0,1)*sb**2*sba)/(2.*cw)',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '(cb**2*ee**2*complex(0,1)*sba)/(2.*cw) + (ee**2*complex(0,1)*sb**2*sba)/(2.*cw)',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '(cb**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sb**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '(cb**2*cba**2*ee**2*complex(0,1))/(2.*sw**2) + (cba**2*ee**2*complex(0,1)*sb**2)/(2.*sw**2) + (cb**2*ee**2*complex(0,1)*sba**2)/(2.*sw**2) + (ee**2*complex(0,1)*sb**2*sba**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-0.5*(cb**2*ee)/sw - (ee*sb**2)/(2.*sw)',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(cb**2*ee)/(2.*sw) + (ee*sb**2)/(2.*sw)',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '-0.5*(cb**2*cba*ee*complex(0,1))/sw - (cba*ee*complex(0,1)*sb**2)/(2.*sw)',
                 order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(cb**2*cba*ee*complex(0,1))/(2.*sw) + (cba*ee*complex(0,1)*sb**2)/(2.*sw)',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '-0.5*(cb**2*ee**2)/sw - (ee**2*sb**2)/(2.*sw)',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '(cb**2*ee**2)/(2.*sw) + (ee**2*sb**2)/(2.*sw)',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(cb**2*cba*ee**2*complex(0,1))/(2.*sw) + (cba*ee**2*complex(0,1)*sb**2)/(2.*sw)',
                 order = {'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '-0.5*(cb**2*ee*complex(0,1)*sba)/sw - (ee*complex(0,1)*sb**2*sba)/(2.*sw)',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(cb**2*ee*complex(0,1)*sba)/(2.*sw) + (ee*complex(0,1)*sb**2*sba)/(2.*sw)',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-0.5*(cb**2*ee**2*complex(0,1)*sba)/sw - (ee**2*complex(0,1)*sb**2*sba)/(2.*sw)',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '(cb**2*ee**2*complex(0,1)*sba)/(2.*sw) + (ee**2*complex(0,1)*sb**2*sba)/(2.*sw)',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-((cw*ee*complex(0,1))/sw)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '-0.5*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-0.5*(cw*ee*complex(0,1))/sw + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '-0.5*(cb**2*cw*ee*complex(0,1))/sw - (cw*ee*complex(0,1)*sb**2)/(2.*sw) + (cb**2*ee*complex(0,1)*sw)/(2.*cw) + (ee*complex(0,1)*sb**2*sw)/(2.*cw)',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-0.5*(cb**2*cba*cw*ee)/sw - (cba*cw*ee*sb**2)/(2.*sw) - (cb**2*cba*ee*sw)/(2.*cw) - (cba*ee*sb**2*sw)/(2.*cw)',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '(cb**2*cw*ee**2*complex(0,1))/sw + (cw*ee**2*complex(0,1)*sb**2)/sw - (cb**2*ee**2*complex(0,1)*sw)/cw - (ee**2*complex(0,1)*sb**2*sw)/cw',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '-0.5*(cb**2*cw*ee*sba)/sw - (cw*ee*sb**2*sba)/(2.*sw) - (cb**2*ee*sba*sw)/(2.*cw) - (ee*sb**2*sba*sw)/(2.*cw)',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '(cb**2*cw*ee*sba)/(2.*sw) + (cw*ee*sb**2*sba)/(2.*sw) + (cb**2*ee*sba*sw)/(2.*cw) + (ee*sb**2*sba*sw)/(2.*cw)',
                 order = {'QED':1})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-(cb**2*ee**2*complex(0,1)) - ee**2*complex(0,1)*sb**2 + (cb**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*sb**2)/(2.*sw**2) + (cb**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*sb**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = 'cb**2*ee**2*complex(0,1) + ee**2*complex(0,1)*sb**2 + (cb**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*sb**2)/(2.*sw**2) + (cb**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*sb**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = 'cb**2*cba**2*ee**2*complex(0,1) + cba**2*ee**2*complex(0,1)*sb**2 + cb**2*ee**2*complex(0,1)*sba**2 + ee**2*complex(0,1)*sb**2*sba**2 + (cb**2*cba**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (cba**2*cw**2*ee**2*complex(0,1)*sb**2)/(2.*sw**2) + (cb**2*cw**2*ee**2*complex(0,1)*sba**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*sb**2*sba**2)/(2.*sw**2) + (cb**2*cba**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2) + (cba**2*ee**2*complex(0,1)*sb**2*sw**2)/(2.*cw**2) + (cb**2*ee**2*complex(0,1)*sba**2*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*sb**2*sba**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '(cb**4*cba*MHA**2)/vev**2 - (cb**4*cba*MHp**2)/vev**2 + (2*cb**2*cba*MHA**2*sb**2)/vev**2 - (2*cb**2*cba*MHp**2*sb**2)/vev**2 + (cba*MHA**2*sb**4)/vev**2 - (cba*MHp**2*sb**4)/vev**2',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '-((cb**4*cba*MHA**2)/vev**2) + (cb**4*cba*MHp**2)/vev**2 - (2*cb**2*cba*MHA**2*sb**2)/vev**2 + (2*cb**2*cba*MHp**2*sb**2)/vev**2 - (cba*MHA**2*sb**4)/vev**2 + (cba*MHp**2*sb**4)/vev**2',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '(cb**4*MHA**2*sba)/vev**2 - (cb**4*MHp**2*sba)/vev**2 + (2*cb**2*MHA**2*sb**2*sba)/vev**2 - (2*cb**2*MHp**2*sb**2*sba)/vev**2 + (MHA**2*sb**4*sba)/vev**2 - (MHp**2*sb**4*sba)/vev**2',
                 order = {'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = '-((cb**4*MHA**2*sba)/vev**2) + (cb**4*MHp**2*sba)/vev**2 - (2*cb**2*MHA**2*sb**2*sba)/vev**2 + (2*cb**2*MHp**2*sb**2*sba)/vev**2 - (MHA**2*sb**4*sba)/vev**2 + (MHp**2*sb**4*sba)/vev**2',
                 order = {'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = '(cb**2*complex(0,1)*m122)/vev**2 + (cb**4*complex(0,1)*m122)/(sb**2*vev**2) - (cb**3*complex(0,1)*MHL**2)/(sb*vev**2) - (complex(0,1)*m122*sb**2)/vev**2 + (complex(0,1)*MHH**2*sb**3)/(cb*vev**2) - (cb*cba**2*complex(0,1)*MHH**2*sb**3)/vev**2 + (cb*cba**2*complex(0,1)*MHL**2*sb**3)/vev**2 - (complex(0,1)*m122*sb**4)/(cb**2*vev**2) - (cba**2*complex(0,1)*MHH**2*sb**5)/(cb*vev**2) + (cba**2*complex(0,1)*MHL**2*sb**5)/(cb*vev**2) + (cb**4*cba*complex(0,1)*MHH**2*sba)/vev**2 - (cb**4*cba*complex(0,1)*MHL**2*sba)/vev**2 + (2*cb**2*cba*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (2*cb**2*cba*complex(0,1)*MHL**2*sb**2*sba)/vev**2 + (cba*complex(0,1)*MHH**2*sb**4*sba)/vev**2 - (cba*complex(0,1)*MHL**2*sb**4*sba)/vev**2 - (cb**5*complex(0,1)*MHH**2*sba**2)/(sb*vev**2) + (cb**5*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) - (cb**3*complex(0,1)*MHH**2*sb*sba**2)/vev**2 + (cb**3*complex(0,1)*MHL**2*sb*sba**2)/vev**2',
                 order = {'QED':2})

GC_68 = Coupling(name = 'GC_68',
                 value = '(2*cb**2*complex(0,1)*m122)/vev**2 + (2*cb**4*complex(0,1)*m122)/(sb**2*vev**2) - (2*cb**3*complex(0,1)*MHL**2)/(sb*vev**2) - (2*complex(0,1)*m122*sb**2)/vev**2 + (2*complex(0,1)*MHH**2*sb**3)/(cb*vev**2) - (2*cb*cba**2*complex(0,1)*MHH**2*sb**3)/vev**2 + (2*cb*cba**2*complex(0,1)*MHL**2*sb**3)/vev**2 - (2*complex(0,1)*m122*sb**4)/(cb**2*vev**2) - (2*cba**2*complex(0,1)*MHH**2*sb**5)/(cb*vev**2) + (2*cba**2*complex(0,1)*MHL**2*sb**5)/(cb*vev**2) + (2*cb**4*cba*complex(0,1)*MHH**2*sba)/vev**2 - (2*cb**4*cba*complex(0,1)*MHL**2*sba)/vev**2 + (4*cb**2*cba*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (4*cb**2*cba*complex(0,1)*MHL**2*sb**2*sba)/vev**2 + (2*cba*complex(0,1)*MHH**2*sb**4*sba)/vev**2 - (2*cba*complex(0,1)*MHL**2*sb**4*sba)/vev**2 - (2*cb**5*complex(0,1)*MHH**2*sba**2)/(sb*vev**2) + (2*cb**5*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) - (2*cb**3*complex(0,1)*MHH**2*sb*sba**2)/vev**2 + (2*cb**3*complex(0,1)*MHL**2*sb*sba**2)/vev**2',
                 order = {'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '(3*cb**2*complex(0,1)*m122)/vev**2 + (3*cb**4*complex(0,1)*m122)/(sb**2*vev**2) - (3*cb**3*complex(0,1)*MHL**2)/(sb*vev**2) - (3*complex(0,1)*m122*sb**2)/vev**2 + (3*complex(0,1)*MHH**2*sb**3)/(cb*vev**2) - (3*cb*cba**2*complex(0,1)*MHH**2*sb**3)/vev**2 + (3*cb*cba**2*complex(0,1)*MHL**2*sb**3)/vev**2 - (3*complex(0,1)*m122*sb**4)/(cb**2*vev**2) - (3*cba**2*complex(0,1)*MHH**2*sb**5)/(cb*vev**2) + (3*cba**2*complex(0,1)*MHL**2*sb**5)/(cb*vev**2) + (3*cb**4*cba*complex(0,1)*MHH**2*sba)/vev**2 - (3*cb**4*cba*complex(0,1)*MHL**2*sba)/vev**2 + (6*cb**2*cba*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (6*cb**2*cba*complex(0,1)*MHL**2*sb**2*sba)/vev**2 + (3*cba*complex(0,1)*MHH**2*sb**4*sba)/vev**2 - (3*cba*complex(0,1)*MHL**2*sb**4*sba)/vev**2 - (3*cb**5*complex(0,1)*MHH**2*sba**2)/(sb*vev**2) + (3*cb**5*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) - (3*cb**3*complex(0,1)*MHH**2*sb*sba**2)/vev**2 + (3*cb**3*complex(0,1)*MHL**2*sb*sba**2)/vev**2',
                 order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-((cb**2*complex(0,1)*MHH**2)/vev**2) - (cb**2*cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 - (complex(0,1)*MHL**2*sb**2)/vev**2 + (cb**2*cba**2*complex(0,1)*MHL**2*sb**2)/vev**2 - (cba**2*complex(0,1)*MHH**2*sb**4)/vev**2 + (cba**2*complex(0,1)*MHL**2*sb**4)/vev**2 + (cb**4*complex(0,1)*MHH**2*sba**2)/vev**2 - (cb**4*complex(0,1)*MHL**2*sba**2)/vev**2 + (cb**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (cb**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2',
                 order = {'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '-((cb**2*complex(0,1)*MHL**2)/vev**2) + (cb**4*complex(0,1)*MHp**2)/vev**2 - (complex(0,1)*MHH**2*sb**2)/vev**2 + (cb**2*cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 - (cb**2*cba**2*complex(0,1)*MHL**2*sb**2)/vev**2 + (2*cb**2*complex(0,1)*MHp**2*sb**2)/vev**2 + (cba**2*complex(0,1)*MHH**2*sb**4)/vev**2 - (cba**2*complex(0,1)*MHL**2*sb**4)/vev**2 + (complex(0,1)*MHp**2*sb**4)/vev**2 - (cb**4*complex(0,1)*MHH**2*sba**2)/vev**2 + (cb**4*complex(0,1)*MHL**2*sba**2)/vev**2 - (cb**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 + (cb**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2',
                 order = {'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '(-2*cb**2*complex(0,1)*MHH**2)/vev**2 - (2*cb**2*cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 - (2*complex(0,1)*MHL**2*sb**2)/vev**2 + (2*cb**2*cba**2*complex(0,1)*MHL**2*sb**2)/vev**2 - (2*cba**2*complex(0,1)*MHH**2*sb**4)/vev**2 + (2*cba**2*complex(0,1)*MHL**2*sb**4)/vev**2 + (2*cb**4*complex(0,1)*MHH**2*sba**2)/vev**2 - (2*cb**4*complex(0,1)*MHL**2*sba**2)/vev**2 + (2*cb**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (2*cb**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2',
                 order = {'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '(2*cb**4*complex(0,1)*MHA**2)/vev**2 - (2*cb**2*complex(0,1)*MHL**2)/vev**2 + (4*cb**2*complex(0,1)*MHA**2*sb**2)/vev**2 - (2*complex(0,1)*MHH**2*sb**2)/vev**2 + (2*cb**2*cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 - (2*cb**2*cba**2*complex(0,1)*MHL**2*sb**2)/vev**2 + (2*complex(0,1)*MHA**2*sb**4)/vev**2 + (2*cba**2*complex(0,1)*MHH**2*sb**4)/vev**2 - (2*cba**2*complex(0,1)*MHL**2*sb**4)/vev**2 - (2*cb**4*complex(0,1)*MHH**2*sba**2)/vev**2 + (2*cb**4*complex(0,1)*MHL**2*sba**2)/vev**2 - (2*cb**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 + (2*cb**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2',
                 order = {'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '(-3*cb**2*complex(0,1)*MHH**2)/vev**2 - (3*cb**2*cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 - (3*complex(0,1)*MHL**2*sb**2)/vev**2 + (3*cb**2*cba**2*complex(0,1)*MHL**2*sb**2)/vev**2 - (3*cba**2*complex(0,1)*MHH**2*sb**4)/vev**2 + (3*cba**2*complex(0,1)*MHL**2*sb**4)/vev**2 + (3*cb**4*complex(0,1)*MHH**2*sba**2)/vev**2 - (3*cb**4*complex(0,1)*MHL**2*sba**2)/vev**2 + (3*cb**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (3*cb**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2',
                 order = {'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '(cb*complex(0,1)*MHH**2*sb)/vev**2 - (cb**3*cba**2*complex(0,1)*MHH**2*sb)/vev**2 - (cb*complex(0,1)*MHL**2*sb)/vev**2 + (cb**3*cba**2*complex(0,1)*MHL**2*sb)/vev**2 - (cb*cba**2*complex(0,1)*MHH**2*sb**3)/vev**2 + (cb*cba**2*complex(0,1)*MHL**2*sb**3)/vev**2 + (cb**4*cba*complex(0,1)*MHH**2*sba)/vev**2 - (cb**4*cba*complex(0,1)*MHL**2*sba)/vev**2 + (2*cb**2*cba*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (2*cb**2*cba*complex(0,1)*MHL**2*sb**2*sba)/vev**2 + (cba*complex(0,1)*MHH**2*sb**4*sba)/vev**2 - (cba*complex(0,1)*MHL**2*sb**4*sba)/vev**2 - (cb**3*complex(0,1)*MHH**2*sb*sba**2)/vev**2 + (cb**3*complex(0,1)*MHL**2*sb*sba**2)/vev**2 - (cb*complex(0,1)*MHH**2*sb**3*sba**2)/vev**2 + (cb*complex(0,1)*MHL**2*sb**3*sba**2)/vev**2',
                 order = {'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '(2*cb*complex(0,1)*MHH**2*sb)/vev**2 - (2*cb**3*cba**2*complex(0,1)*MHH**2*sb)/vev**2 - (2*cb*complex(0,1)*MHL**2*sb)/vev**2 + (2*cb**3*cba**2*complex(0,1)*MHL**2*sb)/vev**2 - (2*cb*cba**2*complex(0,1)*MHH**2*sb**3)/vev**2 + (2*cb*cba**2*complex(0,1)*MHL**2*sb**3)/vev**2 + (2*cb**4*cba*complex(0,1)*MHH**2*sba)/vev**2 - (2*cb**4*cba*complex(0,1)*MHL**2*sba)/vev**2 + (4*cb**2*cba*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (4*cb**2*cba*complex(0,1)*MHL**2*sb**2*sba)/vev**2 + (2*cba*complex(0,1)*MHH**2*sb**4*sba)/vev**2 - (2*cba*complex(0,1)*MHL**2*sb**4*sba)/vev**2 - (2*cb**3*complex(0,1)*MHH**2*sb*sba**2)/vev**2 + (2*cb**3*complex(0,1)*MHL**2*sb*sba**2)/vev**2 - (2*cb*complex(0,1)*MHH**2*sb**3*sba**2)/vev**2 + (2*cb*complex(0,1)*MHL**2*sb**3*sba**2)/vev**2',
                 order = {'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '(3*cb*complex(0,1)*MHH**2*sb)/vev**2 - (3*cb**3*cba**2*complex(0,1)*MHH**2*sb)/vev**2 - (3*cb*complex(0,1)*MHL**2*sb)/vev**2 + (3*cb**3*cba**2*complex(0,1)*MHL**2*sb)/vev**2 - (3*cb*cba**2*complex(0,1)*MHH**2*sb**3)/vev**2 + (3*cb*cba**2*complex(0,1)*MHL**2*sb**3)/vev**2 + (3*cb**4*cba*complex(0,1)*MHH**2*sba)/vev**2 - (3*cb**4*cba*complex(0,1)*MHL**2*sba)/vev**2 + (6*cb**2*cba*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (6*cb**2*cba*complex(0,1)*MHL**2*sb**2*sba)/vev**2 + (3*cba*complex(0,1)*MHH**2*sb**4*sba)/vev**2 - (3*cba*complex(0,1)*MHL**2*sb**4*sba)/vev**2 - (3*cb**3*complex(0,1)*MHH**2*sb*sba**2)/vev**2 + (3*cb**3*complex(0,1)*MHL**2*sb*sba**2)/vev**2 - (3*cb*complex(0,1)*MHH**2*sb**3*sba**2)/vev**2 + (3*cb*complex(0,1)*MHL**2*sb**3*sba**2)/vev**2',
                 order = {'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '-((cb**4*complex(0,1)*MHA**2)/vev**2) - (cb**4*cba**2*complex(0,1)*MHH**2)/vev**2 - (2*cb**2*complex(0,1)*MHL**2)/vev**2 + (cb**4*cba**2*complex(0,1)*MHL**2)/vev**2 + (2*cb**3*complex(0,1)*m122)/(sb*vev**2) + (4*cb*complex(0,1)*m122*sb)/vev**2 - (2*cb**2*complex(0,1)*MHA**2*sb**2)/vev**2 - (2*complex(0,1)*MHH**2*sb**2)/vev**2 + (2*complex(0,1)*m122*sb**3)/(cb*vev**2) - (complex(0,1)*MHA**2*sb**4)/vev**2 + (cba**2*complex(0,1)*MHH**2*sb**4)/vev**2 - (cba**2*complex(0,1)*MHL**2*sb**4)/vev**2 + (cb**5*cba*complex(0,1)*MHH**2*sba)/(sb*vev**2) - (cb**5*cba*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (cb**3*cba*complex(0,1)*MHH**2*sb*sba)/vev**2 - (cb**3*cba*complex(0,1)*MHL**2*sb*sba)/vev**2 - (cb*cba*complex(0,1)*MHH**2*sb**3*sba)/vev**2 + (cb*cba*complex(0,1)*MHL**2*sb**3*sba)/vev**2 - (cba*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) + (cba*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) - (cb**4*complex(0,1)*MHH**2*sba**2)/vev**2 + (cb**4*complex(0,1)*MHL**2*sba**2)/vev**2 + (complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 - (complex(0,1)*MHL**2*sb**4*sba**2)/vev**2',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '-((cb**4*cba**2*complex(0,1)*MHH**2)/vev**2) - (cb**2*complex(0,1)*MHL**2)/vev**2 + (cb**4*cba**2*complex(0,1)*MHL**2)/vev**2 - (2*cb**4*complex(0,1)*MHp**2)/vev**2 + (2*cb**3*complex(0,1)*m122)/(sb*vev**2) + (4*cb*complex(0,1)*m122*sb)/vev**2 - (complex(0,1)*MHH**2*sb**2)/vev**2 - (cb**2*cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 + (cb**2*cba**2*complex(0,1)*MHL**2*sb**2)/vev**2 - (4*cb**2*complex(0,1)*MHp**2*sb**2)/vev**2 + (2*complex(0,1)*m122*sb**3)/(cb*vev**2) - (2*complex(0,1)*MHp**2*sb**4)/vev**2 + (cb**5*cba*complex(0,1)*MHH**2*sba)/(sb*vev**2) - (cb**5*cba*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (cb**3*cba*complex(0,1)*MHH**2*sb*sba)/vev**2 - (cb**3*cba*complex(0,1)*MHL**2*sb*sba)/vev**2 - (cb*cba*complex(0,1)*MHH**2*sb**3*sba)/vev**2 + (cb*cba*complex(0,1)*MHL**2*sb**3*sba)/vev**2 - (cba*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) + (cba*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) + (cb**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (cb**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 + (complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 - (complex(0,1)*MHL**2*sb**4*sba**2)/vev**2',
                 order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '-(complex(0,1)*G**2)',
                order = {'QCD':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '-((cb**4*cba**2*complex(0,1)*MHH**2)/vev**2) - (3*cb**2*complex(0,1)*MHL**2)/vev**2 + (cb**4*cba**2*complex(0,1)*MHL**2)/vev**2 + (2*cb**3*complex(0,1)*m122)/(sb*vev**2) + (4*cb*complex(0,1)*m122*sb)/vev**2 - (3*complex(0,1)*MHH**2*sb**2)/vev**2 + (cb**2*cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 - (cb**2*cba**2*complex(0,1)*MHL**2*sb**2)/vev**2 + (2*complex(0,1)*m122*sb**3)/(cb*vev**2) + (2*cba**2*complex(0,1)*MHH**2*sb**4)/vev**2 - (2*cba**2*complex(0,1)*MHL**2*sb**4)/vev**2 + (cb**5*cba*complex(0,1)*MHH**2*sba)/(sb*vev**2) - (cb**5*cba*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (cb**3*cba*complex(0,1)*MHH**2*sb*sba)/vev**2 - (cb**3*cba*complex(0,1)*MHL**2*sb*sba)/vev**2 - (cb*cba*complex(0,1)*MHH**2*sb**3*sba)/vev**2 + (cb*cba*complex(0,1)*MHL**2*sb**3*sba)/vev**2 - (cba*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) + (cba*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) - (2*cb**4*complex(0,1)*MHH**2*sba**2)/vev**2 + (2*cb**4*complex(0,1)*MHL**2*sba**2)/vev**2 - (cb**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 + (cb**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 + (complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 - (complex(0,1)*MHL**2*sb**4*sba**2)/vev**2',
                 order = {'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '-((cb**4*cba**2*complex(0,1)*MHH**2)/vev**2) + (cb**4*cba**2*complex(0,1)*MHL**2)/vev**2 + (cb**5*complex(0,1)*m122)/(sb**3*vev**2) - (cb**4*complex(0,1)*MHL**2)/(sb**2*vev**2) - (2*cb*complex(0,1)*m122*sb)/vev**2 - (2*cb**2*cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 + (2*cb**2*cba**2*complex(0,1)*MHL**2*sb**2)/vev**2 - (complex(0,1)*MHH**2*sb**4)/(cb**2*vev**2) + (complex(0,1)*m122*sb**5)/(cb**3*vev**2) + (cba**2*complex(0,1)*MHH**2*sb**6)/(cb**2*vev**2) - (cba**2*complex(0,1)*MHL**2*sb**6)/(cb**2*vev**2) + (2*cb**5*cba*complex(0,1)*MHH**2*sba)/(sb*vev**2) - (2*cb**5*cba*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (2*cb**3*cba*complex(0,1)*MHH**2*sb*sba)/vev**2 - (2*cb**3*cba*complex(0,1)*MHL**2*sb*sba)/vev**2 - (2*cb*cba*complex(0,1)*MHH**2*sb**3*sba)/vev**2 + (2*cb*cba*complex(0,1)*MHL**2*sb**3*sba)/vev**2 - (2*cba*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) + (2*cba*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) - (cb**6*complex(0,1)*MHH**2*sba**2)/(sb**2*vev**2) + (cb**6*complex(0,1)*MHL**2*sba**2)/(sb**2*vev**2) + (2*cb**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (2*cb**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 + (complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 - (complex(0,1)*MHL**2*sb**4*sba**2)/vev**2',
                 order = {'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '(-2*cb**4*cba**2*complex(0,1)*MHH**2)/vev**2 + (2*cb**4*cba**2*complex(0,1)*MHL**2)/vev**2 + (2*cb**5*complex(0,1)*m122)/(sb**3*vev**2) - (2*cb**4*complex(0,1)*MHL**2)/(sb**2*vev**2) - (4*cb*complex(0,1)*m122*sb)/vev**2 - (4*cb**2*cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 + (4*cb**2*cba**2*complex(0,1)*MHL**2*sb**2)/vev**2 - (2*complex(0,1)*MHH**2*sb**4)/(cb**2*vev**2) + (2*complex(0,1)*m122*sb**5)/(cb**3*vev**2) + (2*cba**2*complex(0,1)*MHH**2*sb**6)/(cb**2*vev**2) - (2*cba**2*complex(0,1)*MHL**2*sb**6)/(cb**2*vev**2) + (4*cb**5*cba*complex(0,1)*MHH**2*sba)/(sb*vev**2) - (4*cb**5*cba*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (4*cb**3*cba*complex(0,1)*MHH**2*sb*sba)/vev**2 - (4*cb**3*cba*complex(0,1)*MHL**2*sb*sba)/vev**2 - (4*cb*cba*complex(0,1)*MHH**2*sb**3*sba)/vev**2 + (4*cb*cba*complex(0,1)*MHL**2*sb**3*sba)/vev**2 - (4*cba*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) + (4*cba*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) - (2*cb**6*complex(0,1)*MHH**2*sba**2)/(sb**2*vev**2) + (2*cb**6*complex(0,1)*MHL**2*sba**2)/(sb**2*vev**2) + (4*cb**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (4*cb**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 + (2*complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 - (2*complex(0,1)*MHL**2*sb**4*sba**2)/vev**2',
                 order = {'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '(-3*cb**4*cba**2*complex(0,1)*MHH**2)/vev**2 + (3*cb**4*cba**2*complex(0,1)*MHL**2)/vev**2 + (3*cb**5*complex(0,1)*m122)/(sb**3*vev**2) - (3*cb**4*complex(0,1)*MHL**2)/(sb**2*vev**2) - (6*cb*complex(0,1)*m122*sb)/vev**2 - (6*cb**2*cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 + (6*cb**2*cba**2*complex(0,1)*MHL**2*sb**2)/vev**2 - (3*complex(0,1)*MHH**2*sb**4)/(cb**2*vev**2) + (3*complex(0,1)*m122*sb**5)/(cb**3*vev**2) + (3*cba**2*complex(0,1)*MHH**2*sb**6)/(cb**2*vev**2) - (3*cba**2*complex(0,1)*MHL**2*sb**6)/(cb**2*vev**2) + (6*cb**5*cba*complex(0,1)*MHH**2*sba)/(sb*vev**2) - (6*cb**5*cba*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (6*cb**3*cba*complex(0,1)*MHH**2*sb*sba)/vev**2 - (6*cb**3*cba*complex(0,1)*MHL**2*sb*sba)/vev**2 - (6*cb*cba*complex(0,1)*MHH**2*sb**3*sba)/vev**2 + (6*cb*cba*complex(0,1)*MHL**2*sb**3*sba)/vev**2 - (6*cba*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) + (6*cba*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) - (3*cb**6*complex(0,1)*MHH**2*sba**2)/(sb**2*vev**2) + (3*cb**6*complex(0,1)*MHL**2*sba**2)/(sb**2*vev**2) + (6*cb**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (6*cb**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 + (3*complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 - (3*complex(0,1)*MHL**2*sb**4*sba**2)/vev**2',
                 order = {'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '(cb**2*cba**2*complex(0,1)*m122)/vev**2 + (cb**4*cba**2*complex(0,1)*m122)/(sb**2*vev**2) - (cb**3*cba**2*complex(0,1)*MHL**2)/(sb*vev**2) - (cba**2*complex(0,1)*m122*sb**2)/vev**2 + (cba**2*complex(0,1)*MHH**2*sb**3)/(cb*vev**2) - (cb*cba**4*complex(0,1)*MHH**2*sb**3)/vev**2 + (cb*cba**4*complex(0,1)*MHL**2*sb**3)/vev**2 - (cba**2*complex(0,1)*m122*sb**4)/(cb**2*vev**2) - (cba**4*complex(0,1)*MHH**2*sb**5)/(cb*vev**2) + (cba**4*complex(0,1)*MHL**2*sb**5)/(cb*vev**2) - (2*cb**4*cba*complex(0,1)*MHA**2*sba)/vev**2 + (cb**4*cba**3*complex(0,1)*MHH**2*sba)/vev**2 - (cb**2*cba*complex(0,1)*MHL**2*sba)/vev**2 - (cb**4*cba**3*complex(0,1)*MHL**2*sba)/vev**2 - (cb**5*cba*complex(0,1)*m122*sba)/(sb**3*vev**2) + (cb**4*cba*complex(0,1)*MHL**2*sba)/(sb**2*vev**2) + (2*cb**3*cba*complex(0,1)*m122*sba)/(sb*vev**2) + (6*cb*cba*complex(0,1)*m122*sb*sba)/vev**2 - (4*cb**2*cba*complex(0,1)*MHA**2*sb**2*sba)/vev**2 - (cba*complex(0,1)*MHH**2*sb**2*sba)/vev**2 + (3*cb**2*cba**3*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (3*cb**2*cba**3*complex(0,1)*MHL**2*sb**2*sba)/vev**2 + (2*cba*complex(0,1)*m122*sb**3*sba)/(cb*vev**2) - (2*cba*complex(0,1)*MHA**2*sb**4*sba)/vev**2 + (cba*complex(0,1)*MHH**2*sb**4*sba)/(cb**2*vev**2) + (cba**3*complex(0,1)*MHH**2*sb**4*sba)/vev**2 - (cba**3*complex(0,1)*MHL**2*sb**4*sba)/vev**2 - (cba*complex(0,1)*m122*sb**5*sba)/(cb**3*vev**2) - (cba**3*complex(0,1)*MHH**2*sb**6*sba)/(cb**2*vev**2) + (cba**3*complex(0,1)*MHL**2*sb**6*sba)/(cb**2*vev**2) - (cb**2*complex(0,1)*m122*sba**2)/vev**2 - (cb**4*complex(0,1)*m122*sba**2)/(sb**2*vev**2) - (2*cb**5*cba**2*complex(0,1)*MHH**2*sba**2)/(sb*vev**2) + (cb**3*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) + (2*cb**5*cba**2*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) - (2*cb**3*cba**2*complex(0,1)*MHH**2*sb*sba**2)/vev**2 + (2*cb**3*cba**2*complex(0,1)*MHL**2*sb*sba**2)/vev**2 + (complex(0,1)*m122*sb**2*sba**2)/vev**2 - (complex(0,1)*MHH**2*sb**3*sba**2)/(cb*vev**2) + (2*cb*cba**2*complex(0,1)*MHH**2*sb**3*sba**2)/vev**2 - (2*cb*cba**2*complex(0,1)*MHL**2*sb**3*sba**2)/vev**2 + (complex(0,1)*m122*sb**4*sba**2)/(cb**2*vev**2) + (2*cba**2*complex(0,1)*MHH**2*sb**5*sba**2)/(cb*vev**2) - (2*cba**2*complex(0,1)*MHL**2*sb**5*sba**2)/(cb*vev**2) - (cb**4*cba*complex(0,1)*MHH**2*sba**3)/vev**2 + (cb**4*cba*complex(0,1)*MHL**2*sba**3)/vev**2 + (cb**6*cba*complex(0,1)*MHH**2*sba**3)/(sb**2*vev**2) - (cb**6*cba*complex(0,1)*MHL**2*sba**3)/(sb**2*vev**2) - (3*cb**2*cba*complex(0,1)*MHH**2*sb**2*sba**3)/vev**2 + (3*cb**2*cba*complex(0,1)*MHL**2*sb**2*sba**3)/vev**2 - (cba*complex(0,1)*MHH**2*sb**4*sba**3)/vev**2 + (cba*complex(0,1)*MHL**2*sb**4*sba**3)/vev**2 + (cb**5*complex(0,1)*MHH**2*sba**4)/(sb*vev**2) - (cb**5*complex(0,1)*MHL**2*sba**4)/(sb*vev**2) + (cb**3*complex(0,1)*MHH**2*sb*sba**4)/vev**2 - (cb**3*complex(0,1)*MHL**2*sb*sba**4)/vev**2',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '(cb**2*cba**2*complex(0,1)*m122)/vev**2 + (cb**4*cba**2*complex(0,1)*m122)/(sb**2*vev**2) - (cb**3*cba**2*complex(0,1)*MHL**2)/(sb*vev**2) - (cba**2*complex(0,1)*m122*sb**2)/vev**2 + (cba**2*complex(0,1)*MHH**2*sb**3)/(cb*vev**2) - (cb*cba**4*complex(0,1)*MHH**2*sb**3)/vev**2 + (cb*cba**4*complex(0,1)*MHL**2*sb**3)/vev**2 - (cba**2*complex(0,1)*m122*sb**4)/(cb**2*vev**2) - (cba**4*complex(0,1)*MHH**2*sb**5)/(cb*vev**2) + (cba**4*complex(0,1)*MHL**2*sb**5)/(cb*vev**2) + (cb**4*cba**3*complex(0,1)*MHH**2*sba)/vev**2 - (cb**2*cba*complex(0,1)*MHL**2*sba)/vev**2 - (cb**4*cba**3*complex(0,1)*MHL**2*sba)/vev**2 - (2*cb**4*cba*complex(0,1)*MHp**2*sba)/vev**2 - (cb**5*cba*complex(0,1)*m122*sba)/(sb**3*vev**2) + (cb**4*cba*complex(0,1)*MHL**2*sba)/(sb**2*vev**2) + (2*cb**3*cba*complex(0,1)*m122*sba)/(sb*vev**2) + (6*cb*cba*complex(0,1)*m122*sb*sba)/vev**2 - (cba*complex(0,1)*MHH**2*sb**2*sba)/vev**2 + (3*cb**2*cba**3*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (3*cb**2*cba**3*complex(0,1)*MHL**2*sb**2*sba)/vev**2 - (4*cb**2*cba*complex(0,1)*MHp**2*sb**2*sba)/vev**2 + (2*cba*complex(0,1)*m122*sb**3*sba)/(cb*vev**2) + (cba*complex(0,1)*MHH**2*sb**4*sba)/(cb**2*vev**2) + (cba**3*complex(0,1)*MHH**2*sb**4*sba)/vev**2 - (cba**3*complex(0,1)*MHL**2*sb**4*sba)/vev**2 - (2*cba*complex(0,1)*MHp**2*sb**4*sba)/vev**2 - (cba*complex(0,1)*m122*sb**5*sba)/(cb**3*vev**2) - (cba**3*complex(0,1)*MHH**2*sb**6*sba)/(cb**2*vev**2) + (cba**3*complex(0,1)*MHL**2*sb**6*sba)/(cb**2*vev**2) - (cb**2*complex(0,1)*m122*sba**2)/vev**2 - (cb**4*complex(0,1)*m122*sba**2)/(sb**2*vev**2) - (2*cb**5*cba**2*complex(0,1)*MHH**2*sba**2)/(sb*vev**2) + (cb**3*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) + (2*cb**5*cba**2*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) - (2*cb**3*cba**2*complex(0,1)*MHH**2*sb*sba**2)/vev**2 + (2*cb**3*cba**2*complex(0,1)*MHL**2*sb*sba**2)/vev**2 + (complex(0,1)*m122*sb**2*sba**2)/vev**2 - (complex(0,1)*MHH**2*sb**3*sba**2)/(cb*vev**2) + (2*cb*cba**2*complex(0,1)*MHH**2*sb**3*sba**2)/vev**2 - (2*cb*cba**2*complex(0,1)*MHL**2*sb**3*sba**2)/vev**2 + (complex(0,1)*m122*sb**4*sba**2)/(cb**2*vev**2) + (2*cba**2*complex(0,1)*MHH**2*sb**5*sba**2)/(cb*vev**2) - (2*cba**2*complex(0,1)*MHL**2*sb**5*sba**2)/(cb*vev**2) - (cb**4*cba*complex(0,1)*MHH**2*sba**3)/vev**2 + (cb**4*cba*complex(0,1)*MHL**2*sba**3)/vev**2 + (cb**6*cba*complex(0,1)*MHH**2*sba**3)/(sb**2*vev**2) - (cb**6*cba*complex(0,1)*MHL**2*sba**3)/(sb**2*vev**2) - (3*cb**2*cba*complex(0,1)*MHH**2*sb**2*sba**3)/vev**2 + (3*cb**2*cba*complex(0,1)*MHL**2*sb**2*sba**3)/vev**2 - (cba*complex(0,1)*MHH**2*sb**4*sba**3)/vev**2 + (cba*complex(0,1)*MHL**2*sb**4*sba**3)/vev**2 + (cb**5*complex(0,1)*MHH**2*sba**4)/(sb*vev**2) - (cb**5*complex(0,1)*MHL**2*sba**4)/(sb*vev**2) + (cb**3*complex(0,1)*MHH**2*sb*sba**4)/vev**2 - (cb**3*complex(0,1)*MHL**2*sb*sba**4)/vev**2',
                 order = {'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '(cb*cba**2*complex(0,1)*MHH**2*sb)/vev**2 - (cb**3*cba**4*complex(0,1)*MHH**2*sb)/vev**2 - (cb*cba**2*complex(0,1)*MHL**2*sb)/vev**2 + (cb**3*cba**4*complex(0,1)*MHL**2*sb)/vev**2 - (cb*cba**4*complex(0,1)*MHH**2*sb**3)/vev**2 + (cb*cba**4*complex(0,1)*MHL**2*sb**3)/vev**2 - (2*cb**4*cba*complex(0,1)*MHA**2*sba)/vev**2 + (cb**4*cba**3*complex(0,1)*MHH**2*sba)/vev**2 + (2*cb**2*cba*complex(0,1)*MHL**2*sba)/vev**2 - (cb**4*cba**3*complex(0,1)*MHL**2*sba)/vev**2 - (4*cb**2*cba*complex(0,1)*MHA**2*sb**2*sba)/vev**2 + (2*cba*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (2*cba*complex(0,1)*MHA**2*sb**4*sba)/vev**2 - (cba**3*complex(0,1)*MHH**2*sb**4*sba)/vev**2 + (cba**3*complex(0,1)*MHL**2*sb**4*sba)/vev**2 + (cb**2*complex(0,1)*m122*sba**2)/vev**2 + (cb**4*complex(0,1)*m122*sba**2)/(sb**2*vev**2) - (cb**3*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) - (cb**3*cba**2*complex(0,1)*MHH**2*sb*sba**2)/vev**2 + (cb**3*cba**2*complex(0,1)*MHL**2*sb*sba**2)/vev**2 - (complex(0,1)*m122*sb**2*sba**2)/vev**2 + (complex(0,1)*MHH**2*sb**3*sba**2)/(cb*vev**2) - (2*cb*cba**2*complex(0,1)*MHH**2*sb**3*sba**2)/vev**2 + (2*cb*cba**2*complex(0,1)*MHL**2*sb**3*sba**2)/vev**2 - (complex(0,1)*m122*sb**4*sba**2)/(cb**2*vev**2) - (cba**2*complex(0,1)*MHH**2*sb**5*sba**2)/(cb*vev**2) + (cba**2*complex(0,1)*MHL**2*sb**5*sba**2)/(cb*vev**2) + (3*cb**4*cba*complex(0,1)*MHH**2*sba**3)/vev**2 - (3*cb**4*cba*complex(0,1)*MHL**2*sba**3)/vev**2 + (4*cb**2*cba*complex(0,1)*MHH**2*sb**2*sba**3)/vev**2 - (4*cb**2*cba*complex(0,1)*MHL**2*sb**2*sba**3)/vev**2 + (cba*complex(0,1)*MHH**2*sb**4*sba**3)/vev**2 - (cba*complex(0,1)*MHL**2*sb**4*sba**3)/vev**2 - (cb**5*complex(0,1)*MHH**2*sba**4)/(sb*vev**2) + (cb**5*complex(0,1)*MHL**2*sba**4)/(sb*vev**2) - (cb**3*complex(0,1)*MHH**2*sb*sba**4)/vev**2 + (cb**3*complex(0,1)*MHL**2*sb*sba**4)/vev**2',
                 order = {'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '(cb*cba**2*complex(0,1)*MHH**2*sb)/vev**2 - (cb**3*cba**4*complex(0,1)*MHH**2*sb)/vev**2 - (cb*cba**2*complex(0,1)*MHL**2*sb)/vev**2 + (cb**3*cba**4*complex(0,1)*MHL**2*sb)/vev**2 - (cb*cba**4*complex(0,1)*MHH**2*sb**3)/vev**2 + (cb*cba**4*complex(0,1)*MHL**2*sb**3)/vev**2 + (cb**4*cba**3*complex(0,1)*MHH**2*sba)/vev**2 + (2*cb**2*cba*complex(0,1)*MHL**2*sba)/vev**2 - (cb**4*cba**3*complex(0,1)*MHL**2*sba)/vev**2 - (2*cb**4*cba*complex(0,1)*MHp**2*sba)/vev**2 + (2*cba*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (4*cb**2*cba*complex(0,1)*MHp**2*sb**2*sba)/vev**2 - (cba**3*complex(0,1)*MHH**2*sb**4*sba)/vev**2 + (cba**3*complex(0,1)*MHL**2*sb**4*sba)/vev**2 - (2*cba*complex(0,1)*MHp**2*sb**4*sba)/vev**2 + (cb**2*complex(0,1)*m122*sba**2)/vev**2 + (cb**4*complex(0,1)*m122*sba**2)/(sb**2*vev**2) - (cb**3*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) - (cb**3*cba**2*complex(0,1)*MHH**2*sb*sba**2)/vev**2 + (cb**3*cba**2*complex(0,1)*MHL**2*sb*sba**2)/vev**2 - (complex(0,1)*m122*sb**2*sba**2)/vev**2 + (complex(0,1)*MHH**2*sb**3*sba**2)/(cb*vev**2) - (2*cb*cba**2*complex(0,1)*MHH**2*sb**3*sba**2)/vev**2 + (2*cb*cba**2*complex(0,1)*MHL**2*sb**3*sba**2)/vev**2 - (complex(0,1)*m122*sb**4*sba**2)/(cb**2*vev**2) - (cba**2*complex(0,1)*MHH**2*sb**5*sba**2)/(cb*vev**2) + (cba**2*complex(0,1)*MHL**2*sb**5*sba**2)/(cb*vev**2) + (3*cb**4*cba*complex(0,1)*MHH**2*sba**3)/vev**2 - (3*cb**4*cba*complex(0,1)*MHL**2*sba**3)/vev**2 + (4*cb**2*cba*complex(0,1)*MHH**2*sb**2*sba**3)/vev**2 - (4*cb**2*cba*complex(0,1)*MHL**2*sb**2*sba**3)/vev**2 + (cba*complex(0,1)*MHH**2*sb**4*sba**3)/vev**2 - (cba*complex(0,1)*MHL**2*sb**4*sba**3)/vev**2 - (cb**5*complex(0,1)*MHH**2*sba**4)/(sb*vev**2) + (cb**5*complex(0,1)*MHL**2*sba**4)/(sb*vev**2) - (cb**3*complex(0,1)*MHH**2*sb*sba**4)/vev**2 + (cb**3*complex(0,1)*MHL**2*sb*sba**4)/vev**2',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '(cb**4*cba**2*complex(0,1)*MHA**2)/vev**2 - (cb**2*cba**2*complex(0,1)*MHL**2)/vev**2 + (2*cb**2*cba**2*complex(0,1)*MHA**2*sb**2)/vev**2 - (cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 + (cb**2*cba**4*complex(0,1)*MHH**2*sb**2)/vev**2 - (cb**2*cba**4*complex(0,1)*MHL**2*sb**2)/vev**2 + (cba**2*complex(0,1)*MHA**2*sb**4)/vev**2 + (cba**4*complex(0,1)*MHH**2*sb**4)/vev**2 - (cba**4*complex(0,1)*MHL**2*sb**4)/vev**2 - (cb**2*cba*complex(0,1)*m122*sba)/vev**2 - (cb**4*cba*complex(0,1)*m122*sba)/(sb**2*vev**2) + (cb**3*cba*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (cb*cba*complex(0,1)*MHH**2*sb*sba)/vev**2 - (cb**3*cba**3*complex(0,1)*MHH**2*sb*sba)/vev**2 - (cb*cba*complex(0,1)*MHL**2*sb*sba)/vev**2 + (cb**3*cba**3*complex(0,1)*MHL**2*sb*sba)/vev**2 + (cba*complex(0,1)*m122*sb**2*sba)/vev**2 - (cba*complex(0,1)*MHH**2*sb**3*sba)/(cb*vev**2) + (cba*complex(0,1)*m122*sb**4*sba)/(cb**2*vev**2) + (cba**3*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) - (cba**3*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) - (cb**4*complex(0,1)*MHA**2*sba**2)/vev**2 - (cb**4*cba**2*complex(0,1)*MHH**2*sba**2)/vev**2 + (cb**2*complex(0,1)*MHL**2*sba**2)/vev**2 + (cb**4*cba**2*complex(0,1)*MHL**2*sba**2)/vev**2 - (2*cb**2*complex(0,1)*MHA**2*sb**2*sba**2)/vev**2 + (complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (2*cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 + (2*cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 - (complex(0,1)*MHA**2*sb**4*sba**2)/vev**2 - (cba**2*complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 + (cba**2*complex(0,1)*MHL**2*sb**4*sba**2)/vev**2 + (cb**5*cba*complex(0,1)*MHH**2*sba**3)/(sb*vev**2) - (cb**5*cba*complex(0,1)*MHL**2*sba**3)/(sb*vev**2) - (cb*cba*complex(0,1)*MHH**2*sb**3*sba**3)/vev**2 + (cb*cba*complex(0,1)*MHL**2*sb**3*sba**3)/vev**2 + (cb**4*complex(0,1)*MHH**2*sba**4)/vev**2 - (cb**4*complex(0,1)*MHL**2*sba**4)/vev**2 + (cb**2*complex(0,1)*MHH**2*sb**2*sba**4)/vev**2 - (cb**2*complex(0,1)*MHL**2*sb**2*sba**4)/vev**2',
                 order = {'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '-((cb**2*cba**2*complex(0,1)*MHL**2)/vev**2) + (cb**4*cba**2*complex(0,1)*MHp**2)/vev**2 - (cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 + (cb**2*cba**4*complex(0,1)*MHH**2*sb**2)/vev**2 - (cb**2*cba**4*complex(0,1)*MHL**2*sb**2)/vev**2 + (2*cb**2*cba**2*complex(0,1)*MHp**2*sb**2)/vev**2 + (cba**4*complex(0,1)*MHH**2*sb**4)/vev**2 - (cba**4*complex(0,1)*MHL**2*sb**4)/vev**2 + (cba**2*complex(0,1)*MHp**2*sb**4)/vev**2 - (cb**2*cba*complex(0,1)*m122*sba)/vev**2 - (cb**4*cba*complex(0,1)*m122*sba)/(sb**2*vev**2) + (cb**3*cba*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (cb*cba*complex(0,1)*MHH**2*sb*sba)/vev**2 - (cb**3*cba**3*complex(0,1)*MHH**2*sb*sba)/vev**2 - (cb*cba*complex(0,1)*MHL**2*sb*sba)/vev**2 + (cb**3*cba**3*complex(0,1)*MHL**2*sb*sba)/vev**2 + (cba*complex(0,1)*m122*sb**2*sba)/vev**2 - (cba*complex(0,1)*MHH**2*sb**3*sba)/(cb*vev**2) + (cba*complex(0,1)*m122*sb**4*sba)/(cb**2*vev**2) + (cba**3*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) - (cba**3*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) - (cb**4*cba**2*complex(0,1)*MHH**2*sba**2)/vev**2 + (cb**2*complex(0,1)*MHL**2*sba**2)/vev**2 + (cb**4*cba**2*complex(0,1)*MHL**2*sba**2)/vev**2 - (cb**4*complex(0,1)*MHp**2*sba**2)/vev**2 + (complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (2*cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 + (2*cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 - (2*cb**2*complex(0,1)*MHp**2*sb**2*sba**2)/vev**2 - (cba**2*complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 + (cba**2*complex(0,1)*MHL**2*sb**4*sba**2)/vev**2 - (complex(0,1)*MHp**2*sb**4*sba**2)/vev**2 + (cb**5*cba*complex(0,1)*MHH**2*sba**3)/(sb*vev**2) - (cb**5*cba*complex(0,1)*MHL**2*sba**3)/(sb*vev**2) - (cb*cba*complex(0,1)*MHH**2*sb**3*sba**3)/vev**2 + (cb*cba*complex(0,1)*MHL**2*sb**3*sba**3)/vev**2 + (cb**4*complex(0,1)*MHH**2*sba**4)/vev**2 - (cb**4*complex(0,1)*MHL**2*sba**4)/vev**2 + (cb**2*complex(0,1)*MHH**2*sb**2*sba**4)/vev**2 - (cb**2*complex(0,1)*MHL**2*sb**2*sba**4)/vev**2',
                 order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '(-2*cb**4*cba**2*complex(0,1)*MHA**2)/vev**2 - (cb**4*cba**4*complex(0,1)*MHH**2)/vev**2 - (cb**2*cba**2*complex(0,1)*MHL**2)/vev**2 + (cb**4*cba**4*complex(0,1)*MHL**2)/vev**2 + (2*cb**3*cba**2*complex(0,1)*m122)/(sb*vev**2) + (4*cb*cba**2*complex(0,1)*m122*sb)/vev**2 - (4*cb**2*cba**2*complex(0,1)*MHA**2*sb**2)/vev**2 - (cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 - (cb**2*cba**4*complex(0,1)*MHH**2*sb**2)/vev**2 + (cb**2*cba**4*complex(0,1)*MHL**2*sb**2)/vev**2 + (2*cba**2*complex(0,1)*m122*sb**3)/(cb*vev**2) - (2*cba**2*complex(0,1)*MHA**2*sb**4)/vev**2 + (cb**5*cba**3*complex(0,1)*MHH**2*sba)/(sb*vev**2) - (cb**5*cba**3*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (2*cb*cba*complex(0,1)*MHH**2*sb*sba)/vev**2 - (cb**3*cba**3*complex(0,1)*MHH**2*sb*sba)/vev**2 - (2*cb*cba*complex(0,1)*MHL**2*sb*sba)/vev**2 + (cb**3*cba**3*complex(0,1)*MHL**2*sb*sba)/vev**2 - (3*cb*cba**3*complex(0,1)*MHH**2*sb**3*sba)/vev**2 + (3*cb*cba**3*complex(0,1)*MHL**2*sb**3*sba)/vev**2 - (cba**3*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) + (cba**3*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) - (cb**2*complex(0,1)*MHH**2*sba**2)/vev**2 + (2*cb**4*cba**2*complex(0,1)*MHH**2*sba**2)/vev**2 - (2*cb**4*cba**2*complex(0,1)*MHL**2*sba**2)/vev**2 + (4*cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 - (4*cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 + (2*cba**2*complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 - (2*cba**2*complex(0,1)*MHL**2*sb**4*sba**2)/vev**2 - (2*cb**3*cba*complex(0,1)*MHH**2*sb*sba**3)/vev**2 + (2*cb**3*cba*complex(0,1)*MHL**2*sb*sba**3)/vev**2 - (2*cb*cba*complex(0,1)*MHH**2*sb**3*sba**3)/vev**2 + (2*cb*cba*complex(0,1)*MHL**2*sb**3*sba**3)/vev**2 + (cb**4*complex(0,1)*MHH**2*sba**4)/vev**2 - (cb**4*complex(0,1)*MHL**2*sba**4)/vev**2 + (cb**2*complex(0,1)*MHH**2*sb**2*sba**4)/vev**2 - (cb**2*complex(0,1)*MHL**2*sb**2*sba**4)/vev**2',
                 order = {'QED':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '-((cb**4*cba**4*complex(0,1)*MHH**2)/vev**2) - (cb**2*cba**2*complex(0,1)*MHL**2)/vev**2 + (cb**4*cba**4*complex(0,1)*MHL**2)/vev**2 - (2*cb**4*cba**2*complex(0,1)*MHp**2)/vev**2 + (2*cb**3*cba**2*complex(0,1)*m122)/(sb*vev**2) + (4*cb*cba**2*complex(0,1)*m122*sb)/vev**2 - (cba**2*complex(0,1)*MHH**2*sb**2)/vev**2 - (cb**2*cba**4*complex(0,1)*MHH**2*sb**2)/vev**2 + (cb**2*cba**4*complex(0,1)*MHL**2*sb**2)/vev**2 - (4*cb**2*cba**2*complex(0,1)*MHp**2*sb**2)/vev**2 + (2*cba**2*complex(0,1)*m122*sb**3)/(cb*vev**2) - (2*cba**2*complex(0,1)*MHp**2*sb**4)/vev**2 + (cb**5*cba**3*complex(0,1)*MHH**2*sba)/(sb*vev**2) - (cb**5*cba**3*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (2*cb*cba*complex(0,1)*MHH**2*sb*sba)/vev**2 - (cb**3*cba**3*complex(0,1)*MHH**2*sb*sba)/vev**2 - (2*cb*cba*complex(0,1)*MHL**2*sb*sba)/vev**2 + (cb**3*cba**3*complex(0,1)*MHL**2*sb*sba)/vev**2 - (3*cb*cba**3*complex(0,1)*MHH**2*sb**3*sba)/vev**2 + (3*cb*cba**3*complex(0,1)*MHL**2*sb**3*sba)/vev**2 - (cba**3*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) + (cba**3*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) - (cb**2*complex(0,1)*MHH**2*sba**2)/vev**2 + (2*cb**4*cba**2*complex(0,1)*MHH**2*sba**2)/vev**2 - (2*cb**4*cba**2*complex(0,1)*MHL**2*sba**2)/vev**2 + (4*cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 - (4*cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 + (2*cba**2*complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 - (2*cba**2*complex(0,1)*MHL**2*sb**4*sba**2)/vev**2 - (2*cb**3*cba*complex(0,1)*MHH**2*sb*sba**3)/vev**2 + (2*cb**3*cba*complex(0,1)*MHL**2*sb*sba**3)/vev**2 - (2*cb*cba*complex(0,1)*MHH**2*sb**3*sba**3)/vev**2 + (2*cb*cba*complex(0,1)*MHL**2*sb**3*sba**3)/vev**2 + (cb**4*complex(0,1)*MHH**2*sba**4)/vev**2 - (cb**4*complex(0,1)*MHL**2*sba**4)/vev**2 + (cb**2*complex(0,1)*MHH**2*sb**2*sba**4)/vev**2 - (cb**2*complex(0,1)*MHL**2*sb**2*sba**4)/vev**2',
                 order = {'QED':2})

GC_92 = Coupling(name = 'GC_92',
                 value = '(cb*cba**2*complex(0,1)*MHH**2*sb)/vev**2 - (cb**3*cba**4*complex(0,1)*MHH**2*sb)/vev**2 - (cb*cba**2*complex(0,1)*MHL**2*sb)/vev**2 + (cb**3*cba**4*complex(0,1)*MHL**2*sb)/vev**2 - (cb*cba**4*complex(0,1)*MHH**2*sb**3)/vev**2 + (cb*cba**4*complex(0,1)*MHL**2*sb**3)/vev**2 + (2*cb**4*cba*complex(0,1)*MHA**2*sba)/vev**2 - (cb**2*cba*complex(0,1)*MHH**2*sba)/vev**2 + (2*cb**4*cba**3*complex(0,1)*MHH**2*sba)/vev**2 + (cb**2*cba*complex(0,1)*MHL**2*sba)/vev**2 - (2*cb**4*cba**3*complex(0,1)*MHL**2*sba)/vev**2 - (2*cb**3*cba*complex(0,1)*m122*sba)/(sb*vev**2) - (4*cb*cba*complex(0,1)*m122*sb*sba)/vev**2 + (4*cb**2*cba*complex(0,1)*MHA**2*sb**2*sba)/vev**2 + (cba*complex(0,1)*MHH**2*sb**2*sba)/vev**2 + (2*cb**2*cba**3*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (cba*complex(0,1)*MHL**2*sb**2*sba)/vev**2 - (2*cb**2*cba**3*complex(0,1)*MHL**2*sb**2*sba)/vev**2 - (2*cba*complex(0,1)*m122*sb**3*sba)/(cb*vev**2) + (2*cba*complex(0,1)*MHA**2*sb**4*sba)/vev**2 - (cb**5*cba**2*complex(0,1)*MHH**2*sba**2)/(sb*vev**2) + (cb**5*cba**2*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) - (cb*complex(0,1)*MHH**2*sb*sba**2)/vev**2 - (cb**3*cba**2*complex(0,1)*MHH**2*sb*sba**2)/vev**2 + (cb*complex(0,1)*MHL**2*sb*sba**2)/vev**2 + (cb**3*cba**2*complex(0,1)*MHL**2*sb*sba**2)/vev**2 + (cb*cba**2*complex(0,1)*MHH**2*sb**3*sba**2)/vev**2 - (cb*cba**2*complex(0,1)*MHL**2*sb**3*sba**2)/vev**2 + (cba**2*complex(0,1)*MHH**2*sb**5*sba**2)/(cb*vev**2) - (cba**2*complex(0,1)*MHL**2*sb**5*sba**2)/(cb*vev**2) - (2*cb**2*cba*complex(0,1)*MHH**2*sb**2*sba**3)/vev**2 + (2*cb**2*cba*complex(0,1)*MHL**2*sb**2*sba**3)/vev**2 - (2*cba*complex(0,1)*MHH**2*sb**4*sba**3)/vev**2 + (2*cba*complex(0,1)*MHL**2*sb**4*sba**3)/vev**2 + (cb**3*complex(0,1)*MHH**2*sb*sba**4)/vev**2 - (cb**3*complex(0,1)*MHL**2*sb*sba**4)/vev**2 + (cb*complex(0,1)*MHH**2*sb**3*sba**4)/vev**2 - (cb*complex(0,1)*MHL**2*sb**3*sba**4)/vev**2',
                 order = {'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '(cb*cba**2*complex(0,1)*MHH**2*sb)/vev**2 - (cb**3*cba**4*complex(0,1)*MHH**2*sb)/vev**2 - (cb*cba**2*complex(0,1)*MHL**2*sb)/vev**2 + (cb**3*cba**4*complex(0,1)*MHL**2*sb)/vev**2 - (cb*cba**4*complex(0,1)*MHH**2*sb**3)/vev**2 + (cb*cba**4*complex(0,1)*MHL**2*sb**3)/vev**2 - (cb**2*cba*complex(0,1)*MHH**2*sba)/vev**2 + (2*cb**4*cba**3*complex(0,1)*MHH**2*sba)/vev**2 + (cb**2*cba*complex(0,1)*MHL**2*sba)/vev**2 - (2*cb**4*cba**3*complex(0,1)*MHL**2*sba)/vev**2 + (2*cb**4*cba*complex(0,1)*MHp**2*sba)/vev**2 - (2*cb**3*cba*complex(0,1)*m122*sba)/(sb*vev**2) - (4*cb*cba*complex(0,1)*m122*sb*sba)/vev**2 + (cba*complex(0,1)*MHH**2*sb**2*sba)/vev**2 + (2*cb**2*cba**3*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (cba*complex(0,1)*MHL**2*sb**2*sba)/vev**2 - (2*cb**2*cba**3*complex(0,1)*MHL**2*sb**2*sba)/vev**2 + (4*cb**2*cba*complex(0,1)*MHp**2*sb**2*sba)/vev**2 - (2*cba*complex(0,1)*m122*sb**3*sba)/(cb*vev**2) + (2*cba*complex(0,1)*MHp**2*sb**4*sba)/vev**2 - (cb**5*cba**2*complex(0,1)*MHH**2*sba**2)/(sb*vev**2) + (cb**5*cba**2*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) - (cb*complex(0,1)*MHH**2*sb*sba**2)/vev**2 - (cb**3*cba**2*complex(0,1)*MHH**2*sb*sba**2)/vev**2 + (cb*complex(0,1)*MHL**2*sb*sba**2)/vev**2 + (cb**3*cba**2*complex(0,1)*MHL**2*sb*sba**2)/vev**2 + (cb*cba**2*complex(0,1)*MHH**2*sb**3*sba**2)/vev**2 - (cb*cba**2*complex(0,1)*MHL**2*sb**3*sba**2)/vev**2 + (cba**2*complex(0,1)*MHH**2*sb**5*sba**2)/(cb*vev**2) - (cba**2*complex(0,1)*MHL**2*sb**5*sba**2)/(cb*vev**2) - (2*cb**2*cba*complex(0,1)*MHH**2*sb**2*sba**3)/vev**2 + (2*cb**2*cba*complex(0,1)*MHL**2*sb**2*sba**3)/vev**2 - (2*cba*complex(0,1)*MHH**2*sb**4*sba**3)/vev**2 + (2*cba*complex(0,1)*MHL**2*sb**4*sba**3)/vev**2 + (cb**3*complex(0,1)*MHH**2*sb*sba**4)/vev**2 - (cb**3*complex(0,1)*MHL**2*sb*sba**4)/vev**2 + (cb*complex(0,1)*MHH**2*sb**3*sba**4)/vev**2 - (cb*complex(0,1)*MHL**2*sb**3*sba**4)/vev**2',
                 order = {'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = '(cb**2*cba**2*complex(0,1)*m122)/vev**2 + (cb**4*cba**2*complex(0,1)*m122)/(sb**2*vev**2) - (cb**3*cba**2*complex(0,1)*MHL**2)/(sb*vev**2) - (cba**2*complex(0,1)*m122*sb**2)/vev**2 + (cba**2*complex(0,1)*MHH**2*sb**3)/(cb*vev**2) - (cb*cba**4*complex(0,1)*MHH**2*sb**3)/vev**2 + (cb*cba**4*complex(0,1)*MHL**2*sb**3)/vev**2 - (cba**2*complex(0,1)*m122*sb**4)/(cb**2*vev**2) - (cba**4*complex(0,1)*MHH**2*sb**5)/(cb*vev**2) + (cba**4*complex(0,1)*MHL**2*sb**5)/(cb*vev**2) + (2*cb**4*cba*complex(0,1)*MHA**2*sba)/vev**2 + (cb**4*cba**3*complex(0,1)*MHH**2*sba)/vev**2 - (2*cb**2*cba*complex(0,1)*MHL**2*sba)/vev**2 - (cb**4*cba**3*complex(0,1)*MHL**2*sba)/vev**2 + (4*cb**2*cba*complex(0,1)*MHA**2*sb**2*sba)/vev**2 - (2*cba*complex(0,1)*MHH**2*sb**2*sba)/vev**2 + (4*cb**2*cba**3*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (4*cb**2*cba**3*complex(0,1)*MHL**2*sb**2*sba)/vev**2 + (2*cba*complex(0,1)*MHA**2*sb**4*sba)/vev**2 + (3*cba**3*complex(0,1)*MHH**2*sb**4*sba)/vev**2 - (3*cba**3*complex(0,1)*MHL**2*sb**4*sba)/vev**2 - (cb**5*cba**2*complex(0,1)*MHH**2*sba**2)/(sb*vev**2) + (cb**5*cba**2*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) + (cb*complex(0,1)*MHH**2*sb*sba**2)/vev**2 - (2*cb**3*cba**2*complex(0,1)*MHH**2*sb*sba**2)/vev**2 - (cb*complex(0,1)*MHL**2*sb*sba**2)/vev**2 + (2*cb**3*cba**2*complex(0,1)*MHL**2*sb*sba**2)/vev**2 - (cb*cba**2*complex(0,1)*MHH**2*sb**3*sba**2)/vev**2 + (cb*cba**2*complex(0,1)*MHL**2*sb**3*sba**2)/vev**2 - (cb**4*cba*complex(0,1)*MHH**2*sba**3)/vev**2 + (cb**4*cba*complex(0,1)*MHL**2*sba**3)/vev**2 + (cba*complex(0,1)*MHH**2*sb**4*sba**3)/vev**2 - (cba*complex(0,1)*MHL**2*sb**4*sba**3)/vev**2 - (cb**3*complex(0,1)*MHH**2*sb*sba**4)/vev**2 + (cb**3*complex(0,1)*MHL**2*sb*sba**4)/vev**2 - (cb*complex(0,1)*MHH**2*sb**3*sba**4)/vev**2 + (cb*complex(0,1)*MHL**2*sb**3*sba**4)/vev**2',
                 order = {'QED':2})

GC_95 = Coupling(name = 'GC_95',
                 value = '(cb**2*cba**2*complex(0,1)*m122)/vev**2 + (cb**4*cba**2*complex(0,1)*m122)/(sb**2*vev**2) - (cb**3*cba**2*complex(0,1)*MHL**2)/(sb*vev**2) - (cba**2*complex(0,1)*m122*sb**2)/vev**2 + (cba**2*complex(0,1)*MHH**2*sb**3)/(cb*vev**2) - (cb*cba**4*complex(0,1)*MHH**2*sb**3)/vev**2 + (cb*cba**4*complex(0,1)*MHL**2*sb**3)/vev**2 - (cba**2*complex(0,1)*m122*sb**4)/(cb**2*vev**2) - (cba**4*complex(0,1)*MHH**2*sb**5)/(cb*vev**2) + (cba**4*complex(0,1)*MHL**2*sb**5)/(cb*vev**2) + (cb**4*cba**3*complex(0,1)*MHH**2*sba)/vev**2 - (2*cb**2*cba*complex(0,1)*MHL**2*sba)/vev**2 - (cb**4*cba**3*complex(0,1)*MHL**2*sba)/vev**2 + (2*cb**4*cba*complex(0,1)*MHp**2*sba)/vev**2 - (2*cba*complex(0,1)*MHH**2*sb**2*sba)/vev**2 + (4*cb**2*cba**3*complex(0,1)*MHH**2*sb**2*sba)/vev**2 - (4*cb**2*cba**3*complex(0,1)*MHL**2*sb**2*sba)/vev**2 + (4*cb**2*cba*complex(0,1)*MHp**2*sb**2*sba)/vev**2 + (3*cba**3*complex(0,1)*MHH**2*sb**4*sba)/vev**2 - (3*cba**3*complex(0,1)*MHL**2*sb**4*sba)/vev**2 + (2*cba*complex(0,1)*MHp**2*sb**4*sba)/vev**2 - (cb**5*cba**2*complex(0,1)*MHH**2*sba**2)/(sb*vev**2) + (cb**5*cba**2*complex(0,1)*MHL**2*sba**2)/(sb*vev**2) + (cb*complex(0,1)*MHH**2*sb*sba**2)/vev**2 - (2*cb**3*cba**2*complex(0,1)*MHH**2*sb*sba**2)/vev**2 - (cb*complex(0,1)*MHL**2*sb*sba**2)/vev**2 + (2*cb**3*cba**2*complex(0,1)*MHL**2*sb*sba**2)/vev**2 - (cb*cba**2*complex(0,1)*MHH**2*sb**3*sba**2)/vev**2 + (cb*cba**2*complex(0,1)*MHL**2*sb**3*sba**2)/vev**2 - (cb**4*cba*complex(0,1)*MHH**2*sba**3)/vev**2 + (cb**4*cba*complex(0,1)*MHL**2*sba**3)/vev**2 + (cba*complex(0,1)*MHH**2*sb**4*sba**3)/vev**2 - (cba*complex(0,1)*MHL**2*sb**4*sba**3)/vev**2 - (cb**3*complex(0,1)*MHH**2*sb*sba**4)/vev**2 + (cb**3*complex(0,1)*MHL**2*sb*sba**4)/vev**2 - (cb*complex(0,1)*MHH**2*sb**3*sba**4)/vev**2 + (cb*complex(0,1)*MHL**2*sb**3*sba**4)/vev**2',
                 order = {'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = '-((cb**2*cba**2*complex(0,1)*MHH**2)/vev**2) - (cb**2*cba**4*complex(0,1)*MHH**2*sb**2)/vev**2 - (cba**2*complex(0,1)*MHL**2*sb**2)/vev**2 + (cb**2*cba**4*complex(0,1)*MHL**2*sb**2)/vev**2 - (cba**4*complex(0,1)*MHH**2*sb**4)/vev**2 + (cba**4*complex(0,1)*MHL**2*sb**4)/vev**2 - (2*cb*cba*complex(0,1)*MHH**2*sb*sba)/vev**2 + (2*cb**3*cba**3*complex(0,1)*MHH**2*sb*sba)/vev**2 + (2*cb*cba*complex(0,1)*MHL**2*sb*sba)/vev**2 - (2*cb**3*cba**3*complex(0,1)*MHL**2*sb*sba)/vev**2 + (2*cb*cba**3*complex(0,1)*MHH**2*sb**3*sba)/vev**2 - (2*cb*cba**3*complex(0,1)*MHL**2*sb**3*sba)/vev**2 - (2*cb**4*complex(0,1)*MHA**2*sba**2)/vev**2 - (2*cb**4*cba**2*complex(0,1)*MHH**2*sba**2)/vev**2 - (cb**2*complex(0,1)*MHL**2*sba**2)/vev**2 + (2*cb**4*cba**2*complex(0,1)*MHL**2*sba**2)/vev**2 + (2*cb**3*complex(0,1)*m122*sba**2)/(sb*vev**2) + (4*cb*complex(0,1)*m122*sb*sba**2)/vev**2 - (4*cb**2*complex(0,1)*MHA**2*sb**2*sba**2)/vev**2 - (complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (4*cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 + (4*cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 + (2*complex(0,1)*m122*sb**3*sba**2)/(cb*vev**2) - (2*complex(0,1)*MHA**2*sb**4*sba**2)/vev**2 - (2*cba**2*complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 + (2*cba**2*complex(0,1)*MHL**2*sb**4*sba**2)/vev**2 + (cb**5*cba*complex(0,1)*MHH**2*sba**3)/(sb*vev**2) - (cb**5*cba*complex(0,1)*MHL**2*sba**3)/(sb*vev**2) + (3*cb**3*cba*complex(0,1)*MHH**2*sb*sba**3)/vev**2 - (3*cb**3*cba*complex(0,1)*MHL**2*sb*sba**3)/vev**2 + (cb*cba*complex(0,1)*MHH**2*sb**3*sba**3)/vev**2 - (cb*cba*complex(0,1)*MHL**2*sb**3*sba**3)/vev**2 - (cba*complex(0,1)*MHH**2*sb**5*sba**3)/(cb*vev**2) + (cba*complex(0,1)*MHL**2*sb**5*sba**3)/(cb*vev**2) + (cb**2*complex(0,1)*MHH**2*sb**2*sba**4)/vev**2 - (cb**2*complex(0,1)*MHL**2*sb**2*sba**4)/vev**2 + (complex(0,1)*MHH**2*sb**4*sba**4)/vev**2 - (complex(0,1)*MHL**2*sb**4*sba**4)/vev**2',
                 order = {'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '-((cb**2*cba**2*complex(0,1)*MHH**2)/vev**2) - (cb**2*cba**4*complex(0,1)*MHH**2*sb**2)/vev**2 - (cba**2*complex(0,1)*MHL**2*sb**2)/vev**2 + (cb**2*cba**4*complex(0,1)*MHL**2*sb**2)/vev**2 - (cba**4*complex(0,1)*MHH**2*sb**4)/vev**2 + (cba**4*complex(0,1)*MHL**2*sb**4)/vev**2 - (2*cb*cba*complex(0,1)*MHH**2*sb*sba)/vev**2 + (2*cb**3*cba**3*complex(0,1)*MHH**2*sb*sba)/vev**2 + (2*cb*cba*complex(0,1)*MHL**2*sb*sba)/vev**2 - (2*cb**3*cba**3*complex(0,1)*MHL**2*sb*sba)/vev**2 + (2*cb*cba**3*complex(0,1)*MHH**2*sb**3*sba)/vev**2 - (2*cb*cba**3*complex(0,1)*MHL**2*sb**3*sba)/vev**2 - (2*cb**4*cba**2*complex(0,1)*MHH**2*sba**2)/vev**2 - (cb**2*complex(0,1)*MHL**2*sba**2)/vev**2 + (2*cb**4*cba**2*complex(0,1)*MHL**2*sba**2)/vev**2 - (2*cb**4*complex(0,1)*MHp**2*sba**2)/vev**2 + (2*cb**3*complex(0,1)*m122*sba**2)/(sb*vev**2) + (4*cb*complex(0,1)*m122*sb*sba**2)/vev**2 - (complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (4*cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 + (4*cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 - (4*cb**2*complex(0,1)*MHp**2*sb**2*sba**2)/vev**2 + (2*complex(0,1)*m122*sb**3*sba**2)/(cb*vev**2) - (2*cba**2*complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 + (2*cba**2*complex(0,1)*MHL**2*sb**4*sba**2)/vev**2 - (2*complex(0,1)*MHp**2*sb**4*sba**2)/vev**2 + (cb**5*cba*complex(0,1)*MHH**2*sba**3)/(sb*vev**2) - (cb**5*cba*complex(0,1)*MHL**2*sba**3)/(sb*vev**2) + (3*cb**3*cba*complex(0,1)*MHH**2*sb*sba**3)/vev**2 - (3*cb**3*cba*complex(0,1)*MHL**2*sb*sba**3)/vev**2 + (cb*cba*complex(0,1)*MHH**2*sb**3*sba**3)/vev**2 - (cb*cba*complex(0,1)*MHL**2*sb**3*sba**3)/vev**2 - (cba*complex(0,1)*MHH**2*sb**5*sba**3)/(cb*vev**2) + (cba*complex(0,1)*MHL**2*sb**5*sba**3)/(cb*vev**2) + (cb**2*complex(0,1)*MHH**2*sb**2*sba**4)/vev**2 - (cb**2*complex(0,1)*MHL**2*sb**2*sba**4)/vev**2 + (complex(0,1)*MHH**2*sb**4*sba**4)/vev**2 - (complex(0,1)*MHL**2*sb**4*sba**4)/vev**2',
                 order = {'QED':2})

GC_98 = Coupling(name = 'GC_98',
                 value = '-((cb**4*cba**4*complex(0,1)*MHH**2)/vev**2) + (cb**4*cba**4*complex(0,1)*MHL**2)/vev**2 + (cb**5*cba**2*complex(0,1)*m122)/(sb**3*vev**2) - (cb**4*cba**2*complex(0,1)*MHL**2)/(sb**2*vev**2) - (2*cb*cba**2*complex(0,1)*m122*sb)/vev**2 - (2*cb**2*cba**4*complex(0,1)*MHH**2*sb**2)/vev**2 + (2*cb**2*cba**4*complex(0,1)*MHL**2*sb**2)/vev**2 - (cba**2*complex(0,1)*MHH**2*sb**4)/(cb**2*vev**2) + (cba**2*complex(0,1)*m122*sb**5)/(cb**3*vev**2) + (cba**4*complex(0,1)*MHH**2*sb**6)/(cb**2*vev**2) - (cba**4*complex(0,1)*MHL**2*sb**6)/(cb**2*vev**2) + (2*cb**2*cba*complex(0,1)*m122*sba)/vev**2 + (2*cb**4*cba*complex(0,1)*m122*sba)/(sb**2*vev**2) + (2*cb**5*cba**3*complex(0,1)*MHH**2*sba)/(sb*vev**2) - (2*cb**3*cba*complex(0,1)*MHL**2*sba)/(sb*vev**2) - (2*cb**5*cba**3*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (2*cb**3*cba**3*complex(0,1)*MHH**2*sb*sba)/vev**2 - (2*cb**3*cba**3*complex(0,1)*MHL**2*sb*sba)/vev**2 - (2*cba*complex(0,1)*m122*sb**2*sba)/vev**2 + (2*cba*complex(0,1)*MHH**2*sb**3*sba)/(cb*vev**2) - (4*cb*cba**3*complex(0,1)*MHH**2*sb**3*sba)/vev**2 + (4*cb*cba**3*complex(0,1)*MHL**2*sb**3*sba)/vev**2 - (2*cba*complex(0,1)*m122*sb**4*sba)/(cb**2*vev**2) - (4*cba**3*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) + (4*cba**3*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) - (2*cb**4*complex(0,1)*MHA**2*sba**2)/vev**2 + (cb**4*cba**2*complex(0,1)*MHH**2*sba**2)/vev**2 - (cb**2*complex(0,1)*MHL**2*sba**2)/vev**2 - (cb**4*cba**2*complex(0,1)*MHL**2*sba**2)/vev**2 - (cb**6*cba**2*complex(0,1)*MHH**2*sba**2)/(sb**2*vev**2) + (cb**6*cba**2*complex(0,1)*MHL**2*sba**2)/(sb**2*vev**2) + (2*cb**3*complex(0,1)*m122*sba**2)/(sb*vev**2) + (4*cb*complex(0,1)*m122*sb*sba**2)/vev**2 - (4*cb**2*complex(0,1)*MHA**2*sb**2*sba**2)/vev**2 - (complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 + (5*cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (5*cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 + (2*complex(0,1)*m122*sb**3*sba**2)/(cb*vev**2) - (2*complex(0,1)*MHA**2*sb**4*sba**2)/vev**2 + (3*cba**2*complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 - (3*cba**2*complex(0,1)*MHL**2*sb**4*sba**2)/vev**2 - (cb**5*cba*complex(0,1)*MHH**2*sba**3)/(sb*vev**2) + (cb**5*cba*complex(0,1)*MHL**2*sba**3)/(sb*vev**2) - (cb**3*cba*complex(0,1)*MHH**2*sb*sba**3)/vev**2 + (cb**3*cba*complex(0,1)*MHL**2*sb*sba**3)/vev**2 - (cb*cba*complex(0,1)*MHH**2*sb**3*sba**3)/vev**2 + (cb*cba*complex(0,1)*MHL**2*sb**3*sba**3)/vev**2 - (cba*complex(0,1)*MHH**2*sb**5*sba**3)/(cb*vev**2) + (cba*complex(0,1)*MHL**2*sb**5*sba**3)/(cb*vev**2) + (cb**2*complex(0,1)*MHH**2*sb**2*sba**4)/vev**2 - (cb**2*complex(0,1)*MHL**2*sb**2*sba**4)/vev**2 + (complex(0,1)*MHH**2*sb**4*sba**4)/vev**2 - (complex(0,1)*MHL**2*sb**4*sba**4)/vev**2',
                 order = {'QED':2})

GC_99 = Coupling(name = 'GC_99',
                 value = '-((cb**4*cba**4*complex(0,1)*MHH**2)/vev**2) + (cb**4*cba**4*complex(0,1)*MHL**2)/vev**2 + (cb**5*cba**2*complex(0,1)*m122)/(sb**3*vev**2) - (cb**4*cba**2*complex(0,1)*MHL**2)/(sb**2*vev**2) - (2*cb*cba**2*complex(0,1)*m122*sb)/vev**2 - (2*cb**2*cba**4*complex(0,1)*MHH**2*sb**2)/vev**2 + (2*cb**2*cba**4*complex(0,1)*MHL**2*sb**2)/vev**2 - (cba**2*complex(0,1)*MHH**2*sb**4)/(cb**2*vev**2) + (cba**2*complex(0,1)*m122*sb**5)/(cb**3*vev**2) + (cba**4*complex(0,1)*MHH**2*sb**6)/(cb**2*vev**2) - (cba**4*complex(0,1)*MHL**2*sb**6)/(cb**2*vev**2) + (2*cb**2*cba*complex(0,1)*m122*sba)/vev**2 + (2*cb**4*cba*complex(0,1)*m122*sba)/(sb**2*vev**2) + (2*cb**5*cba**3*complex(0,1)*MHH**2*sba)/(sb*vev**2) - (2*cb**3*cba*complex(0,1)*MHL**2*sba)/(sb*vev**2) - (2*cb**5*cba**3*complex(0,1)*MHL**2*sba)/(sb*vev**2) + (2*cb**3*cba**3*complex(0,1)*MHH**2*sb*sba)/vev**2 - (2*cb**3*cba**3*complex(0,1)*MHL**2*sb*sba)/vev**2 - (2*cba*complex(0,1)*m122*sb**2*sba)/vev**2 + (2*cba*complex(0,1)*MHH**2*sb**3*sba)/(cb*vev**2) - (4*cb*cba**3*complex(0,1)*MHH**2*sb**3*sba)/vev**2 + (4*cb*cba**3*complex(0,1)*MHL**2*sb**3*sba)/vev**2 - (2*cba*complex(0,1)*m122*sb**4*sba)/(cb**2*vev**2) - (4*cba**3*complex(0,1)*MHH**2*sb**5*sba)/(cb*vev**2) + (4*cba**3*complex(0,1)*MHL**2*sb**5*sba)/(cb*vev**2) + (cb**4*cba**2*complex(0,1)*MHH**2*sba**2)/vev**2 - (cb**2*complex(0,1)*MHL**2*sba**2)/vev**2 - (cb**4*cba**2*complex(0,1)*MHL**2*sba**2)/vev**2 - (2*cb**4*complex(0,1)*MHp**2*sba**2)/vev**2 - (cb**6*cba**2*complex(0,1)*MHH**2*sba**2)/(sb**2*vev**2) + (cb**6*cba**2*complex(0,1)*MHL**2*sba**2)/(sb**2*vev**2) + (2*cb**3*complex(0,1)*m122*sba**2)/(sb*vev**2) + (4*cb*complex(0,1)*m122*sb*sba**2)/vev**2 - (complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 + (5*cb**2*cba**2*complex(0,1)*MHH**2*sb**2*sba**2)/vev**2 - (5*cb**2*cba**2*complex(0,1)*MHL**2*sb**2*sba**2)/vev**2 - (4*cb**2*complex(0,1)*MHp**2*sb**2*sba**2)/vev**2 + (2*complex(0,1)*m122*sb**3*sba**2)/(cb*vev**2) + (3*cba**2*complex(0,1)*MHH**2*sb**4*sba**2)/vev**2 - (3*cba**2*complex(0,1)*MHL**2*sb**4*sba**2)/vev**2 - (2*complex(0,1)*MHp**2*sb**4*sba**2)/vev**2 - (cb**5*cba*complex(0,1)*MHH**2*sba**3)/(sb*vev**2) + (cb**5*cba*complex(0,1)*MHL**2*sba**3)/(sb*vev**2) - (cb**3*cba*complex(0,1)*MHH**2*sb*sba**3)/vev**2 + (cb**3*cba*complex(0,1)*MHL**2*sb*sba**3)/vev**2 - (cb*cba*complex(0,1)*MHH**2*sb**3*sba**3)/vev**2 + (cb*cba*complex(0,1)*MHL**2*sb**3*sba**3)/vev**2 - (cba*complex(0,1)*MHH**2*sb**5*sba**3)/(cb*vev**2) + (cba*complex(0,1)*MHL**2*sb**5*sba**3)/(cb*vev**2) + (cb**2*complex(0,1)*MHH**2*sb**2*sba**4)/vev**2 - (cb**2*complex(0,1)*MHL**2*sb**2*sba**4)/vev**2 + (complex(0,1)*MHH**2*sb**4*sba**4)/vev**2 - (complex(0,1)*MHL**2*sb**4*sba**4)/vev**2',
                 order = {'QED':2})

