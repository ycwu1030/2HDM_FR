#!/bin/bash

cd ..
# Define the process
parts=("hl" "hh" "ha" "z")

for pid in 0 1 2 3
  do
process=THDM_test
model1="2HDM_CPC_Type-I_EFF_cba_UFO"
procname1=gg_${parts[$pid]}_tt_I_eff
proc1="g g > ${parts[$pid]} > t t~"
opmode1="standalone"
model2="2HDM_CPC_Type-I_NLO_cba_UFO"
procname2=gg_${parts[$pid]}_tt_I_nlo
proc2="g g > ${parts[$pid]} > t t~ aS=2 [virt=QCD]"
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
done
echo "Process generated"
rm $process.log

me2=()
for i in 0 1
  do
    dir=$(ls -d ${procnames[$i]}/SubProcesses/P*)
    cd $dir
    make check > makelogs
    ./check > $process.dat
    tmp=$(sed -n "/Matrix element/p" $process.dat | sed "s/[^0-9]*\([0-9].[0-9]*E[+-][0-9]\{3\}\)[^0-9]*[0-9]/\1/g")
    me2[$i]=$tmp
    cd -
done

echo "${parts[$pid]} ${me2[@]}"
for i in 0 1
  do
    rm -rf ${procnames[$i]}
done
done