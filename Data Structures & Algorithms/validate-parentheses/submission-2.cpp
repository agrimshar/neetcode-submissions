class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;

        for (int i = 0; i < s.length(); ++i)
        {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[')
            {
                stack.push(s[i]);
                continue;
            }

            if (stack.empty())
            {
                return false;
            }

            if (s[i] == ')')
            {
                if (stack.top() != '(')
                {
                    return false;
                }
                else
                {
                    stack.pop();
                }
            }
            if (s[i] == '}')
            {
                if (stack.top() != '{')
                {
                    return false;
                }
                else
                {
                    stack.pop();
                }
            }
            if (s[i] == ']')
            {
                if (stack.top() != '[')
                {
                    return false;
                }
                else
                {
                    stack.pop();
                }
            }
        }

        if (!stack.empty())
        {
            return false;
        }
        
        return true;
    }
};
