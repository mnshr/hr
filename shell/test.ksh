#!/bin/bash

echo "dol dol: $$"
echo "dol exc: $!"
echo "Total arg: " $#
echo "1st & 2nd arg: " $1 $2
echo "file: " $0
echo "At: " $@
echo "star: " $*
#replaces ABC with CDE in a line containing MNO, after line 5 to end of file
#sed -n '5,$p' test.ksh | sed '/MNO/s/ABC/CDE/'
echo "ABC | MNO"
echo "ABC"
#prints the 10th line, with sed and with head/tail
sed -n '10p' test.ksh
head -n 10 test.ksh | tail -n 1
#comm finds common lines 2 sorted files
#Array
A=(10 20 30)
echo $A
#set -x to enable debug output

function abc {
	 echo "hello world"
}
echo "calling echo... "
abc
