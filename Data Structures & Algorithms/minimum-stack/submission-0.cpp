class MinStack {
public:
    vector<int> vec;

    MinStack() {
    }
    
    void push(int val) {

        vec.push_back(val);
        
    }
    
    void pop() {

        vec.pop_back();
        
    }
    
    int top() {
        return vec.back();
    }
    
    int getMin() {
        int minValue = INT_MAX;
        for (int i = 0; i < vec.size(); ++i)
        {
            if (vec[i] < minValue)
            {
                minValue = vec[i];
            }
        }
        return minValue;
    }
};
