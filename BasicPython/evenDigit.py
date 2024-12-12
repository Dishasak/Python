
n1 = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0]) %2 ==0) and (int(s[1]) % 2==0) and (int(s[2]) %2 ==0):
        #print(s(i),end=",")
        n1.append(s)
print(','.join(n1))


# n1 = []

# for i in range(100, 401):
#     s = str(i)
#     if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
#         n1.append(s)
# print(",".join(n1)) 