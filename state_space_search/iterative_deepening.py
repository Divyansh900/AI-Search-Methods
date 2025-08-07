from utils.test import test
from depth_bound_dfs import dbdfs

@test
def dfid(start:str, target:str, alt: bool=False, max_depth: int = 10):
    for depth in range(0, max_depth):
        result = dbdfs(start, target, depth)
        if result:
            return result, depth
    return None, max_depth

if __name__ == '__main__':
    dfid(start='A', target='L', max_depth=10)