from tkinter import *
import random
import tkinter.messagebox



def Questions():
    number1 = random.randrange(1,15)
    number2 = random.randrange(1,15)
    answer = number1 + number2
    prompt = (str(number1) + " + " + str(number2))
    label1 = Label(root, text=prompt, width=len(prompt), bg='light blue')
    label1.pack()
    return answer

def start():
    global count_flag
    global answer
    answer = Questions()


def Submit(answer, entryWidget):
     global count_flag

     count_flag = True
     print ("The Correct answer is",  answer)

     if entryWidget.get().strip() == "":
         tkinter.messagebox.showinfo("Tkinter Entry Widget", "Please enter a number.")

     if answer != int(entryWidget.get().strip()):
         Label(root, text="You got it wrong!").pack()



     else:
         Label (root, text="You got it right!").pack()


# creates the actual tkinter window
root = Tk()

root.title("Math Quiz For Quinn")
root["padx"] = 25
root["pady"] = 20

# Creates the frame
textFrame = Frame(root)

#This just puts that "Answer" text by the entry widget
entryLabel = Label(textFrame)
entryLabel["text"] = "Answer:"
entryLabel.pack(side=LEFT)

#Where you can enter the answer
entryWidget = Entry(textFrame)
entryWidget["width"] = 30
entryWidget.pack(side=LEFT)

textFrame.pack()

# this will be a global flag
count_flag = True


Sub = lambda: Submit(answer, entryWidget)
#stopwatch = lambda: start(answer)

# creates the buttons
btn_submit = Button(root, text="Submit", command = Sub)
btn_start = Button(root, text="Start", command = start)
btn_submit.pack()
btn_start.pack()


#starts the program
root.mainloop()
