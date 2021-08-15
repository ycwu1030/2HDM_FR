#!/bin/bash

cd ..
# Define the process
parts=("hl" "hh" "ha" "z")
fparts=("hl hl" "hl hl" "hl ha" "hh ha")
nparts=("hh ha z" "hl ha z" "hl hh z" "hl hh ha")
for pid in 0 1 2 3
  do
process=THDM_test
model1="2HDM_CPC_Type-I_EFF_cba_UFO"
procname1=gg_${parts[$pid]}_I_eff
proc1="g g > ${fparts[$pid]} / ${nparts[$pid]}"
opmode1="standalone"
model2="2HDM_CPC_Type-I_NLO_cba_UFO"
procname2=gg_${parts[$pid]}_I_nlo
proc2="g g > ${fparts[$pid]} aS=2 / ${nparts[$pid]} [virt=QCD]"
opmode2=""
modelnames=("$model1" "$model2")
procnames=("$procname1" "$procname2")
opmodes=("$opmode1" "$opmode2")
procs=("$proc1" "$proc2")



# Generate the process
for i in 0 1
  do
    rm -rf $process.cmd
    echo "import ${modelnames[$i]}"                          >>$process.cmd
    echo "generate ${procs[$i]}"                             >>$process.cmd
    echo "output ${opmodes[$1]} ${procnames[$i]}"            >>$process.cmd
    echo "exit"                                              >>$process.cmd
    cat $process.cmd >> $process.log
    ./mg5_aMC $process.cmd >> $process.log
    rm -rf $process.cmd
    if [ $i -eq 0 ]
      then
        cp param_card_eff.dat ${procnames[$i]}/Cards/param_card.dat
    fi
    if [ $i -eq 1 ]
      then
        cp param_card_nlo.dat ${procnames[$i]}/Cards/param_card.dat
    fi
done
echo "Process generated"
rm $process.log

me2=()
for i in 0 1
  do
    dir=$(ls -d ${procnames[$i]}/SubProcesses/P*)
    cd $dir
    if [ $i -eq 1 ]
      then
        echo "$p1" > PS.input
        echo "$p2" >> PS.input
        echo "$p3" >> PS.input
        echo "$p4" >> PS.input
        sed -i "" "s/READPS = .FALSE./READPS = .TRUE./g" check_sa.f
    fi
    make check > makelogs
    ./check > $process.dat
    tmp=$(sed -n "/Matrix element/p" $process.dat | sed "s/[^0-9]*\([0-9].[0-9]*E[+-][0-9]\{3\}\)[^0-9]*[0-9]/\1/g")
    me2[$i]=$tmp
    p1=$(awk '$1==1 {print $2" "$3" "$4" "$5}' $process.dat)
    p2=$(awk '$1==2 {print $2" "$3" "$4" "$5}' $process.dat)
    p3=$(awk '$1==3 {print $2" "$3" "$4" "$5}' $process.dat)
    p4=$(awk '$1==4 {print $2" "$3" "$4" "$5}' $process.dat)
    cd -
done

echo "${parts[$pid]} ${me2[@]}"
for i in 0 1
  do
    rm -rf ${procnames[$i]}
done
done