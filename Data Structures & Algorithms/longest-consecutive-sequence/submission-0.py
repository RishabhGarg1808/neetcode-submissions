class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            num_set.add(num)
        
        res = []

        for num in nums:
            if num-1 in num_set :
                continue
            
            n = len(res)
            i = 1
            local_res = [num]
            
            while True:
                if num +i in num_set :
                    local_res.append(num + i)
                    i += 1
                else:
                    break
            
            if len(local_res) > len(res):
                res = local_res
        

        return len(res)
            
