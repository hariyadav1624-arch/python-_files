strs=["flower","flow"]
l=(len(strs[0]))
print(l)
while l<=0:
        for i in range(1, len(strs)):
          if strs[0]==strs[i]:
           print( strs[0])
          else :print(strs[0].pop(l-1))