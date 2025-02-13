# Definition:
# Arbitrary keyword arguments allow a function to accept an unlimited number of keyword

# Example 2:


def student_info(**kwargs):
    for key, value in kwargs.items():
        # print(Ritesh, 21, Python)
        # print(Divyanka, 20, Java)
        # print(Siddhika, 18, Python)
        
        print(f"{key}: {value}")

student_info(name="David", age=22, course="Python")
