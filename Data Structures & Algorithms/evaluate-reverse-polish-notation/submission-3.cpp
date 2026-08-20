class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> values;


        for (int i = 0; i < tokens.size(); ++i)
        {
            if (tokens[i] == "+")
            {
                int secondValue = values.top();
                values.pop();
                int firstValue = values.top();
                values.pop();

                values.push(firstValue + secondValue);
            } 
            else if (tokens[i] == "-")
            {
                int secondValue = values.top();
                values.pop();
                int firstValue = values.top();
                values.pop();

                values.push(firstValue - secondValue);
            } 
            else if (tokens[i] == "/")
            {
                int secondValue = values.top();
                values.pop();
                int firstValue = values.top();
                values.pop();

                values.push(firstValue / secondValue);
            } 
            else if (tokens[i] == "*")
            {
                int secondValue = values.top();
                values.pop();
                int firstValue = values.top();
                values.pop();

                values.push(firstValue * secondValue);
            }
            else
            {
                values.push(stoi(tokens[i]));
            }
        }

        return values.top();

    }
};
