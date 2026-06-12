nums1=[1,2]
nums2=[3,4]
re=sorted(nums1+nums2)
sum=len(re)
if sum%2==1:
 print(re[sum//2])
else:print(re[sum//2-1]+re[sum//2])