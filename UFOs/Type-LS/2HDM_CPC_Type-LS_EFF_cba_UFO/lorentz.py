# This file was automatically created by FeynRules 2.3.36
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Wed 19 Aug 2020 10:30:59


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


UUS1 = Lorentz(name = 'UUS1',
               spins = [ -1, -1, 1 ],
               structure = '1')

UUV1 = Lorentz(name = 'UUV1',
               spins = [ -1, -1, 3 ],
               structure = 'P(3,2) + P(3,3)')

SSS1 = Lorentz(name = 'SSS1',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS1 = Lorentz(name = 'FFS1',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1)')

FFS2 = Lorentz(name = 'FFS2',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) - ProjP(2,1)')

FFS3 = Lorentz(name = 'FFS3',
               spins = [ 2, 2, 1 ],
               structure = 'ProjP(2,1)')

FFS4 = Lorentz(name = 'FFS4',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) + ProjP(2,1)')

FFV1 = Lorentz(name = 'FFV1',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV2 = Lorentz(name = 'FFV2',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV3 = Lorentz(name = 'FFV3',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) - 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV4 = Lorentz(name = 'FFV4',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV5 = Lorentz(name = 'FFV5',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 4*Gamma(3,2,-1)*ProjP(-1,1)')

VSS1 = Lorentz(name = 'VSS1',
               spins = [ 3, 1, 1 ],
               structure = 'P(1,2) - P(1,3)')

VVS1 = Lorentz(name = 'VVS1',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVV1 = Lorentz(name = 'VVV1',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

SSSS1 = Lorentz(name = 'SSSS1',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV2 = Lorentz(name = 'VVVV2',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV5 = Lorentz(name = 'VVVV5',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')




VVStop = Lorentz(name = 'VVStop',
                 spins = [ 3, 3, 1 ],
                 structure = 'FTriEvenTop(2*P(-1,1)*P(-1,2)) * (Metric(1,2)*P(-1,1)*P(-1,2) - P(2,1)*P(1,2))')

VVSbot = Lorentz(name = 'VVSbot',
                 spins = [ 3, 3, 1 ],
                 structure = 'FTriEvenBot(2*P(-1,1)*P(-1,2)) * (Metric(1,2)*P(-1,1)*P(-1,2) - P(2,1)*P(1,2))')

VVSOddtop = Lorentz(name = 'VVSOddtop',
                    spins = [ 3, 3, 1 ],
                    structure = 'FTriOddTop(2*P(-1,1)*P(-1,2)) * (Epsilon(1,2,-1,-2)*P(-1,1)*P(-2,2))')

VVSOddbot = Lorentz(name = 'VVSOddbot',
                    spins = [ 3, 3, 1 ],
                    structure = 'FTriOddBot(2*P(-1,1)*P(-1,2)) * (Epsilon(1,2,-1,-2)*P(-1,1)*P(-2,2))')


VVVtop = Lorentz(name = 'VVVtop',
                    spins = [ 3, 3, 3 ],
                    structure = 'FTriZTop(2*P(-1,1)*P(-1,2)) * (Epsilon(1,2,-1,-2)*P(-1,1)*P(-2,2)*P(3,3))')

VVVbot = Lorentz(name = 'VVVbot',
                    spins = [ 3, 3, 3 ],
                    structure = 'FTriZBot(2*P(-1,1)*P(-1,2)) * (Epsilon(1,2,-1,-2)*P(-1,1)*P(-2,2)*P(3,3))')



VVSSFtop = Lorentz(name = 'VVSSFtop',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'FBoxEvenTop(P(-1,1)*P(-1,2),P(-1,1)*P(-1,3),P(-1,2)*P(-1,3),P(-1,3)*P(-1,3)) * (Metric(1,2)*P(-1,1)*P(-1,2) - P(2,1)*P(1,2))')

VVSSFbot = Lorentz(name = 'VVSSFbot',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'FBoxEvenBot(P(-1,1)*P(-1,2),P(-1,1)*P(-1,3),P(-1,2)*P(-1,3),P(-1,3)*P(-1,3)) * (Metric(1,2)*P(-1,1)*P(-1,2) - P(2,1)*P(1,2))')

VVSSGtop = Lorentz(name = 'VVSSGtop',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'GBoxEvenTop(P(-1,1)*P(-1,2),P(-1,1)*P(-1,3),P(-1,2)*P(-1,3),P(-1,3)*P(-1,3)) * (2*Metric(1,2)*(P(-1,1)*P(-1,3))*(P(-2,2)*P(-2,3)) - (P(-1,3)*P(-1,3))*(P(-2,1)*P(-2,2))*Metric(1,2) + (P(-1,3)*P(-1,3))*P(1,2)*P(2,1) - 2*(P(-1,2)*P(-1,3))*P(2,1)*P(1,3) - 2*(P(-1,1)*P(-1,3))*P(1,2)*P(2,3) + 2*(P(-1,1)*P(-1,2))*P(1,3)*P(2,3))')

VVSSGbot = Lorentz(name = 'VVSSGbot',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'GBoxEvenBot(P(-1,1)*P(-1,2),P(-1,1)*P(-1,3),P(-1,2)*P(-1,3),P(-1,3)*P(-1,3)) * (2*Metric(1,2)*(P(-1,1)*P(-1,3))*(P(-2,2)*P(-2,3)) - (P(-1,3)*P(-1,3))*(P(-2,1)*P(-2,2))*Metric(1,2) + (P(-1,3)*P(-1,3))*P(1,2)*P(2,1) - 2*(P(-1,2)*P(-1,3))*P(2,1)*P(1,3) - 2*(P(-1,1)*P(-1,3))*P(1,2)*P(2,3) + 2*(P(-1,1)*P(-1,2))*P(1,3)*P(2,3))')

VVAAFtop = Lorentz(name = 'VVAAFtop',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'FBoxOddTop(P(-1,1)*P(-1,2),P(-1,1)*P(-1,3),P(-1,2)*P(-1,3),P(-1,3)*P(-1,3)) * (Metric(1,2)*P(-1,1)*P(-1,2) - P(2,1)*P(1,2))')

VVAAFbot = Lorentz(name = 'VVAAFbot',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'FBoxOddBot(P(-1,1)*P(-1,2),P(-1,1)*P(-1,3),P(-1,2)*P(-1,3),P(-1,3)*P(-1,3)) * (Metric(1,2)*P(-1,1)*P(-1,2) - P(2,1)*P(1,2))')

VVAAGtop = Lorentz(name = 'VVAAGtop',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'GBoxOddTop(P(-1,1)*P(-1,2),P(-1,1)*P(-1,3),P(-1,2)*P(-1,3),P(-1,3)*P(-1,3)) * (2*Metric(1,2)*(P(-1,1)*P(-1,3))*(P(-2,2)*P(-2,3)) - (P(-1,3)*P(-1,3))*(P(-2,1)*P(-2,2))*Metric(1,2) + (P(-1,3)*P(-1,3))*P(1,2)*P(2,1) - 2*(P(-1,2)*P(-1,3))*P(2,1)*P(1,3) - 2*(P(-1,1)*P(-1,3))*P(1,2)*P(2,3) + 2*(P(-1,1)*P(-1,2))*P(1,3)*P(2,3))')

VVAAGbot = Lorentz(name = 'VVAAGbot',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'GBoxOddBot(P(-1,1)*P(-1,2),P(-1,1)*P(-1,3),P(-1,2)*P(-1,3),P(-1,3)*P(-1,3)) * (2*Metric(1,2)*(P(-1,1)*P(-1,3))*(P(-2,2)*P(-2,3)) - (P(-1,3)*P(-1,3))*(P(-2,1)*P(-2,2))*Metric(1,2) + (P(-1,3)*P(-1,3))*P(1,2)*P(2,1) - 2*(P(-1,2)*P(-1,3))*P(2,1)*P(1,3) - 2*(P(-1,1)*P(-1,3))*P(1,2)*P(2,3) + 2*(P(-1,1)*P(-1,2))*P(1,3)*P(2,3))')

VVSAFtop = Lorentz(name = 'VVSAFtop',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'FBoxSATop(P(-1,1)*P(-1,2),P(-1,1)*P(-1,3),P(-1,2)*P(-1,3),P(-1,3)*P(-1,3)) * (Epsilon(1,2,-1,-2)*P(-1,1)*P(-2,2))')

VVSAFbot = Lorentz(name = 'VVSAFbot',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'FBoxSABot(P(-1,1)*P(-1,2),P(-1,1)*P(-1,3),P(-1,2)*P(-1,3),P(-1,3)*P(-1,3)) * (Epsilon(1,2,-1,-2)*P(-1,1)*P(-2,2))')

VVSAGtop = Lorentz(name = 'VVSAGtop',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'GBoxSATop(P(-1,1)*P(-1,2),P(-1,1)*P(-1,3),P(-1,2)*P(-1,3),P(-1,3)*P(-1,3)) * (Epsilon(2,-1,-2,-3)*P(-1,1)*P(-2,2)*P(-3,3)*P(1,3)+Epsilon(1,-1,-2,-3)*P(-1,1)*P(-2,2)*P(-3,3)*P(2,3)+Epsilon(1,2,-1,-3)*P(-1,1)*P(-3,3)*P(-2,2)*P(-2,3)+Epsilon(1,2,-2,-3)*P(-2,2)*P(-3,3)*P(-1,1)*P(-1,3))')

VVSAGbot = Lorentz(name = 'VVSAGbot',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'GBoxSABot(P(-1,1)*P(-1,2),P(-1,1)*P(-1,3),P(-1,2)*P(-1,3),P(-1,3)*P(-1,3)) * (Epsilon(2,-1,-2,-3)*P(-1,1)*P(-2,2)*P(-3,3)*P(1,3)+Epsilon(1,-1,-2,-3)*P(-1,1)*P(-2,2)*P(-3,3)*P(2,3)+Epsilon(1,2,-1,-3)*P(-1,1)*P(-3,3)*P(-2,2)*P(-2,3)+Epsilon(1,2,-2,-3)*P(-2,2)*P(-3,3)*P(-1,1)*P(-1,3))')

gagaStop = Lorentz(name = 'gagaStop',
                 spins = [ 3, 3, 1 ],
                 structure = 'FTriPhotonTop(2*P(-1,1)*P(-1,2)) * (Metric(1,2)*P(-1,1)*P(-1,2) - P(2,1)*P(1,2))')

gagaSbot = Lorentz(name = 'gagaSbot',
                 spins = [ 3, 3, 1 ],
                 structure = 'FTriPhotonBot(2*P(-1,1)*P(-1,2)) * (Metric(1,2)*P(-1,1)*P(-1,2) - P(2,1)*P(1,2))')

gagaSW = Lorentz(name = 'gagaSW',
                 spins = [ 3, 3, 1 ],
                 structure = 'FTriPhotonW(2*P(-1,1)*P(-1,2)) * (Metric(1,2)*P(-1,1)*P(-1,2) - P(2,1)*P(1,2))')

gagaSS = Lorentz(name = 'gagaSS',
                 spins = [ 3, 3, 1 ],
                 structure = 'FTriPhotonS(2*P(-1,1)*P(-1,2)) * (Metric(1,2)*P(-1,1)*P(-1,2) - P(2,1)*P(1,2))')

gagaSOddtop = Lorentz(name = 'gagaSOddtop',
                 spins = [ 3, 3, 1 ],
                 structure = 'FTriPhotonOddTop(2*P(-1,1)*P(-1,2)) * (Epsilon(1,2,-1,-2)*P(-1,1)*P(-2,2))')

gagaSOddbot = Lorentz(name = 'gagaSOddbot',
                 spins = [ 3, 3, 1 ],
                 structure = 'FTriPhotonOddBot(2*P(-1,1)*P(-1,2)) * (Epsilon(1,2,-1,-2)*P(-1,1)*P(-2,2))')
