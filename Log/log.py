a=open('LOG.txt','a')


def wr(*args):
    print(args)
    for i in args:
        a.write(str(i)+'\n')