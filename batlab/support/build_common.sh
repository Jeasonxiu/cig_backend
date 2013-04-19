# $Id: build_common.sh 21340 2013-02-07 07:36:36Z ericheien $

# Set up common paths, flags needed for all builds
export PATH=$PATH:$HOME/local/bin/ &&
export LDFLAGS=-L$HOME/local/lib/ &&
export CFLAGS=-I$HOME/local/include/ &&
export CXXFLAGS=-I$HOME/local/include/ &&
export LD_LIBRARY_PATH=$HOME/local/lib/ &&
export PYTHONPATH=$HOME/local/lib/python2.6/site-packages/ &&
export NETCDF_INC=$HOME/local/include/ &&
export NETCDF_LIB=$HOME/local/lib/
