from flask import Flask
from flask import request
import math

sojern_math_app = Flask(__name__)

def k_nums(is_min: bool):
    """Helper function to calculate the k min or max numbers in a list.
    
    Args:
        is_min: Boolean flag to indicate if we need to calculate min or
        max of list.

    Returns:
        Number(s) (String) comma-seperated numbers.
    """
    numbers = request.args.get('numbers')
    k = request.args.get('k', default=1, type=int)

    str_nums = numbers.split(',')
    nums = list(map(int, str_nums))

    result = list(map(str, sorted(nums, reverse=not is_min)))[:k]
    return ', '.join(result)


@sojern_math_app.route("/min")
def min():
    """Given list of numbers and a quantifier (how many), provide min number(s).
        
    Returns:
        Number(s) (String) comma-seperated numbers.
    """
    return k_nums(is_min=True)


@sojern_math_app.route("/max")
def max():
    """Given list of numbers and a quantifier (how many), provide max number(s).
        
    Returns:
        Number(s) (String) comma-seperated numbers.
    """
    return k_nums(is_min=False)

@sojern_math_app.route("/avg")
def avg():
    """Given list of numbers, calculate their average.
        
    Returns:
        Number (string) average of the list of numbers.
    """
    numbers = request.args.get('numbers')
    str_nums = numbers.split(',')
    nums = list(map(int, str_nums))
    avg = sum(nums) / len(nums)
    return str(round(avg, 3))

@sojern_math_app.route("/median")
def median():
    """Given list of numbers, calculate their median.
        
    Returns:
        Number (string) median of list of numbers.
    """
    numbers = request.args.get('numbers')
    str_nums = numbers.split(',')
    nums = list(map(int, str_nums))
    nums.sort()

    mid = (len(nums) - 1) // 2

    if mid % 2:
    	return str(nums[mid])
    else:
    	result = (nums[mid] + nums[mid + 1]) / 2
    	return str(result)

@sojern_math_app.route("/percentile")
def percentile():
    """Given list of numbers and quantifier 'q',
    compute the qth percentile of the list elements.
        
    Returns:
        Number (string) qth percentile, one number from original list.
    """
    numbers = request.args.get('numbers')
    q = request.args.get('q', type=int)
    str_nums = numbers.split(',')
    nums = list(map(int, str_nums))
    nums.sort()

    size = len(nums)
    idx = int(math.ceil((size * q) / 100)) - 1

    return str(nums[idx])
