if __name__ == '__main__':
    annual_interest = 15  # annual interest in %
    annual_business_days = 317  # amount of days you will get interest in a year

    # daily interest divided by 100 soo it's no longer a percentage
    daily_interest = annual_interest / annual_business_days / 100

    account_money = 0  # amount of money you have in your account at the start
    monthly_increase = 5000  # amount of money you will add to your account every month
    stop_at = 1500000  # amount of money you want to reach

    daily_interest_result = 0
    days = 0

    # 1. Calculate the number of days to reach the stop_at
    while account_money < stop_at:
        if days % 7 != 0:
            daily_interest_result = account_money * daily_interest
            account_money += daily_interest_result

        if days % 30 == 0:
            account_money += monthly_increase
        days += 1

    # 2. Print the result
    print(f'You will reach {stop_at} in {days} days.')
    print(f'You will reach {stop_at} in {days/30} months.')
    print(f'You will reach {stop_at} in {days/365} years.')
    print()
    print(f'Your daily gain at this point is: {daily_interest_result}.')
    print(f'Your monthly gain at this point is: {daily_interest_result * 26}.')
    print(f'Your yearly gain at this point is: {daily_interest_result * 26 * 12}.')

