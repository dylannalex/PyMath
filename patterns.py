import re

OPS = re.compile(r'(^\w+)')

# Vectors sintax: vec(a b c d e f) or vec(a,b,c,d,e,f) [n-dimensional]
VEC = re.compile(
    r'\bvec\(((-?\d+[./]?\d*)[\s,])*(-?\d+[./]?\d*)\)')

# Plane's normal vectors sintax: nvec(a b c) or nvec(a,b,c) [3-dimensional]
NVEC = re.compile(
    r'\bnvec\((-?\d+[./]?\d*)[\s,](-?\d+[./]?\d*)[\s,](-?\d+[./]?\d*)\)')

# Points sintax: pt(a b c) or pt(a,b,c) [3-dimensional]
PT = re.compile(
    r'\bpt\((-?\d+[./]?\d*)[\s,](-?\d+[./]?\d*)[\s,](-?\d+[./]?\d*)\)')


MATRIX = re.compile(
    r'\bmatrix[([](((-?\d+[./]?\d*)\s)*(-?\d+[./]?\d*),(\s)*)*((-?\d+[./]?\d*)\s)*(-?\d+[./]?\d*)[])]')
