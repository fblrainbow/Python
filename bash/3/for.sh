#!/bin/bash
#for a in 7 8 9 10
#do 
#	echo -n "$a"
#done
#
#echo 
#echo
# 
#echo -n "Enter \"a\" "
#read a 
#echo "The value of \"a\" is now $a."
#
#echo
#exit 0
#a=`ls -l`
#echo $a
#echo 
#echo "$a"
#exit 0
#R=$(cat /etc/redhat-release)
#arch=$(uname -m)
#exit 0
a=234
let "a += 1"
echo "a = $a "
echo

b=${a/23/BB}
echo "b = $b"
declare -i b
let "b = $b"

let "b += 1"
echo "b = $b"
echo 
exit 
