from tkinter import *

mainwin = Tk()

Label(mainwin, text="Sequence One").grid(row=0, column=0)
seq1 = ScrolledText(mainwin, height=5); seq1.grid(row=0, column=1, pady=5)
Button(mainwin, text="Upload", command=()).grid(row=0, column=2, sticky="EW")
#EXTRACT TEXT sequence1=seq1.get(1.0, END)


Label(mainwin, text="Sequence Two").grid(row=2, column=0)
seq2 = ScrolledText(mainwin, height=5); seq2.grid(row=2, column=1, pady=5)
#SET TEXTseq2.insert(INSERT, "HELLLLLLLLLLLLLLLLLO")
Button(mainwin, text="Upload", command=()).grid(row=2, column=2, sticky="EW")
#EXTRACT TEXT sequence2=seq2.get(1.0, END)


Label(mainwin, text="###############################################################################################################").grid(row=3, column=0, columnspan=3, sticky="EW" )

Label(mainwin, text="Parameters").grid(row=4, column=0, rowspan=1, sticky="E", padx=10 )

Label(mainwin, text="Match").grid(row=7, column=0, sticky="E", padx=10, pady=3)
Entry(mainwin).grid(row=7, column=1, sticky="W")
Label(mainwin, text="Mismatch").grid(row=8, column=0, sticky="E", padx=10, pady=3)
Entry(mainwin).grid(row=8, column=1, sticky="W")
Label(mainwin, text="Gap").grid(row=9, column=0, sticky="E", padx=10, pady=3)
Entry(mainwin).grid(row=9, column=1, sticky="W")

Label(mainwin, text="Alignment Type").grid(row=4, column=1, rowspan=1)

Radiobutton(mainwin, text="Local", value=1, variable=var).grid(row=7, column=1)
Radiobutton(mainwin, text="Global", value=1, variable=var).grid(row=8, column=1)

Label(mainwin, text="###############################################################################################################").grid(row=10, column=0, columnspan=3, sticky="EW" )

Label(mainwin, text="Output").grid(row=11, column=0)
out = ScrolledText(mainwin, height=10); out.grid(row=11, column=1, pady=5, sticky="EW")
Button(mainwin, text="Download (.txt)", command=()).grid(row=11, column=2, sticky="EW")



#Button(mainwin, text="Exit", command=mainwin.destroy).grid(row=7, column=1, columnspan=1, sticky="E")


mainwin.mainloop()