#!/bin/bash
cat file.csv | (
  I=0;
  echo -n"">file0;
  while read line; 
  do
    echo $line >> file$I;
    if [ "$line" == '-|' ];
    then I=$[I+1];
      echo -n "" > file$I;
    fi;
  done;
)
