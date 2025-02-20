# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class DtDiamondRight(Package):
    """This package has an indirect diamond dependency on dt-diamond-bottom"""

    homepage = "http://www.example.com"
    url = "http://www.example.com/dt-diamond-right-1.0.tar.gz"

    version("1.0", md5="0123456789abcdef0123456789abcdef")

    depends_on("dt-diamond-bottom", type=("build", "link", "run"))
