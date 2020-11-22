def withdraw(amount):

    bills = [0, 0, 0]
    # Hundreds
    left_over = (amount % 100)
    bills[0] = int((amount - left_over) / 100)
    amount_left = left_over
    # Fifties
    left_over = left_over % 50
    bills[1] = int((amount_left - left_over) / 50)
    amount_left_after_50 = left_over
    # Twenties
    left_over = left_over % 20
    bills[2] = int((amount_left_after_50 - left_over) / 20)

    # Hacky code for money left over
    if left_over:
        bills[1] -= 1
        bills[2] += 3
    # Hacky code for an amount ending in 30
    if bills[1] < 0:
        bills[0] -= 1
        bills[1] = 1

    return bills
