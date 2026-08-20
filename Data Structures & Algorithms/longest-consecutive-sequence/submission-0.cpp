class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        int sequence = 0;
        int currentSequence = 1;

        sort(nums.begin(), nums.end());

        for(int i = 0; i < nums.size(); ++i)
        {
            if (i == nums.size() - 1) 
            {
                if (currentSequence > sequence)
                {
                    sequence = currentSequence;
                }
            }
            else if (nums[i+1] - nums[i] == 1)
            {
                ++currentSequence;
            }
            else if (nums[i+1] - nums[i] == 0)
            {
                continue;
            }
            else 
            {
                if (currentSequence > sequence)
                {
                    sequence = currentSequence;
                }
                currentSequence = 1;
            }
        }


        return sequence;
    }
};
