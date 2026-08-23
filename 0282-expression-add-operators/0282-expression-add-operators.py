class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def backtrack(index, path, value, tail):
            # Base case: if we've consumed the entire string
            if index == len(num):
                # If the evaluated value matches the target, add the path to results
                if value == target:
                    res.append(path)
                return
            
            # Try all possible lengths for the next operand
            for i in range(index, len(num)):
                # Handle leading zero: if the operand starts with '0' and is more than 1 digit long, it's invalid
                if i > index and num[index] == '0':
                    break
                    
                curr_str = num[index:i+1]
                curr_val = int(curr_str)
                
                if index == 0:
                    # First operand: just start the path, no operators yet
                    backtrack(i + 1, curr_str, curr_val, curr_val)
                else:
                    # Try Addition (+)
                    backtrack(i + 1, path + '+' + curr_str, value + curr_val, curr_val)
                    
                    # Try Subtraction (-)
                    backtrack(i + 1, path + '-' + curr_str, value - curr_val, -curr_val)
                    
                    # Try Multiplication (*)
                    # Undo the last operation (subtract tail) and add (tail * curr_val)
                    backtrack(i + 1, path + '*' + curr_str, value - tail + (tail * curr_val), tail * curr_val)
                    
        if num:
            backtrack(0, "", 0, 0)
            
        return res