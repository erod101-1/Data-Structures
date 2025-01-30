#include <iostream>
#include <vector>
#include <algorithm>
void subset_helper(int i,std::vector<int> nums, std::vector<int>& curr_set, std::vector<std::vector<int>>& subsets);

std::vector<std::vector<int>> subsets(std::vector<int> nums)
{
    std::vector<int> curr_set;
    std::vector<std::vector<int>> subsets;
    subset_helper(0,nums,curr_set,subsets);
    return subsets;
}

std::vector<std::vector<int>> subset_duplicates(std::vector<int> nums)
{
    std::sort(nums.begin(),nums.end());
    std::vector<int> curr_set;
    std::vector<std::vector<int>> subsets;
    subset_helper(0,nums,curr_set,subsets);
    return subsets;
}
void subset_helper(int i, std::vector<int> nums,std::vector<int>& curr_set, std::vector<std::vector<int>>& subsets)
{
    // check that we are within bounds
    if(i >= nums.size())
    {
        std::vector<int> tmp_set;
        for (const auto j : curr_set)
            tmp_set.push_back(j);
        subsets.push_back(tmp_set);
        tmp_set.clear();
        return;
    }

    // decesion to add element to the subset
    curr_set.push_back(nums[i]);
    subset_helper(i+1,nums,curr_set,subsets);
    curr_set.pop_back();

    // desicion to not push
    subset_helper(i+1,nums,curr_set,subsets);
}

void subset_helper_duplicate(int i, std::vector<int> nums,std::vector<int>& curr_set, std::vector<std::vector<int>>& subsets)
{
    // check that we are within bounds
    if(i >= nums.size())
    {
        std::vector<int> tmp_set;
        for (const auto j : curr_set)
            tmp_set.push_back(j);
        subsets.push_back(tmp_set);
        tmp_set.clear();
        return;
    }

    // decesion to add element to the subset
    curr_set.push_back(nums[i]);
    subset_helper(i+1,nums,curr_set,subsets);
    curr_set.pop_back();

    // desicion to not push
    while (i <= nums.size() && nums[i] == nums[i+1])
    {
        i += 1; // skip all the duplicates
    }
    subset_helper_duplicate(i+1,nums,curr_set,subsets);
}
int main(void)
{
    std::vector<int> nums = {1,2,2,3};
    std::vector<std::vector<int>> ss = subset_duplicates(nums);
    for(auto set : ss)
    {
        for(auto num : set)
        {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}