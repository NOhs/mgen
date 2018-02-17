|test| |coverage| |documentation| |pypi| |license|

.. |test| image:: https://travis-ci.org/NOhs/mgen.svg?branch=master
    :target: https://travis-ci.org/NOhs/mgen
.. |coverage| image:: https://coveralls.io/repos/github/NOhs/mgen/badge.svg
    :target: https://coveralls.io/github/NOhs/mgen
.. |documentation| image:: https://readthedocs.org/projects/mgen/badge/?version=latest
    :target: http://mgen.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. |pypi| image:: https://badge.fury.io/py/mgen.svg
    :target: https://badge.fury.io/py/mgen

.. |license| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
    :target: https://opensource.org/licenses/BSD-3-Clause

MGen: Convenient matrix generation functions
============================================

Python and its most popular packages do not offer out-of-the-box convenient
functions to generate rotation matrices. While there are other projects
that offer rotation and vector classes, or offer rotations via the use of quaternions,
if you simply want a rotation matrix, for example if other packages require them
as an input, or you do not wish to change your current data structure to use
special rotation classes, the common suggestion is to implement them yourself
(see for example this discussion on SE:
https://stackoverflow.com/questions/6802577/rotation-of-3d-vector). However,
everybody implementing their own version of the same thing can hardly be seen as
ideal.

Therefore, this package provides simple functions to generate rotation matrices
in 2d for a given angle or in 3d for a given axis and angle, or for three given
angles (proper Euler angles or Tait-Bryan angles).

Additionally, n-dimensional rotations can be generated using an angle and two
orthogonal vectors that span the plane of rotation.

Trivial example usage
----------------------

Below you see examples of how to use mgen to generate rotation matrices. For further
documentation please have a look here: https://mgen.readthedocs.io

.. code:: python

    import numpy as np
    np.set_printoptions(suppress=True)

    from mgen import rotation_around_axis
    from mgen import rotation_from_angles
    from mgen import rotation_around_x
    from mgen import rotation_from_angle_and_plane
    from mgen import rotation_from_angle
    from mgen import random_matrix

    # 2D example
    matrix = rotation_from_angle(np.pi/2)
    matrix.dot([1, 0])
    # array([0., 1.])

    #3D examples
    matrix = rotation_from_angles([np.pi/2, 0, 0], 'XYX')
    matrix.dot([0, 1, 0])
    # array([0., 0., 1.])

    matrix = rotation_around_axis([1, 0, 0], np.pi/2)
    matrix.dot([0, 1, 0])
    # array([0., 0., 1.])

    matrix = rotation_around_x(np.pi/2)
    matrix.dot([0, 1, 0])
    # array([0., 0., 1.])

    # n-dimensional example
    matrix = rotation_from_angle_and_plane(np.pi/2, (0, 1, 0, 0), (0, 0, 1, 0))
    matrix.dot([0, 1, 0, 0])
    # array([0., 0., 1., 0.])

    # n-dimensional random matrix O(n), e.g. n=27
    matrix = random_matrix(27)
