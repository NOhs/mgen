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

- Give three Euler / Tait-Bryan angles
- Give a rotation axis and an angle
- Give an angle and a base axis around which to rotate (x, y, z)

It also offers functions to create n-dimensional rotations.

Simple usage examples
---------------------

The following code snippet shows how to use the three different options::

    >>> import numpy as np
    >>> np.set_printoptions(suppress=True)

    >>> from mgen import rotation_around_axis
    >>> from mgen import rotation_from_angles
    >>> from mgen import rotation_around_x
    >>> from mgen import rotation_from_angle_and_plane

    >>> matrix = rotation_from_angles([np.pi/2, 0, 0], 'XYX')
    >>> matrix.dot([0, 1, 0])
    array([0., 0., 1.])

    >>> matrix = rotation_around_axis([1, 0, 0], np.pi/2)
    >>> matrix.dot([0, 1, 0])
    array([0., 0., 1.])

    >>> matrix = rotation_around_x(np.pi/2)
    >>> matrix.dot([0, 1, 0])
    array([0., 0., 1.])

    >>> matrix = rotation_from_angle_and_plane(np.pi/2, (0, 1, 0, 0), (0, 0, 1, 0))
    >>> matrix.dot([0, 1, 0, 0])
    # array([0., 0., 1., 0.])



Module documentation
--------------------

.. autofunction:: mgen.rotation_from_angles

.. autofunction:: mgen.rotation_around_axis

.. autofunction:: mgen.rotation_around_x

.. autofunction:: mgen.rotation_around_y

.. autofunction:: mgen.rotation_around_z

.. autofuction:: mgen.rotation_from_angle_and_plane

