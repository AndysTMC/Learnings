"""
Fenwick Tree (Binary Indexed Tree)
"""

class BIT:
    def __init__(self, n_or_list: int) -> None:
        if isinstance(n_or_list, int):
        	self.n = n_or_list; self.bit = [0] * (self.n + 1)
        else:
            arr = list(n_or_list)
            self.n = len(arr); self.bit = [0] * (self.n + 1)
            for i, val in enumerate(arr): self.add(i, val)

    def add(self, idx: int, delta: int) -> None:
        i = idx + 1
        while i <= self.n: self.bit[i] += delta; i += i & -i
    
    def prefix_sum(self, idx: int) -> int: 
        if idx < 0: return 0
        result = 0; i = idx + 1
        while i > 0: result += self.bit[i]; i -= i & -i
        return result
    
    def range_sum(self, left: int, right: int) -> int:
        if right < left: return 0
        return self.prefix_sum(right) - self.prefix_sum(left - 1)
    
    def get(self, idx) -> int:
        return self.range_sum(idx, idx)
    
    def set(self, idx: int, value: int) -> None:
        current = self.get(idx); self.add(idx, value - current)
    
    def lower_bound(self, target) -> None:
        if target <= 0: return 0
        idx = 0; bit_mask = 1
        while (bit_mask << 1) <= self.n: bit_mask <<= 1
        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < target:
                idx = nxt; target -= self.bit[nxt]
            bit_mask >>= 1
        return idx
    
    def __len__(self):
        return self.n
    
    def __repr__(self):
        return f"FenwickTree(n={self.n})"
