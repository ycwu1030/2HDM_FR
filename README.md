# 2HDM_FR
The FeynRule 2HDM Files

## About
Actually, in FeynRule model databasis, there is a model file for 2HDM. However, I'm not used to the convention there. So I made this to use another convention.

In current convention, I only consider CP conserving case. The input parameters are

$$v, m_h, m_H, m_A, m_{\pm}, \cos(\beta-\alpha), \tan\beta, m_{12}^2$$

## Download

Either finding the corresponding files in `RELEASE` folder or checking [release page](https://github.com/ycwu1030/2HDM_FR/releases/tag/v0.5.1).

## Usage

I already made several UFOs and FA model files in corresponding folders.

For the UFO files, the name conventions are:
- With `EFF`, the LO model file + Effective gluon-gluon-Scalar, gluon-gluon-Scalar-Scalar and gamma-gamma-scalar vertices with correct form-factor. With these Effective vertices, the numerical value for `ggF` production of scalar or scalar pair should be the same as `NLO` model file. (No charged scalar yet)
- With `NLO`, the model contains the CTs for QCD NLO calculation in MG5
- Without any of above, it is a LO model file. Loop-induced vertices can not be calculated.

## TODO

- [x] Adding the loop-induced vertex as effective vertex with form factors, such that $h\to\gamma\gamma$ can be handled.
- [ ] Adding the loop-induced vertex as effective vertex for charged scalar.
- [ ] Adding CP-violation case.

## WARNING

For the model with **effective vertices**, we don't fully check through those effective vertices. As far as we checked, for process not involving interference effects, they should be fine (we've checked the scalar-pair productions with triangle and box diagrams). But be careful in any case one wants to check the interference effects (we've checked the $t\bar t$ case)! For the interference effects involving effective vertices, one might also want to using NLO model and check [hacking the MG5](https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/LoopInducedTimesTree).
