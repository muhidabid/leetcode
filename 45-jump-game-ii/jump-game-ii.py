class Solution(object):
    def jump(self, nums):
        ans = 0
        end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                ans += 1
                break
            if i == end:     
                ans += 1        
                end = farthest  
        return ans

# class Solution(object):
#     def jump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         unvisited = {}
#         cost = {}

#         if len(nums) > 0:
#             for i, n in enumerate(nums):
#                 unvisited[i] = True
#                 cost[i] = float('inf')
            
#             unvisited[0] = False
#             cost[0] = 0
#             i = 0
#             tmp = float('inf')

#             while True in unvisited:
#                 tmp = float('inf')
#             # for i, n in enumerate(nums):
#                 # get node with minimum cost which isn't visited
#                 for x in cost:
#                     if cost[x] < tmp and unvisited[x] == True:
#                         tmp = cost[x]
#                         i = x
#                 # i = min(cost, key=cost.get)  
#                 unvisited[i] = False  # mark that as visited
#                 for j in range(nums[i]):
#                     if i+j < len(nums) and cost[i] + 1 < cost[i+j]:
#                         cost[i+j] += cost[i] + 1

#             return cost[len(nums)-1]
#         else:
#             return 1
