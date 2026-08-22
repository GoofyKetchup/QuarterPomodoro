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

def AddCreditsToTheWindow(window, name, role, name2, role2, fg_color, text_color):
    global Credits
    Credits = CTkLabel(
        window,
        text=f"Credits : {name} {role}\n Credits : {name2} {role2}",
        fg_color=fg_color,
        text_color=text_color,
    )
    Credits.pack(side="bottom")

def AddMainTextToTheWindow(window, text_content, fg_color, text_color, font):
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
    MainText.pack(side="top")

def AddTimerTextToTheWindow(window, fg_color, text_color, font):
    global Timer
    Timer = CTkLabel(
        window,
        text="25:00",
        fg_color=fg_color,
        text_color=text_color,
        font=(font, 90),
        width=150,
        height=190,
    )
    Timer.pack()

def AddButtonsContainersToTheWindow(window, fg_color):
    global ButtonsContainer1, ButtonsContainer2, ButtonsContainer3
    ButtonsContainer1 = CTkFrame(window, fg_color=fg_color)
    ButtonsContainer1.pack(pady=5)

    ButtonsContainer2 = CTkFrame(window, fg_color=fg_color)
    ButtonsContainer2.pack(pady=5)

    ButtonsContainer3 = CTkFrame(window, fg_color=fg_color)
    ButtonsContainer3.pack(pady=5)

def AddSetWorkTimerButtonToTheWindow(fg_color, text_color, font, button_command):
    global SetWorkTimerButton
    SetWorkTimerButton = CTkButton(
        ButtonsContainer1,
        text="Set To Work Time",
        fg_color=fg_color,
        text_color=text_color,
        font=(font, 20),
        corner_radius=10,
        border_width=1.5,
        border_color="red",
        command=button_command
    )
    SetWorkTimerButton.pack(side="left")

def AddSetBreakTimerButtonToTheWindow(fg_color, text_color, font, button_command):
    global SetBreakTimerButton
    SetBreakTimerButton = CTkButton(
        ButtonsContainer1,
        text="Set To Break Time",
        fg_color=fg_color,
        text_color=text_color,
        font=(font, 20),
        corner_radius=10,
        border_width=1.5,
        border_color="red",
        command=button_command
    )
    SetBreakTimerButton.pack(side="left")

def AddSetFourthBreakTimerButtonToTheWindow(fg_color, text_color, font, button_command):
    global SetFourthBreakTimerButton
    SetFourthBreakTimerButton = CTkButton(
        ButtonsContainer1,
        text="Set To Break Four Time",
        fg_color=fg_color,
        text_color=text_color,
        font=(font, 20),
        corner_radius=10,
        border_width=1.5,
        border_color="red",
        command=button_command
    )
    SetFourthBreakTimerButton.pack(side="left")

def AddStartTimerButtonToTheWindow(fg_color, text_color, font, button_command):
    global StartTimerButton
    StartTimerButton = CTkButton(
        ButtonsContainer2,
        text="Start Timer",
        fg_color=fg_color,
        text_color=text_color,
        font=(font, 20),
        corner_radius=10,
        border_width=1.5,
        border_color="red",
        command=button_command
    )
    StartTimerButton.pack(side="left", padx=5)

def AddStopTimerButtonToTheWindow(fg_color, text_color, font, button_command):
    global StopTimerButton
    StopTimerButton = CTkButton(
        ButtonsContainer2,
        text="Stop Timer",
        fg_color=fg_color,
        text_color=text_color,
        font=(font, 20),
        corner_radius=10,
        border_width=1.5,
        border_color="red",
        command=button_command
    )
    StopTimerButton.pack(side="left", padx=5)

def AddStopRingtoneButtonToTheWindow(fg_color, text_color, font, button_command):
    global StopRingtoneButton
    StopRingtoneButton = CTkButton(
        ButtonsContainer2,
        text="Stop Ringtone",
        fg_color=fg_color,
        text_color=text_color,
        font=(font, 20),
        corner_radius=10,
        border_width=1.5,
        border_color="red",
        command=button_command,
    )
    StopRingtoneButton.pack(side="left", padx=5)

def AddAutoCycleButtonToTheWindow(fg_color, text_color, font, button_command):
    global AutoCycleButton
    AutoCycleButton = CTkButton(
        ButtonsContainer3,
        text="Auto Cycle(not available yet)",
        fg_color=fg_color,
        text_color=text_color,
        font=(font, 20),
        corner_radius=10,
        border_width=1.5,
        border_color="red",
        command=button_command,
    )
    AutoCycleButton.pack(side="left", padx=5)

def AddSettingButtonToTheWindow(fg_color, text_color, font, button_command):
    global SettingButton
    SettingButton = CTkButton(
    ButtonsContainer3,
    text="Open Settings",
    fg_color=fg_color,
    text_color=text_color,
    font=(font, 20),
    corner_radius=10,
    border_width=1.5,
    border_color="red",
    command=button_command,
    )
    SettingButton.pack(side="left", padx=5)

def RunTheAppRootWindow(root):
    root.mainloop()