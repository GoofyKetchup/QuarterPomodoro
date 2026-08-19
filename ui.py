from customtkinter import *
import ctypes

def CreateAppWindow(title, width_size, height_size, fg_color, favicon):
    global root
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "GoofyKetchup.QuarterPomodoro.Main"
    )
    root = CTk()
    root.title(title)
    root.geometry(f"{width_size}x{height_size}")
    root.configure(fg_color=fg_color)
    root.resizable(False, False)
    root.iconbitmap(favicon)

def AddCreditsToTheWindow(window, name, role, fg_color, text_color):
    global Credits
    Credits = CTkLabel(
        window,
        text=f"Credits : {name} {role}",
        fg_color=fg_color,
        text_color=text_color,
    )
    Credits.pack(side="bottom")

def AddMainTextToTheWindow(window, text_content, fg_color, text_color, font, TextSide):
    global MainText
    MainText = CTkLabel(
        window,
        text=text_content,
        fg_color=fg_color,
        text_color=text_color,
        font=(font, 25),
        width=150,
        height=50,
        corner_radius=10,
        border_width = 1.5,
        border_color="red",
    )
    MainText.pack(side=TextSide)

def AddTimerTextToTheWindow(window, fg_color, text_color, font):
    global Timer
    Timer = CTkLabel(
        window,
        text="25:00",
        fg_color=fg_color,
        text_color=text_color,
        font=(font, 90)
    )
    Timer.place(relx=0.5, rely=0.5, anchor="center")

def RunTheAppRootWindow(root):
    root.mainloop()