# print(10 % 3)
# print (-10 % 3)

# calculate time on clock 

current_time = 10  # 10:00 am
hr_later = 8
time_on_clock = (current_time + hr_later) % 12 # formula for calculating time on clock (12 hr clock)
print ("time on clock after 8 hr's is ", time_on_clock)

# Even or Odd
number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
    