class Solution(object):
    def rotate(self, nums, k):
        def reverse(arr,a,b):
            while(a<=b):
                arr[a],arr[b]=arr[b],arr[a]
                a+=1
                b-=1
        n=len(nums)
        k=k%n
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-k-1)
        reverse(nums,0,n-1)

        