class MinStack {
private:
    vector<int> stack;
    vector<int> minStack;

public:
    MinStack() {
    }
    
    void push(int val) {

        if(minStack.empty())
        {
            stack.push_back(val);
            minStack.push_back(val);
        } 
        else
        {
            stack.push_back(val);
            if (val < minStack.back())
            {
                minStack.push_back(val);
            }
            else
            {
                minStack.push_back(minStack.back());
            }
        }
        
    }
    
    void pop() {

        stack.pop_back();
        minStack.pop_back();
        
    }
    
    int top() {
        return stack.back();
    }
    
    int getMin() {
        return minStack.back();
    }
};
