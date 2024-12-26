# We have to calculate Total amount after 3 years with Compund Interest

principal = 1000  # Initial amount (Principal = P)
rate = 0.05  # 5% --> 0.05 /100 = 5  (Interest = I)
years = 3 # (Time = T)

amount = principal * (1 + rate) ** years

print("Total amount after 3 years ",amount)
