# This file was automatically created by FeynRules 2.3.36
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Wed 12 Aug 2020 14:10:11


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_242_76,(0,0,1):C.R2GC_242_77})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_197_47,(2,0,1):C.R2GC_197_48,(0,0,0):C.R2GC_197_47,(0,0,1):C.R2GC_197_48,(6,0,0):C.R2GC_200_52,(6,0,1):C.R2GC_247_83,(4,0,0):C.R2GC_195_43,(4,0,1):C.R2GC_195_44,(3,0,0):C.R2GC_195_43,(3,0,1):C.R2GC_195_44,(8,0,0):C.R2GC_196_45,(8,0,1):C.R2GC_196_46,(7,0,0):C.R2GC_201_54,(7,0,1):C.R2GC_246_82,(5,0,0):C.R2GC_195_43,(5,0,1):C.R2GC_195_44,(1,0,0):C.R2GC_195_43,(1,0,1):C.R2GC_195_44,(11,3,0):C.R2GC_199_50,(11,3,1):C.R2GC_199_51,(10,3,0):C.R2GC_199_50,(10,3,1):C.R2GC_199_51,(9,3,1):C.R2GC_198_49,(2,1,0):C.R2GC_197_47,(2,1,1):C.R2GC_197_48,(0,1,0):C.R2GC_197_47,(0,1,1):C.R2GC_197_48,(4,1,0):C.R2GC_195_43,(4,1,1):C.R2GC_195_44,(3,1,0):C.R2GC_195_43,(3,1,1):C.R2GC_195_44,(8,1,0):C.R2GC_196_45,(8,1,1):C.R2GC_248_84,(6,1,0):C.R2GC_243_78,(6,1,1):C.R2GC_243_79,(7,1,0):C.R2GC_201_54,(7,1,1):C.R2GC_201_55,(5,1,0):C.R2GC_195_43,(5,1,1):C.R2GC_195_44,(1,1,0):C.R2GC_195_43,(1,1,1):C.R2GC_195_44,(2,2,0):C.R2GC_197_47,(2,2,1):C.R2GC_197_48,(0,2,0):C.R2GC_197_47,(0,2,1):C.R2GC_197_48,(4,2,0):C.R2GC_195_43,(4,2,1):C.R2GC_195_44,(3,2,0):C.R2GC_195_43,(3,2,1):C.R2GC_195_44,(8,2,0):C.R2GC_196_45,(8,2,1):C.R2GC_245_81,(6,2,0):C.R2GC_200_52,(6,2,1):C.R2GC_200_53,(7,2,0):C.R2GC_244_80,(7,2,1):C.R2GC_197_48,(5,2,0):C.R2GC_195_43,(5,2,1):C.R2GC_195_44,(1,2,0):C.R2GC_195_43,(1,2,1):C.R2GC_195_44})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_256_87,(0,1,0):C.R2GC_258_89})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.H__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_257_88,(0,1,0):C.R2GC_261_92})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_236_69})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.HA ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_238_71})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.HL ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_237_70})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.HH ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_239_72})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_258_89,(0,1,0):C.R2GC_256_87})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.H__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_261_92,(0,1,0):C.R2GC_257_88})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_259_90})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.HA ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_262_93})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_260_91})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_263_94})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_205_59})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_205_59})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_205_59})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_202_56})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_202_56})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_202_56})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_203_57})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_203_57})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_203_57})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_203_57})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_203_57})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_203_57})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_226_64})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_228_66})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_222_60})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_224_62})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_253_86})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_227_65})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_223_61})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_229_67})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_225_63})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_253_86})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_177_33,(0,1,0):C.R2GC_158_1})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_177_33,(0,1,0):C.R2GC_158_1})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_177_33,(0,1,0):C.R2GC_158_1})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_178_34,(0,1,0):C.R2GC_159_2})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_178_34,(0,1,0):C.R2GC_159_2})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_178_34,(0,1,0):C.R2GC_159_2})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_204_58})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_204_58})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_252_85,(0,2,0):C.R2GC_252_85,(0,1,0):C.R2GC_204_58,(0,3,0):C.R2GC_204_58})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_204_58})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_204_58})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_233_68,(0,2,0):C.R2GC_233_68,(0,1,0):C.R2GC_204_58,(0,3,0):C.R2GC_204_58})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.R2GC_241_75,(0,1,0):C.R2GC_162_3,(0,1,3):C.R2GC_162_4,(0,2,1):C.R2GC_240_73,(0,2,2):C.R2GC_240_74})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.g, P.g, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_163_5,(0,0,1):C.R2GC_163_6})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.g, P.g, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_164_7,(0,0,1):C.R2GC_164_8})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_184_38,(0,0,1):C.R2GC_184_39,(0,0,2):C.R2GC_184_40,(0,0,3):C.R2GC_184_41,(0,0,4):C.R2GC_184_42,(0,1,0):C.R2GC_184_38,(0,1,1):C.R2GC_184_39,(0,1,2):C.R2GC_184_40,(0,1,3):C.R2GC_184_41,(0,1,4):C.R2GC_184_42,(0,2,0):C.R2GC_184_38,(0,2,1):C.R2GC_184_39,(0,2,2):C.R2GC_184_40,(0,2,3):C.R2GC_184_41,(0,2,4):C.R2GC_184_42})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_173_25,(0,0,1):C.R2GC_173_26,(0,1,0):C.R2GC_173_25,(0,1,1):C.R2GC_173_26,(0,2,0):C.R2GC_173_25,(0,2,1):C.R2GC_173_26})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_176_31,(0,0,1):C.R2GC_176_32,(0,1,0):C.R2GC_176_31,(0,1,1):C.R2GC_176_32,(0,2,0):C.R2GC_176_31,(0,2,1):C.R2GC_176_32})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_171_21,(0,0,1):C.R2GC_171_22,(0,1,0):C.R2GC_171_21,(0,1,1):C.R2GC_171_22,(0,2,0):C.R2GC_171_21,(0,2,1):C.R2GC_171_22})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_175_29,(1,0,1):C.R2GC_175_30,(0,1,0):C.R2GC_174_27,(0,1,1):C.R2GC_174_28,(0,2,0):C.R2GC_174_27,(0,2,1):C.R2GC_174_28,(0,3,0):C.R2GC_174_27,(0,3,1):C.R2GC_174_28})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_172_23,(0,0,1):C.R2GC_172_24,(0,1,0):C.R2GC_172_23,(0,1,1):C.R2GC_172_24,(0,2,0):C.R2GC_172_23,(0,2,1):C.R2GC_172_24})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.g, P.g, P.HL, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_166_11,(0,0,1):C.R2GC_166_12})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.g, P.g, P.HH, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_168_15,(0,0,1):C.R2GC_168_16})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.g, P.g, P.HH, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_169_17,(0,0,1):C.R2GC_169_18})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.g, P.g, P.HA, P.HA ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_167_13,(0,0,1):C.R2GC_167_14})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.g, P.g, P.H__minus__, P.H__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_181_36})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.HA ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_170_19,(0,0,1):C.R2GC_170_20})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_165_9,(0,0,1):C.R2GC_165_10})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.g, P.g, P.G__plus__, P.H__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_182_37})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.H__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_182_37})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_180_35})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV7, L.VVV8, L.VVV9 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,1,0):C.UVGC_242_60,(0,1,1):C.UVGC_242_61,(0,1,4):C.UVGC_242_62,(0,2,2):C.UVGC_185_1,(0,0,3):C.UVGC_186_2})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,3):C.UVGC_196_9,(2,0,4):C.UVGC_196_8,(0,0,3):C.UVGC_196_9,(0,0,4):C.UVGC_196_8,(6,0,0):C.UVGC_246_74,(6,0,2):C.UVGC_246_75,(6,0,3):C.UVGC_247_79,(6,0,4):C.UVGC_247_80,(6,0,5):C.UVGC_246_78,(4,0,3):C.UVGC_195_6,(4,0,4):C.UVGC_195_7,(3,0,3):C.UVGC_195_6,(3,0,4):C.UVGC_195_7,(8,0,3):C.UVGC_196_8,(8,0,4):C.UVGC_196_9,(7,0,0):C.UVGC_246_74,(7,0,2):C.UVGC_246_75,(7,0,3):C.UVGC_246_76,(7,0,4):C.UVGC_246_77,(7,0,5):C.UVGC_246_78,(5,0,3):C.UVGC_195_6,(5,0,4):C.UVGC_195_7,(1,0,3):C.UVGC_195_6,(1,0,4):C.UVGC_195_7,(11,3,3):C.UVGC_199_12,(11,3,4):C.UVGC_199_13,(10,3,3):C.UVGC_199_12,(10,3,4):C.UVGC_199_13,(9,3,3):C.UVGC_198_10,(9,3,4):C.UVGC_198_11,(2,1,3):C.UVGC_196_9,(2,1,4):C.UVGC_196_8,(0,1,3):C.UVGC_196_9,(0,1,4):C.UVGC_196_8,(4,1,3):C.UVGC_195_6,(4,1,4):C.UVGC_195_7,(3,1,3):C.UVGC_195_6,(3,1,4):C.UVGC_195_7,(8,1,0):C.UVGC_248_81,(8,1,2):C.UVGC_248_82,(8,1,3):C.UVGC_248_83,(8,1,4):C.UVGC_248_84,(8,1,5):C.UVGC_248_85,(6,1,0):C.UVGC_243_63,(6,1,3):C.UVGC_243_64,(6,1,4):C.UVGC_243_65,(6,1,5):C.UVGC_243_66,(7,1,1):C.UVGC_200_14,(7,1,3):C.UVGC_201_16,(7,1,4):C.UVGC_201_17,(5,1,3):C.UVGC_195_6,(5,1,4):C.UVGC_195_7,(1,1,3):C.UVGC_195_6,(1,1,4):C.UVGC_195_7,(2,2,3):C.UVGC_196_9,(2,2,4):C.UVGC_196_8,(0,2,3):C.UVGC_196_9,(0,2,4):C.UVGC_196_8,(4,2,3):C.UVGC_195_6,(4,2,4):C.UVGC_195_7,(3,2,3):C.UVGC_195_6,(3,2,4):C.UVGC_195_7,(8,2,0):C.UVGC_245_69,(8,2,2):C.UVGC_245_70,(8,2,3):C.UVGC_245_71,(8,2,4):C.UVGC_245_72,(8,2,5):C.UVGC_245_73,(6,2,1):C.UVGC_200_14,(6,2,3):C.UVGC_200_15,(6,2,4):C.UVGC_198_10,(7,2,0):C.UVGC_243_63,(7,2,3):C.UVGC_244_67,(7,2,4):C.UVGC_244_68,(7,2,5):C.UVGC_243_66,(5,2,3):C.UVGC_195_6,(5,2,4):C.UVGC_195_7,(1,2,3):C.UVGC_195_6,(1,2,4):C.UVGC_195_7})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_256_95,(0,0,2):C.UVGC_256_96,(0,0,1):C.UVGC_256_97,(0,1,0):C.UVGC_258_101,(0,1,2):C.UVGC_258_102,(0,1,1):C.UVGC_258_103})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.H__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_257_98,(0,0,2):C.UVGC_257_99,(0,0,1):C.UVGC_257_100,(0,1,0):C.UVGC_261_106,(0,1,2):C.UVGC_261_107,(0,1,1):C.UVGC_261_108})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_236_50})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.HA ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_238_52})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_237_51})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_239_53})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_258_101,(0,0,2):C.UVGC_258_102,(0,0,1):C.UVGC_258_103,(0,1,0):C.UVGC_256_95,(0,1,2):C.UVGC_256_96,(0,1,1):C.UVGC_256_97})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.H__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_261_106,(0,0,2):C.UVGC_261_107,(0,0,1):C.UVGC_261_108,(0,1,0):C.UVGC_257_98,(0,1,2):C.UVGC_257_99,(0,1,1):C.UVGC_257_100})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_259_104})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.HA ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_262_109})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_260_105})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_263_110})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_205_21,(0,1,0):C.UVGC_188_4,(0,2,0):C.UVGC_188_4})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_205_21,(0,1,0):C.UVGC_188_4,(0,2,0):C.UVGC_188_4})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_205_21,(0,1,0):C.UVGC_250_87,(0,2,0):C.UVGC_250_87})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_202_18,(0,1,0):C.UVGC_190_5,(0,2,0):C.UVGC_190_5})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_202_18,(0,1,0):C.UVGC_190_5,(0,2,0):C.UVGC_190_5})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_202_18,(0,1,0):C.UVGC_231_45,(0,2,0):C.UVGC_231_45})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_203_19,(0,1,0):C.UVGC_206_22,(0,1,1):C.UVGC_206_23,(0,1,2):C.UVGC_206_24,(0,1,3):C.UVGC_206_25,(0,1,5):C.UVGC_206_26,(0,1,4):C.UVGC_206_27,(0,2,0):C.UVGC_206_22,(0,2,1):C.UVGC_206_23,(0,2,2):C.UVGC_206_24,(0,2,3):C.UVGC_206_25,(0,2,5):C.UVGC_206_26,(0,2,4):C.UVGC_206_27})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_203_19,(0,1,0):C.UVGC_206_22,(0,1,1):C.UVGC_206_23,(0,1,3):C.UVGC_206_24,(0,1,4):C.UVGC_206_25,(0,1,5):C.UVGC_206_26,(0,1,2):C.UVGC_206_27,(0,2,0):C.UVGC_206_22,(0,2,1):C.UVGC_206_23,(0,2,3):C.UVGC_206_24,(0,2,4):C.UVGC_206_25,(0,2,5):C.UVGC_206_26,(0,2,2):C.UVGC_206_27})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_203_19,(0,1,0):C.UVGC_206_22,(0,1,1):C.UVGC_206_23,(0,1,2):C.UVGC_206_24,(0,1,3):C.UVGC_206_25,(0,1,5):C.UVGC_206_26,(0,1,4):C.UVGC_251_88,(0,2,0):C.UVGC_206_22,(0,2,1):C.UVGC_206_23,(0,2,2):C.UVGC_206_24,(0,2,3):C.UVGC_206_25,(0,2,5):C.UVGC_206_26,(0,2,4):C.UVGC_251_88})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_203_19,(0,1,0):C.UVGC_206_22,(0,1,1):C.UVGC_206_23,(0,1,3):C.UVGC_206_24,(0,1,4):C.UVGC_206_25,(0,1,5):C.UVGC_206_26,(0,1,2):C.UVGC_206_27,(0,2,0):C.UVGC_206_22,(0,2,1):C.UVGC_206_23,(0,2,3):C.UVGC_206_24,(0,2,4):C.UVGC_206_25,(0,2,5):C.UVGC_206_26,(0,2,2):C.UVGC_206_27})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_203_19,(0,1,0):C.UVGC_206_22,(0,1,1):C.UVGC_206_23,(0,1,2):C.UVGC_206_24,(0,1,3):C.UVGC_206_25,(0,1,5):C.UVGC_206_26,(0,1,4):C.UVGC_206_27,(0,2,0):C.UVGC_206_22,(0,2,1):C.UVGC_206_23,(0,2,2):C.UVGC_206_24,(0,2,3):C.UVGC_206_25,(0,2,5):C.UVGC_206_26,(0,2,4):C.UVGC_206_27})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_203_19,(0,1,0):C.UVGC_206_22,(0,1,2):C.UVGC_206_23,(0,1,3):C.UVGC_206_24,(0,1,4):C.UVGC_206_25,(0,1,5):C.UVGC_206_26,(0,1,1):C.UVGC_232_46,(0,2,0):C.UVGC_206_22,(0,2,2):C.UVGC_206_23,(0,2,3):C.UVGC_206_24,(0,2,4):C.UVGC_206_25,(0,2,5):C.UVGC_206_26,(0,2,1):C.UVGC_232_46})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_226_36,(0,0,1):C.UVGC_226_37})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_228_40,(0,0,1):C.UVGC_228_41})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_222_28,(0,0,0):C.UVGC_222_29})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_224_32,(0,0,1):C.UVGC_224_33})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_253_90,(0,0,2):C.UVGC_253_91,(0,0,1):C.UVGC_253_92})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_227_38,(0,0,1):C.UVGC_227_39})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_223_30,(0,0,0):C.UVGC_223_31})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_229_42,(0,0,1):C.UVGC_229_43})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_225_34,(0,0,1):C.UVGC_225_35})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_253_90,(0,0,2):C.UVGC_253_91,(0,0,1):C.UVGC_253_92})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_254_93,(0,1,0):C.UVGC_255_94})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_234_48,(0,1,0):C.UVGC_235_49})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_204_20,(0,1,0):C.UVGC_187_3,(0,2,0):C.UVGC_187_3})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_204_20,(0,1,0):C.UVGC_187_3,(0,2,0):C.UVGC_187_3})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_252_89,(0,2,0):C.UVGC_252_89,(0,1,0):C.UVGC_249_86,(0,3,0):C.UVGC_249_86})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_204_20,(0,1,0):C.UVGC_187_3,(0,2,0):C.UVGC_187_3})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_204_20,(0,1,0):C.UVGC_187_3,(0,2,0):C.UVGC_187_3})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_233_47,(0,2,0):C.UVGC_233_47,(0,1,0):C.UVGC_230_44,(0,3,0):C.UVGC_230_44})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_241_56,(0,0,1):C.UVGC_241_57,(0,0,2):C.UVGC_241_58,(0,0,3):C.UVGC_241_59,(0,1,0):C.UVGC_240_54,(0,1,3):C.UVGC_240_55})

