import time
import customtkinter
import pygame # pyright: ignore[reportMissingImports]

timer_states = {
    "running": False,
    "remaining_seconds": 25 * 60,
    "after_id": None,
}

def _update_timer_display(timer):
    minutes = timer_states["remaining_seconds"] // 60
    seconds = timer_states["remaining_seconds"] % 60
    timer.configure(text=f"{minutes:02d}:{seconds:02d}")

def SetTimerOnWorkTime(timer):
    if not timer_states["running"]:
        timer_states["remaining_seconds"] = 25 * 60
        timer.configure(text="25:00")

def SetTimerOnBreakTime(timer):
    if not timer_states["running"]:
        timer_states["remaining_seconds"] = 10
        timer.configure(text="05:00")

def SetTimerOnFourthBreakTime(timer):
    if not timer_states["running"]:
        timer_states["remaining_seconds"] = 30 * 60
        timer.configure(text="30:00")

def _tick(timer):
    if timer_states["running"]:
        if timer_states["remaining_seconds"] > 0:
            timer_states["remaining_seconds"] -= 1
            _update_timer_display(timer)
            timer_states["after_id"] = timer.after(1000, _tick, timer)
        else:
            timer_states["running"] = False
            timer.configure(text="00:00")
            pygame.mixer.music.play()

def StartTimer(timer):
    if not timer_states["running"] and timer_states["remaining_seconds"] > 0:
        timer_states["running"] = True
        timer_states["after_id"] = timer.after(1000, _tick, timer)

def StopTimer(timer):
    if timer_states["running"]:
        timer_states["running"] = False
        if timer_states["after_id"]:
            timer.after_cancel(timer_states["after_id"])
            timer_states["after_id"] = None
        _update_timer_display(timer)

def StopRingtone():
    pygame.mixer.music.stop()