
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
