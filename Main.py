print('=' * 25)
print('Kalkulator sederhana')
print('1.jumlah \t [+]')
print('2.kurang \t [-]')
print('3.kali \t [*]')
print('4.bagi \t [/]')


def tambah(A,B):
    return A+B

def kurang(A,B):
    return A-B

def perkalian(A,B):
    return A*B

def pembagian(A,B):
    return A/B


A = int(input('Angka Pertama:'))# variable untuk menyimpan value int dan input dari  user
operator = input('Operator yang ingin digunakan ? ')
B = int(input('Angka Kedua:'))

print('=\t' * 25,)
print("Hasil dari kedua bilangan di atas")


#Pengkondisian untuk inputan dan operator 
if operator == '+': 
    print(A, '+', B, '=', tambah(A, B))
elif operator == '-':
    print(A, '-', B,'=',kurang(A, B))
elif operator == '*':
    print(A,'*', B,'=',perkalian(A, B))
elif operator == '/':
    print(A,'/', B, '=',pembagian(A, B))
else:
    print("Inputan salah")
    
    
    
