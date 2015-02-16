from gcd import gcd
def gcd_test():
    assert gcd(48,64)==16
    assert gcd(-48,-64)== "ValueError"
    assert gcd(48.1,64) == "TypeError"
    
if __name__=="__main__":
    gcd_test()
