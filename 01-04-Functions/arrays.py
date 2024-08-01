'''
cara lain untuk comment
bisa untuk beberapa paragraf
'''
# assign a list
list = ['soobin', 'beomgyu', 'yeonjun', 'taehyun', 'kai'] # tipe list

# mencampurkan beberapa tipe data
list2 = ['2', 'beomgyu', '1.8']

print(list2[1]) # untuk menampilkan 1 item saja

# change
list[1] = 'pd nim'
print(list)

# sort a list
# mengurutkan sesuai alfabetnya
list.sort()
print(list)

# assign a tuple
# tuple is unchangeable
tupple = ('soobin', 'rabbit', 'cute')

# try to change tuple
# tuple[1] = 'bunny' # will be error

# assign a set
# tidak urut, tidak bisa diubah, berubah secara random

set = {'soobin', 'beomgyu', 'yeonjun'}

for x in set:
    print(x)

# assign a dictionary
# punya yang namanya item sama value
# dictionary = {idKey:Value}
dict = {"nama":"soobin", "status":"my boyfriend"}
print(dict["status"])