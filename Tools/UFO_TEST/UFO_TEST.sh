#!/bin/bash

MG5DIR="/home/ycwu/Workings/MC-Tools/MG5_aMC_v2_6_3_2"
RUNNINGDIR="/home/ycwu/Workings/MC-Tools/MG5_aMC_v2_6_3_2/TEDWORK/THDM_UFO_TEST"
PARADIR="/home/ycwu/Workings/MC-Tools/MG5_aMC_v2_6_3_2/TEDWORK/THDM_UFO_TEST/Cards"
OVERALLLOG=$RUNNINGDIR/cache

FINALSTATES=("hl hl" "hl hh" "hh hh" "hl ha" "hh ha" "ha ha")
PROCESSNAME=("hlhl" "hlhh" "hhhh" "hlha" "hhha" "haha")

WIDTHSCALAR=("hl" "hh" "ha" "h+")

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

calc_width_param()
{
    runtype=$1
    mg5dir=$RUNNINGDIR/Decays_${runtype}
    tmpdir=${PARADIR}_${runtype}
    curdir=$(pwd)
    paraid=0
    NParameters=${#TB[@]}
    while [ $paraid -lt $NParameters ]
      do
        cd $curdir
        echo "import model 2HDM_CPC_${runtype}_NLO_UFO" > Decays_${runtype}.cmd
        echo "generate hl > all all" >> Decays_${runtype}.cmd
        echo "add process hh > all all" >> Decays_${runtype}.cmd
        echo "add process ha > all all" >> Decays_${runtype}.cmd
        echo "add process h+ > all all" >> Decays_${runtype}.cmd
        echo "output $RUNNINGDIR/Decays_${runtype} -f" >> Decays_${runtype}.cmd
        echo "exit" >> Decays_${runtype}.cmd
        cat Decays_${runtype}.cmd >> $OVERALLLOG-Decays_${runtype}.log
        $MG5DIR/bin/mg5_aMC Decays_${runtype}.cmd >> $OVERALLLOG-Decays_${runtype}.log
        cd $mg5dir
        mhh=${MHH[$paraid]}
        mha=${MHA[$paraid]}
        mhp=${MHp[$paraid]}
        M122=${m122[$paraid]}
        tb=${TB[$paraid]}
        beta=$(echo "a($tb)" | bc -l)
        alprn=${alp[$paraid]}
        alpha=$(echo "$alprn*a(1)*4" | bc -l)
        # cp $RUNNINGDIR/Decays_${runtype}/Cards/param_card.dat $tmpdir/param_card_$paraid.dat
        rundir=run_2HDM_DECAY_"$paraid"
        echo "calculate_decay_widths $rundir" > RUNNINGCOMMAND
        echo "0" >> RUNNINGCOMMAND
        echo "set MHH $mhh" >> RUNNINGCOMMAND
        echo "set MHA $mha" >> RUNNINGCOMMAND
        echo "set MHp $mhp" >> RUNNINGCOMMAND
        echo "set m122 $M122" >> RUNNINGCOMMAND
        echo "set beta $beta" >> RUNNINGCOMMAND
        echo "set alpha $alpha" >> RUNNINGCOMMAND
        echo "0" >> RUNNINGCOMMAND
        ./bin/madevent RUNNINGCOMMAND >> $OVERALLLOG-Decays_${runtype}.log
        cd $curdir
        cp $mg5dir/Events/$rundir/param_card.dat $tmpdir/param_card_$paraid.dat
        paraid=$[$paraid+1]
      done
}

calc_cs_for_param()
{
    Name=$1
    runtype=$2
    outputfile=$3
    mg5dir=$RUNNINGDIR/$Name
    tmpdir=${PARADIR}_${runtype}

    paraid=0
    NParameters=${#TB[@]}

    curdir=$(pwd)
    while [ $paraid -lt $NParameters ]
      do
        cd $curdir
        cd $mg5dir
        mhh=${MHH[$paraid]}
        mha=${MHA[$paraid]}
        mhp=${MHp[$paraid]}
        M122=${m122[$paraid]}
        tb=${TB[$paraid]}
        beta=$(echo "a($tb)" | bc -l)
        alprn=${alp[$paraid]}
        alpha=$(echo "$alprn*a(1)*4" | bc -l)
        cp $tmpdir/param_card_$paraid.dat Cards/param_card.dat
        rundir=run_2HDM_ggF_"$paraid"
        echo "generate_events $rundir" > RUNNINGCOMMAND
        echo "0" >> RUNNINGCOMMAND
        echo "set ebeam1 7000" >> RUNNINGCOMMAND
        echo "set ebeam2 7000" >> RUNNINGCOMMAND
        echo "set nevents 10000" >> RUNNINGCOMMAND
        echo "set no_parton_cut" >> RUNNINGCOMMAND
        echo "set MHH $mhh" >> RUNNINGCOMMAND
        echo "set MHA $mha" >> RUNNINGCOMMAND
        echo "set MHp $mhp" >> RUNNINGCOMMAND
        echo "set m122 $M122" >> RUNNINGCOMMAND
        echo "set beta $beta" >> RUNNINGCOMMAND
        echo "set alpha $alpha" >> RUNNINGCOMMAND
        echo "0" >> RUNNINGCOMMAND
        ./bin/madevent RUNNINGCOMMAND >> $OVERALLLOG-$Name.log
        CSFile=Events/$rundir/parton_systematics.log
        CS=$(awk '$2=="original" {print $4*1000}' $CSFile)
        ScaleLine=$(awk '$2=="scale" {print $0}' $CSFile)
        ScaleUP=$(echo "$ScaleLine" | grep -Eo '\+\s*[0-9]*\.*[0-9]*%' | grep -Eo '[0-9]*\.*[0-9]*%')
        ScaleDO=$(echo "$ScaleLine" | grep -Eo '\-\s*[0-9]*\.*[0-9]*%' | grep -Eo '[0-9]*\.*[0-9]*%')
        PDFLine=$(awk '$2=="PDF" {print $0}' $CSFile)
        PDFUP=$(echo "$PDFLine" | grep -Eo '\+\s*[0-9]*\.*[0-9]*%' | grep -Eo '[0-9]*\.*[0-9]*%')
        PDFDO=$(echo "$PDFLine" | grep -Eo '\-\s*[0-9]*\.*[0-9]*%' | grep -Eo '[0-9]*\.*[0-9]*%')
        # echo "$id  $m5  $CS  +$ScaleUP  -$ScaleDO  +$PDFUP  -$PDFDO" > $mg5dir/Events/CStmp.dat
        rm -r $mg5dir/Events/$rundir
        rm -r $mg5dir/HTML/$rundir
        rm -r $mg5dir/crossx.html
        rm -r $mg5dir/HTML/results.pkl
        cd $curdir
        echo "$paraid $CS  +$ScaleUP  -$ScaleDO  +$PDFUP  -$PDFDO" >> $outputfile
        paraid=$[$paraid+1]
      done
}

for typ in Type-I Type-II
  do
    # First generate the folder for calculating the decay width
    # For form factor coding in fortran, auto option is not working
    mkdir ${PARADIR}_${typ}
    calc_width_param $typ
    procid=0
    NProcesses=${#FINALSTATES[@]}
    while [ $procid -lt $NProcesses ]
      do
        # Generate LO proess
        model=2HDM_CPC_${typ}_EFF_UFO
        proname=2HDM_${typ}_ggF_EFF_${PROCESSNAME[$procid]}
        process="g g > ${FINALSTATES[$procid]}"
        generate_proc "$proname" "$model" "$process"
        calc_cs_for_param "$proname" "$typ" "CS_EFF_$proname.dat"
        
        # Generate NLO process
        model=2HDM_CPC_${typ}_NLO_UFO
        proname=2HDM_${typ}_ggF_NLO_${PROCESSNAME[$procid]}
        process="g g > ${FINALSTATES[$procid]} [QCD]"
        generate_proc "$proname" "$model" "$process"
        calc_cs_for_param "$proname" "$typ" "CS_NLO_$proname.dat"

        procid=$[$procid+1]
      done
  done
