# print("Loan principal: 1000\nMonth 1: repaid 250\nMonth 2: repaid 250\nMonth 3: repaid 500\n"
#       "The loan has been repaid!")
# import math
#
# loan_principal = int(input("Enter the loan principal:\n>"))
# a = input("""What do you want to calculate?
# type "m" – for number of monthly payments,
# type "p" – for the monthly payment:\n>""")
# if a == "m":
#     monthly_payment = int(input("Enter the monthly payment:\n>"))
#     b = loan_principal / monthly_payment
#     b = math.ceil(b)
#     print(b)
# if a == "p":
#     number_of_months = int(input("Enter the number of months:\n>"))
#     c = loan_principal / number_of_months
#     c = math.ceil(c)
#     d = loan_principal - (number_of_months - 1) * c
#     if c == d:
#         print("Your monthly payment = ", c)
#     else:
#         print("Your monthly payment = ", c, "and the last payment =", d)
# import math
# a = input("""What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:
# >""")
# if a == "n":
#     loan_principal = int(input("Enter the loan principal:\n>"))
#     monthly_payment = int(input("Enter the monthly payment:\n>"))
#     loan_interest = int(input("Enter the loan interest:\n>"))
#     i = loan_interest * 0.01 / 12
#     number_of_monthly_payments = math.log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i)
#     number_of_monthly_payments = math.ceil(number_of_monthly_payments)
#     year = number_of_monthly_payments / 12
#     month = (year - math.floor(year)) * 12
#     if math.floor(month) != 0:
#         print(f"It will take {math.floor(year)} years and {math.ceil(month)} months to repay this loan!\n")
#     else:
#         print(f"It will take {math.ceil(year)} years to repay this loan!\n")
# elif a == "a":
#     loan_principal = int(input("Enter the loan principal:\n>"))
#     number_of_periods = int(input("Enter the number of periods:\n>"))
#     loan_interest = int(input("Enter the loan interest:\n>"))
#     i = loan_interest * 0.01 / 12
#     sym = pow(1 + i, number_of_periods)
#     annual_payment = loan_principal * ((i * sym) / (sym - 1))
#     print(f"Your monthly payment = {math.ceil(annual_payment)}!")
# elif a == "p":
#     annuity_payment = float(input("Enter the annuity payment:\n>"))
#     number_of_periods = int(input("Enter the number of periods:\n>"))
#     loan_interest = float(input("Enter the loan interest:\n>"))
#     i = loan_interest * 0.01 / 12
#     sym = pow(1 + i, number_of_periods)
#     principal_loan_amount = float(annuity_payment / ((i * sym) / (sym - 1)))
#     principal_loan_amount = math.floor(principal_loan_amount)
#     print(f"Your loan principal = {principal_loan_amount}!")
import math
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--annuity", type=float)
args = parser.parse_args()


def diff(principal, periods, interest):
    i = interest * 0.01 / 12
    number_of_month = 0
    overpayment = 0
    while number_of_month != periods:
        d = math.ceil(principal / periods) + i * (principal - (principal * number_of_month) / periods)
        d = math.ceil(d)
        number_of_month += 1
        overpayment += d
        print(f"Month {number_of_month}: payment is {d}")
    print(f"Overpayment {math.ceil(overpayment - principal)}")


def n(principal, payment, interest):
    i = interest * 0.01 / 12
    number_of_monthly_payments = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    year = number_of_monthly_payments / 12
    month = (year - math.floor(year)) * 12
    if math.floor(month) != 0:
        print(f"It will take {math.floor(year)} years and {math.ceil(month)} months to repay this loan!\n")
    else:
        print(f"It will take {math.ceil(year)} years to repay this loan!\n")
        print(f"Overpayment {int(principal * (1 + interest * 0.01 / 0.75) - principal)}")


    def a(principal, periods, interest):
        i = (interest * 0.01 / 12)
        sys = pow(1 + i, periods)
        annual_payment = principal * ((i * sys) / (sys - 1))
        print(f"Your monthly payment = {math.ceil(annual_payment)}!\n")
        print(f"Overpayment {math.ceil(annual_payment) * periods - principal}")

    def p(payment, periods, interest):
        i = (interest * 0.01 / 12)
        sym = pow(1 + i, periods)
        principal_loan_amount = float(payment / ((i * sym) / (sym - 1)))
    principal_loan_amount = math.floor(principal_loan_amount)
    print(f"Your loan principal = {principal_loan_amount}!")
    print(f"Overpayment {payment * periods - principal_loan_amount}")



if args.type == "diff":
    if args.principal > 0 and args.periods > 0 and args.interest > 0:
        diff(args.principal, args.periods, args.interest)
    else:
        print("Incorrect parameters")

elif args.type == "annuity":
    if args.payment is not None and args.principal is not None:
        if args.principal > 0 and args.payment > 0 and args.interest > 0:
            n(args.principal, args.payment, args.interest)
        else:
            print("Incorrect parameters")
    elif args.principal is not None and args.periods is not None:
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            a(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters")
    elif args.payment is not None:
        if args.payment > 0 and args.periods > 0 and args.interest > 0:
            p(args.payment, args.periods, float(args.interest))
        else:
            print("Incorrect parameters")
else:
    print("Incorrect parameters")
