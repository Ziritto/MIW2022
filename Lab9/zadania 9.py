import math as m
import numpy as np


def projection(u,v):
    u_v = np.dot(u.T,v)
    u_u = np.dot(u.T,u)
    return (u_v/u_u)*u


def matrix_len(u):
    return m.sqrt(np.dot(u.T,u))



a=np.array([[1,0],[1,1],[0,1]])


v_list=[ [ x[i] for x in a ] for i in range(len(a[1])) ]
u_list = []
q = []

for v in v_list:
    v = np.array(v)
    sum_proj = 0
    for u_x in u_list:
        u_x = np.array(u_x)
        sum_proj+=projection(u_x, v)
    u = v - sum_proj
    u_list.append(u)
    e = (1/matrix_len(u))*u
    q.append(e)
    
q = np.array(q).T
r = np.dot(q.T,a)

new_a = np.round(np.dot(q,r),decimals=8)
        


print(q,r,new_a,sep="\n\n")
print(q,r,new_a,sep="\n\n")