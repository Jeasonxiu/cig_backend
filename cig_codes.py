#!/usr/bin/env python

# A class to keep the current set of CIG codes and related information for use in backend operations
class CodeDB:
    def __init__(self):
        self.full_name = {}
        self.repo_url = {}
        self.repo_type = {}
        self.release_src = {}
        self.release_version = {}
        self.dev_doxygen = {}
        self.release_doxygen = {}

    def register(self, short_name, full_name, repo_url, repo_type, release_src, release_version, dev_doxygen, release_doxygen):
        self.full_name[short_name] = full_name
        self.repo_url[short_name] = repo_url
        self.repo_type[short_name] = repo_type
        self.release_src[short_name] = release_src
        self.release_version[short_name] = release_version
        self.dev_doxygen[short_name] = dev_doxygen
        self.release_doxygen[short_name] = release_doxygen

    def codes(self):
        return self.repo_url.keys()

    def code_full_names(self):
        return [self.full_name[x] for x in self.full_name]

    def code_doxygen_release(self, code_name):
        return self.release_doxygen[code_name]

    def code_doxygen_dev(self, code_name):
        return self.dev_doxygen[code_name]

    def check_url(self, url):
        for code_name in self.repo_url:
            if self.repo_url[code_name] and self.repo_url[code_name].count(url) > 0:
                return code_name
        return None

# Declare the current set of CIG codes

code_db = CodeDB()

###############################
# Description of each argument to register()
# name: A unique short non-capitalized non-whitespace name for each code, must correspond to directory name
# full_name: The full name of the code - may include whitespace, caps, etc
# repo_url: The URL to the development repository of the code, used to generate doxygen docs
# repo_type: The source control system for the repository, one of svn, hg, or git
# release_src: The tarball containing the source of the release version, used to generate doxygen docs
# release_version: The version number of the released source, used to generate doxygen docs
# dev_doxygen: Whether to create doxygen docs based on the development repository
# release_doxygen: Whether to create doxygen docs based on the release tarball
###############################

###############################
# Short-Term Crustal Dynamics #
###############################
code_db.register(short_name="pylith",
                 full_name="PyLith",
                 repo_url="http://geodynamics.org/svn/cig/short/3D/PyLith/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/pylith/pylith-1.8.0.tgz",
                 release_version="1.8.0",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="relax",
                 full_name="RELAX",
                 repo_url="http://geodynamics.org/hg/short/3D/relax",
                 repo_type="hg",
                 release_src="http://geodynamics.org/cig/software/relax/Relax-1_0_4.tgz",
                 release_version="1.0.4",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="selen",
                 full_name="SELEN",
                 repo_url="https://github.com/geodynamics/selen.git",
                 repo_type="git",
                 release_src="http://geodynamics.org/cig/software/selen/SELEN_2.9.10.4.tar.gz",
                 release_version="2.9.10.4",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="lithomop",
                 full_name="LithoMop",
                 repo_url="http://geodynamics.org/svn/cig/short/3D/lithomop/trunk/",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/lithomop/lithomop3d-0.7.2.tar.gz",
                 release_version="0.7.2",
                 dev_doxygen=True,
                 release_doxygen=True)

#######################
# Long-Term Tectonics #
#######################
code_db.register(short_name="gale",
                 full_name="Gale",
                 repo_url="http://geodynamics.org/hg/long/3D/gale",
                 repo_type="hg",
                 release_src="http://geodynamics.org/cig/software/gale/Gale-2_0_1.tgz",
                 release_version="2.0.1",
                 dev_doxygen=False,
                 release_doxygen=False)

code_db.register(short_name="plasti",
                 full_name="Plasti",
                 repo_url="http://geodynamics.org/svn/cig/long/2D/plasti/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/plasti/plasti-1.0.0.tar.gz",
                 release_version="1.0.0",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="snac",
                 full_name="SNAC",
                 repo_url="http://geodynamics.org/svn/cig/long/3D/SNAC/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/snac/SNAC-1.2.0.tar.gz",
                 release_version="1.2.0",
                 dev_doxygen=False,
                 release_doxygen=False)

#####################
# Mantle Convection #
#####################
code_db.register(short_name="citcomcu",
                 full_name="CitcomCU",
                 repo_url="http://geodynamics.org/svn/cig/mc/3D/CitcomCU/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/citcomcu/CitcomCU-1.0.3.tar.gz",
                 release_version="1.0.3",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="citcoms",
                 full_name="CitcomS",
                 repo_url="http://geodynamics.org/svn/cig/mc/3D/CitcomS/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/citcoms/CitcomS-3.2.0.tar.gz",
                 release_version="3.2.0",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="conman",
                 full_name="ConMan",
                 repo_url="http://geodynamics.org/svn/cig/mc/2D/ConMan/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/conman/ConMan-2.0.0.tar.gz",
                 release_version="2.0.0",
                 dev_doxygen=False,
                 release_doxygen=False)

code_db.register(short_name="ellipsis3d",
                 full_name="Ellipsis3D",
                 repo_url="http://geodynamics.org/svn/cig/mc/3D/ellipsis3d/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/ellipsis3d/Ellipsis3D-1.0.2.tar.gz",
                 release_version="1.0.2",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="hc",
                 full_name="HC",
                 repo_url="http://geodynamics.org/svn/cig/mc/1D/hc/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/hc/HC-1_0.tgz",
                 release_version="1.0",
                 dev_doxygen=True,
                 release_doxygen=True)

##############
# Seismology #
##############
code_db.register(short_name="specfem3d",
                 full_name="SPECFEM3D Cartesian",
                 repo_url="http://geodynamics.org/svn/cig/seismo/3D/SPECFEM3D/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/specfem3d/SPECFEM3D_Cartesian_V2.0.2.tar.gz",
                 release_version="2.0.2",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="specfem3d-globe",
                 full_name="SPECFEM3D GLOBE",
                 repo_url="http://geodynamics.org/svn/cig/seismo/3D/SPECFEM3D_GLOBE/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/specfem3d-globe/SPECFEM3D_GLOBE_V5.1.5.tar.gz",
                 release_version="5.1.5",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="specfem3d-geotech",
                 full_name="SPECFEM3D GEOTECH",
                 repo_url="http://geodynamics.org/svn/cig/seismo/3D/SPECFEM3D_GEOTECH/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/specfem3d-geotech/SPECFEM3D_GEOTECH_V1.1b.tar.gz",
                 release_version="1.1b",
                 dev_doxygen=False,
                 release_doxygen=False)

code_db.register(short_name="specfem2d",
                 full_name="SPECFEM2D",
                 repo_url="http://geodynamics.org/svn/cig/seismo/2D/SPECFEM2D/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/specfem2d/SPECFEM2D-7.0.0.tar.gz",
                 release_version="7.0.0",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="specfem1d",
                 full_name="SPECFEM1D",
                 repo_url="http://geodynamics.org/svn/cig/seismo/1D/SPECFEM1D/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/specfem1d/SPECFEM1D-1.0.3.tar.gz",
                 release_version="1.0.3",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="mineos",
                 full_name="Mineos",
                 repo_url="http://geodynamics.org/svn/cig/seismo/1D/mineos/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/mineos/mineos-1.0.2.tgz",
                 release_version="1.0.2",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="flexwin",
                 full_name="Flexwin",
                 repo_url="http://geodynamics.org/svn/cig/seismo/3D/ADJOINT_TOMO/flexwin",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/flexwin/FLEXWIN-1.0.1.tar.gz",
                 release_version="1.0.1",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="seismic_cpml",
                 full_name="SEISMIC_CPML",
                 repo_url="http://geodynamics.org/svn/cig/seismo/3D/CPML/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/seismic_cpml/SEISMIC_CPML_1.2.tar.gz",
                 release_version="1.2",
                 dev_doxygen=True,
                 release_doxygen=True)

#############
# Geodynamo #
#############
code_db.register(short_name="mag",
                 full_name="MAG",
                 repo_url="http://geodynamics.org/svn/cig/geodyn/3D/MAG/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/mag/MAG-1.0.2.tar.gz",
                 release_version="1.0.2",
                 dev_doxygen=True,
                 release_doxygen=True)

#########################
# Computational Science #
#########################
code_db.register(short_name="cigma",
                 full_name="Cigma",
                 repo_url="http://geodynamics.org/svn/cig/cs/benchmark/cigma/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/cigma/cigma-1.0.0.tar.gz",
                 release_version="1.0.0",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="exchanger",
                 full_name="Exchanger",
                 repo_url="http://geodynamics.org/svn/cig/cs/Exchanger/trunk",
                 repo_type="svn",
                 release_src="http://geodynamics.org/cig/software/exchanger/Exchanger-1.0.1.tar.gz",
                 release_version="1.0.1",
                 dev_doxygen=True,
                 release_doxygen=True)

code_db.register(short_name="pythia",
                 full_name="Pythia",
                 repo_url="",
                 repo_type="none",
                 release_src="http://geodynamics.org/cig/software/pythia/pythia-0.8.1.15.tar.gz",
                 release_version="0.8.1.15",
                 dev_doxygen=False,
                 release_doxygen=True)

