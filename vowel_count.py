n=str(input())
#vowel_list=list(map(str,['a','e','i','o','u']))
vowel_list=['a','e','i','o','u','A','E','I','O','U']
vowel_count=0
constant_count=0
for i in n:
    if i in vowel_list:
        vowel_count+=1
    else:
        constant_count+=1
print(vowel_count)
print(constant_count)