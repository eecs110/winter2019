from tkinter import Canvas, Tk, Listbox, Label, StringVar, \
        Frame, Entry, Button, END, N, W, E, S, messagebox
import wikipedia

# 1. Define functions
def search_wikipedia(event=None):
    listbox.delete(0, END)
    results = wikipedia.search(search_term_var.get())
    for item in results:
        listbox.insert(END, item)

# 2. Initialize window and variables:
gui = Tk()
gui.title('Wikipedia Browser')
search_term_var = StringVar(gui)
results_var = StringVar(gui)

# 3. Configure layout:
mainframe = Frame(gui, bg='#EEEEEE', padx=5, pady=5)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
gui.rowconfigure(0, weight=1) # row 0 takes up 10% of screen
gui.rowconfigure(1, weight=9) # row 1 takes up 90% of screen


# 4. create textbox:
Entry(
    mainframe,
    textvariable=search_term_var
).grid(column=0, row=0, sticky=E)

# 5. create button:
Button(
    mainframe,
    padx=5, 
    pady=5,
    text='SEARCH',
    command=search_wikipedia
).grid(column=1, row=0, sticky=E)

# Also bind the enter key to execute the search (for accessibility):
gui.bind('<Return>', search_wikipedia)

# 6. create listbox menu:
listbox = Listbox(gui,
    height=20, 
    width=60,
    border=0
)
listbox.grid(column=0, row=1, sticky=W)

gui.mainloop()