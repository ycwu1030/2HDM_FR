
V_gagaHL = Vertex(name = 'V_gagaHL',
                particles = [ P.a, P.a, P.HL ],
                color = [ '1' ],
                lorentz = [ L.gagaStop, L.gagaSbot, L.gagaSW, L.gagaSS ],
                couplings = {(0,0):C.GC_gagaHLtop,(0,1):C.GC_gagaHLbot,(0,2):C.GC_gagaHLW,(0,3):C.GC_gagaHLS})

V_gagaHH = Vertex(name = 'V_gagaHH',
                particles = [ P.a, P.a, P.HH ],
                color = [ '1' ],
                lorentz = [ L.gagaStop, L.gagaSbot, L.gagaSW, L.gagaSS ],
                couplings = {(0,0):C.GC_gagaHHtop,(0,1):C.GC_gagaHHbot,(0,2):C.GC_gagaHHW,(0,3):C.GC_gagaHHS})

V_gagaHA = Vertex(name = 'V_gagaHA',
                particles = [ P.a, P.a, P.HA ],
                color = [ '1' ],
                lorentz = [ L.gagaSOddtop, L.gagaSOddbot],
                couplings = {(0,0):C.GC_gagaHAtop,(0,1):C.GC_gagaHAbot})
