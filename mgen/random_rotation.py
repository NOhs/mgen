import numpy as np

def random_rotation(n):
    '''
    Generate a nxn random matrix.
    The distribution of rotations is uniform on the n-sphere.
    The random matrix is from the O(n) group (not SO(n)) and uses the gram-schmidt algorithm to orthogonalize the random matrix,
    see http://www.ams.org/notices/200511/what-is.pdf
    If a rotation from SO(n) is needed, look for: "A statistical model for random rotations" doi:10.1016/j.jmva.2005.03.009
    
    :param n: dimension of space in which the rotation operates
	:type n: int
	:returns: rotation matrix
	:rtype: a nxn :any:`numpy.ndarray`
	'''
    if n < 2:
        raise ValueError('n must be greater than 1 but is ' + str(n) + '.')
    
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