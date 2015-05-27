from random import *
from string import lowercase

N_ROWS = 100000
f = open('benchmarks/table/files/large/unclustered.txt', 'w')
f.write('str,int,float\n')
for i in range(N_ROWS):
    a = ''.join([choice(lowercase) for j in range(6)])
    b = randint(-1000000, 1000000)
    c = round(random()*200-100, 5)
    f.write('{0},{1},{2}\n'.format(a, b, c))
f.close()
