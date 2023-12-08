
import tkinter as tk
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = client["phonebook"]
mycol = mydb["contacts"]


root = tk.Tk()
root.geometry("600x400+1200+500")
canvas1 = tk.Canvas(root, width=400, height=400)
canvas1.pack()

label1 = tk.Label(root, text='Lastname')
canvas1.create_window(100, 90, window=label1)

entry2 = tk.Entry(root)
canvas1.create_window(220, 90, window=entry2)

label1 = tk.Label(root, text='phone number')
canvas1.create_window(100, 120, window=label1)

entry3 = tk.Entry(root)
canvas1.create_window(220, 120, window=entry3)

line = canvas1.create_line(10, 40, 300, 40, fill='black', width=3)

label1 = tk.Label(root, text='Search')
canvas1.create_window(90, 20, window=label1)

entry4 = tk.Entry(root)
canvas1.create_window(220, 20, window=entry4)



