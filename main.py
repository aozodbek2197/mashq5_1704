# 1-mashq
nums = [1, 2, 2, 3]
print(list(set(nums)))
# 2-mashq
text = "apple banana apple"
words = text.split()

d = {}
for w in words:
    d[w] = d.get(w, 0) + 1

print(d)
# 3-mashq
nums = [1, 2, 2, 3, 2]

d = {}
for n in nums:
    d[n] = d.get(n, 0) + 1

print(max(d, key=d.get))
# 4-mashq
nums = [1, 2, 3, 4]
print([x for x in nums if x % 2 == 0])
# 5-mashq
t = (5, 1, 9)
print(max(t))
