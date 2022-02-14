# You are given an integer array values where values[i] represents 
# the value of the ith sightseeing spot. 
# 
# Two sightseeing spots i and j have a distance j - i between them.
# 
# The score of a pair (i < j) of sightseeing spots is 
# values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, 
# minus the distance between them.
# 
# Return the maximum score of a pair of sightseeing spots.


class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        n = len(values)
        max_score = values[0] + values[1] + 0 - 1
        if n == 2:
            return max_score
        
        max_score = values[0]
        best_index = 0
        
        for i in range(1,n):
            max_score = max(max_score, values[best_index] + best_index + values[i] - i)
            if values[best_index] + best_index < values[i] + i:
                best_index = i

        return max_score
