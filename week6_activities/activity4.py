# factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# # Example usage
# num = 5
# print(f"Factorial of {num} is {factorial(num)}")

# data =[]

# for i in range(5):
#     data.append(lambda x, i=i*2: i*x)
#     print(data[i](10))  # This will print 10, 11, 12, 13, 14        

data=['a5', 'b2', 'c9', 'd1' ,'e7']
sorted_data = sorted(data, key=lambda x: int(x[1]))

print(sorted_data)  # Output: ['d1', 'b2', 'a5', 'e7', 'c9']


