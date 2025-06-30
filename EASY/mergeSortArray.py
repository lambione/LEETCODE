


def merge(nums1, m, nums2, n):
        if len(nums2) == 0 :
            return nums1 
        arr = []
        counted = 0
        other = 0
        for _ in range(m):
            if other < n :
                if nums1[counted] <= nums2[other]:
                    arr.append(nums1[counted])
                    counted += 1
                else:
                    arr.append(nums2[other])
                    other += 1
            else :
                arr.append(nums1[counted])
                counted += 1

        for _ in range((n-other) + (m - counted)):
            if counted < m:
                if(other < n):
                    if nums1[counted] < nums2[other]:
                        arr.append(nums1[counted])
                        counted += 1
                    else :
                        arr.append(nums2[other])
                        other += 1
                else :
                    arr.append(nums1[counted])
                    counted += 1
            else :
                arr.append(nums2[other])
                other += 1
                
        for l in range(m+n):
            nums1[l] = arr[l]
        
        return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))