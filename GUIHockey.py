import tkinter as tk
    
root = tk.Tk()

def goalSub():
	temp = labelgoal["text"]
	temp = int(temp)
	if temp >0:
		temp = temp -1
		labelgoal.config(text = str(temp))

def goalAdd():
	temp = labelgoal["text"]
	temp = int(temp)
	temp = temp +1
	labelgoal.config(text = str(temp))

def shotSub():
	temp = labelshot["text"]
	temp = int(temp)
	if temp >0:
		temp = temp -1
		labelshot.config(text = str(temp))

def shotAdd():
	temp = labelshot["text"]
	temp = int(temp)
	temp = temp +1
	labelshot.config(text = str(temp))

def assistsSub():
	temp = labelassists["text"]
	temp = int(temp)
	if temp >0:
		temp = temp -1
		labelassists.config(text = str(temp))

def assistsAdd():
	temp = labelassists["text"]
	temp = int(temp)
	temp = temp +1
	labelassists.config(text = str(temp))

def PMSub():
	temp = labelpm["text"]
	temp = int(temp)
	if temp >0:
		temp = temp -1
		labelpm.config(text = str(temp))

def PMAdd():
	temp = labelpm["text"]
	temp = int(temp)
	temp = temp +1
	labelpm.config(text = str(temp))

def Homesub():
	temp = label8["text"]
	temp = int(temp)
	if temp >0:
		temp = temp -1
		label8.config(text = str(temp))

def Homeadd():
	temp = label8["text"]
	temp = int(temp)
	temp = temp +1
	label8.config(text = str(temp))

def Awayadd():
	temp = label9["text"]
	temp = int(temp)
	temp = temp +1
	label9.config(text = str(temp))

def Awaysub():
	temp = label9["text"]
	temp = int(temp)
	if temp >0:
		temp = temp -1
		label9.config(text = str(temp))



output = tk.Text(root,height = 30, width = 10)



label = tk.Label(root, text = "Hockey Helper", font = ("Times", "24", "bold italic"))
label.grid(row = 0, column = 5, )


label1 = tk.Label(root, text = "Goals = ", font = ("Helvetica", "16"))
label1.grid(row = 2, column = 0)

label2 = tk.Label(root, text = "Shots = ", font = ("Helvetica", "16"))
label2.grid(row = 4, column = 0)

label3 = tk.Label(root, text = "Assists = ", font = ("Helvetica", "16"))
label3.grid(row = 6, column = 0)

label4 = tk.Label(root, text = "PM = ", font = ("Helvetica", "16"))
label4.grid(row = 8, column = 0)

btn1 = tk.Button(root, text = "-", command = goalSub)
btn1.grid(row = 2, column = 2)

labelgoal = tk.Label(root, text = "0", font = ("Helvetica", "16"))
labelgoal.grid(row = 2, column = 3)

btn2 = tk.Button(root, text = "+", command = goalAdd)
btn2.grid(row = 2, column = 4)

btn3 = tk.Button(root, text = "-", command = shotSub)
btn3.grid(row = 4, column = 2)

labelshot = tk.Label(root, text = "0", font = ("Helvetica", "16"))
labelshot.grid(row = 4, column = 3)

btn4 = tk.Button(root, text = "+", command = shotAdd)
btn4.grid(row = 4, column = 4)

btn5 = tk.Button(root, text = "-", command = assistsSub)
btn5.grid(row = 6, column = 2)

labelassists = tk.Label(root, text = "0", font = ("Helvetica", "16"))
labelassists.grid(row = 6, column = 3)

btn6 = tk.Button(root, text = "+", command = assistsAdd)
btn6.grid(row = 6, column = 4)

btn7 = tk.Button(root, text = "-", command = PMSub)
btn7.grid(row = 8, column = 2)

labelpm = tk.Label(root, text = "0", font = ("Helvetica", "16"))
labelpm.grid(row = 8, column = 3)

btn8 = tk.Button(root, text = "+", command = PMAdd)
btn8.grid(row = 8, column = 4)

label5 = tk.Label(root, text = "Score", font = ("Times", "20", "bold italic"))
label5.grid(row = 2, column = 9)

label6 = tk.Label(root, text = "Home", font = ("Helvetica", "16"))
label6.grid(row = 4, column = 7, columnspan = 1)

label7 = tk.Label(root, text = "Away", font = ("helvetica", "16"))
label7.grid(row = 4, column = 10)

btn9 = tk.Button(root, text = "-", command = Homesub)
btn9.grid(row = 6, column = 6)

label8 = tk.Label(root, text = "0", font = ("helvetica", "16"))
label8.grid(row = 6, column = 7)

btn10 = tk.Button(root, text = "+", command = Homeadd)
btn10.grid(row = 6, column = 8)

btn11 = tk.Button(root, text = "-", command = Awaysub)
btn11.grid(row = 6, column = 9)

label9 = tk.Label(root, text = "0", font = ("Helvetica", "16"))
label9.grid(row = 6, column = 10)

btn12 = tk.Button(root, text = "+", command = Awayadd)
btn12.grid(row = 6, column = 11)



root.mainloop()