from random import *
from string import lowercase

N_ROWS = 100000
f = open('benchmarks/table/files/large/clustered2.txt', 'w')
f.write('str,int,float\n')
for i in range(N_ROWS):
    a = ''.join([choice(lowercase) for j in range(2)])
    b = randint(-100, 100)
    c = round(random()*20-10, 1)
    f.write('{0},{1},{2}\n'.format(a, b, c))
f.close()
