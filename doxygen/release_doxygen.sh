#!/bin/sh

QUEUE_CMD="../queue/queue_daemon.sh doxy_queue"

###############################
# Short-Term Crustal Dynamics #
###############################
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/pylith/pylith-1.8.0.tgz 1.8.0 PyLith" &
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/relax/Relax-1_0_4.tgz 1.0.4 RELAX" &
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/selen/SELEN_2.9.10.4.tar.gz 2.9.10.4 SELEN" &
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/lithomop/lithomop3d-0.7.2.tar.gz 0.7.2 LithoMop" &

#######################
# Long-Term Tectonics #
#######################
#$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/gale/Gale-2_0_1.tgz 2.0.1 Gale" &
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/plasti/plasti-1.0.0.tar.gz 1.0.0 Plasti" &
#$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/snac/SNAC-1.2.0.tar.gz 1.2.0 SNAC" &

#####################
# Mantle Convection #
#####################
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/citcomcu/CitcomCU-1.0.3.tar.gz 1.0.3 CitcomCU" &
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/citcoms/CitcomS-3.2.0.tar.gz 3.2.0 CitcomS" &
# ConMan distribution isn't packaged correctly
#./generate_doxygen.sh url http://geodynamics.org/cig/software/conman/ConMan-2.0.0.tar.gz 2.0.0 ConMan
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/hc/HC-1_0.tgz 1.0 HC" &

##############
# Seismology #
##############
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/specfem3d/SPECFEM3D_Cartesian_V2.0.2.tar.gz 2.0.2 SPECFEM3D_Cartesian" &
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/specfem3d-globe/SPECFEM3D_GLOBE_V5.1.5.tar.gz 5.1.5 SPECFEM3D_GLOBE" &
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/specfem3d-geotech/SPECFEM3D_GEOTECH_V1.1b.tar.gz 1.1b SPECFEM3D_GEOTECH" &
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/specfem2d/SPECFEM2D-7.0.0.tar.gz 7.0.0 SPECFEM2D" &
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/specfem1d/SPECFEM1D-1.0.3.tar.gz 1.0.3 SPECFEM1D" &
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/mineos/mineos-1.0.2.tgz 1.0.2 Mineos" &
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/flexwin/FLEXWIN-1.0.1.tar.gz 1.0.1 Flexwin" &
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/seismic_cpml/SEISMIC_CPML_1.2.tar.gz 1.2 SEISMIC_CPML" &

#############
# Geodynamo #
#############
$QUEUE_CMD "cd `pwd` ; ./generate_doxygen.sh url http://geodynamics.org/cig/software/mag/MAG-1.0.2.tar.gz 1.0.2 MAG" &

