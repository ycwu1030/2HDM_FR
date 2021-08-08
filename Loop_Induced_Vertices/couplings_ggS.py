
GC_ggHLtop = Coupling(name = 'GC_ggHLtop',
                      value = 'G**2*kHLUp/(8.*cmath.pi**2*vev)',
                      order = {'QCD':2,'QED':1, 'NLO':1})

GC_ggHLbot = Coupling(name = 'GC_ggHLbot',
                      value = 'G**2*kHLDo/(8.*cmath.pi**2*vev)',
                      order = {'QCD':2,'QED':1, 'NLO':1})

GC_ggHHtop = Coupling(name = 'GC_ggHHtop',
                      value = 'G**2*kHHUp/(8.*cmath.pi**2*vev)',
                      order = {'QCD':2,'QED':1, 'NLO':1})

GC_ggHHbot = Coupling(name = 'GC_ggHHbot',
                      value = 'G**2*kHHDo/(8.*cmath.pi**2*vev)',
                      order = {'QCD':2,'QED':1, 'NLO':1})

GC_ggHAtop = Coupling(name = 'GC_ggHAtop',
                      value = 'G**2*kHAUp/(8.*cmath.pi**2*vev)',
                      order = {'QCD':2,'QED':1, 'NLO':1})

GC_ggHAbot = Coupling(name = 'GC_ggHAbot',
                      value = 'G**2*kHADo/(8.*cmath.pi**2*vev)',
                      order = {'QCD':2,'QED':1, 'NLO':1})
