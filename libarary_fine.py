"""
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e. fine=0) 
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, 15(difference in date) 
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the  500*(difference in month)
If the book is returned after the calendar year in which it was expected, there is a fixed fine of . 10000

""""



import sys

def calculate_fine(actual_date, expected_date):
    actual_day, actual_month, actual_year = map(int, actual_date.split())
    expected_day, expected_month, expected_year = map(int, expected_date.split())
    
    if actual_year < expected_year or (actual_year == expected_year and actual_month < expected_month) or (actual_year == expected_year and actual_month == expected_month and actual_day <= expected_day):
        return 0  # No fine
    
    if actual_year > expected_year:
        return 10000  # Fixed fine if returned in a different year
    
    if actual_month > expected_month:
        return 500 * (actual_month - expected_month)  # Fine based on months
    
    return 15 * (actual_day - expected_day)  # Fine based on days

# Example usage
actual_date = sys.stdin.readline().strip()
expected_date = sys.stdin.readline().strip()
fine = calculate_fine(actual_date, expected_date)
print(fine)
