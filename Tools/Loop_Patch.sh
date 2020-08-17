#!/bin/bash

SourceDir=$1
TargetDir=$2

LoopFileDir="Loop_Induced_Vertices"

VertexTypes=("ggS" "ggZ" "ggSS")

cp -r $SourceDir $TargetDir
mkdir -p $TargetDir/Fortran
touch $TargetDir/Fortran/functions.f 
cat $LoopFileDir/parameters.py >> $TargetDir/parameters.py

for vtype in ${VertexTypes[@]}
  do
    cat $LoopFileDir/couplings_$vtype.py >> $TargetDir/couplings.py
    cat $LoopFileDir/lorentz_$vtype.py >> $TargetDir/lorentz.py
    cat $LoopFileDir/vertices_$vtype.py >> $TargetDir/vertices.py
    # cat $LoopFileDir/parameters_$vtype.py >> $TargetDir/parameters.py
    cat $LoopFileDir/Fortran/functions_$vtype.f >> $TargetDir/Fortran/functions.f
  done