L = ['Kek', 3, 3.14]
print(len(L))

L += [4, "lol", 4.15]

print(L)

L.append('append')
L.pop(0)
del L[0]
print(L)

M = [[1, 2 ,3],
     [4 ,5 ,6],
     [7, 8, 9]]
print(M)

for i in M:
    for j in i:
        print(j, end="")
    print("\n")

col2 = [row[1] + 1 for row in M if row[1] % 2 == 0]
print(col2)

diagonal = [M[i][i] for i in range(3)]
print(diagonal)

dub = [c * 2 for c in "spam"]
print("".join(dub))

generate_matrix = [[x, x / 2, x ** 2] for x in range(-9, 20, 3) if x > 0]
print(generate_matrix)

sum_M = [sum(row) for row in M]
print(sum_M)

print(list(map(sum, M)))

print({i : sum(M[i]) for i in range(len(M))})

a = [ord(x) for x in "spaam"]
b = {ord(x) for x in "spaam"}
c = {x: ord(x) for x in "spaam"}

print(f"a: {type(a)} {a} \nb: {type(b)} {b}\nc: {type(c)} {c}")


