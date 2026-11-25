a='hel@ lo'
v=['a','e','i','o','u']
vowel=[]
con=[]
special=[]
for ch in a:
    if ch in v:
        vowel.append(ch)
    elif ((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
        con.append(ch)
    else:
        special.append(ch)
        
print(vowel)
print(con)
print(special)