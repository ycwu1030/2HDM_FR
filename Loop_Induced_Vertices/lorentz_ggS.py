


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
