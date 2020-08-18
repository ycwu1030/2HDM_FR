
      DOUBLE COMPLEX FUNCTION FTriPhotonF(shat, MQ)
      IMPLICIT NONE
      DOUBLE COMPLEX shat
      DOUBLE PRECISION MQ,MQ2,S,tauQ,REPS
      DOUBLE COMPLEX CQ2,CA5,C0AB,ftau

      REPS=1D-15

      MQ2 = MQ**2
      S = shat/MQ2
      tauQ = 4D0/S

      CQ2 = MQ2*DCMPLX(1.D0,-REPS)
      CA5 = CDSQRT(1.D0-4.D0*CQ2/shat)
      C0AB = 0.5D0*CDLOG((CA5+1.D0)/(CA5-1.D0))**2/shat*MQ2
      C0AB = C0AB/MQ2

      ftau = -shat/2D0*C0AB
      
      FTriPhotonF = -2D0*tauQ*(1D0+(1D0-tauQ)*ftau)

      RETURN
      END

      DOUBLE COMPLEX FUNCTION FTriPhotonTop(shat)
      IMPLICIT NONE
      DOUBLE COMPLEX shat
      DOUBLE COMPLEX FTriPhotonF
      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      FTriPhotonTop = FTriPhotonF(shat,MDL_MT)

      RETURN
      END

      DOUBLE COMPLEX FUNCTION FTriPhotonBot(shat)
      IMPLICIT NONE
      DOUBLE COMPLEX shat
      DOUBLE COMPLEX FTriPhotonF
      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      FTriPhotonBot = FTriPhotonF(shat,MDL_MB)

      RETURN
      END

      DOUBLE COMPLEX FUNCTION FTriPhotonW(shat)
      IMPLICIT NONE
      DOUBLE COMPLEX shat
      DOUBLE PRECISION MW,MW2,S,tauW,REPS
      DOUBLE COMPLEX CQ2,CA5,C0AB,ftau
      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      REPS=1D-15

      MW = MDL_MW
      MW2 = MW**2
      S = shat/MW2
      tauW = 4D0/S

      CQ2 = MW2*DCMPLX(1.D0,-REPS)
      CA5 = CDSQRT(1.D0-4.D0*CQ2/shat)
      C0AB = 0.5D0*CDLOG((CA5+1.D0)/(CA5-1.D0))**2/shat*MW2
      C0AB = C0AB/MW2

      ftau = -shat/2D0*C0AB
      
      FTriPhotonW = 2D0 + 3D0*tauW + 3D0*tauW*(2D0-tauW)*ftau

      RETURN
      END

      DOUBLE COMPLEX FUNCTION FTriPhotonS(shat)
      IMPLICIT NONE
      DOUBLE COMPLEX shat
      DOUBLE PRECISION MS,MS2,S,tauS,REPS
      DOUBLE COMPLEX CQ2,CA5,C0AB,ftau
      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      REPS=1D-15

      MS = MDL_MHp
      MS2 = MS**2
      S = shat/MS2
      tauS = 4D0/S

      CQ2 = MS2*DCMPLX(1.D0,-REPS)
      CA5 = CDSQRT(1.D0-4.D0*CQ2/shat)
      C0AB = 0.5D0*CDLOG((CA5+1.D0)/(CA5-1.D0))**2/shat*MS2
      C0AB = C0AB/MS2

      ftau = -shat/2D0*C0AB
      
      FTriPhotonS = tauS*(1D0-tauS*ftau)

      RETURN
      END

      DOUBLE COMPLEX FUNCTION FTriPhotonOddF(shat, MQ)
      IMPLICIT NONE
      DOUBLE COMPLEX shat
      DOUBLE PRECISION MQ,MQ2,S,tauQ,REPS
      DOUBLE COMPLEX CQ2,CA5,C0AB,ftau

      REPS=1D-15

      MQ2 = MQ**2
      S = shat/MQ2
      tauQ = 4D0/S

      CQ2 = MQ2*DCMPLX(1.D0,-REPS)
      CA5 = CDSQRT(1.D0-4.D0*CQ2/shat)
      C0AB = 0.5D0*CDLOG((CA5+1.D0)/(CA5-1.D0))**2/shat*MQ2
      C0AB = C0AB/MQ2

      ftau = -shat/2D0*C0AB
      
      FTriPhotonOddF = -2D0*tauQ*ftau

      RETURN
      END

      DOUBLE COMPLEX FUNCTION FTriPhotonOddTop(shat)
      IMPLICIT NONE
      DOUBLE COMPLEX shat
      DOUBLE COMPLEX FTriPhotonOddF
      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      FTriPhotonOddTop = FTriPhotonOddF(shat,MDL_MT)

      RETURN
      END

      DOUBLE COMPLEX FUNCTION FTriPhotonOddBot(shat)
      IMPLICIT NONE
      DOUBLE COMPLEX shat
      DOUBLE COMPLEX FTriPhotonOddF
      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc'

      FTriPhotonOddBot = FTriPhotonOddF(shat,MDL_MB)

      RETURN
      END
