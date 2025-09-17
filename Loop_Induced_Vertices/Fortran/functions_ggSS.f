
      SUBROUTINE BERNINI(N)
C-----------------------------------)
C-- INITIALIZE THE BERNOULLI NUMBER,
C-- USED IN DILOGARITHM EXPANSION
C-----------------------------------)
      IMPLICIT DOUBLE PRECISION (A-H,O-Z)
      COMMON/BERNOULLI/B(18)
      COMMON/CONST/ZETA2
      COMMON/POLY/NBER

      NBER=N
      PI=4.D0*DATAN(1.D0)

      B(1)=-1.D0/2.D0
      B(2)=1.D0/6.D0
      B(3)=0.D0
      B(4)=-1.D0/30.D0
      B(5)=0.D0
      B(6)=1.D0/42.D0
      B(7)=0.D0
      B(8)=-1.D0/30.D0
      B(9)=0.D0
      B(10)=5.D0/66.D0
      B(11)=0.D0
      B(12)=-691.D0/2730.D0
      B(13)=0.D0
      B(14)=7.D0/6.D0
      B(15)=0.D0
      B(16)=-3617.D0/510.D0
      B(17)=0.D0
      B(18)=43867.D0/798.D0
      ZETA2=PI**2/6.D0

C-- DEVIDED BY (I+1)!, WHICH WILL BE USED IN DILOGRITHM
      DO 995 I=1,18
        B(I)=B(I)/FAC(I+1)
995   CONTINUE
      RETURN
      END


      DOUBLE PRECISION FUNCTION FAC(N)
C-- MATHEMATICAL FACTORIAL
      IMPLICIT DOUBLE PRECISION (A-H,O-Z)
      FAC=1.D0
      IF(N.EQ.0) RETURN
      DO 986 I=1,N
        FAC=FAC*DFLOAT(I)
986   CONTINUE
      RETURN
      END


      DOUBLE COMPLEX FUNCTION CLI2(X)
C----------------------------------------------------)
C-- TAYLOR-EXPANSION FOR COMPLEX DILOGARITHM
C-- REFERENCE:
C--   Eq.(4.3) in Proc. R. Soc. Lond. A 459 (2003) 2807-2819
C-- CONVERGE WHEN |-CDLOG(1D0-X)|<2*PI
C----------------------------------------------------)
      IMPLICIT DOUBLE PRECISION (A-H,O-Z)
      DOUBLE COMPLEX X,Z
      COMMON/BERNOULLI/B(18)
      COMMON/CONST/ZETA2
      COMMON/POLY/NBER

      N=NBER-1
      Z=-CDLOG(1.D0-X)
      CLI2=B(NBER)
      DO 111 I=N,1,-1
        CLI2=Z*CLI2+B(I)
111   CONTINUE
      CLI2=Z**2*CLI2+Z
      RETURN
      END

      DOUBLE COMPLEX FUNCTION LI2(X)
C-------------------------------------------------------------)
C-- COMPLEX DILOGARITHM (SPENCE-FUNCTION)
C-- SOME LINEAR TRANSFORMATIONS OF THE DILOGARITHM ARE ALSO USED
C-- REFERENCE:
C--   Eq.(3.2) TO Eq.(3.6) in
C--       Proc. R. Soc. Lond. A 459 (2003) 2807-2819
C-------------------------------------------------------------)
      IMPLICIT DOUBLE PRECISION (A-H,O-Z)
      DOUBLE COMPLEX X,Y,CLI2
      COMMON/CONST/ZETA2
      ZERO=1.D-40
      XR=DREAL(X)
      XI=DIMAG(X)
      R2=XR*XR+XI*XI
      IF(R2.LE.ZERO)THEN
        LI2=X
        RETURN
      ENDIF
      RR=XR/R2
      IF(R2.EQ.1.D0.AND.XI.EQ.0.D0)THEN
        IF(XR.EQ.1.D0)THEN
          LI2=DCMPLX(ZETA2)
        ELSE
          LI2=-DCMPLX(ZETA2/2.D0)
        ENDIF
        RETURN
      ELSEIF(R2.GT.1.D0.AND.RR.GT.0.5D0)THEN
        Y=(X-1.D0)/X
        LI2=CLI2(Y)+ZETA2-CDLOG(X)*CDLOG(1.D0-X)+0.5D0*CDLOG(X)**2
        RETURN
      ELSEIF(R2.GT.1.D0.AND.RR.LE.0.5D0)THEN
        Y=1.D0/X
        LI2=-CLI2(Y)-ZETA2-0.5D0*CDLOG(-X)**2
        RETURN
      ELSEIF(R2.LE.1.D0.AND.XR.GT.0.5D0)THEN
        Y=1.D0-X
        LI2=-CLI2(Y)+ZETA2-CDLOG(X)*CDLOG(1.D0-X)
        RETURN
      ELSEIF(R2.LE.1.D0.AND.XR.LE.0.5D0)THEN
        Y=X
        LI2=CLI2(Y)
        RETURN
      ENDIF
      END

      DOUBLE COMPLEX FUNCTION MYMDL_CI(A,B,C)
C--------------------------------------------------)
C-- BASIC SCALAR INTEGRAL
C-- I(a,b,c) = Integrate[Log[a*x+b]/(x-c),{x,0,1}]
C--    = Log(a*c+b)*Log(1-1/c)-Li2(1-(a+b)/(a*c+b))+Li2(1-b/(a*c+b))
C-- REFERENCE:
C--   Phys. Rev. D 42 (1990) 3100
C--------------------------------------------------)
      IMPLICIT DOUBLE PRECISION (A-H,O-Z)
      DOUBLE COMPLEX C,LI2

      MYMDL_CI = CDLOG(A*C+B)*CDLOG(1.D0-1.D0/C)
     &    -LI2(1.D0-(A+B)/(A*C+B))+LI2(1.D0-B/(A*C+B))
      RETURN
      END


      DOUBLE COMPLEX FUNCTION CJ(A,B,C)
C-----------------------------------------------------)
C-- BASIC SCALAR INTEGRAL
C-- J(a,b,c) = Integrate[Log[a*x*(1-x)-b]/(x-c),{x,0,1}]
C--   = Log(a*c*(1-c)-b)*Log(1-1/c)-Li2((c-1)/(c-ap))
C--    +Li2(c/(c-ap))-Li2((c-1)/(c-am))+Li2(c/(c-am))
C-- REFERENCE:
C--   Phys. Rev. D 42 (1990) 3100
C-----------------------------------------------------)
      IMPLICIT DOUBLE PRECISION (A-H,O-Z)
      DOUBLE COMPLEX C,CB,AP,AM,LI2
      COMMON/CUTS/EPS,REPS
      CB = B*DCMPLX(1.D0,-REPS)
      C=DCMPLX(DREAL(C),DIMAG(C)/1.D3)
      CC = C
      AP = 0.5D0*(1.D0+CDSQRT(1.D0-4.D0*CB/A))
      AM = 0.5D0*(1.D0-CDSQRT(1.D0-4.D0*CB/A))
      CJ = CDLOG(A*CC*(1.D0-CC)-CB)*CDLOG(1.D0-1.D0/C)
     &    -LI2((CC-1.D0)/(CC-AP))+LI2(CC/(CC-AP))
     &    -LI2((CC-1.D0)/(CC-AM))+LI2(CC/(CC-AM))
      RETURN
      END


      SUBROUTINE INISCAL(AMQ,S,T,U,M1,M2,
     &    C0AB,C0AC,C0AD,C0BC,C0BD,C0CD,D0ABC,D0BAC,D0ACB)
C---------------------------------------------------------)
C-- ROUTINE USED TO CALCULATE SCALAR INTEGRAL
C-- COPIED FROM 'hpair' PROGRAM, by Michael Spira
C-- Website: http://tiger.web.psi.ch/proglist.html
C---------------------------------------------------------)
      IMPLICIT DOUBLE PRECISION (A-B,D-H,O-Z)
      IMPLICIT DOUBLE COMPLEX (C)
      DOUBLE PRECISION M1,M2
      DOUBLE COMPLEX D04
      DOUBLE COMPLEX C03
      DOUBLE COMPLEX LI2
      DOUBLE COMPLEX MYMDL_CI,CJ
      DOUBLE COMPLEX R,R0,X,XP,XM
      DOUBLE COMPLEX C0AB,C0AC,C0AD,C0BC,C0BD,C0CD,D0ABC,D0BAC,D0ACB
      DOUBLE PRECISION EPS, REPS
      COMMON/CUTS/ EPS,REPS

      EPS=1d-8
      REPS=1d-15
      CALL BERNINI(18)

      DQ2=AMQ**2

      CQ2=DQ2*DCMPLX(1.D0,-REPS)
      CA5 = CDSQRT(1.D0-4.D0*CQ2/S)
      C0AB = 0.5D0*CDLOG((CA5+1.D0)/(CA5-1.D0))**2/S*DQ2

      S1=M1**2
      S2=M2**2
      S5=S
      CA1 = CDSQRT(1.D0-4.D0*CQ2/S1)
      CA2 = CDSQRT(1.D0-4.D0*CQ2/S2)
      CA5 = CDSQRT(1.D0-4.D0*CQ2/S5)
      XLAM=DSQRT(S1**2+S2**2+S5**2-2.D0*(S1*S2+S1*S5+S2*S5))
      CB1=1.D0/XLAM*(S1-S2-S5)
      CB2=1.D0/XLAM*(S2-S1-S5)
      CB5=1.D0/XLAM*(S5-S1-S2)
      C0CD = -(
     &       LI2((1.D0+CB1)/(CA1+CB1)) - LI2((1.D0-CB1)/(CA1-CB1))
     &     - LI2((-1.D0+CB1)/(CA1+CB1)) + LI2((-1.D0-CB1)/(CA1-CB1))
     &     + LI2((1.D0+CB2)/(CA2+CB2)) - LI2((1.D0-CB2)/(CA2-CB2))
     &     - LI2((-1.D0+CB2)/(CA2+CB2)) + LI2((-1.D0-CB2)/(CA2-CB2))
     &     + LI2((1.D0+CB5)/(CA5+CB5)) - LI2((1.D0-CB5)/(CA5-CB5))
     &     - LI2((-1.D0+CB5)/(CA5+CB5)) + LI2((-1.D0-CB5)/(CA5-CB5))
     &       )/XLAM*DQ2
      S1=0.D0
      S2=M1**2
      S5=T
      CA2 = CDSQRT(1.D0-4.D0*CQ2/S2)
      CA5 = CDSQRT(1.D0-4.D0*CQ2/S5)
      XLAM=DSQRT(S1**2+S2**2+S5**2-2.D0*(S1*S2+S1*S5+S2*S5))
      CB2=1.D0/XLAM*(S2-S1-S5)
      CB5=1.D0/XLAM*(S5-S1-S2)
      C0AC = -(
     &       LI2((1.D0+CB2)/(CA2+CB2)) - LI2((1.D0-CB2)/(CA2-CB2))
     &     - LI2((-1.D0+CB2)/(CA2+CB2)) + LI2((-1.D0-CB2)/(CA2-CB2))
     &     + LI2((1.D0+CB5)/(CA5+CB5)) - LI2((1.D0-CB5)/(CA5-CB5))
     &     - LI2((-1.D0+CB5)/(CA5+CB5)) + LI2((-1.D0-CB5)/(CA5-CB5))
     &       )/XLAM*DQ2
      S1=0.D0
      S2=M2**2
      S5=U
      CA2 = CDSQRT(1.D0-4.D0*CQ2/S2)
      CA5 = CDSQRT(1.D0-4.D0*CQ2/S5)
      XLAM=DSQRT(S1**2+S2**2+S5**2-2.D0*(S1*S2+S1*S5+S2*S5))
      CB2=1.D0/XLAM*(S2-S1-S5)
      CB5=1.D0/XLAM*(S5-S1-S2)
      C0AD = -(
     &       LI2((1.D0+CB2)/(CA2+CB2)) - LI2((1.D0-CB2)/(CA2-CB2))
     &     - LI2((-1.D0+CB2)/(CA2+CB2)) + LI2((-1.D0-CB2)/(CA2-CB2))
     &     + LI2((1.D0+CB5)/(CA5+CB5)) - LI2((1.D0-CB5)/(CA5-CB5))
     &     - LI2((-1.D0+CB5)/(CA5+CB5)) + LI2((-1.D0-CB5)/(CA5-CB5))
     &       )/XLAM*DQ2
      S1=0.D0
      S2=M1**2
      S5=U
      CA2 = CDSQRT(1.D0-4.D0*CQ2/S2)
      CA5 = CDSQRT(1.D0-4.D0*CQ2/S5)
      XLAM=DSQRT(S1**2+S2**2+S5**2-2.D0*(S1*S2+S1*S5+S2*S5))
      CB2=1.D0/XLAM*(S2-S1-S5)
      CB5=1.D0/XLAM*(S5-S1-S2)
      C0BC = -(
     &       LI2((1.D0+CB2)/(CA2+CB2)) - LI2((1.D0-CB2)/(CA2-CB2))
     &     - LI2((-1.D0+CB2)/(CA2+CB2)) + LI2((-1.D0-CB2)/(CA2-CB2))
     &     + LI2((1.D0+CB5)/(CA5+CB5)) - LI2((1.D0-CB5)/(CA5-CB5))
     &     - LI2((-1.D0+CB5)/(CA5+CB5)) + LI2((-1.D0-CB5)/(CA5-CB5))
     &       )/XLAM*DQ2
      S1=0.D0
      S2=M2**2
      S5=T
      CA2 = CDSQRT(1.D0-4.D0*CQ2/S2)
      CA5 = CDSQRT(1.D0-4.D0*CQ2/S5)
      XLAM=DSQRT(S1**2+S2**2+S5**2-2.D0*(S1*S2+S1*S5+S2*S5))
      CB2=1.D0/XLAM*(S2-S1-S5)
      CB5=1.D0/XLAM*(S5-S1-S2)
      C0BD = -(
     &       LI2((1.D0+CB2)/(CA2+CB2)) - LI2((1.D0-CB2)/(CA2-CB2))
     &     - LI2((-1.D0+CB2)/(CA2+CB2)) + LI2((-1.D0-CB2)/(CA2-CB2))
     &     + LI2((1.D0+CB5)/(CA5+CB5)) - LI2((1.D0-CB5)/(CA5-CB5))
     &     - LI2((-1.D0+CB5)/(CA5+CB5)) + LI2((-1.D0-CB5)/(CA5-CB5))
     &       )/XLAM*DQ2
      Z=M1**2
      H=M2**2
      S1=S
      S2=Z
      S5=H
      XLAM=DSQRT(S1**2+S2**2+S5**2-2.D0*(S1*S2+S1*S5+S2*S5))
      XN=T*U-Z*H
      R0=CDSQRT(1.D0+4.D0*S*CQ2/XN)
      R=(1.D0+R0)/2.D0
      RR=DREAL(R0)
      D0ACB = 2.D0/XN/RR*(CJ(Z,AMQ**2,R)+CJ(H,AMQ**2,R)
     &                   -CJ(T,AMQ**2,R)-CJ(U,AMQ**2,R))*DQ2**2
      X=CDSQRT(1.D0+4.D0*XN/S/U**2*CQ2)
      X0=DSQRT(1.D0+4.D0*XN/S/U**2*DQ2)
      XP=-U/(T-U+XLAM)*(1.D0+X)
      XM=-U/(T-U+XLAM)*(1.D0-X)
      ALP=(S+Z-H+XLAM)/2.D0/S
      BET=(U-T+XLAM)/2.D0/S
      ZERO=0.D-15
      D0ABC = 1.D0/S/U/X0*(MYMDL_CI(S,ZERO,XP)-MYMDL_CI(T-H,S,(1.D0-XM)/(1.D0-ALP))
     &      -MYMDL_CI(Z-U,ZERO,XP/ALP)+MYMDL_CI(Z-U,ZERO,XP/BET)
     &      -MYMDL_CI(T-H,S,XP/BET)
     &      -CJ(S,AMQ**2,XP)+CJ(H,AMQ**2,(1.D0-XM)/(1.D0-ALP))
     &      +CJ(Z,AMQ**2,XP/ALP)-CJ(U,AMQ**2,XP/BET)
     &      +CJ(H,AMQ**2,XP/BET)
     &      -(MYMDL_CI(S,ZERO,XM)-MYMDL_CI(T-H,S,(1.D0-XP)/(1.D0-ALP))
     &      -MYMDL_CI(Z-U,ZERO,XM/ALP)+MYMDL_CI(Z-U,ZERO,XM/BET)
     &      -MYMDL_CI(T-H,S,XM/BET)
     &      -CJ(S,AMQ**2,XM)+CJ(H,AMQ**2,(1.D0-XP)/(1.D0-ALP))
     &      +CJ(Z,AMQ**2,XM/ALP)-CJ(U,AMQ**2,XM/BET)
     &      +CJ(H,AMQ**2,XM/BET)))*DQ2**2
      X=CDSQRT(1.D0+4.D0*XN/S/T**2*CQ2)
      X0=DSQRT(1.D0+4.D0*XN/S/T**2*DQ2)
      XP=-T/(U-T+XLAM)*(1.D0+X)
      XM=-T/(U-T+XLAM)*(1.D0-X)
      ALP=(S+Z-H+XLAM)/2.D0/S
      BET=(T-U+XLAM)/2.D0/S
      D0BAC = 1.D0/S/T/X0*(MYMDL_CI(S,ZERO,XP)-MYMDL_CI(U-H,S,(1.D0-XM)/(1.D0-ALP))
     &      -MYMDL_CI(Z-T,ZERO,XP/ALP)+MYMDL_CI(Z-T,ZERO,XP/BET)
     &      -MYMDL_CI(U-H,S,XP/BET)
     &      -CJ(S,AMQ**2,XP)+CJ(H,AMQ**2,(1.D0-XM)/(1.D0-ALP))
     &      +CJ(Z,AMQ**2,XP/ALP)-CJ(T,AMQ**2,XP/BET)
     &      +CJ(H,AMQ**2,XP/BET)
     &      -(MYMDL_CI(S,ZERO,XM)-MYMDL_CI(U-H,S,(1.D0-XP)/(1.D0-ALP))
     &      -MYMDL_CI(Z-T,ZERO,XM/ALP)+MYMDL_CI(Z-T,ZERO,XM/BET)
     &      -MYMDL_CI(U-H,S,XM/BET)
     &      -CJ(S,AMQ**2,XM)+CJ(H,AMQ**2,(1.D0-XP)/(1.D0-ALP))
     &      +CJ(Z,AMQ**2,XM/ALP)-CJ(T,AMQ**2,XM/BET)
     &      +CJ(H,AMQ**2,XM/BET)))*DQ2**2

      RETURN
      END

      DOUBLE COMPLEX FUNCTION FBoxEven(Q12,Q13,Q23,Q32,MQ)
C------------------------------------------------------------)
C-- THE FORM FACTOR FOR BOX DIAGRAM, F
C-- INPUT:
C--    Q12 = P1.P2
C--    Q13 = P1.P3
C--    Q23 = P2.P3
C--    Q32 = P3.P3
C-- NOTE THAT IN MADGRAPH CONVENTION, P1 P2 P3 P4 ARE ALL INCOMING
C-- THUS T = (P1+P3)^2 = P3^2 + 2*P1.P3, SIMILAR FOR U
C-------------------------------------------------------------)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32,Q42
      DOUBLE PRECISION S,T,U,MQ,MQ2,SS,TT,UU,M1,M2
      DOUBLE PRECISION RHOC,RHOD,TAUQ,TT1,UU1,TT2,UU2,EPM
      DOUBLE COMPLEX C0AB,C0AC,C0AD,C0BC,C0BD,C0CD,D0ABC,D0BAC,D0ACB

      MQ2 = MQ**2

      S = 2*Q12
      T = Q32 + 2*Q13
      U = Q32 + 2*Q23
      Q42 = S + T + U - Q32

      SS = S/MQ2
      TT = T/MQ2
      UU = U/MQ2

      RHOC = Q32/MQ2
      RHOD = Q42/MQ2

      TAUQ = 4D0/SS
      TT1 = TT - RHOC
      UU1 = UU - RHOC
      TT2 = TT - RHOD
      UU2 = UU - RHOD

      CALL INISCAL(MQ,S,T,U,DSQRT(Q32),DSQRT(Q42),
     &     C0AB,C0AC,C0AD,C0BC,C0BD,C0CD,D0ABC,D0BAC,D0ACB)

      C0AB = C0AB/MQ2
      C0AC = C0AC/MQ2
      C0AD = C0AD/MQ2
      C0BC = C0BC/MQ2
      C0BD = C0BD/MQ2
      C0CD = C0CD/MQ2

      D0ABC = D0ABC/MQ2**2
      D0BAC = D0BAC/MQ2**2
      D0ACB = D0ACB/MQ2**2

      FBoxEven = 1D0/SS**2*(4D0*SS+8D0*SS*MQ2*C0AB
     &   -2D0*SS*(SS+RHOC+RHOD-8D0)*MQ2**2*(D0ABC+D0BAC+D0ACB)
     &   +(RHOC+RHOD-8D0)*MQ2*(TT1*C0AC+UU1*C0BC
     &   +TT2*C0BD+UU2*C0AD-(TT*UU-RHOC*RHOD)*MQ2*D0ACB))

      RETURN
      END

      DOUBLE COMPLEX FUNCTION FBoxEvenTop(Q12,Q13,Q23,Q32)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32
      DOUBLE COMPLEX FBoxEven

      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      FBoxEvenTop = FBoxEven(Q12,Q13,Q23,Q32,MDL_MT)

      RETURN
      END

      DOUBLE COMPLEX FUNCTION FBoxEvenBot(Q12,Q13,Q23,Q32)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32
      DOUBLE COMPLEX FBoxEven

      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      FBoxEvenBot = FBoxEven(Q12,Q13,Q23,Q32,MDL_MB)

      RETURN
      END

      DOUBLE COMPLEX FUNCTION GBoxEven(Q12,Q13,Q23,Q32,MQ)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32,Q42
      DOUBLE PRECISION S,T,U,MQ,MQ2,SS,TT,UU,M1,M2
      DOUBLE PRECISION RHOC,RHOD,TAUQ,TT1,UU1,TT2,UU2,PT2
      DOUBLE COMPLEX C0AB,C0AC,C0AD,C0BC,C0BD,C0CD,D0ABC,D0BAC,D0ACB
      DOUBLE COMPLEX GBoxEvenQ

      MQ2 = MQ**2

      S = 2*Q12
      T = Q32 + 2*Q13
      U = Q32 + 2*Q23
      Q42 = S + T + U - Q32

      SS = S/MQ2
      TT = T/MQ2
      UU = U/MQ2

      RHOC = Q32/MQ2
      RHOD = Q42/MQ2

      TAUQ = 4D0/SS
      TT1 = TT - RHOC
      UU1 = UU - RHOC
      TT2 = TT - RHOD
      UU2 = UU - RHOD

      PT2 = 2*Q13*Q23/Q12 - Q32

      CALL INISCAL(MQ,S,T,U,DSQRT(Q32),DSQRT(Q42),
     &     C0AB,C0AC,C0AD,C0BC,C0BD,C0CD,D0ABC,D0BAC,D0ACB)

      C0AB = C0AB/MQ2
      C0AC = C0AC/MQ2
      C0AD = C0AD/MQ2
      C0BC = C0BC/MQ2
      C0BD = C0BD/MQ2
      C0CD = C0CD/MQ2

      D0ABC = D0ABC/MQ2**2
      D0BAC = D0BAC/MQ2**2
      D0ACB = D0ACB/MQ2**2

      GBoxEvenQ = 1D0/(SS*(TT*UU-RHOC*RHOD))*(
     &  (TT**2+RHOC*RHOD-8D0*TT)*MQ2*
     &  (SS*C0AB+TT1*C0AC+TT2*C0BD-SS*TT*MQ2*D0BAC)
     &  +(UU**2+RHOC*RHOD-8D0*UU)*MQ2*
     &  (SS*C0AB+UU1*C0BC+UU2*C0AD-SS*UU*MQ2*D0ABC)
     &  -(TT**2+UU**2-2*RHOC*RHOD)*(TT+UU-8D0)*MQ2*C0CD
     &  -2D0*(TT+UU-8D0)*(TT*UU-RHOC*RHOD)*MQ2**2
     &     *(D0ABC+D0BAC+D0ACB))

C--Compared with hep-ph/9603205, I put the extra PT^2 in A2munu in the form factor
      GBoxEven = GBoxEvenQ/PT2

      RETURN
      END


      DOUBLE COMPLEX FUNCTION GBoxEvenTop(Q12,Q13,Q23,Q32)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32
      DOUBLE COMPLEX GBoxEven

      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      GBoxEvenTop = GBoxEven(Q12,Q13,Q23,Q32,MDL_MT)

      RETURN
      END

      DOUBLE COMPLEX FUNCTION GBoxEvenBot(Q12,Q13,Q23,Q32)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32
      DOUBLE COMPLEX GBoxEven

      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      GBoxEvenBot = GBoxEven(Q12,Q13,Q23,Q32,MDL_MB)

      RETURN
      END


      DOUBLE COMPLEX FUNCTION FBoxOdd(Q12,Q13,Q23,Q32,MQ)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32,Q42
      DOUBLE PRECISION S,T,U,MQ,MQ2,SS,TT,UU,M1,M2
      DOUBLE PRECISION RHOC,RHOD,TAUQ,TT1,UU1,TT2,UU2,EPM
      DOUBLE COMPLEX C0AB,C0AC,C0AD,C0BC,C0BD,C0CD,D0ABC,D0BAC,D0ACB

      MQ2 = MQ**2

      S = 2*Q12
      T = Q32 + 2*Q13
      U = Q32 + 2*Q23
      Q42 = S + T + U - Q32

      SS = S/MQ2
      TT = T/MQ2
      UU = U/MQ2

      RHOC = Q32/MQ2
      RHOD = Q42/MQ2

      TAUQ = 4D0/SS
      TT1 = TT - RHOC
      UU1 = UU - RHOC
      TT2 = TT - RHOD
      UU2 = UU - RHOD

      CALL INISCAL(MQ,S,T,U,DSQRT(Q32),DSQRT(Q42),
     &     C0AB,C0AC,C0AD,C0BC,C0BD,C0CD,D0ABC,D0BAC,D0ACB)

      C0AB = C0AB/MQ2
      C0AC = C0AC/MQ2
      C0AD = C0AD/MQ2
      C0BC = C0BC/MQ2
      C0BD = C0BD/MQ2
      C0CD = C0CD/MQ2

      D0ABC = D0ABC/MQ2**2
      D0BAC = D0BAC/MQ2**2
      D0ACB = D0ACB/MQ2**2

      FBoxOdd = 1D0/SS**2*(4D0*SS+8D0*SS*MQ2*C0AB
     &   -2D0*SS*(TT+UU)*MQ2**2*(D0ABC+D0BAC+D0ACB)
     &   +(RHOC+RHOD)*MQ2*(TT1*C0AC+UU1*C0BC
     &   +TT2*C0BD+UU2*C0AD-(TT*UU-RHOC*RHOD)*MQ2*D0ACB))

      RETURN
      END

      DOUBLE COMPLEX FUNCTION FBoxOddTop(Q12,Q13,Q23,Q32)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32
      DOUBLE COMPLEX FBoxOdd

      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      FBoxOddTop = FBoxOdd(Q12,Q13,Q23,Q32,MDL_MT)

      RETURN
      END

      DOUBLE COMPLEX FUNCTION FBoxOddBot(Q12,Q13,Q23,Q32)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32
      DOUBLE COMPLEX FBoxOdd

      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      FBoxOddBot = FBoxOdd(Q12,Q13,Q23,Q32,MDL_MB)

      RETURN
      END

      DOUBLE COMPLEX FUNCTION GBoxOdd(Q12,Q13,Q23,Q32,MQ)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32,Q42
      DOUBLE PRECISION S,T,U,MQ,MQ2,SS,TT,UU,M1,M2
      DOUBLE PRECISION RHOC,RHOD,TAUQ,TT1,UU1,TT2,UU2,PT2
      DOUBLE COMPLEX C0AB,C0AC,C0AD,C0BC,C0BD,C0CD,D0ABC,D0BAC,D0ACB
      DOUBLE COMPLEX GBoxOddQ

      MQ2 = MQ**2

      S = 2*Q12
      T = Q32 + 2*Q13
      U = Q32 + 2*Q23
      Q42 = S + T + U - Q32

      SS = S/MQ2
      TT = T/MQ2
      UU = U/MQ2

      RHOC = Q32/MQ2
      RHOD = Q42/MQ2

      TAUQ = 4D0/SS
      TT1 = TT - RHOC
      UU1 = UU - RHOC
      TT2 = TT - RHOD
      UU2 = UU - RHOD

      PT2 = 2*Q13*Q23/Q12 - Q32

      CALL INISCAL(MQ,S,T,U,DSQRT(Q32),DSQRT(Q42),
     &     C0AB,C0AC,C0AD,C0BC,C0BD,C0CD,D0ABC,D0BAC,D0ACB)

      C0AB = C0AB/MQ2
      C0AC = C0AC/MQ2
      C0AD = C0AD/MQ2
      C0BC = C0BC/MQ2
      C0BD = C0BD/MQ2
      C0CD = C0CD/MQ2

      D0ABC = D0ABC/MQ2**2
      D0BAC = D0BAC/MQ2**2
      D0ACB = D0ACB/MQ2**2

      GBoxOddQ = 1D0/(SS*(TT*UU-RHOC*RHOD))*(
     &  (TT**2+RHOC*RHOD)*MQ2*
     &  (SS*C0AB+TT1*C0AC+TT2*C0BD-SS*TT*MQ2*D0BAC)
     &  +(UU**2+RHOC*RHOD)*MQ2*
     &  (SS*C0AB+UU1*C0BC+UU2*C0AD-SS*UU*MQ2*D0ABC)
     &  -(TT**2+UU**2-2*RHOC*RHOD)*(TT+UU)*MQ2*C0CD
     &  -2D0*(TT+UU)*(TT*UU-RHOC*RHOD)*MQ2**2
     &     *(D0ABC+D0BAC+D0ACB))

      GBoxOdd = GBoxOddQ/PT2

      RETURN
      END


      DOUBLE COMPLEX FUNCTION GBoxOddTop(Q12,Q13,Q23,Q32)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32
      DOUBLE COMPLEX GBoxOdd

      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      GBoxOddTop = GBoxOdd(Q12,Q13,Q23,Q32,MDL_MT)

      RETURN
      END

      DOUBLE COMPLEX FUNCTION GBoxOddBot(Q12,Q13,Q23,Q32)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32
      DOUBLE COMPLEX GBoxOdd

      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      GBoxOddBot = GBoxOdd(Q12,Q13,Q23,Q32,MDL_MB)

      RETURN
      END


      DOUBLE COMPLEX FUNCTION FBoxSA(Q12,Q13,Q23,Q32,MQ)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32,Q42
      DOUBLE PRECISION S,T,U,MQ,MQ2,SS,TT,UU,M1,M2
      DOUBLE PRECISION RHOC,RHOD,TAUQ,TT1,UU1,TT2,UU2,EPM
      DOUBLE COMPLEX C0AB,C0AC,C0AD,C0BC,C0BD,C0CD,D0ABC,D0BAC,D0ACB

      MQ2 = MQ**2

      S = 2*Q12
      T = Q32 + 2*Q13
      U = Q32 + 2*Q23
      Q42 = S + T + U - Q32

      SS = S/MQ2
      TT = T/MQ2
      UU = U/MQ2

      RHOC = Q32/MQ2
      RHOD = Q42/MQ2

      TAUQ = 4D0/SS
      TT1 = TT - RHOC
      UU1 = UU - RHOC
      TT2 = TT - RHOD
      UU2 = UU - RHOD

      CALL INISCAL(MQ,S,T,U,DSQRT(Q32),DSQRT(Q42),
     &     C0AB,C0AC,C0AD,C0BC,C0BD,C0CD,D0ABC,D0BAC,D0ACB)

      C0AB = C0AB/MQ2
      C0AC = C0AC/MQ2
      C0AD = C0AD/MQ2
      C0BC = C0BC/MQ2
      C0BD = C0BD/MQ2
      C0CD = C0CD/MQ2

      D0ABC = D0ABC/MQ2**2
      D0BAC = D0BAC/MQ2**2
      D0ACB = D0ACB/MQ2**2

      FBoxSA = 1D0/SS**2*(-2D0*SS*(SS+RHOC-RHOD)*MQ2**2
     &   *(D0ABC+D0BAC+D0ACB)
     &   +(RHOC-RHOD)*MQ2*(TT1*C0AC+UU1*C0BC
     &   +TT2*C0BD+UU2*C0AD-(TT*UU-RHOC*RHOD)*MQ2*D0ACB))

      RETURN
      END

      DOUBLE COMPLEX FUNCTION FBoxSATop(Q12,Q13,Q23,Q32)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32
      DOUBLE COMPLEX FBoxSA

      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      FBoxSATop = FBoxSA(Q12,Q13,Q23,Q32,MDL_MT)

      RETURN
      END

      DOUBLE COMPLEX FUNCTION FBoxSABot(Q12,Q13,Q23,Q32)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32
      DOUBLE COMPLEX FBoxSA

      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      FBoxSABot = FBoxSA(Q12,Q13,Q23,Q32,MDL_MB)

      RETURN
      END


      DOUBLE COMPLEX FUNCTION GBoxSA(Q12,Q13,Q23,Q32,MQ)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32,Q42
      DOUBLE PRECISION S,T,U,MQ,MQ2,SS,TT,UU,M1,M2
      DOUBLE PRECISION RHOC,RHOD,TAUQ,TT1,UU1,TT2,UU2,PT2
      DOUBLE COMPLEX C0AB,C0AC,C0AD,C0BC,C0BD,C0CD,D0ABC,D0BAC,D0ACB
      DOUBLE COMPLEX GBoxSAQ

      MQ2 = MQ**2

      S = 2*Q12
      T = Q32 + 2*Q13
      U = Q32 + 2*Q23
      Q42 = S + T + U - Q32

      SS = S/MQ2
      TT = T/MQ2
      UU = U/MQ2

      RHOC = Q32/MQ2
      RHOD = Q42/MQ2

      TAUQ = 4D0/SS
      TT1 = TT - RHOC
      UU1 = UU - RHOC
      TT2 = TT - RHOD
      UU2 = UU - RHOD

      PT2 = 2*Q13*Q23/Q12 - Q32

      CALL INISCAL(MQ,S,T,U,DSQRT(Q32),DSQRT(Q42),
     &     C0AB,C0AC,C0AD,C0BC,C0BD,C0CD,D0ABC,D0BAC,D0ACB)

      C0AB = C0AB/MQ2
      C0AC = C0AC/MQ2
      C0AD = C0AD/MQ2
      C0BC = C0BC/MQ2
      C0BD = C0BD/MQ2
      C0CD = C0CD/MQ2

      D0ABC = D0ABC/MQ2**2
      D0BAC = D0BAC/MQ2**2
      D0ACB = D0ACB/MQ2**2

      GBoxSAQ = 1D0/(SS*(TT*UU-RHOC*RHOD))*(
     &  -(TT**2-RHOC*RHOD)*MQ2*
     &  (SS*C0AB+TT1*C0AC+TT2*C0BD-SS*TT*MQ2*D0BAC)
     &  +(UU**2-RHOC*RHOD)*MQ2*
     &  (SS*C0AB+UU1*C0BC+UU2*C0AD-SS*UU*MQ2*D0ABC)
     &  +((TT+UU)**2-4*RHOC*RHOD)*(TT-UU)*MQ2*C0CD
     &  +2D0*(TT-UU)*(TT*UU-RHOC*RHOD)*MQ2**2
     &     *(D0ABC+D0BAC+D0ACB))

      GBoxSA = GBoxSAQ/PT2

      RETURN
      END


      DOUBLE COMPLEX FUNCTION GBoxSATop(Q12,Q13,Q23,Q32)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32
      DOUBLE COMPLEX GBoxSA

      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      GBoxSATop = GBoxSA(Q12,Q13,Q23,Q32,MDL_MT)

      RETURN
      END

      DOUBLE COMPLEX FUNCTION GBoxSABot(Q12,Q13,Q23,Q32)
      IMPLICIT NONE

      DOUBLE PRECISION Q12,Q13,Q23,Q32
      DOUBLE COMPLEX GBoxSA

      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      GBoxSABot = GBoxSA(Q12,Q13,Q23,Q32,MDL_MB)

      RETURN
      END
