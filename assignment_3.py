# Question 1: Check Discount Eligibility
total_purchase = float(input("Enter total purchase amount: $"))
if total_purchase > 100:
    final_price = total_purchase * 0.9
else:
    final_price = total_purchase
print(f"Final Price: ${final_price:.2f}")

# Question 2: Calculate Bulk Discount
num_items = int(input("Enter number of items: "))
total_price = float(input("Enter total price: $"))
if num_items > 5:
    final_price = total_price * 0.85
else:
    final_price = total_price
print(f"Final Price: ${final_price:.2f}")

# Question 3: Membership Discount
is_member = input("Is the customer a member (yes/no)? ").lower() == "yes"
total_price = float(input("Enter total price: $"))
if is_member:
    final_price = total_price * 0.8
else:
    final_price = total_price * 0.95
print(f"Discounted Price: ${final_price:.2f}")

# Question 4: Seasonal Sale
is_holiday = input("Is today a holiday (yes/no)? ").lower() == "yes"
total_price = float(input("Enter total price: $"))
if is_holiday:
    final_price = total_price * 0.75
else:
    final_price = total_price * 0.9
print(f"Price after discount: ${final_price:.2f}")

# Question 5: Buy-One-Get-One-Free
num_items = int(input("Enter number of items: "))
if num_items % 2 == 0:
    items_to_pay = num_items // 2
else:
    items_to_pay = num_items
print(f"Items to pay for: {items_to_pay}")

# Question 6: Sales Tax
price = float(input("Enter price of the item: $"))
if price > 500:
    total_price = price * 1.15
else:
    total_price = price * 1.08
print(f"Total Price after tax: ${total_price:.2f}")

# Question 7: Income Tax
annual_income = float(input("Enter annual income: $"))
if annual_income > 50000:
    tax = annual_income * 0.2
else:
    tax = annual_income * 0.1
print(f"Tax Amount: ${tax:.2f}")

# Question 8: Tax Bracket
income = float(input("Enter income: $"))
if income < 30000:
    tax_bracket = "Low Tax"
elif income < 100000:
    tax_bracket = "Medium Tax"
else:
    tax_bracket = "High Tax"
print(f"Tax Bracket: {tax_bracket}")

# Question 9: VAT Calculation
is_essential = input("Is the item essential (yes/no)? ").lower() == "yes"
price = float(input("Enter price of the item: $"))
if is_essential:
    final_price = price * 1.05
else:
    final_price = price * 1.12
print(f"Final Price: ${final_price:.2f}")

# Question 10: Tax-Free Day
tax_free = input("Is today a tax-free day (yes/no)? ").lower() == "yes"
price = float(input("Enter original price: $"))
if tax_free:
    final_price = price
else:
    final_price = price * 1.07
print(f"Total Price: ${final_price:.2f}")

# Question 11: Free Shipping
total_purchase = float(input("Enter total purchase amount: $"))
if total_purchase > 50:
    shipping_cost = 0
else:
    shipping_cost = 5
total_amount = total_purchase + shipping_cost
print(f"Total Amount including shipping: ${total_amount:.2f}")

# Question 12: Discount Code
code = input("Enter discount code: ")
price = float(input("Enter total price: $"))
if code == "DISCOUNT10":
    final_price = price * 0.9
else:
    final_price = price
print(f"Total Price: ${final_price:.2f}")

# Question 13: Tiered Discounts
total_price = float(input("Enter total price: $"))
if total_price > 100:
    final_price = total_price * 0.8
elif total_price > 50:
    final_price = total_price * 0.9
else:
    final_price = total_price
print(f"Final Price: ${final_price:.2f}")

# Question 14: Minimum Purchase Requirement
total_amount = float(input("Enter total amount: $"))
if total_amount < 20:
    print("Minimum purchase of $20 is required.")
else:
    print(f"Total Amount: ${total_amount:.2f}")

# Question 15: Loyalty Points
is_loyal = input("Is the customer a loyal member (yes/no)? ").lower() == "yes"
purchase_amount = float(input("Enter purchase amount: $"))
if is_loyal:
    loyalty_points = purchase_amount * 2
else:
    loyalty_points = purchase_amount
print(f"Loyalty Points Earned: {loyalty_points}")

# Question 16: Travel Discount
distance = float(input("Enter travel distance in miles: "))
ticket_price = float(input("Enter ticket price: $"))
if distance > 500:
    final_price = ticket_price * 0.8
else:
    final_price = ticket_price
print(f"Final Ticket Price: ${final_price:.2f}")

# Question 17: Child or Senior Discount
age = int(input("Enter passenger's age: "))
ticket_price = float(input("Enter ticket price: $"))
if age < 12 or age > 60:
    final_price = ticket_price * 0.85
else:
    final_price = ticket_price
print(f"Final Ticket Price: ${final_price:.2f}")

# Question 18: Ticket Type Pricing
is_weekend = input("Is the ticket for a weekend (yes/no)? ").lower() == "yes"
ticket_price = float(input("Enter ticket price: $"))
if is_weekend:
    final_price = ticket_price * 1.1
else:
    final_price = ticket_price
print(f"Final Ticket Price: ${final_price:.2f}")

# Question 19: Baggage Fee
baggage_weight = float(input("Enter total baggage weight (kg): "))
if baggage_weight > 20:
    extra_weight = baggage_weight - 20
    extra_fee = extra_weight * 10
else:
    extra_fee = 0
print(f"Baggage Fee: ${extra_fee:.2f}")

# Question 20: Early Bird Discount
advance_days = int(input("Enter number of days in advance the ticket was booked: "))
ticket_price = float(input("Enter ticket price: $"))
if advance_days > 30:
    final_price = ticket_price * 0.9
else:
    final_price = ticket_price
print(f"Final Ticket Price: ${final_price:.2f}")

# Question 21: Pass or Fail
score = int(input("Enter student score: "))
if score >= 40:
    print("Pass")
else:
    print("Fail")

# Question 22: Grade Assignment
score = int(input("Enter student score: "))
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")

# Question 23: Bonus Marks
completed_assignments = input("Has the student completed all assignments (yes/no)? ").lower() == "yes"
score = int(input("Enter student score: "))
if completed_assignments:
    final_score = score + 5
else:
    final_score = score
print(f"Final Score: {final_score}")

# Question 24: Attendance Eligibility
attendance = float(input("Enter student's attendance percentage: "))
if attendance >= 75:
    print("Eligible to take the exam")
else:
    print("Not eligible to take the exam")

# Question 25: Scholarship Eligibility
grade = input("Enter student's grade: ").upper()
family_income = float(input("Enter annual family income: $"))
if grade == "A" and family_income < 30000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
