class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> answer;
        for (int i = 0; i < numbers.size(); ++i)
        {
            for(int j = i; j < numbers.size(); ++j)
            {
                if (numbers[i] + numbers[j] == target)
                {
                    answer.push_back(i + 1);
                    answer.push_back(j + 1);
                    return answer;
                }
            }
        }
    }
};
