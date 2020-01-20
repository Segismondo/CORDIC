# CORDIC
Implementation of CORDIC algorithm in Python

Proof that is workin' fine:

https://gyazo.com/e49885e5552e10b6206660954da4a9c3


In CORDIC2.py the default number of iterations is 40 (N). It can be changed in lane 33: 

cos_val, sin_val = cordic_trig(beta)  //Default value = 40

OR

cos_val, sin_val = cordic_trig(beta, 3) //3 iterations

