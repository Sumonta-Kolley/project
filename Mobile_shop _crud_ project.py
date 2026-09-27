# 6. Multiplication Table
def multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

num = int(input("Enter a number: "))
multiplication_table(num)