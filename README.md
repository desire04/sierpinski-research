# sierpinski-research
The file isCow.py contains 3 functions. The first function takes in an index i, a prime number p, and its corresponding Cow sequence period in mod p, and returns the corresponding
cow sequence number at that index converted to mod p. The 2nd function takes in a factor of 24/36, the number generated from the first function, and the prime number used in the 
first function, and returns the number used with the factor to make a covering. The 3rd function simply takes in a number and a mod and returns the number reduced to the mod.
Overall, the functions in this file are useful to backtrack when an index in the cow sequence which also represents a Sierpinski number is generated. The functions help one backtrack
to the very beginning to generate the covering set that produces the sierpinski number in question. 
