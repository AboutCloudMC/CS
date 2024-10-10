#3. Output The 2 x table
#4. Output the 4 x table
#5. Output the 12 x table
#6. Output every number divisible by 3 from 0 - 1000
#7. Output every number divisible by 5 from 0 - 1000
#8. Output Fizz if a number is a multiple of 3 from 0 - 1000
#9. Output buzz if a number is a multiple of 5 from 0 - 1000
#10. Output FizzBuzz if the number is a multiple of 3 and 5 from 0 - 1000
#11. Output the letters of a string
#12. Output the vowels in a string
#13. Count the number of vowels in a string
#14. Output the number of each vowel in a string

a = int(input("Input the first number: "))
b = int(input("Input the second number: "))

i=0
adiv = []
while i <= a:
    print(i)
    if a%i == 0: adiv.append(i)

i=0
bdiv = []
while i <= b:
    if a%i == 0: adiv.append(i)