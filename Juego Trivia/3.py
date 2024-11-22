import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os
from PIL import Image, ImageTk

class GameSettings:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Settings")
        self.root.geometry("400x600")
        self.root.configure(bg="#1a1a1a")

        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="#1a1a1a")
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Cargar la imagen al inicializar
        try:
            # Reemplaza 'tu_imagen.png' con el nombre de tu archivo de imagen
            image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imagen/qrcode-generado.png')
            self.original_image = Image.open(image_path)
            # Redimensionar la imagen si es necesario (ajusta los números según el tamaño que desees)
            self.original_image = self.original_image.resize((300, 300), Image.Resampling.LANCZOS)
            self.photo_image = ImageTk.PhotoImage(self.original_image)
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            self.photo_image = None

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.main_frame,
            text="Game settings",
            font=("Arial", 24, "bold"),
            bg="#1a1a1a",
            fg="white"
        )
        title_label.pack(anchor="w", pady=(0, 30))

        # Settings container
        settings_frame = tk.Frame(self.main_frame, bg="#1a1a1a")
        settings_frame.pack(fill="x", pady=10)

        # Round time setting
        self.create_setting_row(settings_frame, "Round time", "30s", 0)

        # Max players setting
        self.create_setting_row(settings_frame, "Max players", "4", 1)

        # Score limit setting
        self.create_setting_row(settings_frame, "Score limit", "10", 2)

        # Randomize questions toggle
        self.create_toggle_row(settings_frame, "Randomize questions", 3)

        # Buttons container
        buttons_frame = tk.Frame(self.main_frame, bg="#1a1a1a")
        buttons_frame.pack(fill="x", pady=(40, 0))

        # Start game button
        start_button = tk.Button(
            buttons_frame,
            text="Start game",
            bg="#007bff",
            fg="white",
            font=("Arial", 12),
            width=20,
            height=2,
            border=0,
            command=self.start_game
        )
        start_button.pack(side="left", padx=(0, 10))

        # Invite button
        invite_button = tk.Button(
            buttons_frame,
            text="Invite",
            bg="#1e2732",
            fg="white",
            font=("Arial", 12),
            width=20,
            height=2,
            border=0,
            command=self.invite_players
        )
        invite_button.pack(side="left")

    def create_setting_row(self, parent, label_text, value_text, row):
        frame = tk.Frame(parent, bg="#1a1a1a")
        frame.pack(fill="x", pady=10)

        label = tk.Label(
            frame,
            text=label_text,
            font=("Arial", 12),
            bg="#1a1a1a",
            fg="white"
        )
        label.pack(side="left")

        value = tk.Label(
            frame,
            text=value_text,
            font=("Arial", 12),
            bg="#1a1a1a",
            fg="white"
        )
        value.pack(side="right")

    def create_toggle_row(self, parent, label_text, row):
        frame = tk.Frame(parent, bg="#1a1a1a")
        frame.pack(fill="x", pady=10)

        label = tk.Label(
            frame,
            text=label_text,
            font=("Arial", 12),
            bg="#1a1a1a",
            fg="white"
        )
        label.pack(side="left")

        self.toggle_var = tk.BooleanVar()
        toggle_switch = tk.Checkbutton(
            frame,
            variable=self.toggle_var,
            bg="#1a1a1a",
            activebackground="#1a1a1a",
            selectcolor="#007bff",
            width=2,
            height=1
        )
        toggle_switch.pack(side="right")

    def start_game(self):
        # Obtener la ruta del directorio actual
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Nombre del archivo que quieres abrir (reemplaza '2.py' con el nombre de tu archivo)
        game_file = os.path.join(current_dir, '2.py')

        try:
            # Ejecuta el archivo game.py en una nueva ventana/proceso
            subprocess.Popen([sys.executable, game_file])
        except FileNotFoundError:
            # Manejo de error si el archivo no existe
            tk.messagebox.showerror("Error", f"No se encontró el archivo {game_file}")
        except Exception as e:
            # Manejo de otros posibles errores
            tk.messagebox.showerror("Error", str(e))

    def invite_players(self):
        if hasattr(self, 'image_window'):
            self.image_window.destroy()  # Cerrar ventana anterior si existe

        # Crear nueva ventana
        self.image_window = tk.Toplevel(self.root)
        self.image_window.title("Invitación")
        self.image_window.geometry("400x400")
        self.image_window.configure(bg="#1a1a1a")

        if self.photo_image:
            # Crear label para mostrar la imagen
            image_label = tk.Label(
                self.image_window,
                image=self.photo_image,
                bg="#1a1a1a"
            )
            image_label.pack(pady=20)
        else:
            # Mostrar mensaje si no se pudo cargar la imagen
            error_label = tk.Label(
                self.image_window,
                text="No se pudo cargar la imagen",
                font=("Arial", 12),
                bg="#1a1a1a",
                fg="white"
            )
            error_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameSettings(root)
    root.mainloop()