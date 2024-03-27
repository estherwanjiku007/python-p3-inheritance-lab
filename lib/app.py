def solution(A, D):
    total_income = 0
    total_card_transactions = 0

    for i in range(len(A)):
        amount = A[i]
        date = D[i]
        year, month, _ = date.split('-')

        if amount >= 0:
            total_income += amount
        else:
            total_card_transactions += 1
    

# Calculate the total fee deductions
    fee_deductions = 5 * (12 - (total_card_transactions / 3))

# Calculate the final balance
    final_balance = total_income - fee_deductions

    return final_balance