num="54325"
digit="5"
Max_num=""
for i in range(len(num)):
    if(num[i]==digit):
        new_num= num[:i]+num[i+1:]
        if(new_num>Max_num):
            Max_num=new_num
            print(Max_num)