# Recipe Batches

Write a function that receives a recipe in the form of a dictionary, as well as all of the ingredients you have available to you, also in the form of a dictionary. Both of these dictionaries will have the same form, and might look something like this:

```python
{
  'eggs': 5,
  'butter': 10,
  'sugar': 8,
  'flour': 15
}
```

The keys will be the ingredient names, with their associated values being the amounts. In the case of the recipe dictionary, these amounts will represent the amount of each ingredient needed for the recipe, while in the case of the ingredients dictionary, the amounts represent the amounts available to you. 

Your function should output the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you, as indicated by the second dictionary. 

For example

```python
# should return 0 since we don't have enough butter!
recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 138, 'butter': 48, 'flour': 51 }
)
```

## Testing 

Run the test file by executing `python test_recipe_batches.py`.

You can also test your implementation manually by executing `python recipe_batches.py`.

## Hints

 * If there's a dictionary operation you aren't sure of how to perform in Python, look it up!
 * What's the _minimum_ number of loops we need to perform in order to write a working implementation?

## Steps
1. Initialize `batch_count` to 0
2. Iterate over the recipe dict and the ingredients dict at the same time.
3. Check each item amount and compare it to the item amount in the recipe, making sure we have enough of it in our ingredients dict to make the recipe at least once
    3a. If we DON'T have enough of something, break, because we can't make even one whole batch in that case
    3b. If we DO have enough, subtract the amount needed from what we have and continue
    3c. If we have enough of each ingredient to make a batch, increment `batch_count` by 1
    3d. Repeat Step 3
4. return `batch_count`


