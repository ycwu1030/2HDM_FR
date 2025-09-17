

V_ggHL = Vertex(name = 'V_ggHL',
                particles = [ P.g, P.g, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVStop, L.VVSbot ],
                couplings = {(0,0):C.GC_ggHLtop,(0,1):C.GC_ggHLbot})

V_ggHH = Vertex(name = 'V_ggHH',
                particles = [ P.g, P.g, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVStop, L.VVSbot ],
                couplings = {(0,0):C.GC_ggHHtop,(0,1):C.GC_ggHHbot})

V_ggHA = Vertex(name = 'V_ggHA',
                particles = [ P.g, P.g, P.HA ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSOddtop, L.VVSOddbot ],
                couplings = {(0,0):C.GC_ggHAtop,(0,1):C.GC_ggHAbot})
