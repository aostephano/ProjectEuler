def isPuthTriplet(a, b, c):
    if a < b < c:
        if a * a + b * b == c * c:
            return True
        else:
            return False
    else:
        return False
#
# for a in range(0, 1000):
#     for b in range(0, 1000):
#         for c in range(0, 1000):
#             if isPuthTriplet(a, b, c):
#                 if a + b + c == 1000:
#                     print("Found:", "a:", a, "b:", b, "c:", c)
#                     break

print(200*375*425)