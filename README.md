# LuhnAlgorithm
Luhn Algoritm - 101computing.net challange 

source of the challenge : https://www.101computing.net/is-my-credit-card-valid/
This repo is my solution.

HOW DOES THE LUHN ALGORITHM WORK?

~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~[ ABOUT ]~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
|                                                                     |
|            The Luhn Algorithm consists of 4 key steps:              |
|                                                                     |
|                [4,1,3,7,8,9,4,7,1,1,7,5,5,9,0,4]                    |
|                 i   i   i   i   i   i   i   i                       |
|                                                                     |
|            step 1: Double the value of every second digit           |
|                [8,1,6,7,16,9,8,7,2,1,14,5,10,9,0,4]                 |
|                 i   i   i    i   i   i    i    i                    |
|                                                                     |
|           step 2: If the result of this doubling operation is       |
|            greater than 9 (e.g 16),then add the digits              |
|                   of the product(e.g 1 + 6 = 7)                     |
|                                                                     |
|                [8,1,6,7,7,9,8,7,2,1,5,5,1,9,0,4]                    |
|                         i           i   i                           |
|                                                                     |
|            step 3: Take the sum of all the digits.                  |
| 8 + 1 + 6 + 7 + 7 + 9 + 8 + 7 + 1 + 2 + 5 + 5 + 1 + 9 + 0 + 4 = 80  |
|                                                                     |
|            step 4: If the total ends in zero,this is a valid        |
|            card number, If not,it is an invalid card number         |
|                                                                     |
~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~[ xo0ox ]~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
