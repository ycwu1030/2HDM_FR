
GC_gagaHLtop = Coupling(name='GC_gagaHLtop',
                        value='-complex(0,1)*3.*(2./3.)**2*aEW*kHLUp/(2.*cmath.pi*vev)',
                        order={'QED': 3, 'NLOEW': 1, 'NLOEWHL': 1})

GC_gagaHLbot = Coupling(name='GC_gagaHLbot',
                        value='-complex(0,1)*3.*(1./3.)**2*aEW*kHLDo/(2.*cmath.pi*vev)',
                        order={'QED': 3, 'NLOEW': 1, 'NLOEWHL': 1})

GC_gagaHLW = Coupling(name='GC_gagaHLW',
                      value='-complex(0,1)*aEW*kHLW/(2.*cmath.pi*vev)',
                      order={'QED': 3, 'NLOEW': 1, 'NLOEWHL': 1})

GC_gagaHLS = Coupling(name='GC_gagaHLS',
                      value='-complex(0,1)*aEW*kHLHpm/(2.*cmath.pi*vev)',
                      order={'QED': 3, 'NLOEW': 1, 'NLOEWHL': 1})

GC_gagaHHtop = Coupling(name='GC_gagaHHtop',
                        value='-complex(0,1)*3.*(2./3.)**2*aEW*kHHUp/(2.*cmath.pi*vev)',
                        order={'QED': 3, 'NLOEW': 1, 'NLOEWHH': 1})

GC_gagaHHbot = Coupling(name='GC_gagaHHbot',
                        value='-complex(0,1)*3.*(1./3.)**2*aEW*kHHDo/(2.*cmath.pi*vev)',
                        order={'QED': 3, 'NLOEW': 1, 'NLOEWHH': 1})

GC_gagaHHW = Coupling(name='GC_gagaHHW',
                      value='-complex(0,1)*aEW*kHHW/(2.*cmath.pi*vev)',
                      order={'QED': 3, 'NLOEW': 1, 'NLOEWHH': 1})

GC_gagaHHS = Coupling(name='GC_gagaHHS',
                      value='-complex(0,1)*aEW*kHHHpm/(2.*cmath.pi*vev)',
                      order={'QED': 3, 'NLOEW': 1, 'NLOEWHH': 1})

GC_gagaHAtop = Coupling(name='GC_gagaHAtop',
                        value='-complex(0,1)*complex(0,1)*3.*(2./3.)**2*aEW*kHAUp/(2.*cmath.pi*vev)',
                        order={'QED': 3, 'NLOEW': 1, 'NLOEWHA': 1})

GC_gagaHAbot = Coupling(name='GC_gagaHAbot',
                        value='-complex(0,1)*complex(0,1)*3.*(2./3.)**2*aEW*kHADo/(2.*cmath.pi*vev)',
                        order={'QED': 3, 'NLOEW': 1, 'NLOEWHA': 1})
