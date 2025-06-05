class Solution(object):
    def findRotateSteps(self, ring, key):
        n = len(ring)
        pos = {}
        for i, ch in enumerate(ring):
            pos.setdefault(ch, []).append(i)
        first_positions = pos[key[0]]
        dp = []
        for idx in first_positions:
            d = idx if idx <= n - idx else n - idx
            dp.append(d + 1)
        prev_positions = first_positions
        for ch in key[1:]:
            cur_positions = pos[ch]
            new_dp = []
            for cur in cur_positions:
                best = 10**9
                for cost_prev, prev in zip(dp, prev_positions):
                    d = prev - cur if prev >= cur else cur - prev
                    step = d if d <= n - d else n - d
                    c = cost_prev + step + 1
                    if c < best:
                        best = c
                new_dp.append(best)
            dp = new_dp
            prev_positions = cur_positions
        return min(dp)
