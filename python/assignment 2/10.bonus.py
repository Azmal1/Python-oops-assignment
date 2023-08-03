
# 10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
def calculate_bonus(salary, years_of_service):
    bonus = 0.05 * salary  # 5% bonus
    if years_of_service > 5:
        return bonus
    else:
        return 0


if __name__ == "__main__":
    salary = float(input("Enter your salary: "))
    years_of_service = int(input("Enter your years of service: "))

    net_bonus = calculate_bonus(salary, years_of_service)
    print(f"Net bonus amount: {net_bonus:.2f}")

