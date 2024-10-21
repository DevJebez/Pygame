import os 
print('PRESS ONE FOR SPACE INVADERS')
print('PRESS TWO FOR CONNECT FOUR')
ch=int(input('ENTER YOUR CHOICE : '))
if ch==2:
    for file in os.listdir('E:\JEBEZ\SCHOOL PVM\CSC PROJECT\csc project'):
        if file.startswith('connect_four'):
            exfile=os.path.join('E:\JEBEZ\SCHOOL PVM\CSC PROJECT\csc project',file)
            exec(open(exfile).read())
            break
elif ch==1:
    for file in os.listdir('E:\JEBEZ\SCHOOL PVM\CSC PROJECT\csc project'):
        if file.startswith('main'):
            exfile=os.path.join('E:\JEBEZ\SCHOOL PVM\CSC PROJECT\csc project',file)
            exec(open(exfile).read())
            break

        

