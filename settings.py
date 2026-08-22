from customtkinter import *

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
        font=("Arial", 15),
        width=75,
        height=25,
        corner_radius=10,
        border_width = 1.5,
        border_color="red",
    ).pack(side="top")

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

    swindow.mainloop()