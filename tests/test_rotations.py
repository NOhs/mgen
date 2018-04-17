from unittest import TestCase
import random
import numpy as np
from math import cos, sin

from mgen.rotation_matrix_3d import _generate_matrix_XZX
from mgen.rotation_matrix_3d import _generate_matrix_XYX
from mgen.rotation_matrix_3d import _generate_matrix_YXY
from mgen.rotation_matrix_3d import _generate_matrix_YZY
from mgen.rotation_matrix_3d import _generate_matrix_ZYZ
from mgen.rotation_matrix_3d import _generate_matrix_ZXZ
from mgen.rotation_matrix_3d import _generate_matrix_XZY
from mgen.rotation_matrix_3d import _generate_matrix_XYZ
from mgen.rotation_matrix_3d import _generate_matrix_YXZ
from mgen.rotation_matrix_3d import _generate_matrix_YZX
from mgen.rotation_matrix_3d import _generate_matrix_ZYX
from mgen.rotation_matrix_3d import _generate_matrix_ZXY
from mgen import rotation_from_angles
from mgen import rotation_around_x
from mgen import rotation_around_y
from mgen import rotation_around_z
from mgen import rotation_around_axis
from mgen import rotation_from_angle_and_plane
from mgen import rotation_from_angle
from mgen import random_matrix

def is_close(m1, m2):
    np.testing.assert_allclose(m1, m2, atol=1.e-7)

def test_matrix_generation(func, single_rotations, name):
    rot_m = lambda a1, a2, a3: func(cos(a1), cos(a2), cos(a3), sin(a1), sin(a2), sin(a3))
    r1, r2, r3 = single_rotations
    rot_conv = lambda a1, a2, a3: rotation_from_angles((a1, a2, a3), name)

    for rand1, rand2, rand3 in np.random.uniform(-np.pi, np.pi, (10000, 3)):
        is_close(rot_m(rand1, rand2, rand3), r1(rand1).dot(r2(rand2)).dot(r3(rand3)))
        is_close(rot_m(rand1, rand2, rand3), rot_conv(rand1, rand2, rand3))

class TestRotations(TestCase):
    def test_rotation_2d(self):
        is_close(rotation_from_angle(0), np.eye(2))
        is_close(rotation_from_angle(np.pi/2), [[0, -1], [1, 0]])
        is_close(rotation_from_angle(np.pi), [[-1, 0], [0, -1]])
    def test_rotation_x(self):
        is_close(rotation_around_x(0), np.eye(3))
        is_close(rotation_around_x(np.pi/2), [[1, 0, 0], [0, 0, -1], [0, 1, 0]])
        is_close(rotation_around_x(np.pi), np.diag([1,-1,-1]))

    def test_rotation_y(self):
        is_close(rotation_around_y(0), np.eye(3))
        is_close(rotation_around_y(np.pi/2), [[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
        is_close(rotation_around_y(np.pi), np.diag([-1, 1, -1]))

    def test_rotation_z(self):
        is_close(rotation_around_z(0), np.eye(3))
        is_close(rotation_around_z(np.pi/2), [[0, -1, 0], [1, 0, 0], [0, 0, 1]])
        is_close(rotation_around_z(np.pi), np.diag([-1, -1, 1]))


    def test_rotation_XZX(self):
        test_matrix_generation(_generate_matrix_XZX, (rotation_around_x, rotation_around_z, rotation_around_x), 'XZX')

    def test_rotation_XYX(self):
        test_matrix_generation(_generate_matrix_XYX, (rotation_around_x, rotation_around_y, rotation_around_x), 'XYX')

    def test_rotation_YXY(self):
        test_matrix_generation(_generate_matrix_YXY, (rotation_around_y, rotation_around_x, rotation_around_y), 'YXY')

    def test_rotation_YZY(self):
        test_matrix_generation(_generate_matrix_YZY, (rotation_around_y, rotation_around_z, rotation_around_y), 'YZY')

    def test_rotation_ZYZ(self):
        test_matrix_generation(_generate_matrix_ZYZ, (rotation_around_z, rotation_around_y, rotation_around_z), 'ZYZ')

    def test_rotation_ZXZ(self):
        test_matrix_generation(_generate_matrix_ZXZ, (rotation_around_z, rotation_around_x, rotation_around_z), 'ZXZ')

    def test_rotation_XZY(self):
        test_matrix_generation(_generate_matrix_XZY, (rotation_around_x, rotation_around_z, rotation_around_y), 'XZY')

    def test_rotation_XYZ(self):
        test_matrix_generation(_generate_matrix_XYZ, (rotation_around_x, rotation_around_y, rotation_around_z), 'XYZ')

    def test_rotation_YXZ(self):
        test_matrix_generation(_generate_matrix_YXZ, (rotation_around_y, rotation_around_x, rotation_around_z), 'YXZ')

    def test_rotation_YZX(self):
        test_matrix_generation(_generate_matrix_YZX, (rotation_around_y, rotation_around_z, rotation_around_x), 'YZX')

    def test_rotation_ZYX(self):
        test_matrix_generation(_generate_matrix_ZYX, (rotation_around_z, rotation_around_y, rotation_around_x), 'ZYX')

    def test_rotation_ZXY(self):
        test_matrix_generation(_generate_matrix_ZXY, (rotation_around_z, rotation_around_x, rotation_around_y), 'ZXY')

    def test_raises_if_sequence_unknown(self):
        with self.assertRaises(ValueError):
            rotation_from_angles((0, 0, 0), 'AXY')

    def test_rotation_around_axis(self):
        for random in (np.random.rand(10000) - 0.5) * 2 * np.pi:
            is_close(rotation_around_axis([1, 0, 0], random), rotation_around_x(random))
            is_close(rotation_around_axis([0, 1, 0], random), rotation_around_y(random))
            is_close(rotation_around_axis([0, 0, 1], random), rotation_around_z(random))
            # Test if non-normalised axis works, too
            is_close(rotation_around_axis([2, 0, 0], random), rotation_around_x(random))

        is_close(rotation_around_axis([1, 1, 1], 2*np.pi/3), rotation_from_angles([0, np.pi/2, np.pi/2], 'XYZ'))

    def test_accepts_tuple_list_and_array(self):
        angles_t = (0.1, 0.2, 0.3)
        angles_l = list(angles_t)
        angles_a = np.array(angles_l)

        np.testing.assert_allclose(
            rotation_from_angles(angles_t, 'YZY'),
            rotation_from_angles(angles_l, 'YZY'))

        np.testing.assert_allclose(
            rotation_from_angles(angles_t, 'YZY'),
            rotation_from_angles(angles_a, 'YZY'))

    def test_rotation_nd(self):
        for rand1 in np.random.uniform(-np.pi, np.pi, 100):
            # Test 2D case
            is_close(rotation_from_angle(rand1), rotation_from_angle_and_plane(rand1, (1,0), (0,1)))
            # Test 3D case
            is_close(rotation_around_z(rand1), rotation_from_angle_and_plane(rand1, (1,0,0), (0,1,0)))
            # Test normalisation of first parameter
            is_close(rotation_around_z(rand1), rotation_from_angle_and_plane(rand1, (2,0,0), (0,1,0)))
            # Test normalisation of second parameter
            is_close(rotation_around_z(rand1), rotation_from_angle_and_plane(rand1, (1,0,0), (0,2,0)))
            # Test normalisation of both parameters
            is_close(rotation_around_z(rand1), rotation_from_angle_and_plane(rand1, (2,0,0), (0,2,0)))

            is_close(rotation_around_x(rand1), rotation_from_angle_and_plane(rand1, (0,1,0), (0,0,1)))
            is_close(rotation_around_y(rand1), rotation_from_angle_and_plane(rand1, (0,0,1), (1,0,0)))

            # Test non orthogonal vectors
            is_close(rotation_around_x(rand1), rotation_from_angle_and_plane(rand1, (0, 1, 1), (0, 1, 2)))

            # Test generic properties of higher dimensional rotations

            # create two perpendicular random vectors
            dimension = random.randint(4,100)
            v1 = np.random.uniform(-1., 1., dimension)
            v1 = v1/np.linalg.norm(v1)
            v2 = np.random.uniform(-1., 1., dimension)
            v2 = v2/np.linalg.norm(v2)
            v2 = v2 - v2.dot(v1)*v1

            m = rotation_from_angle_and_plane(rand1, v1, v2)
            m_inv = rotation_from_angle_and_plane(-rand1, v1, v2)
            is_close(m.dot(m.T), np.eye(dimension))
            self.assertAlmostEqual(np.linalg.det(m), 1.0)
            is_close(m, m_inv.T)

        with self.assertRaises(ValueError):
            rotation_from_angle_and_plane(0., (1,0,0), (0,1,0,0))
        with self.assertRaises(ValueError):
            rotation_from_angle_and_plane(0., (1,0,0,0), (0,1,0))
        with self.assertRaises(ValueError):
            rotation_from_angle_and_plane(0., (1,0,0), (1,0,0))
        with self.assertRaises(ValueError):
            rotation_from_angle_and_plane(0., (0,0), (1,0))
        with self.assertRaises(ValueError):
            rotation_from_angle_and_plane(0., (1,0), (0,0))

    def test_random_matrix(self):
        for x in range(2,7):
            vecx = np.zeros(x, dtype=np.float64)
            vecx[0] = 1.0
            m = random_matrix(x)
            rotx = np.matmul(m,vecx)
            lengthx = np.sum(rotx*rotx)
            self.assertAlmostEqual(lengthx, 1.0)
        with self.assertRaises(ValueError):
            random_matrix(1)
