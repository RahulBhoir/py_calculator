from tkinter import*
import re
import cmath

########## quadratic ##########


def quadratic():
    num = str(e1.get())
    num = num.split('.')

    a = float(num[0])
    b = float(num[1])
    c = float(num[2])

    d = (b**2) - (4*a*c)        # calculate the discriminant

    sol1 = (-b-cmath.sqrt(d))/(2*a)     # find two solutions
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    e1.delete(0, END)
    e1.insert(0, (sol1, sol2))

############ factorial ##################


def fact():
    num = int(e1.get())
    factorial = 1
    if num < 0:
        e1.insert(0, "error")
    elif num == 0:
        e1.insert(0, "1")
    else:
        for i in range(1, num + 1):
            factorial = factorial*i

    e1.delete(0, END)
    e1.insert(0, factorial)
    return
########## buttons ############


def button(number):
    e1.insert(100, number)
    return

######### answer button ###############


def answer():
    num1 = e1.get()
    e1.delete(0, END)
    e1.insert(0, eval(num1))
    return

############# clear screen ###########


def clear_all():
    e1.delete(0, END)
    return

########### Square function ###########


def power():
    num = str(e1.get())
    num = num.split('.')

    a = float(num[0])
    b = float(num[1])

    num1 = a**b
    e1.delete(0, END)
    e1.insert(0, num1)
    return


############## front-end ##############
root = Tk()
root.title("Calculator")

#########  entry bar ##############
e1 = Entry(root, font=('arial', 20, 'bold'), insertwidth=4,
           bg='light blue', bd=35, justify='center')
e1.grid(columnspan=4)

############# BUTTONS ####################

bclr = Button(root, text="clr", padx=10, bd=8, fg="black",
              font=('arial', 20, 'bold'), command=clear_all)
bclr.grid(row=1, column=3)

bsq = Button(root, text="pow", padx=10, bd=8, fg="black",
             font=('arial', 20, 'bold'), command=power)
bsq.grid(row=1, column=1)

bfact = Button(root, text="x!", padx=20, bd=8, fg="black",
               font=('arial', 20, 'bold'), command=fact)
bfact.grid(row=1, column=2)

bquad = Button(root, text="quad", padx=-10, bd=8, fg="black",
               font=('arial', 20, 'bold'), command=quadratic)
bquad.grid(row=1, column=0)

# row 5
b1 = Button(root, text="1", padx=20, bd=8, fg="black", font=(
    'arial', 20, 'bold'), command=lambda: button(1))
b1.grid(row=5, column=0)

b2 = Button(root, text="2", padx=20, bd=8, fg="black", font=(
    'arial', 20, 'bold'), command=lambda: button(2))
b2.grid(row=5, column=1)

b3 = Button(root, text="3", padx=20, bd=8, fg="black", font=(
    'arial', 20, 'bold'), command=lambda: button(3))
b3.grid(row=5, column=2)

bmulti = Button(root, text="*", padx=20, bd=8, fg="black",
                font=('arial', 20, 'bold'), command=lambda: button("*"))
bmulti.grid(row=5, column=3)
# row 4
b4 = Button(root, text="4", padx=20, bd=8, fg="black", font=(
    'arial', 20, 'bold'), command=lambda: button(4))
b4.grid(row=4, column=0)

b5 = Button(root, text="5", padx=20, bd=8, fg="black", font=(
    'arial', 20, 'bold'), command=lambda: button(5))
b5.grid(row=4, column=1)

b6 = Button(root, text="6", padx=20, bd=8, fg="black", font=(
    'arial', 20, 'bold'), command=lambda: button(6))
b6.grid(row=4, column=2)

bsub = Button(root, text="-", padx=20, bd=8, fg="black",
              font=('arial', 20, 'bold'), command=lambda: button("-"))
bsub.grid(row=4, column=3)
# row 3
b7 = Button(root, text="7", padx=20, bd=8, fg="black", font=(
    'arial', 20, 'bold'), command=lambda: button(7))
b7.grid(row=3, column=0)

b8 = Button(root, text="8", padx=20, bd=8, fg="black", font=(
    'arial', 20, 'bold'), command=lambda: button(8))
b8.grid(row=3, column=1)

b9 = Button(root, text="9", padx=20, bd=8, fg="black", font=(
    'arial', 20, 'bold'), command=lambda: button(9))
b9.grid(row=3, column=2)

b9add = Button(root, text="+",  padx=20, bd=8, fg="black",
               font=('arial', 20, 'bold'), command=lambda: button("+"))
b9add.grid(row=3, column=3)
# row 6
b0 = Button(root, text="0", padx=20, bd=8, fg="black", font=(
    'arial', 20, 'bold'), command=lambda: button(0))
b0.grid(row=6, column=0)

bdot = Button(root, text=".", padx=25, bd=8, fg="black", font=(
    'arial', 20, 'bold'), command=lambda: button("."))
bdot.grid(row=6, column=1)

bans = Button(root, text="=", command=answer, padx=20,
              bd=8, fg="black", font=('arial', 20, 'bold'))
bans.grid(row=6, column=2)

bdivide = Button(root, text="\u00F7", padx=20, bd=8, fg="black",
                 font=('arial', 20, 'bold'), command=lambda: button("/"))
bdivide.grid(row=6, column=3)

root.mainloop()
