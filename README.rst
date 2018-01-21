MGen: Convenient matrix generation functions
============================================

Python and its most popular packages do not offer out-of-the-box convenient
functions to generate rotation matrices in 3D. While there are other projects
that offer rotation and vector classes, or offer rotations via the use of quaternions,
if you simply want a rotation matrix, for example if other packages require them
as an input, or you do not wish to change your current data structure to use
special rotation classes, the common suggestion is to implement them yourself
(see for example this discussion on SE:
https://stackoverflow.com/questions/6802577/rotation-of-3d-vector). However,
everybody implementing their own version of the same thing can hardly be seen as
ideal.
Therefore, this package provides simple functions to generate rotation matrices
for a given axis and angle, or for three given angles (proper Euler angles
or Tait-Bryan angles)

.. code:: python

        import numpy as np
        from mgen import rotation_around_axis
        from mgen import rotation_from angles
        from mgen import rotation_around_x

        matrix = rotation_around_axis([1, 0, 0], np.pi/2)
        matrix.dot([0, 1, 0])
        # [0, 0, 1]

        matrix = rotation_from_angles([np.pi/2, 0, 0], 'XYX')
        matrix.dot([0, 1, 0])
        # [0, 0, 1]

        matrix = rotation_around_x(np.pi/2)
        matrix.dot([0, 1, 0])
        # [0, 0, 1]
