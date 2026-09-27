import pyautogui
import threading
import time


running = False
worker_thread = None


def move_mouse(duration_seconds):
    global running

    end_time = time.monotonic() + duration_seconds

    width = 200
    height = 100

    while running and time.monotonic() < end_time:

        # Move right
        pyautogui.moveRel(
            width,
            0,
            duration=0.5
        )

        if not running:
            break

        # Move down
        pyautogui.moveRel(
            0,
            height,
            duration=0.5
        )

        if not running:
            break

        # Move left
        pyautogui.moveRel(
            -width,
            0,
            duration=0.5
        )

        if not running:
            break

        # Move up
        pyautogui.moveRel(
            0,
            -height,
            duration=0.5
        )

    running = False
    print("Rectangle movement finished.")


def start_mouse(duration_seconds):
    global running, worker_thread

    if running:
        return

    running = True

    worker_thread = threading.Thread(
        target=move_mouse,
        args=(duration_seconds,),
        daemon=True
    )

    worker_thread.start()


def stop_mouse():
    global running

    running = False