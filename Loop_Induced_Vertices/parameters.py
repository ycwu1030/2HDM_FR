
# This is for Type-II, should add other type later.
kHLUp = Parameter(name = 'kHLUp',
                   nature = 'internal',
                   type = 'real',
                   value = 'ca/sb',
                   texname = '\\kappa_{HL}^{u}')

kHLDo = Parameter(name = 'kHLDo',
                   nature = 'internal',
                   type = 'real',
                   value = '-sa/cb',
                   texname = '\\kappa_{HL}^{d}')

kHHUp = Parameter(name = 'kHHUp',
                   nature = 'internal',
                   type = 'real',
                   value = 'sa/sb',
                   texname = '\\kappa_{HH}^{u}')

kHHDo = Parameter(name = 'kHHDo',
                   nature = 'internal',
                   type = 'real',
                   value = 'ca/cb',
                   texname = '\\kappa_{HH}^{d}')

kHAUp = Parameter(name = 'kHAUp',
                   nature = 'internal',
                   type = 'real',
                   value = 'cb/sb',
                   texname = '\\kappa_{HA}^{u}')

kHADo = Parameter(name = 'kHADo',
                   nature = 'internal',
                   type = 'real',
                   value = 'sb/cb',
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
