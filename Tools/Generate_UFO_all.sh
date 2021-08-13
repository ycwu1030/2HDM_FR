#!/bin/bash

# Generate UFOs for LO and NLO
for type in 1 2 3 4
  do
    for order in 1 2
      do
        ./Tools/Generate_UFO.m $type $order
    done
done
