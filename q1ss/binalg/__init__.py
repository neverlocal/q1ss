"""
Binary linear algebra primitives:

- The class :class:`binvec` implements binary vectors and common operations.
- The class :class:`binmat` implements binary matrices and common operations.
- The class :class:`AffineSubspace` implements affine subspaces of binary vector
  spaces, with a variety of operations and transformations.

"""

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations
from .binvec import binvec
from .binmat import binmat
from .affine import AffineSubspace

__all__ = ("binvec", "binmat", "AffineSubspace")
