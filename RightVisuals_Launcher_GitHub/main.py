import os
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

APP_TITLE = "RightVisuals Launcher"
MINECRAFT_VERSION = "1.21.11"
LOADER = "Fabric"

BG = "#080D18"
PANEL = "#101A2B"
PANEL2 = "#14233A"
BLUE = "#2787FF"
TEXT = "#F3F7FF"
MUTED = "#9AAAC2"

def find_official_launcher():
    candidates = [
        os.path.expandvars(r"%ProgramFiles(x86)%\Minecraft Launcher\MinecraftLauncher.exe"),
        os.path.expandvars(r"%ProgramFiles%\Minecraft Launcher\MinecraftLauncher.exe"),
        os.path.expandvars(r"%LOCALAPPDATA%\Programs\Minecraft Launcher\MinecraftLauncher.exe"),
    ]
    for candidate in candidates:
        if candidate and os.path.isfile(candidate):
            return candidate
    return None

class Launcher:
    def __init__(self, window):
        self.window = window
        window.title(APP_TITLE)
        window.geometry("1000x650")
        window.minsize(850, 560)
        window.configure(bg=BG)
        self.build()

    def build(self):
        header = tk.Frame(self.window, bg=BG)
        header.pack(fill="x", padx=34, pady=(25, 18))
        tk.Label(header, text="RIGHT", font=("Segoe UI", 22, "bold"),
                 fg=TEXT, bg=BG).pack(side="left")
        tk.Label(header, text="VISUALS", font=("Segoe UI", 22, "bold"),
                 fg=BLUE, bg=BG).pack(side="left")
        tk.Label(header, text="MINECRAFT JAVA • FABRIC",
                 font=("Segoe UI", 9, "bold"), fg=MUTED, bg=BG).pack(side="right", pady=10)

        hero = tk.Frame(self.window, bg=PANEL, highlightthickness=1,
                        highlightbackground="#1E3557")
        hero.pack(fill="both", expand=True, padx=34, pady=(0, 24))

        left = tk.Frame(hero, bg=PANEL)
        left.pack(side="left", fill="both", expand=True, padx=34, pady=34)

        tk.Label(left, text="ТВОЙ МИР.\nТВОИ ПРАВИЛА.", justify="left",
                 font=("Segoe UI", 31, "bold"), fg=TEXT, bg=PANEL).pack(anchor="w")
        tk.Label(left, text="RightVisuals — Minecraft Java Edition",
                 font=("Segoe UI", 12), fg=MUTED, bg=PANEL).pack(anchor="w", pady=(14, 25))

        info = tk.Frame(left, bg=PANEL2, padx=18, pady=15)
        info.pack(anchor="w", fill="x", pady=(0, 22))
        tk.Label(info, text="ВЕРСИЯ ИГРЫ", font=("Segoe UI", 8, "bold"),
                 fg=MUTED, bg=PANEL2).pack(anchor="w")
        tk.Label(info, text=MINECRAFT_VERSION, font=("Segoe UI", 20, "bold"),
                 fg=TEXT, bg=PANEL2).pack(anchor="w")
        tk.Label(info, text="ЗАГРУЗЧИК", font=("Segoe UI", 8, "bold"),
                 fg=MUTED, bg=PANEL2).pack(anchor="w", pady=(10, 0))
        tk.Label(info, text=LOADER, font=("Segoe UI", 14, "bold"),
                 fg=BLUE, bg=PANEL2).pack(anchor="w")

        tk.Label(left, text="ПАМЯТЬ JAVA (RAM, ГБ)",
                 font=("Segoe UI", 9, "bold"), fg=MUTED, bg=PANEL).pack(anchor="w")
        self.ram = ttk.Spinbox(left, from_=2, to=16, width=8)
        self.ram.set("4")
        self.ram.pack(anchor="w", pady=(7, 20))

        tk.Button(left, text="  ОТКРЫТЬ MINECRAFT  ",
                  command=self.launch, font=("Segoe UI", 12, "bold"),
                  fg="white", bg=BLUE, activebackground="#176BD2",
                  activeforeground="white", relief="flat",
                  padx=20, pady=14, cursor="hand2").pack(anchor="w")

        tk.Label(left, text="Перед запуском установи профиль Fabric 1.21.11\n"
                            "в официальном Minecraft Launcher.",
                 justify="left", font=("Segoe UI", 9), fg=MUTED,
                 bg=PANEL).pack(anchor="w", pady=(14, 0))

        right = tk.Frame(hero, bg=PANEL2, width=270)
        right.pack(side="right", fill="y", padx=22, pady=22)
        right.pack_propagate(False)
        tk.Label(right, text="RIGHTVISUALS NEWS", font=("Segoe UI", 11, "bold"),
                 fg=TEXT, bg=PANEL2).pack(anchor="w", padx=20, pady=(22, 18))
        tk.Label(right, text="Добро пожаловать!",
                 font=("Segoe UI", 13, "bold"), fg=BLUE, bg=PANEL2).pack(anchor="w", padx=20)
        tk.Label(right, text="Новости проекта и объявления\nпоявятся здесь после подключения\nисточника новостей.",
                 justify="left", font=("Segoe UI", 10), fg=MUTED,
                 bg=PANEL2).pack(anchor="w", padx=20, pady=(8, 20))
        tk.Frame(right, bg="#29415F", height=1).pack(fill="x", padx=20, pady=8)
        tk.Label(right, text="ПРОФИЛЬ", font=("Segoe UI", 9, "bold"),
                 fg=MUTED, bg=PANEL2).pack(anchor="w", padx=20, pady=(12, 5))
        tk.Label(right, text="Minecraft Java 1.21.11\nFabric Loader",
                 font=("Segoe UI", 10), fg="#70D6A0",
                 bg=PANEL2, justify="left").pack(anchor="w", padx=20)

        footer = tk.Frame(self.window, bg=BG)
        footer.pack(fill="x", padx=34, pady=(0, 16))
        tk.Label(footer, text="RIGHTVISUALS • COMMUNITY LAUNCHER",
                 font=("Segoe UI", 8), fg="#60728D", bg=BG).pack(side="left")
        tk.Label(footer, text="v0.2.0", font=("Segoe UI", 8),
                 fg="#60728D", bg=BG).pack(side="right")

    def launch(self):
        launcher = find_official_launcher()
        if launcher:
            try:
                subprocess.Popen([launcher])
                messagebox.showinfo(
                    "RightVisuals",
                    "Официальный Minecraft Launcher открыт.\n"
                    "Выбери установленный профиль Fabric 1.21.11 и нажми «Играть»."
                )
            except OSError as exc:
                messagebox.showerror("Ошибка запуска", str(exc))
        else:
            messagebox.showwarning(
                "Minecraft Launcher не найден",
                "Установи официальный Minecraft Launcher.\n"
                "Затем установи Fabric Loader для Minecraft 1.21.11."
            )

if __name__ == "__main__":
    app = tk.Tk()
    Launcher(app)
    app.mainloop()
