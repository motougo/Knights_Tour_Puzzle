msg_ = []
msg_.insert(0,"Enter an equation")
msg_.insert(1,"Do you even know what numbers are? Stay focused!")
msg_.insert(2,"Yes ... an interesting math operation. You've slept through all classes, haven't you?")
msg_.insert(3,"Yeah... division by zero. Smart move...")
msg_.insert(4,"Do you want to store the result? (y / n):")
msg_.insert(5,"Do you want to continue calculations? (y / n):")
msg_.insert(6," ... lazy")
msg_.insert(7," ... very lazy")
msg_.insert(8," ... very, very lazy")
msg_.insert(9,"You are")
msg_.insert(10,"Are you sure? It is only one digit! (y / n)")
msg_.insert(11,"Don't be silly! It's just one number! Add to the memory? (y / n)")
msg_.insert(12,"Last chance! Do you really want to embarrass yourself? (y / n)")

def is_one_digit(v):
    f = float(v)
    if( f > -10 and f < 10 and f.is_integer()):
        return True
    else:
        return False

def check(v1, v2, v3):
    msg = ''

    if(is_one_digit(v1) and is_one_digit(v2) ):
        msg = msg + msg_[6]

    if((v1 == '1' or v2 == '1') and v3 == '*'):
        msg = msg + msg_[7]

    if((v1 == '0' or v2 == '0') and (v3 == '*' or v3 == '+' or v3 == '-')):
        msg = msg + msg_[8]

    if (msg != ''):
        msg = msg_[9] + msg
        print(msg)

# calc format: x operation y
# x & y: float or int
# operation: single character string

memory = 0

repeatprogram = 1
while repeatprogram:
    while True:
        print(msg_[0])
        calc = input()

        inputlist = calc.split()

        x = inputlist[0]
        oper = inputlist[1]
        y = inputlist[2]

        if ( x == 'M'):
            x = str(memory)

        if ( y == 'M'):
            y = str(memory)

        if ( not x.replace('.','',1).isnumeric() or not y.replace('.','',1).isnumeric() ):
            print(msg_[1])
        elif ( oper != '+' and oper != '-' and oper != '*' and oper != '/'):
            print(msg_[2])
        else:
            check(x,y,oper)
            if (oper == '+'):
                result = float(x) + float(y)
                break
            elif(oper == '-'):
                result = float(x) - float(y)
                break
            elif(oper == '*'):
                result = float(x) * float(y)
                break
            elif(oper == '/' and y != '0'):
                result = float(x) / float(y)
                break
            else:
                print(msg_[3])

    print(result)

    loop = 1
    while loop:
        print(msg_[4])
        answer = input()

        if (answer == 'y'):
            if( is_one_digit(result) ):
                msg_index = 10
                while True:
                    print(msg_[msg_index])
                    answer = input()
                    if ( answer == 'y'):
                        if (msg_index < 12 ):
                            msg_index += 1
                        else:
                            memory = result
                            loop = 0
                            break
                    elif ( answer == 'n'):
                        loop = 0
                        break
            else:
                memory = result
                break
        elif (answer == 'n'):
            break

    while True:
        print(msg_[5])
        answer = input()

        if(answer == 'y'):
            break   #go to beginning
        elif (answer == 'n'):
            repeatprogram = 0
            break   #End






