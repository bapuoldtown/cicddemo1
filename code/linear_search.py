from typing import List
def linear_search(nums: List , x: int):
    for i in nums:
        if i == x:
            return True
    return False

if __name__ == "__main__":
    print(linear_search([1,2,3], 30))
    