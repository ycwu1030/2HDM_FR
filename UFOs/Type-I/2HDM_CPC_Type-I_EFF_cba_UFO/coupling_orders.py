# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.0.1 for Mac OS X ARM (64-bit) (January 28, 2022)
# Date: Fri 8 Jul 2022 20:48:24


from object_library import all_orders, CouplingOrder


QCD = CouplingOrder(name = 'QCD',
                    expansion_order = 99,
                    hierarchy = 1)

QED = CouplingOrder(name = 'QED',
                    expansion_order = 99,
                    hierarchy = 2)


NLOT = CouplingOrder(name = 'NLOT', # ggS triangle nlo couplings
                    expansion_order = 1,
                    hierarchy = 2)

NLOTHL = CouplingOrder(name = 'NLOTHL', # ggS triangle nlo couplings for HL
                    expansion_order = 1,
                    hierarchy = 2)

NLOTHH = CouplingOrder(name = 'NLOTHH', # ggS triangle nlo couplings for HH
                    expansion_order = 1,
                    hierarchy = 2)

NLOTHA = CouplingOrder(name = 'NLOTHA', # ggS triangle nlo couplings for HA
                    expansion_order = 1,
                    hierarchy = 2)

NLOB = CouplingOrder(name = 'NLOB', # ggSS box nlo couplings
                    expansion_order = 1,
                    hierarchy = 2)

NLOZ = CouplingOrder(name = 'NLOZ', # ggZ nlo couplings
                    expansion_order = 1,
                    hierarchy = 2)

NLOEW = CouplingOrder(name = 'NLOEW', # gagaS nlo couplings
                    expansion_order = 1,
                    hierarchy = 2)

NLOEWHL = CouplingOrder(name = 'NLOEWHL', # gagaS nlo couplings for HL
                    expansion_order = 1,
                    hierarchy = 2)

NLOEWHH = CouplingOrder(name = 'NLOEWHH', # gagaS nlo couplings for HH
                    expansion_order = 1,
                    hierarchy = 2)

NLOEWHA = CouplingOrder(name = 'NLOEWHA', # gagaS nlo couplings for HA
                    expansion_order = 1,
                    hierarchy = 2)
