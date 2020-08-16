
      DOUBLE COMPLEX FUNCTION FTriZTop(shat)
      IMPLICIT NONE
      DOUBLE COMPLEX shat
      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc' ! include model parameter

      DOUBLE PRECISION MQ,MQ2,S,REPS
      DOUBLE COMPLEX CQ2,CA5,C0AB

      REPS=1D-15

      MQ = MDL_MT
      MQ2 = MQ**2
      S = shat/MQ2
      
      CQ2 = MQ2*DCMPLX(1.D0,-REPS)
      CA5 = CDSQRT(1.D0-4.D0*CQ2/shat)
      C0AB = 0.5D0*CDLOG((CA5+1.D0)/(CA5-1.D0))**2/shat*MQ2
      C0AB = C0AB/MQ2

      FTriZTop = (1D0+2D0*MQ2*C0AB)/(shat/2D0)
      
      RETURN
      END


      DOUBLE COMPLEX FUNCTION FTriZBot(shat)
      IMPLICIT NONE
      DOUBLE COMPLEX shat
      INCLUDE 'coupl.inc'
      INCLUDE 'input.inc' ! include model parameter

      DOUBLE PRECISION MQ,MQ2,S,REPS
      DOUBLE COMPLEX CQ2,CA5,C0AB

      REPS=1D-15

      MQ = MDL_MB
      MQ2 = MQ**2
      S = shat/MQ2
      
      CQ2 = MQ2*DCMPLX(1.D0,-REPS)
      CA5 = CDSQRT(1.D0-4.D0*CQ2/shat)
      C0AB = 0.5D0*CDLOG((CA5+1.D0)/(CA5-1.D0))**2/shat*MQ2
      C0AB = C0AB/MQ2

      FTriZBot = (1D0+2D0*MQ2*C0AB)/(shat/2D0)
      
      RETURN
      END
