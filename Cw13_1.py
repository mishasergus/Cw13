"""users = {'+111': "Tom",
        '+222' : "Bob",
        '+333' : "Taras"}
print(users["+222"])
users["+444"] = "Stas"
users["+444"] = "Bobidas"
print(users["+222"])



key = "+111"
u1 = users["+333"]
print(u1)
if key in users:
    print(users[key])
else:
    print(1234)

u2 = users.get("+444")
print(u2)


ke ='+111'
if ke in users:
    del users[ke]
print(users)


delus = users.pop('+222')
print(delus)
print(users)
stud = users.copy()
print(stud)
userlist1 = {1: "Tom", 2:"Bob"}
userlist2 = {3: "Alice", 4:"Kate"}
userlist1.update(userlist2)
print(userlist1)
print(userlist2)

for keys, value in users.items():
    print(keys,value)

for keys in users.keys():
    print(keys)"""


users = {'name':'','age':0,'comp':'','lang':[]}
while True:
    nam = input("Name: ")
    age = int(input("age: "))
    clas = input("class: ")
    comp = input("comp: ")
    n_of_l = int(input("n_of_l"))
    progr_lang = [input("progr_lang: ") for i in range(n_of_l)]
    users['name'] = nam
    users['age'] =age
    users['comp'] = comp
    users['lang'] = progr_lang
    print(users['name'],users['lang'][-1])
    print(users)