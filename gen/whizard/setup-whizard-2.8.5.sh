#!/bin/bash

#source /cvmfs/clicdp.cern.ch/compilers/gcc/7.3.0/x86_64-centos7/setup.sh
#source /cvmfs/clicdp.cern.ch/compilers/ocaml/4.05.0/x86_64-slc6/setup.sh
source /cvmfs/sft.cern.ch/lcg/contrib/gcc/7.3.0/x86_64-centos7/setup.sh
source /cvmfs/clicdp.cern.ch/compilers/ocaml/4.04.0/x86_64-centos7/setup.sh
#export OCAMLDIR=/cvmfs/sft.cern.ch/lcg/releases/ocaml/4.07.1-6bb40/x86_64-centos7-gcc7-opt
#export PATH=${OCAMLDIR}/bin:${PATH}
#export LD_LIBRARY_PATH=${OCAMLDIR}/lib:${LD_LIBRARY_PATH}

export PYTHONDIR=/cvmfs/clicdp.cern.ch/software/Python/2.7.14/x86_64-centos7-gcc7-opt
export PATH=${PYTHONDIR}/bin:$PATH
export LD_LIBRARY_PATH=${PYTHONDIR}/lib:${LD_LIBRARY_PATH}

export LCIO_DIR=/cvmfs/sft.cern.ch/lcg/releases/LCIO/02.12.01-a2fbf/x86_64-centos7-gcc7-opt
export HEPMC_DIR=/cvmfs/sft.cern.ch/lcg/releases/HepMC/2.06.09-0a23a/x86_64-centos7-gcc7-opt
export LHAPDF_DIR=/cvmfs/sft.cern.ch/lcg/releases/MCGenerators/lhapdf/6.2.1-fd400/x86_64-centos7-gcc7-opt

export LD_LIBRARY_PATH=$LCIO_DIR/lib:$HEPMC_DIR/lib:$LHAPDF_DIR/lib:$LD_LIBRARY_PATH
export PATH=$LCIO_DIR/bin:$LHAPDF_DIR/bin:$PATH

#WHIZARD
#export LD_LIBRARY_PATH=/cvmfs/clicdp.cern.ch/software/WHIZARD/2.6.3/x86_64-slc6-gcc7-opt/lib:${LD_LIBRARY_PATH}
#export PATH=/cvmfs/clicdp.cern.ch/software/WHIZARD/2.6.3/x86_64-slc6-gcc7-opt/bin:$PATH
#export LD_LIBRARY_PATH=/sw/ilc/gcc730/whizard/trunk-mpi/lib:${LD_LIBRARY_PATH}
#export PATH=/sw/ilc/gcc730/whizard/trunk-mpi/bin:$PATH
export LD_LIBRARY_PATH=/sw/ilc/gcc730/whizard/2.8.5/lib:${LD_LIBRARY_PATH}
export PATH=/sw/ilc/gcc730/whizard/2.8.5/bin:$PATH

#m4
export M4_DIR=/cvmfs/sft.cern.ch/lcg/releases/m4/1.4.18-b8d0d/x86_64-centos7-gcc7-opt
export LD_LIBRARY_PATH=${M4_DIR}/lib:${LD_LIBRARY_PATH}
export PATH=${M4_DIR}/bin:$PATH

#libtool
#export LIBTOOL_DIR=/cvmfs/sft.cern.ch/lcg/releases/libtool/2.4.2-9ad34/x86_64-centos7-gcc7-opt
#export LIBTOOL_DIR=/cvmfs/clicdp.cern.ch/software/libtool/2.4.6/x86_64-slc6-gcc7-opt
#export LD_LIBRARY_PATH=${LIBTOOL_DIR}/lib:${LD_LIBRARY_PATH}
#export PATH=${LIBTOOL_DIR}/bin:$PATH


# for mpi
#export OPENMPI_DIR=/cvmfs/sft.cern.ch/lcg/releases/openmpi/3.1.0-37032/x86_64-centos7-gcc7-opt
#export OPENMPI_DIR=/cvmfs/clicdp.cern.ch/software/OpenMPI/3.1.0/x86_64-slc6-gcc7-opt
export OPENMPI_DIR=/sw/ilc/gcc730/openmpi/4.0.5
export LD_LIBRARY_PATH=${OPENMPI_DIR}/lib:$LD_LIBRARY_PATH
export PATH=${OPENMPI_DIR}/bin:$PATH
#
