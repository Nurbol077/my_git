#task 1

# num = int(input("; "))
# if num % 2==0:
#     print("Четное")
# else:
#     print("Нечетное")

#task 2

# numm= map(int,input("; ").split())
# maxx = max(numm)
# print(maxx)

#task 3

# numm = int(input('; '))
# for i in range(1,11):
#     print(f'{numm} * {i} = {numm * i}')

#task 4
# a = input("; ")
# numm = "а, е, и, о, у, э, ы, ю, я"
# count = 0
# for i in a:
#     if i in numm:
#         count+=1
# print(count)
#

#task 5

# n = int(input('; '))
# factoriall = 1
# for i in range(1,n+1):
#     factoriall *= i
# print(factoriall)

#task 6

# a= input(': ')
# if a == a[::-1]:
#     print("палиндром")
# else:
#     print('Непалиндром')

#task 7

# a= map(int,input("; ").split())
# b = sum(a)
# print(b)

#task 8

# a = input("; ")
# print(len(a))

#task 9

# def square(num):
#     return num ** 2
# print(square(5))

#task 10

# def minimum(a,b):
#     return min(a,b)
# print(minimum(2,3))

#task 11

# def is_even(a):
#     if a % 2==0:
#         print("True")
#     else:
#         print("False")
# is_even(2)

#task 12
# def count_vowels(b):
#     numm = "ayieuo"
#     count = 0
#     for i in b:
#         if i in numm:
#             count+=1
#     return count
#
# text = "Hello, world"
# print(count_vowels(text))

#task 13

# def factoriall(n):
#     num=1
#     for i in range(1,n+1):
#         num *=i
#     return num
# print(factoriall(5))

#task 14

# def average(numbers):
#     return sum(numbers) / len(numbers)
# numbers= [1,2,3,4,5,6]
# print(average(numbers))

#task 15
# def is_palindrome(p):
#     return p == p[::-1]
# print(is_palindrome("madam"))
# print(is_palindrome("Nurbol"))

#task 16

# def count_words(s):
#     return len(s)
# print(count_words("Nurbol"))
