#!/bin/bash

# Point to any additional installed libraries
source ./build_common.sh

# Move to the CitcomS directory
cd citcoms

# Move the Regional example
if [ "$1" == "null" ]
then
    echo "Null test"
elif [ "$1" == "regional1proc" ]
then
    cd examples/Regional/ &&
    cat input.sample | sed '/datadir/c\
datadir="scratch"\
' > regional.params &&
    mpirun -np 1 ../../bin/CitcomSRegional regional.params
elif [ "$1" == "regional4proc" ]
then
    cd examples/Regional/ &&
    cat input.sample | sed '/datadir/c\
datadir="scratch"\
' > regional.params &&
    mpirun -np 4 ../../bin/CitcomSRegional regional.params &&
    cd ../../.. &&
    tar -xzf benchmark_Regional_4proc.tar.gz &&
    python citcoms_compare.py Regional citcoms/examples/Regional 4 80
else
    echo "Unknown test: $1"
    exit 1
fi

exit $?

