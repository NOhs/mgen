import numpy as np

def random_rotation(n):
    '''
    Generate a nxn rotation matrix with a random direction in n-dimensional space
    and angle of rotation.
    The distribution of rotations is uniform on the n-sphere.
    
    :param n: dimension of space in which the rotation operates
	:type n: int
	:returns: rotation matrix
	:rtype: a nxn :any:`numpy.ndarray`
	'''
    if n < 2:
        raise ValueError('n must be greater than 1 but is ' + n + '.')
    
    a = np.random.randn(n,n)
    
    a[0] = a[0]/np.linalg.norm(a[0])
    
    iter = n*(n-1)//2
    base = 0
    mod = base + 1
    for i in range(0,iter):	
        a[mod] = a[mod] - a[base]*np.dot(a[mod],a[base])
        a[mod] = a[mod]/np.linalg.norm(a[mod])
        
        if mod < n-1:
            mod += 1
        else:
            base += 1
            mod = base + 1
    return a