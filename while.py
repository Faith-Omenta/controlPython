# Write a Python program that takes a list of strings as input and outputs the 
# number of times each string appears in the list, using a dictionary and conditional
# statements.
def CountFrequency(my_list):
    count = {}
    for i in [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]:
        count[i] = count.get(i, 0) + 1
    return count
if __name__ == "__main__":
    my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
    print(CountFrequency(my_list))


# Write a Python program that takes a list of numbers as input and outputs the 
# median of the numbers
def cal_median(nums):
  nums.sort()
  n = len(nums)
  m = n // 2
  if n % 2 == 0:
    return (nums[m - 1] + nums[m]) / 2
  else:
    return nums[m]
print(cal_median([1,2,3,4,5]))

# Write a Python program that takes a list of numbers as input and outputs the 
# second largest number in the list using conditional statements and a for loop.
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Second largest element is:",a[n-2])

# Write a Python program that takes a year as input and determines if it is a leap 
# year.
year=int(input("Enter the year:"))
if yr %100==0:
    if yr % 400==0:
        print("year is leap year")
    else:
        print("year is not year")
    if yr % 400==0:
        print("year is not leap year")
    else:
        print("year is not a leap year")

# Write a Python program that takes a string as input and checks if it is a palindrome
# (reads the same forwards and backwards), ignoring spaces and punctuation.
x="racecar"
w=""
for i in x:
    w=i+w
if (x==w):
    print("isPalindrome")
else:
    print("is not palindrome")