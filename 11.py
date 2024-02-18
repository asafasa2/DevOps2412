for i in range(5):
    print("hello"+ str(i))

for i in range(10):
    print("you are number"+ str(i))


def my_printer(prefix,amout_of_times):
    for i in range(amout_of_times):
        print(prefix+str(i))





my_printer("hello",5)
my_printer("you are number",10)