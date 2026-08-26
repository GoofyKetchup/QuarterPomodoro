from customtkinter import *
from pathlib import Path

def OpenSettings():
    swindow = CTkToplevel()
    swindow.geometry("350x350")
    swindow.title("QuarterPomodoro --- Settings")
    swindow.config(background="#000000")
    swindow.resizable(False, False)
    swindow.iconbitmap("QuarterPomodoroIcon.ico")
    CTkLabel(
        swindow,
        fg_color="#000000",
        text="  Configure settings here!  ",
        font=("Arial", 25),
        width=100,
        height=30,
        corner_radius=10,
        border_width = 1.5,
        border_color="red",
    ).pack(side="top", pady=15)

    ParametersContainer1 = CTkFrame(swindow, fg_color="#000000")
    ParametersContainer1.pack(pady=5)

    ParametersContainer2 = CTkFrame(swindow, fg_color="#000000")
    ParametersContainer2.pack(pady=5)

    ParametersContainer3 = CTkFrame(swindow, fg_color="#000000")
    ParametersContainer3.pack(pady=5)

    ParametersContainer4 = CTkFrame(swindow, fg_color="#000000")
    ParametersContainer4.pack(pady=5)

    ParametersContainer5 = CTkFrame(swindow, fg_color="#000000")
    ParametersContainer5.pack(pady=5)
    
    ParametersContainer6 = CTkFrame(swindow, fg_color="#000000")
    ParametersContainer6.pack(pady=5)

    Change_Ringtone_Button = CTkButton(
        ParametersContainer1,
        text="Change ringtone",
        fg_color="#000000",
        text_color="#FFFFFF",
        font=("Arial", 15),
        corner_radius=10,
        border_width=1.5,
        border_color="red",
        command=lambda: Change_Ringtone(),
    )
    Change_Ringtone_Button.pack(side="left", padx=5)

    swindow.mainloop()

def Change_Ringtone():
    # with open(f"{Path.cwd()}\\timer_finished.mp3", "w") as og:
       # with open(filedialog.askopenfilename(initialdir="/", filetypes=("all files","*.*"), title="Choose your ringtone file."), "r") as new:
        pass