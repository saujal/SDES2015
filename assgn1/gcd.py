def gcd(a,b):
    t_a=type(a)
    t_b=type(b)
    try:
        if a<0 or b<0:
            raise ValueError
        elif (t_a!=int and t_a!=long) or (t_b!=int and t_b!=long):
            raise TypeError
        else:
           if a == 0:
	    	return b
	   while b != 0:
		if a > b:
		  	a = a - b
		else:
			b = b - a
	return a
    except ValueError:
        return "ValueError"
    except TypeError:
        return "TypeError"
