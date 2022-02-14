import code_1014_best_sightseeing_pair as c

def test_example_1():
    s = c.Solution()
    assert s.maxScoreSightseeingPair([8,1,5,2,6]) == 11

def test_example_2():
    s = c.Solution()
    assert s.maxScoreSightseeingPair([1,2]) == 2

def test_large_array():
    s = c.Solution()
    file_object = open('large_input_array.txt', 'r')
    arr = [int(s) for s in file_object.read().splitlines()]
    result = s.maxScoreSightseeingPair(arr)