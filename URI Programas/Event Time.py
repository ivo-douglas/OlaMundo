# coding: utf-8

a=(293654//60//60)%24

day_start = int(input("Dia "))

t1a, t1b, t1c = map(int, input().split(":"))

day_end = int(input("Dia "))

t2a, t2b, t2c = map(int, input().split(":"))

day_end_minus_day_start = day_end - day_start
days_to_seconds = day_end_minus_day_start*24*60*60

ta = (t1a-t2a)*3600
if ta < 0:
    ta = ta*-1
    
tb = (t1b-t2b)*60
if tb < 0:
    tb = tb*-1

tc = (t1c-t2c)
if tc < 0:
    tc = tc*-1

total_seconds = ta + tb + tc

if total_seconds < 0:
    total_seconds = total_seconds*-1


final_seconds = days_to_seconds - total_seconds

if final_seconds < 0:
    final_seconds = final_seconds*-1

W = final_seconds//60//60//24
X = (final_seconds//60//60)%24
Y = X//60%60%24
Z = X%3600%24

print(W, "dia(s)")
print(X, "hora(s)")
print(Y, "minuto(s)")
print(Z, "segundo(s)")