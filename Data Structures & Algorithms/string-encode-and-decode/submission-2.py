class Solution:

    def encode(self, strs: List[str]) -> str:
        

        a=[]
        for i in strs:
            a.append(str(len(i)))
            a.append('^')
            a.append(i)
            
        return ''.join(a)



    def decode(self, s: str) -> List[str]:
        ans=[]
        if not s:
            return []
        i=0
        j=0
        while i<len(s):
            while s[i]!='^':
                i+=1
            length=int(s[j:i])
            ans.append(s[i+1:i+length+1])
            i+=length+1
            j=i
        
        return ans

            



