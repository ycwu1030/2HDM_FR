#!/bin/bash

MG5DIR="/home/ycwu/Workings/MC-Tools/MG5_aMC_v2_6_3_2"
RUNNINGDIR="/home/ycwu/Workings/MC-Tools/MG5_aMC_v2_6_3_2/TEDWORK/THDM_UFO_TEST"
OVERALLLOG=$RUNNINGDIR/cache

FINALSTATES=("hl hl" "hl hh" "hh hh" "hl ha" "hh ha" "ha ha")
PROCESSNAME=("hlhl" "hlhh" "hhhh" "hlha" "hhha" "haha")

BenchType=("Type-II" "Type-II" "Type-II" "Type-I" "Type-I" "Type-II" "Type-II")
TB=(1.75 1.50 2.22 1.2 20.0 10.00 10.00)
alp=(-0.1872 -0.2162 -0.1397 -0.1760 0.0 -0.0382 0.0323)
MHH=(300 700 200 200 200 500 500)
MHA=(441 701 350 500 500 500 500)
MHp=(442 670 350 500 500 500 500)
m122=(38300 180000 12000 -60000 2000 24746 24746)

# Generate process
generate_proc()
{
    Name=$1
    Model=$2
    Process=$3

    echo "import model $Model" > $Name.cmd
    echo "generate $Process" >> $Name.cmd
    echo "output $RUNNINGDIR/$Name" >> $Name.cmd
    echo "exit" >> $Name.cmd
    cat $Name.cmd >> $OVERALLLOG-$Name.log

    $MG5DIR/bin/mg5_aMC $Name.cmd >> $OVERALLLOG-$Name.log
    echo "Process generated"
}



for typ in Type-I Type-II
  do
    for each process
      do
        generate LO process
        generate NLO process
        for parameters
          do
            run LO and get cs
            run NLO and get cs
            record the cs
          done
      done
  done