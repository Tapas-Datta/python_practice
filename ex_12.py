
correct_pin =12345
limit = 0
while limit < 3:
    user = int(input("Enter your pin number: "))
    if user == correct_pin:
        print("you have done good and correct pin.")
        break
    elif user != correct_pin:
        print("you have done bad and wrong pin.")
        limit = limit + 1
    if limit == 3:
        print(" you are totally done")
        break


correct_pin = 12345
balance  = 10000
limit =  0
while limit < 3:
    user  = int(input("Enter your pin number : "))
    if user == correct_pin:
        print("Correct Pin ,congratulation")
        wish= int(input("Enter Check Balance:  Withdraw Money/Deposit Money/ Exit: "))
        if wish == 1:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Invalid withdrawal amount")
            elif amount > balance:
                print("Insufficient balance")
            else:
                balance -= amount
            print(f"you withdraw amount is {amount} and you total balance is now {balance}")
        elif wish == 2:
            amount = int(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Invalid deposit amount")
            else:
                balance += amount
                print(f"you deposit amount is {amount} and you total balance is now {balance}")
        elif wish == 3:
            print("Thank you for using our service,stay tuned ")
            exit()
    elif user != correct_pin:
        limit += 1
        print(f"Wrong Pin , try again anf your limit left {3-limit}")
        if limit == 3:
            print("Thank you you have done max ,contact with the bank ")

def age_calculator(current_year,birth_year):
    age = current_year - birth_year
    if age < 18:
        return "you are minor"
    else:
        return "you are major"
year_of_birth = int(input("Enter your birth year: "))
year_of_now = int(input("Enter your current year: "))
print(age_calculator(year_of_now,year_of_birth,))



def grade_calculator(marks):
    if 100 >= marks >= 90:
        return "A+"
    elif 89 >= marks >= 80:
        return "A"
    elif 79 >= marks >= 70:
        return "B"
    elif 69 >= marks >= 60:
        return "C"
    elif 59 >= marks >= 40:
        return "D"
    elif 0 <= marks < 40:
        return "F"
    else:
        return "Marks are not valid"
user_grade = int(input("Enter your marks: "))
print(grade_calculator(user_grade))


def salary_calculator(basic_salary):
    if basic_salary >= 50000:
        bonus = (basic_salary * 20) / 100
        total_salary = basic_salary + bonus
        return total_salary
    elif 49999 > basic_salary >= 30000:
        bonus = (basic_salary * 15) / 100
        total_salary = basic_salary + bonus
        return total_salary
    elif 29999 > basic_salary >= 20000:
        bonus = (basic_salary * 10) / 100
        total_salary = basic_salary + bonus
        return total_salary
    elif 0 < basic_salary < 20000:
        bonus = (basic_salary * 5) / 100
        total_salary = basic_salary + bonus
        return total_salary
    else:
        return "negative is not calculated"
manager = int(input("Enter your stuff salary: "))
print(salary_calculator(manager))



def loan_eligibility(age, salary, credit_score):
Requirements:
1. Age 18-এর নিচে হলে Not Eligible।
2. Salary 20,000-এর নিচে হলে Not Eligible।
3. Credit Score 750 বা বেশি হলে Excellent।
4. Credit Score 650–749 হলে Good।
5. Credit Score 600–649 হলে Average।
6. Credit Score 600-এর নিচে হলে Rejected।
Input Example:
Enter your age: 25
Enter your monthly salary: 35000
# Enter your credit score: 780

def loan_eligibility(age, salary, credit_score):

    if age < 18:
        return "Not Eligible: Age must be 18 or above"
    elif salary < 20000:
        return "Not Eligible: Salary is too low"
    elif credit_score < 0 or credit_score > 850:
        return "Invalid Credit Score"
    elif credit_score >= 750:
        return "Excellent"
    elif 650 <= credit_score < 750:
        return "Good"
    elif 600 <= credit_score < 650:
        return "Average"
    else:
        return "Rejected"
user = int(input("Enter your age: "))
salary_your = int(input("Enter your salary: "))
your_credit_score = int(input("Enter your credit score: "))
print(loan_eligibility(user, salary_your, your_credit_score))


    




