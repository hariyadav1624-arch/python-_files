name1=input("enter the boy name:")
name2=input("enter the girl name:")
for i in name1:
    for j in name2:
        if i==j:
           name1= name1.replace(i,"",1)
           name2= name2.replace(j,"",1)
print(name1,name2)
num=len(name1+name2)
print(num)
f=['F','L','A','M','S']
index = 0

while len(f) > 1:
    index = (index + num- 1) % len(f)
    f.pop(index)
result = {
    "F": "Friends",
    "L": "Love",
    "A": "Affection",
    "M": "Marriage",
    "E": "Enemy",
    "S": "Sister"
}
print(result[f[0]])