import tkinter as tk
import subprocess
import sys
import os
from tkinter import messagebox
#generador de qr buscar

class TriviadosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Triviados")
        self.root.geometry("400x700")
        self.root.configure(bg="#1a1a1a")

        self.create_widgets()

    def create_widgets(self):
        # Header frame
        header_frame = tk.Frame(self.root, bg="#1a1a1a")
        header_frame.pack(fill="x", padx=20, pady=10)

        # Title "Triviados"
        title_label = tk.Label(
            header_frame,
            text="Triviados",
            font=("Arial", 16),
            bg="#1a1a1a",
            fg="white"
        )
        title_label.pack(side="left", padx=10)

        # Main content
        main_frame = tk.Frame(self.root, bg="#1a1a1a")
        main_frame.pack(fill="both", expand=True, padx=20)

        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="Juega en línea con amigos",
            font=("Arial", 18, "bold"),
            bg="#1a1a1a",
            fg="white"
        )
        subtitle_label.pack(anchor="w", pady=(20, 5))

        # Play button
        play_button = tk.Button(
            main_frame,
            text="Jugar ahora",
            font=("Arial", 12, "bold"),
            bg="#007bff",
            fg="white",
            bd=0,
            padx=20,
            pady=12,
            width=30,
            command=self.start_game
        )
        play_button.pack(pady=30)

        # Options text (now as a button)
        options_button = tk.Label(
            main_frame,
            text="Ajustes",
            font=("Arial", 10),
            bg="#1a1a1a",
            fg="gray",
            cursor="hand2"  # Changes cursor to hand when hovering
        )
        options_button.pack(pady=10)
        # Bind click event to the label
        options_button.bind("<Button-1>", lambda e: self.open_settings())

    def create_city_card(self, parent, city, status, side):
        # Create card frame
        card_frame = tk.Frame(
            parent,
            bg="#2a2a2a",
            width=180,
            height=120
        )
        card_frame.pack(side=side, padx=5)
        card_frame.pack_propagate(False)

        # Create placeholder for image (dark gray rectangle)
        image_frame = tk.Frame(
            card_frame,
            bg="#3a3a3a",
            width=180,
            height=80
        )
        image_frame.pack(fill="x")

        # City name
        city_label = tk.Label(
            card_frame,
            text=city,
            font=("Arial", 12, "bold"),
            bg="#2a2a2a",
            fg="white"
        )
        city_label.pack(anchor="w", padx=10, pady=(5, 0))

        # Status
        status_label = tk.Label(
            card_frame,
            text=status,
            font=("Arial", 10),
            bg="#2a2a2a",
            fg="gray"
        )
        status_label.pack(anchor="w", padx=10)

    def start_game(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        game_file = os.path.join(current_dir, '2.py')

        try:
            subprocess.Popen([sys.executable, game_file])
        except FileNotFoundError:
            messagebox.showerror("Error", f"No se encontró el archivo {game_file}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def open_settings(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        settings_file = os.path.join(current_dir, '3.py')

        try:
            subprocess.Popen([sys.executable, settings_file])
        except FileNotFoundError:
            messagebox.showerror("Error", f"No se encontró el archivo {settings_file}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = TriviadosApp(root)
    root.mainloop()