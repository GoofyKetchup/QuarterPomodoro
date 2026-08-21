import ui
import _timer
import pygame # pyright: ignore[reportMissingImports]

pygame.mixer.init()
pygame.mixer.music.load("timer_finished.mp3")

ui.CreateAppWindow("QuarterPomodoro", 600, 400, "#000000", "QuarterPomodoroIcon.ico")

ui.AddCreditsToTheWindow(ui.root, "Celeste_Chibi", "made the icon", "Kalcetoo", "made the original ringtone","#000000", "#FFFFFF")

ui.AddMainTextToTheWindow(ui.root, "      Configure your work/break time here!      ", "#000000", "#FFFFFF", "Arial")

ui.AddTimerTextToTheWindow(ui.root, "#000000", "#FFFFFF", "Arial")

ui.AddButtonsContainersToTheWindow(ui.root, "#000000")

ui.AddSetWorkTimerButtonToTheWindow(ui.root, "#000000", "#FFFFFF", "Arial", lambda: _timer.SetTimerOnWorkTime(ui.Timer))

ui.AddSetBreakTimerButtonToTheWindow(ui.root, "#000000", "#FFFFFF", "Arial", lambda: _timer.SetTimerOnBreakTime(ui.Timer))

ui.AddSetFourthBreakTimerButtonToTheWindow(ui.root, "#000000", "#FFFFFF", "Arial", lambda: _timer.SetTimerOnFourthBreakTime(ui.Timer))

ui.AddStartTimerButtonToTheWindow(ui.root, "#000000", "#FFFFFF", "Arial", lambda: _timer.StartTimer(ui.Timer))

ui.AddStopTimerButtonToTheWindow(ui.root, "#000000", "#FFFFFF", "Arial", lambda: _timer.StopTimer(ui.Timer))

ui.AddStopRingtoneButtonToTheWindow(ui.root, "#000000", "#FFFFFF", "Arial", lambda: _timer.StopRingtone())

ui.RunTheAppRootWindow(ui.root)