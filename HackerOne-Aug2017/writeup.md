Post on BrakeSec slack - CTF channel

https://docs.google.com/document/d/1sz2-n-IiqPGDm6b6NF8ajYogTbirOddNm45Uvj3eBq8/edit

"Capture The Flag: reversing the password
Yesterday, at 08:01:00am (-0700 DST), a criminal gained access to a company’s system and changed all the administrator passwords. It then tried to remove all its traces. In the process of doing so, one of the logging systems happened to run a backup to another data center.

One of the company’s system administrator, Barry Collin, was able to retrieve part of the data, which might allow them to recover the updated password to regain access to the system. Unfortunately, the criminal noticed the running backup and shut it off immediately by killing the process. The data got corrupted and some LSBs have shifted. Barry really hopes there’s a pattern in the corrupted bits, but he hasn’t been able to figure it out… He also asks himself why they had to use a hashing algorithm to store the passwords. It makes recovery so hard.

The challenge: recover the data, reverse both passwords, and help the system administrator gain access to the system again.

Email the solution to j@hackerone.com. First 5 correct submissions get a HackerOne hoodie. You only have 2 chances and your answer has to include a proof of concept how you found the solution. CTF ends at 10pm August 12th, 2017 (PDT).

Good luck!

7b 0a 20 a0 22 65 76 e5
6e 74 22 ba 20 22 70 e1
73 73 77 ef 72 64 5f e3
68 61 6e e7 65 22 2c 8a
20 20 22 f5 73 65 72 ee
61 6d 65 a2 3a 20 22 e2
63 6f 6c ec 69 6e 22 ac
0a 20 20 a2 6f 6c 64 df
70 61 73 f3 77 6f 72 e4
22 3a 20 a2 3a 5c 78 c3
37 5c 78 c6 34 5c 6e dc
78 41 46 a9 29 37 43 dc
78 31 35 dc 78 44 30 dc
78 46 33 dc 78 44 45 e9
55 3b 22 ac 0a 20 20 a2
6e 65 77 df 70 61 73 f3
77 6f 72 e4 22 3a 20 a2
39 5c 78 c6 41 5c 78 b9
39 5c 78 c3 41 5c 78 c5
44 5c 78 c6 32 58 53 c7
5c 78 44 c4 2d 5c 78 c3
32 5c 78 b8 45 7a 48 eb
22 2c 0a a0 20 22 74 e9
6d 65 73 f4 61 6d 70 a2
3a 20 31 b5 30 31 38 b5
38 38 36 b0 30 30 30 8a
7d 0a"


Converted hex into ascii

{
  "evånt"º "pásswïrd_ãhançe",  "õserîame¢: "âcolìin"¬
  ¢oldßpasóworä": ¢:\xÃ7\xÆ4\nÜxAF©)7CÜx15ÜxD0ÜxF3ÜxDEéU;"¬
  ¢newßpasóworä": ¢9\xÆA\x¹9\xÃA\xÅD\xÆ2XSÇ\xDÄ-\xÃ2\x¸EzHë",
  "témesôamp¢: 1µ018µ886°000}



