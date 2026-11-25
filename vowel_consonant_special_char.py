a='hel@ lo'
v=['a','e','i','o','u']
vowel=[]
con=[]
special=[]
v_count=0
c_count=0
s_count=0
for ch in a:
    if ch in v:
        v_count+=1
        vowel.append(ch)
    elif ((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
        c_count+=1
        con.append(ch)
    else:
        s_count+=1
        special.append(ch)
        
print(vowel)
print(con)
print(special)
print("Vowel count:",v_count)
print("constant count:",c_count)
print("special character count:",s_count)