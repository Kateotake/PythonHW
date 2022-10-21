# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# # Получение данных из файла

def read_file(file):
    with open(str(file), 'r') as data:
        st = data.read()
    return st

st1 = read_file('hello1.txt')
print(st1)
st2 = read_file('hello2.txt')
print(st2)



# преобразовываю многочлен (коэффициент, степень)

def newst(st):
    st = st.replace(' = 0', '') #заменяет 0 на ничего
    st = st.replace('*', ' ')
    st = st.replace('^', ' ')
    st = st.split(' + ')
    st = [char.split() for char in st]
    for i in st:
        if i[0] == 'x': i.insert(0, 1) # добавь на 0ю поз -1
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)

    st = [tuple(int(n) for n in j if n != 'x') for j in st]
    print(st)
    return st

stn1 = newst(st1)
stn2 = newst(st2)

# Сумма значений (коэф1 + коэф2, степень)
lenn =0
if len(stn1) > len(stn2):
    lenn = len(stn1)
else:
    lenn = len(stn2)
st3 = []

# почему-то вот так он выводит список :

st3.append((stn1[0][0]+stn2[0][0], stn1[0][1]))
st3.append((stn1[1][0]+stn2[1][0], stn1[1][1]))
print(st3)

# а с помощью for не выводит..

for i in range(len(stn1)):
    for j in range(len(stn2)+1):
        if stn1[i][1] == stn2[j][1]:
                k = stn1[i][0]+stn2[j][0]
                m = stn1[i][1]
                st3 = st3.append((k, m)) 
print(st3)

# все, на этом мой мозг умер