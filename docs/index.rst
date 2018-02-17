.. mgen documentation master file, created by
   sphinx-quickstart on Mon Jan 29 23:20:54 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

mgen package documentation
==========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

The mgen package offers functions to generate plain rotation matrices using either of
the following options:

- (2D) Give an angle
- (3D) Give three Euler / Tait-Bryan angles
- (3D) Give a rotation axis and an angle
- (3D) Give an angle and a cartesian coordinate axis around which to rotate (x, y, z)
- (nD) Give an angle and a pair of orthogonal vectors that span a plane

Simple usage examples
---------------------

The following code snippet show how to use the 2D function::

    >>> import numpy as np
    >>> np.set_printoptions(suppress=True)
    >>> from mgen import rotation_from_angle

    >>> matrix = rotation_from_angle(np.pi/2)
    >>> matrix.dot([1, 0])
    # array([0., 1.])

The following code snippet shows how to use the three different 3D options::

    >>> import numpy as np
    >>> np.set_printoptions(suppress=True)

    >>> from mgen import rotation_around_axis
    >>> from mgen import rotation_from_angles
    >>> from mgen import rotation_around_x

    >>> matrix = rotation_from_angles([np.pi/2, 0, 0], 'XYX')
    >>> matrix.dot([0, 1, 0])
    array([0., 0., 1.])

    >>> matrix = rotation_around_axis([1, 0, 0], np.pi/2)
    >>> matrix.dot([0, 1, 0])
    array([0., 0., 1.])

    >>> matrix = rotation_around_x(np.pi/2)
    >>> matrix.dot([0, 1, 0])
    array([0., 0., 1.])

Here is an example of how to create an n-dimensional rotation::

    >>> import numpy as np
    >>> np.set_printoptions(suppress=True)

    >>> from mgen import rotation_from_angle_and_plane

    >>> matrix = rotation_from_angle_and_plane(np.pi/2, (0, 1, 0, 0), (0, 0, 1, 0))
    >>> matrix.dot([0, 1, 0, 0])
    # array([0., 0., 1., 0.])

Finally an example of a nxn random matrix :math:`\in O(n)` which can be used to rotate a vector 
with uniform distribution on the unit n-sphere::

    >>> from mgen import random_matrix

    >>> n = 6
    >>> matrices = np.array([random_matrix(n) for _ in range(100)])
    >>> vector = np.zeros(n)
    >>> vector[0] = 1.0

    # vectors of length one should keep length one
    >>> rotated = np.matmul(matrices,vector)
    >>> lengths = np.sum(rotated*rotated, axis=1)
    >>> print("Minimum length: %.5f; Maximum length: %.5f"%(np.amin(lengths),np.amax(lengths)))


Module documentation
--------------------

2D rotation matrix functions
############################

.. autofunction:: mgen.rotation_from_angle

3D rotation matrix functions
############################

.. autofunction:: mgen.rotation_from_angles

.. autofunction:: mgen.rotation_around_axis

.. autofunction:: mgen.rotation_around_x

.. autofunction:: mgen.rotation_around_y

.. autofunction:: mgen.rotation_around_z

nD rotation matrix functions
############################

.. autofunction:: mgen.rotation_from_angle_and_plane

.. autofunction:: mgen.random_matrix
