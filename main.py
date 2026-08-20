import ui
import _timer

ui.CreateAppWindow("QuarterPomodoro", 600, 400, "#000000", "QuarterPomodoroIcon.ico")

ui.AddCreditsToTheWindow(ui.root, "Celeste_Chibi", "made the icon", "#000000", "#FFFFFF")

ui.AddMainTextToTheWindow(ui.root, "      Configure your work/break time here!      ", "#000000", "#FFFFFF", "Arial")

ui.AddTimerTextToTheWindow(ui.root, "#000000", "#FFFFFF", "Arial")

ui.AddButtonsContainersToTheWindow(ui.root, "#000000")

ui.AddSetWorkTimerButtonToTheWindow(ui.root, "#000000", "#FFFFFF", "Arial", _timer.SetTimerOnWorkTime(ui.Timer))

ui.AddSetBreakTimerButtonToTheWindow(ui.root, "#000000", "#FFFFFF", "Arial", _timer.SetTimerOnBreakTime(ui.Timer))

ui.AddSetFourthBreakTimerButtonToTheWindow(ui.root, "#000000", "#FFFFFF", "Arial", _timer.SetTimerOnFourthBreakTime(ui.Timer))

ui.AddStartTimerButton(ui.root, "#000000", "#FFFFFF", "Arial", _timer.StartTimer(ui.Timer))

ui.AddStopTimerButton(ui.root, "#000000", "#FFFFFF", "Arial", _timer.StopTimer(ui.Timer))

ui.RunTheAppRootWindow(ui.root)