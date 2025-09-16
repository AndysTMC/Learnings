"""
Segment Tree Sum 
"""

class SegmentTreeSum:

    def __init__(self, data: List[int], lazy: bool = False) -> None:
        if not data: raise ValueError("datamust be non-empty")
        self.n = len(data); self.size = 1
        while self.size < self.n: self.size <<= 1
        self.tree = [0] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def point_set(self, idx: int, val: int) -> None:
        if not (0 <= idx < self.n): raise IndexError("index out of range")
        i = self.size + idx; self.tree[i] = val; i //= 2
        while i: self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]; i //= 2
    
    def point_add(self, idx: int, delta: int) -> None:
        if not (0 <= idx < self.n): raise IndexError("index out of range")
        i = self.size + idx; self.tree[i] += delta; i //= 2
        while i: self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]; i //= 2

    def get(self, idx: int) -> int:
        if not (0 <= idx < self.n): raise IndexError("index out of range")
        return self.tree[self.size + idx]
    
    def range_sum(self, left: int, right: int) -> int:
        if left > right: return 0
        if not (0 <= left <= right < self.n): raise IndexError("range_sum indices out of range")
        l = left + self.size; r = right + self.size; result = 0
        while l <= r:
            if l & 1: result += self.tree[l]; l += 1
            if not (r & 1): result += self.tree[r]; r -= 1
            l //= 2; r //= 2
        return result
    
    def to_list(self) -> List[int]:
        base = self.size
        return [self.tree[base + i] for i in range(self.n)]

    def lower_bound_prefix(self, target: int) -> int:
        if target <= 0: return 0
        if self.tree[1] < target: return self.n
        idx = 1; left, right = 0, self.size - 1
        while left != right:
            mid = (left + right) // 2
            if self.tree[2 * idx] >= target: idx = 2 * idx; right = mid
            else: target -= self.tree[2 * idx]; idx = 2 * idx + 1; left = mid + 1
        return left if left < self.n else self.n
    
    def __repr__(self):
        return f"SegmentTreeSum(n={self.n}, size={self.size})"
