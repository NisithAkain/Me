import numpy as np 
import ttkbootstrap as ttk 


#window
window = ttk.Window(themename='journal')
window.title("simultaneous equation solver")
window.geometry('600x400')

#widget 
window.columnconfigure((0,1,2,3,4), weight = 1 )
window.rowconfigure((0,1), weight =1)
entry1 = ttk.Entry(window)
entry1.grid(row=0, column=0)
label1 = ttk.Label(window, text ="x  +  ")
label1.grid(row=0, column=1)


entry2 = ttk.Entry(window)
entry2.grid(row = 0, column=2)
label2 = ttk.Label(window)


entry3 = ttk.Label(window)






a = np.array([[4,0.3333333],
              [10, 3]])

b = np.array([5,19]).reshape(2,1)

print(a)
print(b)

answer = np.linalg.solve(a,b)
print(answer)



#run
window.mainloop()
