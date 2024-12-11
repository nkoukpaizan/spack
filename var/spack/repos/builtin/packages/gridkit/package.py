# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Gridkit(CMakePackage):
    """Experimental code for prototyping interfaces betwen numerical libraries and network models."""

    homepage = "https://github.com/ORNL/GridKit"
    git = "https://github.com/ORNL/GridKit.git"

    maintainers("nkoukpaizan", "pelesh")

    version("develop", submodules=True, branch="develop")

    depends_on("cxx", type="build")
    depends_on("suite-sparse")
    depends_on("sundials@7:+klu~mpi")
    depends_on("ipopt~mumps")
