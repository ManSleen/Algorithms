#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_min_price_so_far = prices[0]
    max_profit_so_far = 0

    if sorted(prices, reverse=True) == prices:
        max_profit_so_far = prices[1] - prices[0]
        for index in range(2, len(prices) - 1):
            if prices[index + 1] - prices[index] > max_profit_so_far:
                max_profit_so_far = prices[index + 1] - prices[index]
    else:
        for index in range(1, len(prices)):
            if prices[index] <= current_min_price_so_far:
                current_min_price_so_far = prices[index]
            else:
                if prices[index] - current_min_price_so_far > max_profit_so_far:
                    max_profit_so_far = prices[index] - \
                        current_min_price_so_far

    return max_profit_so_far


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
