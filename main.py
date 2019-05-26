from tkinter import *

import M1
import M2
import M3
import M4
import M5
import M6

def modules():
    print("----M1------")
    exp = text_re.get("1.0", "end-1c")
    pos_exp = M1.postfixNotation(exp)
    print(pos_exp)
    print("\n")

    print("----M2------")
    alf, matriz_Trans, init_st, final_st = M2.regularExpressionToNFA_e(pos_exp)
    M2.printTransTable(matriz_Trans,alf)
    print("\n")

    print("----M3------")
    matriz_Trans, final_st, alf = M3.NFAconverter(alf,matriz_Trans,init_st,final_st)
    M2.printTransTable(matriz_Trans, alf)
    print("\n")

    print("----M4------")
    matriz_Trans, final_st = M4.afdConverter(matriz_Trans, final_st)
    M2.printTransTable(matriz_Trans, alf)
    print("\n")

    print("----M5------")
    matriz_Trans, final_st =  M5.Minimize(matriz_Trans, final_st)
    M2.printTransTable(matriz_Trans, alf)
    print("\n")

    print("----M6------")
    f = text_input.get("1.0", END)
    result = M6.parse(matriz_Trans,final_st,f,alf)
    text_output.config(state=NORMAL)
    text_output.delete('1.0', END)
    text_output.insert(INSERT, result)
    text_output.config(state=DISABLED)
    print("\n")

root = Tk()
root.title("Automaton Module")

label = Label(root, text="Expresión regular:")
text_re = Text(root, width=12, height=1)
button = Button(root, text="Buscar", fg="green", command=modules)
label_input = Label(root, text="Texto plano:")
text_input = Text(root, width=30, height=10)
label_output = Label(root, text="Texto aprobado:")
text_output = Text(root, width=30, height=10)

label.grid(row=0, padx=20, pady=5, sticky=W)
text_re.grid(row=0, column=1, pady=5, sticky=W)
button.grid(row=0, column=2, columnspan=2, padx=20, pady=5, sticky=W)
label_input.grid(row=1, columnspan=2, padx=20, sticky=W)
label_output.grid(row=1, column=2, columnspan=2, padx=20, sticky=W)
text_input.grid(row=2, columnspan=2, padx=20, pady=10, sticky=W)
text_output.grid(row=2, column=2, columnspan=2, padx=20, pady=10, sticky=W)

root.mainloop()