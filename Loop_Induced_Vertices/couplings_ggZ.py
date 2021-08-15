
GC_ggZtop = Coupling(name = 'GC_ggZtop',
                      value = '-complex(0,1)*complex(0,1)*G**2*AUp*MZ/(16.*cmath.pi**2*vev)',
                      order = {'QCD':2,'QED':1, 'NLOZ':1})

GC_ggZbot = Coupling(name = 'GC_ggZbot',
                      value = '-complex(0,1)*complex(0,1)*G**2*ADo*MZ/(16.*cmath.pi**2*vev)',
                      order = {'QCD':2,'QED':1, 'NLOZ':1})
