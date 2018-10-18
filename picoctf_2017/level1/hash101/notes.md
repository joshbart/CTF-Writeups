# Challenge: Hash101
## Clue Text:
Prove your knowledge of hashes and claim a flag as your prize! Connect to the service at shell2017.picoctf.com:33628

UPDATED 16:12 EST 1 Apr.

## 14 Oct 2018
**1311** I initially assumed I was supposed to SSH into this challenge.  After having some trouble, I ended up trying `$ nc shell2017.picoctf.com 33628` and connecting.

**1415** Well, this challenge is tricky.  The `nc` connection will time out if I'm not fast enough, and there are 4 levels.  It asks for the following things:
- Convert binary string to ASCII
- Convert that ASCII to hexadecimal
- Convert the ASCII to decimal
- Input a string that produces a desired hash
- Input a string that produces a particular MD5 hash
I'll have to get a set of sites up to be able make all the conversions.

## 17 Oct 2018
**2316** So, I've managed to get a setup that should hopefully get me all the way through the challenge.
- For the binary to ASCII portion, I'm using [this site](https://www.binaryhexconverter.com/binary-to-ascii-text-converter).
- For the ASCII to hex and decimal, I'm just converting straight from binary into these using [this site](https://www.rapidtables.com/convert/number/binary-to-hex.html)
- For the backwards hash, the algorithm specified was just the sum of the binary values of data and modulus that by 16.  This would produce a single remainder.  Because the challenge used a consistent algorithm, I found that one character [from the ASCII table](http://www.asciitable.com/) that aligned with the remainder desired was all that was needed. (i.e. If a remainder of 2 was asked for, I could plug in the letter 'b' to pass the level."
- While I have not yet been able to get past level 4, I'm hopeful I'll be able to with my next attempt.  I created a rainbow table using rtgen on Kali using a lowercase alphanumeric character set.

**2342** That did it!  I had a number of problems with some of the words not being able to get past the hex conversion.  However, I finally did.  I got the binary string "0111000001100101011000010110001101100101" which converts to "peace".  "peace" converts to "7065616365" in hex and "482737218405" in decimal.  I was then asked for mod 5, so I entered "e".  Finally, I was asked to find a string for "8bb421ff32a77382408a6e1539855e40".  With rcrack, I was able to find the string r4m13.  With that, I had Success!
