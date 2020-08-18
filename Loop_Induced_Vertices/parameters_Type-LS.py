
# This is for Type-LS
kHLUp = Parameter(name = 'kHLUp',
                  nature = 'internal',
                  type = 'real',
                  value = 'ca/sb',
                  texname = '\\kappa_{HL}^{u}')

kHLDo = Parameter(name = 'kHLDo',
                  nature = 'internal',
                  type = 'real',
                  value = 'ca/sb',
                  texname = '\\kappa_{HL}^{d}')

kHHUp = Parameter(name = 'kHHUp',
                  nature = 'internal',
                  type = 'real',
                  value = 'sa/sb',
                  texname = '\\kappa_{HH}^{u}')

kHHDo = Parameter(name = 'kHHDo',
                  nature = 'internal',
                  type = 'real',
                  value = 'sa/sb',
                  texname = '\\kappa_{HH}^{d}')

kHAUp = Parameter(name = 'kHAUp',
                  nature = 'internal',
                  type = 'real',
                  value = 'cb/sb',
                  texname = '\\kappa_{HA}^{u}')

kHADo = Parameter(name = 'kHADo',
                  nature = 'internal',
                  type = 'real',
                  value = '-cb/sb',
                  texname = '\\kappa_{HA}^{d}')

# Axial Charge
AUp = Parameter(name = 'AUp',
                nature = 'internal',
                type = 'real',
                value = '1',
                texname = 'a_{Z}^{u}')

# Axial Charge
ADo = Parameter(name = 'ADo',
                nature = 'internal',
                type = 'real',
                value = '-1',
                texname = 'a_{Z}^{d}')

kHLW = Parameter(name = 'kHLW',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sin(beta - alpha)',
                 texname = '\\kappa_{HL}^{W}')

kHHW = Parameter(name = 'kHHW',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.cos(beta-alpha)',
                 texname = '\\kappa_{HH}^{W}')

# The HL-Hp-Hm Coupling normlized to 2*MHp2/v
kHLHpm = Parameter(name = 'kHLHpm',
                   nature = 'internal',
                   type = 'real',
                   value = 'cmath.sin(beta-alpha)-m122*cmath.cos(alpha+beta)/(cb**2*sb**2*2.*MHp**2)+MHL**2*(cmath.cos(alpha-3.*beta)+3.*cmath.cos(alpha+beta))/(8.*cb*sb*MHp**2)',
                   texname = '\\kappa_{HL}^{H^{\\pm}}')

kHHHpm = Parameter(name = 'kHHHpm',
                   nature = 'internal',
                   type = 'real',
                   value = 'cmath.cos(alpha-beta)-m122*cmath.sin(alpha+beta)/(2.*cb**2*sb**2*MHp**2)+MHH**2*(cmath.sin(alpha-3*beta)+3.*cmath.sin(alpha+beta))/(8.*cb*sb*MHp**2)',
                   texname = '\\kappa_{HH}^{H^{\\pm}}')
