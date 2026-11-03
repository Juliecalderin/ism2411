# SELF-ASSESSMENT
# Q2. What apply_discount(price, tier) does:
# It takes a price (a number) and a tier (a string: "gold", "silver",
# or "bronze"). It works out the discount for that tier (gold 15%,
# silver 10%, bronze 5%, anything else 0%) and returns the price after
# the discount is taken off. A colleague could use it without reading
# the code because the name, inputs, and return value are clear.
#
# AI DISCLOSURE:
# I used Google's AI Overview (Gemini) to look up the meaning of a
# term/error. I wrote the code myself.

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0.0
    return price * (1 - discount)


print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


# --- Exercise 3 ---
discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${discounted + calculate_tax(discounted, 0.07):.2f}")


def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    return discounted + calculate_tax(discounted, tax_rate)


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---


# --- Exercise 6 ---
x = 100  # global variable


def double_it():
    x = 999  # local variable, different from the global x
    return x * 2


print(x)            # 100
print(double_it())  # 1998
print(x)            # 100 (global x never changed)

# Scope explanation: a variable made inside a function is local, so it
# only exists while that function runs. double_it() has its own x (999),
# which hides the global x (100) inside the function but doesn't change
# it. That's why the global x is still 100 after the call.
