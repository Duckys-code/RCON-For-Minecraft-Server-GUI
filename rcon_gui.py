import tkinter as tk
from tkinter import ttk
from mcrcon import MCRcon
import threading
import time

mcr = None
connected = False

def connect():
    global mcr, connected
    try:
        mcr = MCRcon(host_entry.get(), password_entry.get(), port=int(port_entry.get()))
        mcr.connect()
        connected = True
        append_output("[Connected to server]\n")
        threading.Thread(target=update_stats_loop, daemon=True).start()
    except Exception as e:
        append_output(f"[Connection Error] {e}\n")
        connected = False

def send_command():
    if not connected:
        append_output("[Error] Not connected.\n")
        return
    command = command_entry.get()
    try:
        response = mcr.command(command)
        append_output(f"> {command}\n{response}\n")
        command_entry.delete(0, tk.END)
    except Exception as e:
        append_output(f"[Error] {e}\n")

def stop_server():
    if connected:
        mcr.command("stop")
        append_output("[STOP command sent]\n")

def restart_server():
    if connected:
        mcr.command("restart")
        append_output("[RESTART command sent]\n")

def update_stats_loop():
    while connected:
        try:
            response = mcr.command("list")
            player_count.set(parse_player_count(response))
        except:
            player_count.set("N/A")
        time.sleep(5)

def parse_player_count(response):
    if "There are" in response:
        try:
            count = response.split("There are ")[1].split(" ")[0]
            return count
        except:
            return "?"
    return "?"

def append_output(text):
    output_text.config(state='normal')
    output_text.insert(tk.END, text)
    output_text.see(tk.END)
    output_text.config(state='disabled')

# --- GUI ---
root = tk.Tk()
root.title("RCON Control Panel")
root.geometry("700x550")
root.configure(bg="#0d0d0d")

style = ttk.Style()
style.theme_use("clam")

# Global Colors
bg_dark = "#0d0d0d"
purple = "#4b0082"
entry_bg = "#1a1a1a"
fg_white = "#ffffff"

# Button style
style.configure("Rounded.TButton",
    font=("Segoe UI", 10),
    padding=6,
    borderwidth=0,
    relief="flat",
    background=purple,
    foreground="white"
)
style.map("Rounded.TButton", background=[('active', '#5f00a6')])

# Entry style
style.configure("Custom.TEntry",
    fieldbackground=entry_bg,
    foreground="white",
    padding=5,
    borderwidth=0,
    relief="flat"
)

# Label style
style.configure("TLabel", foreground=fg_white, background=bg_dark, font=("Segoe UI", 10))

def styled_entry(master, text="", show=None):
    e = ttk.Entry(master, style="Custom.TEntry")
    if text:
        e.insert(0, text)
    if show:
        e.config(show=show)
    return e

# Inputs
ttk.Label(root, text="Host:").pack(pady=(10, 0))
host_entry = styled_entry(root, "127.0.0.1")
host_entry.pack(pady=5)

ttk.Label(root, text="Port:").pack()
port_entry = styled_entry(root, "8155")
port_entry.pack(pady=5)

ttk.Label(root, text="Password:").pack()
password_entry = styled_entry(root, show="*")
password_entry.pack(pady=5)

ttk.Button(root, text="Connect", command=connect, style="Rounded.TButton").pack(pady=(10, 10))

# Buttons Row
btn_frame = tk.Frame(root, bg=bg_dark)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="STOP", command=stop_server, style="Rounded.TButton").grid(row=0, column=0, padx=10)
ttk.Button(btn_frame, text="RESTART", command=restart_server, style="Rounded.TButton").grid(row=0, column=1, padx=10)

# Command Input
ttk.Label(root, text="Command:").pack()
command_entry = styled_entry(root)
command_entry.pack(pady=5)

ttk.Button(root, text="Send", command=send_command, style="Rounded.TButton").pack(pady=10)

# Stats
player_count = tk.StringVar(value="N/A")
ttk.Label(root, textvariable=player_count, font=("Segoe UI", 12, "bold")).pack(pady=(5, 0))
ttk.Label(root, text="Players Online").pack()

# Output Area
output_text = tk.Text(root, state='disabled', bg="#1a1a1a", fg="#ad8eff", font=("Consolas", 10), height=10, wrap="word", relief="flat", borderwidth=0)
output_text.pack(padx=10, pady=10, fill='both', expand=True)

root.mainloop()
