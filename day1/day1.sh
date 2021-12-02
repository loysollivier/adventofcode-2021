#!/bin/bash

i=0
n_1=-1
n=-1
increase=0
for line in $(cat day1_input.txt)
do
	if [ $n_1 -eq -1 ];
	then
		n_1=$line
    continue
	fi
  n=$line
  if [ $n -gt $n_1 ];
  then
      let "increase++"
      echo $n_1 $n
  fi
  n_1=$n
done
echo "There was $increase measurements larger than the previous one."

