class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int maxPiles = -1;

        for (int i = 0; i < piles.size(); ++i)
        {
            maxPiles = max(maxPiles, piles[i]);
        }

        int l = 1;
        int r = maxPiles;
        int res = r;
        while (l <= r)
        {
            int k = (l + r) / 2;

            long long totalTime = 0;
            for (int p : piles)
            {
                totalTime += ceil((double)p / k);
            }

            if (totalTime <= h)
            {
                res = k;
                r = k - 1;
            }
            else
            {
                l = k + 1;
            }
        }
        return res;
    }
};
