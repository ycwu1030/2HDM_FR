
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
