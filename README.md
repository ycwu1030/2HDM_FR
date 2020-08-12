# 2HDM_FR
The FeynRule 2HDM Files

## About
Actually, in FeynRule model databasis, there is a model file for 2HDM. However, I'm not used to the convention there. So I made this to use another convention.

In current convention, I only consider CP conserving case. The input parameters are

$$v, m_h, m_H, m_A, m_{\pm}, \alpha, \beta, m_{12}^2$$

## Usage

I already made several UFOs and FA model files in corresponding folders.

For the UFO files, the name conventions are:
- With `ggF`, the model contains the effective `ggF` vertices for Higgs production. The numerical value is not correct, just easier for event generation
- With `NLO`, the model contains the CTs for QCD NLO calculation in MG5
- Without any of above, it is a LO model file. Loop-induced vertices can not be calculated.

## TODO

- [ ] Adding the loop-induced vertex as effective vertex with form factors, such that $h\to\gamma\gamma$ can be handled
- [ ] Adding CP-violation case.