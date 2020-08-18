#!/bin/bash

LoopFileDir="Loop_Induced_Vertices"

VertexTypes=("ggS" "ggZ" "ggSS" "gagaS")
YukawaTypes=("Type-I" "Type-II" "Type-LS" "Type-FL")

for ytype in ${YukawaTypes[@]}
  do
    SourceDir=UFOs/${ytype}/2HDM_CPC_${ytype}_UFO
    TargetDir=UFOs/${ytype}/2HDM_CPC_${ytype}_EFF_UFO
    cp -r $SourceDir $TargetDir
    mkdir -p $TargetDir/Fortran
    touch $TargetDir/Fortran/functions.f 
    cat $LoopFileDir/parameters_${ytype}.py >> $TargetDir/parameters.py
    for vtype in ${VertexTypes[@]}
        do
            cat $LoopFileDir/couplings_$vtype.py >> $TargetDir/couplings.py
            cat $LoopFileDir/lorentz_$vtype.py >> $TargetDir/lorentz.py
            cat $LoopFileDir/vertices_$vtype.py >> $TargetDir/vertices.py
            cat $LoopFileDir/Fortran/functions_$vtype.f >> $TargetDir/Fortran/functions.f
        done
  done