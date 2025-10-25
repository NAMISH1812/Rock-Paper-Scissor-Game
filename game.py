# Rock - paper - scissor
import random
import tkinter as tk
from tkinter import PhotoImage
list=["rock", "paper", "scissor"]
score=0
computer_score=0
def game(user):
    global score,computer_score
   
    computer=random.choice(list)
    update_computer_images(computer)
    if(user==computer and score<10):
        result=f"It's a tie ! You both chose {user}"
        
    elif(user=="rock"and computer=="paper" and score<10):
        result="Computer wins !"
        computer_score+=1
        
    elif(user=="rock" and computer=="scissor" and score<10):
        result="You win !"
        score+=1
        
    elif(user=="paper" and computer=="rock" and score<10):
        result=" You win !"
        score+=1
            
    elif(user=="paper" and computer=="scissor" and score<10):
        result="Computer wins !"
        computer_score+=1
        
    elif(user=="scissor" and computer=="rock" and score <10):
        result="Computer wins !"
        computer_score+=1
        
    elif(user=="scissor" and computer=="paper" and score<10):
        result="You win !"
        score+=1
            
    else:
        result="Invalid input ! Please choose rock, paper or scissor"
    score_label.config(text=f" Your Score : {score} Computer Score : {computer_score} ")
    result_label.config(text=result)
    if score>=5:
        result_label.config(text="Congratulations! You reached 5 points and won the game!")
        disable_buttons()
    elif computer_score>=5:
        result_label.config(text="Computer reached 5 points and won the game! Better luck next time.")
        disable_buttons()
def disable_buttons():
    rock_btn.config(state=tk.DISABLED)
    paper_btn.config(state=tk.DISABLED)
    scissor_btn.config(state=tk.DISABLED)
def update_computer_images(choice):
    if choice=="rock":
        computer_label.config(image=rock_img)
    elif choice=="paper":
        computer_label.config(image=paper_img)
    elif choice=="scissor":
        computer_label.config(image=scissor_img)
def reset_game():
      rock_btn.config(state=tk.NORMAL)
      paper_btn.config(state=tk.NORMAL)
      scissor_btn.config(state=tk.NORMAL)
      global score
      score=0
      score_label.config(text=f"Score : {score}")
      result_label.config(text="Make your move")
      computer_label.config(image=question_img)
    
#GUI Setup
root=tk.Tk()
root.title("Rock-Paper-Scissor Game")
root.geometry("400x300")
root.config(bg="#d0f0f7")
tk.Label(root, text="Rock-Paper-Scissor", font=("Helvetica", 18,"bold"), bg="#d0f0f7").pack(pady=10)
score_label=tk.Label(root, text=f"Score : {score}", font=("Helvetica", 14), bg="#d0f0f7")
score_label.pack(pady=5)
result_label=tk.Label(root, text="Make your move", font=("Helvetica", 12,"bold"), bg="#d0f0f7")
result_label.pack(pady=5)
winner_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg="#d0f0f7")
winner_label.pack(pady=5)
rock_img=PhotoImage(file="Rock.png")
paper_img=PhotoImage(file="paper.png")
scissor_img=PhotoImage(file="Scissor.png")
question_img=PhotoImage(file="questionmark.png")
frame=tk.Frame(root, bg="lightblue")
frame.pack(pady=10)
rock_btn=tk.Button(frame, image=rock_img, command=lambda: game("rock"), bg="#d0f0f7",relief="raised")
rock_btn.grid(row=0, column=0, padx=15)
paper_btn=tk.Button(frame, image=paper_img, command=lambda: game("paper"), bg="#f0f8ff",relief= "raised")
paper_btn.grid(row=0, column=1, padx=15)
scissor_btn=tk.Button(frame, image=scissor_img, command=lambda: game("scissor"), bg="#f0f8ff",relief="raised")
scissor_btn.grid(row=0, column=2, padx=15)
tk.Label(root, text="Computer's Choice", font=("Helvetica", 12), bg="#d0f0f7").pack(pady=5)
computer_label = tk.Label(root, image=question_img, bg="#d0f0f7")
computer_label.pack(pady=5)
tk.Button(root, text="Play Again", command=lambda: reset_game(), font=("Helvetica", 12, "bold"), bg="#a0e7e5").pack(pady=15)
root.paper_img=paper_img
root.scissor_img=scissor_img
root.question_img=question_img
root.mainloop()

    
        
