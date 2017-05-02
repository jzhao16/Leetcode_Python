class Solution(object):
        def reverse(self,x):
            y = str(x)
            if y[0] == '-':
                z = int('-'+y[1:][::-1])
            else:
                z = int(y[::-1])
            return z * (abs(z) < 2**31)
           
        
