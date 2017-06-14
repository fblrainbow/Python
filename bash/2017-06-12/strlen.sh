#!/bin/bash
string="abcdefghijklmn"
echo ${#string}
echo ${string:1:10}
echo `expr index "$string" j`

