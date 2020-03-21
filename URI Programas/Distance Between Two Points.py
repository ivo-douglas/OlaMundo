# coding: utf-8


x1_str, y1_str = map(float, input().split())
x2_str, y2_str = map(float, input().split())


x1 = float("{:.1f}".format(x1_str))

y1 = float("{:.1f}".format(y1_str))

x2 = float("{:.1f}".format(x2_str))

y2 = float("{:.1f}".format(y2_str))

print("{:.4f}".format(((x2-x1)**2+(y2-y1)**2)**0.5))