class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        m = min([len(s) for s in strs])
        sl = len(strs)

        for i in range(m):
            demo = []
            for j in range(sl):
                demo.append(strs[j][i])

            if len(set(demo)) == 1:
                res += demo[0]
            else:
                break
        return res
