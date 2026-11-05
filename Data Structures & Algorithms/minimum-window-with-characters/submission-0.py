class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        counts={}
        window={}
        for c in t:
            counts[c]=1+counts.get(c,0)
        have=0
        need=len(counts)
        l=0
        reslen=float("infinity")
        res=[-1,-1]
        for r in range(0,len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in counts and window[c]==counts[c]:
                have+=1
            while have==need:
                if (r-l+1) < reslen:
                    reslen=r-l+1
                    res=[l,r]
                window[s[l]]-=1
                if s[l] in counts and window[s[l]] < counts[s[l]]:
                    have-=1
                l+=1
        l,r=res
        if reslen != float("infinity"):
         return s[l:r+1]
        else:
            return ""