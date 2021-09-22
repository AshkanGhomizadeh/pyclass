#Ashkan Ghomizadeh Thursdays 14:00 - 18:00
#Jomleye Fenglishe kamel gerefte shavad va kootah chap shavad
ebarat = input("Ebarate khod ra be soorate Fenglishe kamel vared konid.\n")
vowels = {"a", "e", "i", "o", "u"}
ebarate_nahayi = ""
for harf in ebarat:
    if harf in vowels:
        harf = ""
    else:
        pass
    ebarate_nahayi = ebarate_nahayi + harf
print(ebarate_nahayi)
