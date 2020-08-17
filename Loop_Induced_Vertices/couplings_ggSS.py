
GC_ggHLHLtop = Coupling(name = 'GC_ggHLHLtop',
                      value = 'G**2*kHLUp*kHLUp/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':1})

GC_ggHLHLbot = Coupling(name = 'GC_ggHLHLbot',
                      value = 'G**2*kHLDo*kHLDo/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':1})

GC_ggHLHHtop = Coupling(name = 'GC_ggHLHHtop',
                      value = 'G**2*kHLUp*kHHUp/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':1})

GC_ggHLHHbot = Coupling(name = 'GC_ggHLHHbot',
                      value = 'G**2*kHLDo*kHHDo/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':1})

GC_ggHHHHtop = Coupling(name = 'GC_ggHHHHtop',
                      value = 'G**2*kHHUp*kHHUp/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':1})

GC_ggHHHHbot = Coupling(name = 'GC_ggHHHHbot',
                      value = 'G**2*kHHDo*kHHDo/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':1})
