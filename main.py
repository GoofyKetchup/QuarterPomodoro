import ui

ui.CreateAppWindow("QuarterPomodoro", 600, 400, "#000000", "QuarterPomodoroIcon.ico")

ui.AddCreditsToTheWindow(ui.root, "Celeste_Chibi", "made the icon", "#000000", "#FFFFFF")

ui.AddMainTextToTheWindow(ui.root, "      Configure your work/break time here!      ", "#000000", "#FFFFFF", "Arial", "top")

ui.AddTimerTextToTheWindow(ui.root, "#000000", "#FFFFFF", "Arial")

ui.RunTheAppRootWindow(ui.root)