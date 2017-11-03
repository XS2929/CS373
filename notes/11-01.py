# -----------
# Wed, 1 Nov
# -----------

a = [2, 3, 4]
print(a[1:2]) # [3]
print(a[1:1]) # []
print(a[1:3]) # [3, 4]
print(a[0:3]) # [2, 3, 4]
print(a[:])   # [2, 3, 4]
print(a[1:])  # [3, 4]
print(a[:2])  # [2, 3]

print(a[:] is a[:]) # false

a = (2, 3, 4)
print(a[:] is a[:]) # true

a = "abc"
print(a[:] is a[:]) # true

    -3 -2 -1
     0  1  2
a = [2, 3, 4]
print(a[-1])  # 4

a = [...]
print(a[2 : 5 : 2]) # skip elements

print(a[::-1]) # reverse list
