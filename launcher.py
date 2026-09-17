import os
import subprocess
import tkinter as tk
from tkinter import messagebox


def find_roblox_studio():
    versions_path = os.path.expandvars(
        r"%LOCALAPPDATA%\Roblox\Versions"
    )

    if not os.path.exists(versions_path):
        return None

    studios = []

    for folder in os.listdir(versions_path):
        studio_path = os.path.join(
            versions_path,
            folder,
            "RobloxStudioBeta.exe"
        )

        if os.path.isfile(studio_path):
            studios.append(studio_path)

    if not studios:
        return None

    studios.sort(
        key=lambda x: os.path.getmtime(x),
        reverse=True
    )

    return studios[0]


def launch_studio():
    studio = find_roblox_studio()

    if studio is None:
        messagebox.showerror(
            "Roblox Studio Launcher",
            "Roblox Studio не знайдено!\n\n"
            "Переконайся, що Roblox Studio встановлений."
            "Скачати роблокс студіо: https://create.roblox.com/docs/studio/setup"
        )
        return

    try:
        subprocess.Popen(
            [studio],
            cwd=os.path.dirname(studio)
        )

        root.destroy()

    except Exception as error:
        messagebox.showerror(
            "Помилка",
            f"Не вдалося запустити Roblox Studio.\n\n"
            f"{error}"
        )


root = tk.Tk()

root.title("Roblox Studio Launcher")
root.geometry("450x300")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Roblox Studio Launcher",
    font=("Segoe UI", 20, "bold")
)

title.pack(pady=30)

description = tk.Label(
    root,
    text="Launcher для запуску Roblox Studio",
    font=("Segoe UI", 11)
)

description.pack()

launch_button = tk.Button(
    root,
    text="▶  Запустити Roblox Studio",
    font=("Segoe UI", 13, "bold"),
    width=28,
    height=2,
    command=launch_studio
)

launch_button.pack(pady=40)

version = tk.Label(
    root,
    text="Version 0.1",
    font=("Segoe UI", 9)
)

version.pack()

root.mainloop()