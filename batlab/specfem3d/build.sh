#!/bin/bash

# Point to any additional installed libraries
source ./build_common.sh

# Build SPECFEM3D
cd SPECFEM3D* || cd specfem3d*
./configure && make all

exit $?

