class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> output(nums.size(), 0);
        int prod = 1;
        int zero_count = 0;

        for (int i = 0; i < nums.size(); ++i)
        {
            if (nums[i] != 0)
            {
                prod *= nums[i];
            }
            else
            {
                zero_count++;
            }
        }

        if (zero_count > 1)
        {
            return output;
        }

        for (int i = 0; i < nums.size(); ++i)
        {

            if (zero_count == 0)
            {
                output[i] = prod / nums[i];
            }
            else
            {
                if (nums[i] == 0)
                {
                    output[i] = prod;
                }
            }
        }

        return output;
    }
};
