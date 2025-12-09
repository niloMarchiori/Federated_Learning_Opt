class Teste():
    def __init__(self,args):
        self.atributo=None
        self.__dict__.update(args)
class Teste2():
    def __init__(self,args):
        self.atributo='c'
        self.__dict__.update(args)
args={"atributo":"b"}
a=[Teste,Teste2]
b=a[0](args)
c=a[1]({})

a=None
for i in a:
    print(1)