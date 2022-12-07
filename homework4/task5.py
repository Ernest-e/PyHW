#  5'. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9



with open('file1.txt', 'r', encoding='utf-8') as fid:
    poli1 = fid.readline()

with open('file2.txt', 'r', encoding='utf-8') as fid:
    poli2 = fid.readline()

betas1 = poli1.replace(' ', '').split('+')
betas2 = poli2.replace(' ', '').split('+')

for i in range(len(betas1)):
    betas1[i] = betas1[i].split('*')
    betas2[i] = betas2[i].split('*')

resbetas = []
for i in range(len(betas1)):
    resbetas.append(str(int(betas1[i][0])+int(betas2[i][0])))


poli = ''
for i in range(len(resbetas)):
    poli += f'{resbetas[i]}*x**{len(resbetas)-1-i}'
    if i != len(resbetas)-1:
        poli += ' + '

with open('fileres.txt', 'w', encoding='utf-8') as fid:
    fid.write(poli)


