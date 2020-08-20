
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

V_ggHAHA = Vertex(name = 'V_ggHAHA',
                particles = [ P.g, P.g, P.HA, P.HA ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVAAFtop, L.VVAAFbot, L.VVAAGtop, L.VVAAGbot ],
                couplings = {(0,0):C.GC_ggHAHAtop,(0,1):C.GC_ggHAHAbot,(0,2):C.GC_ggHAHAtop,(0,3):C.GC_ggHAHAbot})

V_ggHLHA = Vertex(name = 'V_ggHLHA',
                particles = [ P.g, P.g, P.HA, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSAFtop, L.VVSAFbot, L.VVSAGtop, L.VVSAGbot ],
                couplings = {(0,0):C.GC_ggHLHAtop,(0,1):C.GC_ggHLHAbot,(0,2):C.GC_ggHLHAtop,(0,3):C.GC_ggHLHAbot})

V_ggHHHA = Vertex(name = 'V_ggHHHA',
                particles = [ P.g, P.g, P.HA, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSAFtop, L.VVSAFbot, L.VVSAGtop, L.VVSAGbot ],
                couplings = {(0,0):C.GC_ggHHHAtop,(0,1):C.GC_ggHHHAbot,(0,2):C.GC_ggHHHAtop,(0,3):C.GC_ggHHHAbot})
