# Python Test Questions

A set of problems to solve using Python. 

## Test 1

"You are going to be given a word. Your job is to return the 
middle character of the word. If the word's length is odd, 
return the middle character. If the word's length is even,
return the middle 2 characters."

Examples -

```python
return_middle('test') # returns 'es'
return_middle('testing') # returns 't'
return_middle('middle') # returns 'dd'
```

## Test 2

"An ATM only has 100, 50 and 20 dollar bills (USD) available to be dispensed.

Given an amount between 40 and 10000 dollars (inclusive) and assuming that the ATM wants to use as few bills as possible, determinate the minimal number of 100, 50 and 20 dollar bills the ATM needs to dispense (in that order).
"
250	[2,1,0]
260	[2,0,3]
370	[3,1,1]
Examples -
```python
withdraw(250) # returns [2,1,0]
withdraw(260) # returns [2,0,3]
withdraw(370) # returns [3,1,1]
```
## Test 3
When relying on witnesses to remember a license plate, there are some characters that are often easily confused. We want to make sure that we don't allow two people to have a license plate that is visually similar. For example, BOX and B0X.

Your Challenge
Write a function that returns true if the two provided license plates strings are visually similar. For this test, we will only need to consider the 26 English uppercase characters A to Z and the digits 0 to 9.

We won't worry about length (though your inputs will never be longer than 10 characters), and we'll ignore spaces in the comparison, so "A A A" would be considered the same as "A AA"

These characters will be considered visually equivalent

`0, O, and Q`

`1, I, and T`

`2 and Z`

`5 and S`

`8 and B`

Examples -
```python
similar_license_plates("ABC","DEF") # returns False
similar_license_plates("AAA","A A A") # returns True
similar_license_plates("BOX","B0X") # returns True
similar_license_plates("BIZ","812") # returns True
```
