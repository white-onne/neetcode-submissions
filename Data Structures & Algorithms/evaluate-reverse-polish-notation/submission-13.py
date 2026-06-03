class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t.isdigit() or (len(t)>1 and t[0] == "-"):
                st.append(int(t))
            else:
                b = st.pop()
                a = st.pop()
                if t == "+":
                    st.append(a+b)
                elif t == "*":
                    st.append(a*b)
                elif t == "-":
                    st.append(a-b)
                elif t == "/":
                    st.append(int(a/b))
            print(st)
        return st[-1]