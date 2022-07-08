#!/bin/bash

types=("Type-I" "Type-II" "Type-LS" "Type-FL")
# Generate UFOs for LO and NLO
for type in 1 2 3 4
  do
    id=$[$type-1]
    mkdir -p UFOs/${types[$id]}
    for order in 1 2
      do
        ./Tools/Generate_UFO.m $type $order
    done
done

./Tools/Patch_All.sh
