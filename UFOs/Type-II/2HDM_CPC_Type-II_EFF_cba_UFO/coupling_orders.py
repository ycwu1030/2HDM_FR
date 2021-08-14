# This file was automatically created by FeynRules 2.3.36
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Fri 13 Aug 2021 16:16:21


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

NLOB = CouplingOrder(name = 'NLOB', # ggSS box nlo couplings
                    expansion_order = 1,
                    hierarchy = 2)

NLOZ = CouplingOrder(name = 'NLOZ', # ggZ nlo couplings
                    expansion_order = 1,
                    hierarchy = 2)

NLOEW = CouplingOrder(name = 'NLOEW', # gagaS nlo couplings
                    expansion_order = 1,
                    hierarchy = 2)
