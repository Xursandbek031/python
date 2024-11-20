# def info(i,f,y,j,e,t):
#     user_info={
#         'ism':i,
#         'familiya':f,
#         'yili':y,
#         'joyi':j,
#         'email':e,
#         'tel_nomer':t
#     }
#     return user_info


# ism = input("Ismi: ")
# familiya = input("Familiyasi: ")
# tyil = int(input("Tug'ilgan yili: "))
# tjoy = input("Tug'ilgan joyi: ")
# email = input("Email: ")
# telefon = input("Telefon raqami: ")
# a=info(ism,familiya,tyil,tjoy,email,telefon)
# print(a)


# def kattasi(a,b,c):
#     max=a
#     if b>=max:
#         max=b
#     if c>=max:
#         max=c
#     return max
# x=int(input('x='))
# y=int(input('y='))
# z=int(input('z='))
# print("Eng katta son",kattasi(x,y,z))


# from math import *
# def aylana_info(r):
#     aylana={
#         'radius':r,
#         'diametr':2*r,
#         'Uzunligi':2*r*pi,
#         'Yuzi':pi*r*r
#     }
#     return aylana
# r=int(input('r='))
# aa=aylana_info(r)
# for k,q in aa.items():
#     print(f"{k}={q}")


# def tub_sonlar_top(a,b):
#     tub_sonlar=[]
#     for i in range(a,b+1):
#         tub=True
#         if i==1:
#             tub=False
#         if i==2:
#             tub=True
#         else:
#             for x in range(2,i):
#                 if i%x==0:
#                     tub=False
#         if tub:
#             tub_sonlar.append(i)
#     return tub_sonlar

# a=int(input("a="))
# b=int(input("b="))
# print(tub_sonlar_top(a,b))


def talaba_info(familiya,ism,yoshi):
    talaba_info={
        'familiya':familiya,
        'ism':ism,
        'yoshi':yoshi
    }
    return talaba_info

f=input("familiya: ")
i=input("ism")
y=input("yoshi")
print(talaba_info(f,i,y))