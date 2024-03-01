def func1():
    global f_counter
    f_counter+=1
    print(f_counter)
    func2()
def func2():
    global f_counter
    f_counter+=1
    print(f_counter)
    func1()

f_counter=0
func1()
