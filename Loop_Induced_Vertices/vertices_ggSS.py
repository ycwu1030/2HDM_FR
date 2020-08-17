
V_ggHLHL = Vertex(name = 'V_ggHLHL',
                particles = [ P.g, P.g, P.HL, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSSFtop, L.VVSSFbot, L.VVSSGtop, L.VVSSGbot ],
                couplings = {(0,0):C.GC_ggHLHLtop,(0,1):C.GC_ggHLHLbot,(0,2):C.GC_ggHLHLtop,(0,3):C.GC_ggHLHLbot})

V_ggHLHH = Vertex(name = 'V_ggHLHH',
                particles = [ P.g, P.g, P.HL, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSSFtop, L.VVSSFbot, L.VVSSGtop, L.VVSSGbot ],
                couplings = {(0,0):C.GC_ggHLHHtop,(0,1):C.GC_ggHLHHbot,(0,2):C.GC_ggHLHHtop,(0,3):C.GC_ggHLHHbot})

V_ggHHHH = Vertex(name = 'V_ggHHHH',
                particles = [ P.g, P.g, P.HH, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSSFtop, L.VVSSFbot, L.VVSSGtop, L.VVSSGbot ],
                couplings = {(0,0):C.GC_ggHHHHtop,(0,1):C.GC_ggHHHHbot,(0,2):C.GC_ggHHHHtop,(0,3):C.GC_ggHHHHbot})
