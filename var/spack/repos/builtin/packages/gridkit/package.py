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

    version("develop", submodules=True, branch="nicholson/enzyme-support")

    variant("enzyme", default=False, description="Enable/Disable Enzyme")
    variant("ipopt", default=False, description="Enable/Disable Ipopt")
    variant("klu", default=True, description="Enable/Disable KLU")
    variant("sundials", default=True, description="Enable/Disable SUNDIALS")

    conflicts("+klu", when="~sundials")

    depends_on("cxx", type="build")
    depends_on("enzyme", when="+enzyme")
    depends_on("ipopt~mumps+coinhsl", when="+ipopt")
    depends_on("sundials@7:+klu~mpi", when="+sundials+klu")
    depends_on("sundials@7:~klu~mpi", when="+sundials~klu")

    def cmake_args(self):
        args = []
        spec = self.spec

        args.extend(
            [
                self.define_from_variant("GRIDKIT_ENABLE_IPOPT", "ipopt"),
                self.define_from_variant("GRIDKIT_ENABLE_SUNDIALS", "sundials"),
                self.define_from_variant("GRIDKIT_ENABLE_SUNDIALS_SPARSE", "klu"),
                self.define_from_variant("GRIDKIT_ENABLE_ENZYME", "enzyme"),
            ]
        )

        return args
