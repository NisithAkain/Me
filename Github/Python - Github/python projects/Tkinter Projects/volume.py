import tkinter as tk
import ttkbootstrap as ttk
import math 

#window
window= ttk.Window(themename='journal')
window.geometry('800x400')
window.minsize(800, 400)
window.maxsize(800,400)
window.title('Volume for cylinder, cone, sphere')


#Notebook
notebook=ttk.Notebook(master = window)



#volume of sphere
def calculate_volume_sphere():
    try:
        r = float(sphere_radius.get())
        vol = (4/3) * math.pi * r**3
        area = 4 * math.pi * r**2
        sphere_volume.set(f'{vol:.2f} units cubed')
        sphere_area.set(f'{area:.2f} units squared')
    except ValueError:
        sphere_volume.set('Invalid input')
        sphere_area.set('Invalid input')
    
sphere_frame = ttk.Frame(master=window)
label1= ttk.Label(master=sphere_frame, text = 'Volume for sphere', font="Calibri 24 bold")
sphere_volume = tk.StringVar()
sphere_area = tk.StringVar()
label2 = ttk.Label(master = sphere_frame, textvariable=sphere_volume)
label3 = ttk.Label(master = sphere_frame, text='Surface Area:')
label4 = ttk.Label(master = sphere_frame, textvariable=sphere_area)
sphere_radius = tk.StringVar()
frame1= ttk.Frame(master = sphere_frame)
entry1 = ttk.Entry(master=frame1, textvariable=sphere_radius)

button1= ttk.Button(master = frame1,text = 'Calculate', command = calculate_volume_sphere)
sphere_frame.pack(expand = True, fill = 'both')
label1.pack(pady = 5)
label2.pack()
label3.pack()
label4.pack()
frame1.pack()
entry1.pack(side = 'left', padx=10)
button1.pack(side = 'right')

#Volume of cylinder
def calculate_volume_cylinder():
    try:
        r = float(cylinder_radius.get())
        h = float(cylinder_height.get())
        vol = math.pi * r**2 * h
        surface_area = 3.14 * 2 * r * (r+h)
        cylinder_volume.set(f'{vol:.2f} units cubed, suface area is {surface_area}')

    except ValueError:
        cylinder_volume.set('Invalid input')

    

cylinder_frame = ttk.Frame(master=window)
cylinder_label = ttk.Label(master=cylinder_frame, text='Volume for cylinder', font="Calibri 24 bold")
cylinder_volume = tk.StringVar()
cylinder_volume_label = ttk.Label(master=cylinder_frame, textvariable=cylinder_volume)
cylinder_radius = tk.StringVar()
cylinder_height = tk.StringVar()
cylinder_frame1 = ttk.Frame(master=cylinder_frame)
cylinder_radius_label = ttk.Label(master=cylinder_frame1, text='Radius:')
cylinder_radius_entry = ttk.Entry(master=cylinder_frame1, textvariable=cylinder_radius)
cylinder_height_label = ttk.Label(master=cylinder_frame1, text='Height:')
cylinder_height_entry = ttk.Entry(master=cylinder_frame1, textvariable=cylinder_height)
cylinder_button = ttk.Button(master=cylinder_frame1, text='Calculate', command=calculate_volume_cylinder)
cylinder_frame.pack(expand=True, fill='both')
cylinder_label.pack(pady=5)
cylinder_volume_label.pack()
cylinder_frame1.pack()
cylinder_radius_label.pack(side='left')
cylinder_radius_entry.pack(side='left', padx=5)
cylinder_height_label.pack(side='left')
cylinder_height_entry.pack(side='left', padx=5)
cylinder_button.pack(side='left')

#Volume of cone
def calculate_volume_cone():
    try:
        r = float(cone_radius.get())
        h = float(cone_height.get())
        vol = (1/3) * math.pi * r**2 * h
        suface_area = 3.14 * (r*r) + (3.14 * r * math.sqrt((r*r) + (h*h)))
        cone_volume.set(f'{vol:.2f} units cubed, surface area {suface_area}')
    except ValueError:
        cone_volume.set('Invalid input')

cone_frame = ttk.Frame(master=window)
cone_label = ttk.Label(master=cone_frame, text='Volume for cone', font="Calibri 24 bold")
cone_volume = tk.StringVar()
cone_volume_label = ttk.Label(master=cone_frame, textvariable=cone_volume)
cone_radius = tk.StringVar()
cone_height = tk.StringVar()
cone_frame1 = ttk.Frame(master=cone_frame)
cone_radius_label = ttk.Label(master=cone_frame1, text='Radius:')
cone_radius_entry = ttk.Entry(master=cone_frame1, textvariable=cone_radius)
cone_height_label = ttk.Label(master=cone_frame1, text='Height:')
cone_height_entry = ttk.Entry(master=cone_frame1, textvariable=cone_height)
cone_button = ttk.Button(master=cone_frame1, text='Calculate', command=calculate_volume_cone)
cone_frame.pack(expand=True, fill='both')
cone_label.pack(pady=5)
cone_volume_label.pack()
cone_frame1.pack()
cone_radius_label.pack(side='left')
cone_radius_entry.pack(side='left', padx=5)
cone_height_label.pack(side='left')
cone_height_entry.pack(side='left', padx=5)
cone_button.pack(side='left')


pyramid_frame = ttk.Frame(master =  window)
pyramid_label = ttk.Label(master=pyramid_frame, text='Volume of Pyramid', font="Calibri 24 bold")
cone_volume = tk.StringVar()
pyramid_label.pack()

pyramid_frame2 = ttk.Frame(master = pyramid_frame)
pyramid_width =  tk.StringVar()
pyramid_height = tk.StringVar()
pyramid_length =  tk.StringVar()

pyramid_width_entry = ttk.Entry(master=pyramid_frame2, textvariable= pyramid_width)
pyramid_width_label = ttk.Label(master=pyramid_frame2, text='width:')
pyramid_height_label = ttk.Label(master=pyramid_frame2, text='Height:')
pyramid_height_entry = ttk.Entry(master=pyramid_frame2, textvariable=pyramid_height)

pyramid_length_label = ttk.Label(master=pyramid_frame2, text='length:')
pyramid_length_entry = ttk.Entry(master=pyramid_frame2, textvariable=pyramid_length)


pyramid_volume = tk.StringVar()

pyramid_volume_label = ttk.Label(master=pyramid_frame, textvariable=pyramid_volume)
pyramid_volume_label.pack()

def calculate_volume_pyramid():
    try:
        w = float(pyramid_width.get())
        h = float(pyramid_height.get())
        l= float(pyramid_length.get())

        vol = (1/3) * w * h * l
        suface_area = "too lazy to calculate - akain"
        pyramid_volume.set(f'{vol:.2f} units cubed, surface area {suface_area}')
    except ValueError:
        pyramid_volume.set('Invalid input')

pyramid_calculate_button = ttk.Button(pyramid_frame, text = 'calculate', command = calculate_volume_pyramid)



pyramid_frame2.pack()
pyramid_width_label.pack()
pyramid_width_entry.pack() 
pyramid_height_label.pack() 
pyramid_height_entry.pack() 
pyramid_length_label.pack() 
pyramid_length_entry.pack() 
pyramid_calculate_button.pack(side = 'left')




#Notebook adding
notebook.add(sphere_frame, text = 'sphere')
notebook.add(cylinder_frame, text = 'cylinder')
notebook.add(cone_frame, text = 'cone')
notebook.add(pyramid_frame, text = 'pyramid')
notebook.pack(expand=True, fill = 'both')



#run 
window.mainloop()