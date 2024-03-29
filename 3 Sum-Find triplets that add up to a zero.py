from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    ans = []
    temp = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                temp = []
                if nums[i] + nums[j] + nums[k] == 0:
                    temp.append(nums[i])
                    temp.append(nums[j])
                    temp.append(nums[k])
                if len(temp) != 0:
                    ans.append(temp)
    return ans

if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    ans = threeSum(arr)
    print("The triplets are as follows: ")
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()
