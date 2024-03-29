from typing import List
def linear_search(nums: List , x: int):
    for i in nums:
        if i == x:
            return True
    return False
    