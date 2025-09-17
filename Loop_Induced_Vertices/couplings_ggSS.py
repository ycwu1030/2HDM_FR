
GC_ggHLHLtop = Coupling(name = 'GC_ggHLHLtop',
                      value = '-complex(0,1)*G**2*kHLUp*kHLUp/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':2, 'NLOB':1})

GC_ggHLHLbot = Coupling(name = 'GC_ggHLHLbot',
                      value = '-complex(0,1)*G**2*kHLDo*kHLDo/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':2, 'NLOB':1})

GC_ggHLHHtop = Coupling(name = 'GC_ggHLHHtop',
                      value = '-complex(0,1)*G**2*kHLUp*kHHUp/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':2, 'NLOB':1})

GC_ggHLHHbot = Coupling(name = 'GC_ggHLHHbot',
                      value = '-complex(0,1)*G**2*kHLDo*kHHDo/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':2, 'NLOB':1})

GC_ggHHHHtop = Coupling(name = 'GC_ggHHHHtop',
                      value = '-complex(0,1)*G**2*kHHUp*kHHUp/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':2, 'NLOB':1})

GC_ggHHHHbot = Coupling(name = 'GC_ggHHHHbot',
                      value = '-complex(0,1)*G**2*kHHDo*kHHDo/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':2, 'NLOB':1})

GC_ggHAHAtop = Coupling(name = 'GC_ggHAHAtop',
                      value = '-complex(0,1)*G**2*kHAUp*kHAUp/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':2, 'NLOB':1})

GC_ggHAHAbot = Coupling(name = 'GC_ggHAHAbot',
                      value = '-complex(0,1)*G**2*kHADo*kHADo/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':2, 'NLOB':1})

GC_ggHLHAtop = Coupling(name = 'GC_ggHLHAtop',
                      value = '-complex(0,1)*G**2*kHLUp*kHAUp/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':2, 'NLOB':1})

GC_ggHLHAbot = Coupling(name = 'GC_ggHLHAbot',
                      value = '-complex(0,1)*G**2*kHLDo*kHADo/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':2, 'NLOB':1})

GC_ggHHHAtop = Coupling(name = 'GC_ggHHHAtop',
                      value = '-complex(0,1)*G**2*kHHUp*kHAUp/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':2, 'NLOB':1})

GC_ggHHHAbot = Coupling(name = 'GC_ggHHHAbot',
                      value = '-complex(0,1)*G**2*kHHDo*kHADo/(8.*cmath.pi**2*vev**2)',
                      order = {'QCD':2,'QED':2, 'NLOB':1})
