class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if char == '{' or char == '[' or char == '(':
                st.append(char)
            elif char == '}' and len(st) > 0:
                if st[-1] == '{':
                    st.pop()
                else:
                    return False
            elif char == ')' and len(st) > 0:
                if st[-1] == '(':
                    st.pop()
                else:
                    return False
            elif char == ']' and len(st) > 0:
                if st[-1] == '[':
                    st.pop()
                else:
                    return False
            else:
                return False
        
        return len(st) == 0
        