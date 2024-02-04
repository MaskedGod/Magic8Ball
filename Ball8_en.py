from tkinter import *
import random

# Responses list
english_responses = [
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "Outlook not so good",
    "My sources say no",
    "Signs point to yes",
    "Definitely not",
    "It is certain",
    "Without a doubt",
    "Very doubtful",
    "Reply hazy, try again",
    "Better not tell you now",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes, definitely"
]

FONT = ("Hevetika", 20, 'bold')

class Ball():

    def __init__(self,root):
        
        self.speed = 800
        self.num_of_shuffle = random.randint(9,20)
        self.response = random.randint(0,18)
        self.counter = 0
        
        self.root = root
        self.root.title("8 Ball")
        self.root.config(padx=5,pady=5, bg='blue')
        self.root.geometry('+600+150')
        self.root.resizable(False, False)
        self.root.iconbitmap('satanism_icon.ico')

        
        self.canvas = Canvas(root, width=600, height=600, highlightthickness=0)
        self.canvas.grid(column=0, columnspan=3,row=0)
        self.ball_img = PhotoImage(file='blue_back.png')
        self.canvas.create_image(300,300, image=self.ball_img)

        self.text_id = self.canvas.create_text(
            300, 300, text="Hey, Let's See What Destiny Got For You", font=FONT, fill="yellow")
        
        self.shuff_but = Button(root, text='Shuffle', width=20,font=FONT, fg='Black',bg='lightblue', relief='solid', command=self.shuffle)
        self.shuff_but.grid(column=1,row=1)
        

    def shuffle(self):

        self.shuff_but.config(state=DISABLED)
        self.canvas.itemconfig(self.text_id, text=english_responses[self.response],font=FONT)
        self.response = random.randint(0,19)
        # self.response = (self.response + self.counter) % len(english_responses)
        self.counter += 1
        self.speed -= 50
        
        if self.counter == self.num_of_shuffle:
            self.canvas.itemconfig(self.text_id, text=english_responses[self.response],font=('Helvetika', 32, 'bold'))
            self.shuff_but.config(state=NORMAL)
            self.speed = 800
            self.num_of_shuffle = 12
            self.response = random.randint(0,18)
            self.counter = 0
            return
        self.root.after(self.speed, self.shuffle)

        



    
        
        



if __name__ == "__main__":
    window = Tk()
    baller = Ball(window)
    window.mainloop()

        # self.shuff_but.config(state=NORMAL)