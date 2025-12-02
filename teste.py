def func(a=None,b=None,**kwargs):
    print(a,b)


arg={'a':4,'b':5,'c':10}
func(**arg)
