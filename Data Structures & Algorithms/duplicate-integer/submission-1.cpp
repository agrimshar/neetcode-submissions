class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> s{};
        for (int i = 0; i < nums.size(); i++)
        {
            if (auto iter = s.find(nums[i]); iter != s.end())
            {
                return true;
            }
            s.insert(nums[i]);
        }

        return false;
    }
};
