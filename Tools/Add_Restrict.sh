#!/bin/bash

YukawaTypes=("Type-I" "Type-II" "Type-LS" "Type-FL")

for ytype in ${YukawaTypes[@]}
  do
    cp restrict_alignment.dat UFOs/${ytype}/2HDM_CPC_${ytype}_cba_UFO/restrict_alignment.dat
    cp restrict_default.dat UFOs/${ytype}/2HDM_CPC_${ytype}_cba_UFO/restrict_default.dat
    cp restrict_alignment.dat UFOs/${ytype}/2HDM_CPC_${ytype}_EFF_cba_UFO/restrict_alignment.dat
    cp restrict_default.dat UFOs/${ytype}/2HDM_CPC_${ytype}_EFF_cba_UFO/restrict_default.dat
    cp restrict_alignment_nlo.dat UFOs/${ytype}/2HDM_CPC_${ytype}_NLO_cba_UFO/restrict_alignment.dat
    cp restrict_default_nlo.dat UFOs/${ytype}/2HDM_CPC_${ytype}_NLO_cba_UFO/restrict_default.dat
done
