from module.funs import factorial, factorial_rec


print("Hello World")

num = 5

a = factorial(num)
b = factorial_rec(num)

print(f"Using loop: {num}! = {a}")
print(f"Using recursion: {num}! = {b}")
