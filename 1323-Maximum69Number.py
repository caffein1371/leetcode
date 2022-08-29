class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = num
        x = [str(a) for a in str(num)]
        #print(x)  
        for i in range(len(x)):
            if x[i]=="6":
                x[i]="9"
                break
        #print ("".join(x))
        #print (max(temp,int("".join(x))))
        return max(temp,int("".join(x)))