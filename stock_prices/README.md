# Stock Prices

You want to write a bot that will automate the task of day-trading for you while you're going through Lambda. You decide to have your bot just focus on buying and selling Amazon stock. 

Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

## Testing

Run the test file by executing `python test_stock_prices.py`.

You can also test your implementation manually by executing `python stock_prices.py [integers_separated_by_a_single_space]`

## Hints

 For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices. 

 So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`? 


 ## Steps
 1. Traverse the list one by one, setting the first element to `current_min_price_so_far`
 2. Compare `current_min_price_so_far` to the next item. 
    2A. If next item is less than `current_min_price_so_far`, make that the new `current_min_price_so_far`
    2B. If next item is greater than `current_min_price_so_far` AND if `current_min_price_so_far` - the current price is greater than `max_profit_so_far`, subtract `current_min_price_so_far` from the current price and store the difference in `max_profit_so_far`
 3. Repeat until we reach the end of the list
 4. If the list is sorted in descending order, aka the price only drops, we need to find the least amount of loss and save it as the `max_profit_so_far`