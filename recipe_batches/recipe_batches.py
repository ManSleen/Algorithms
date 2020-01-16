#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batch_count = 0
    arr = []
    for key in recipe:
        print("key: ", key)
        if key in ingredients:
            amount_needed = recipe[key]
            amount_we_have = ingredients[key]
            batches = 0
            if amount_needed <= amount_we_have:
                while amount_needed <= amount_we_have:
                    amount_we_have -= amount_needed
                    batches += 1
                    print("amount we have left:", amount_we_have)
                    print("batches:", batches)
            else:
                break

            arr.append(batches)
        else:
            arr.append(0)
    print(arr)
    batch_count = min(arr)

    return batch_count


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 300, 'butter': 50, 'flour': 300}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
