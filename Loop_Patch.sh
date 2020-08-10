#!/bin/bash

SourceDir=$1
TargetDir=$2

cp -r $SourceDir $TargetDir
cp -r $LoopFileDir/Fortran $TargetDir/Fortran

LoopFileDir="Loop_Induced_Vertices"

VertexTypes=("ggS")

for vtype in ${VertexTypes[@]}
  do
    cat $LoopFileDir/couplings_$vtype.py >> $TargetDir/couplings.py
    cat $LoopFileDir/lorentz_$vtype.py >> $TargetDir/lorentz.py
    cat $LoopFileDir/vertices_$vtype.py >> $TargetDir/vertices.py
    cat $LoopFileDir/parameters.py >> $TargetDir/parameters.py
  done