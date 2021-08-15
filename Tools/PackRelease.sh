#!/bin/bash

version=0.5.1
RELEASEDIR='RELEASE'
UFOFolders=("Type-I" "Type-II" "Type-LS" "Type-FL")
FAFolders=("Type-I" "Type-II")

CURDIR=$(pwd)

for typ in ${UFOFolders[@]}
  do
    cd UFOs/$typ
    for folder in */
      do
        folder=${folder%/}
        tar -czvf $CURDIR/$RELEASEDIR/$folder-v$version.tar.gz $folder
      done
    cd $CURDIR
  done

for typ in ${FAFolders[@]}
  do
    cd FAs/$typ
    for folder in */
      do
        folder=${folder%/}
        tar -czvf $CURDIR/$RELEASEDIR/$folder-v$version.tar.gz $folder
      done
    cd $CURDIR
  done
