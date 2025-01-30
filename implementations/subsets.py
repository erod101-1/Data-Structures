# Given a list of distinct nums return all possible distinct subsets

# [1 2 3 ]
# Subets: [1] [2] [3] [1,2] [1,3] [2,3] [1,2,3]
# Not: [1,2] and [2,1] are the same

# The number of subsets is always 2^n where n is the number of elements in the list
# Standard bracktracking implementation

def subsets(nums):
    subsets, current_set = [],[]
    subset_helper(0,nums=nums,current_set=current_set,subsets=subsets)
    return subsets

def subset_helper(i,nums,current_set,subsets):
    if i >= len(nums):
        subsets.append(current_set.copy())
        return
    
    # decision 1: include the set in our subset
    current_set.append(nums[i])
    subset_helper(i+1,nums=nums,current_set=current_set,subsets=subsets)
    current_set.pop()

    # desision 2: dont include the set in our subset
    subset_helper(i+1,nums,current_set=current_set , subsets=subsets)


def main():
    print(subsets([1,2,3]))


if __name__=='__main__':
    main()