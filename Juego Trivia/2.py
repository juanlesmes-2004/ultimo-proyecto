import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import time
from tkinter import messagebox


class ModernQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Moderno")
        self.root.geometry("400x600")
        self.root.configure(bg="#1a1a1a")

        # Configuración del tema oscuro
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Base de preguntas
        self.questions = [
            {
                "question": "¿Cuál es la capital de Francia?",
                "options": ["London", "Paris", "New York", "Tokyo"],
                "correct": "Paris"
            },
            {
                "question": "¿Qué planeta se conoce como el Planeta Rojo?",
                "options": ["Venus", "Jupiter", "Mars", "Saturn"],
                "correct": "Mars"
            },
            {
                "question": "¿Cuál es el mamífero más grande del mundo?",
                "options": ["elefante africanot", "ballena azul", "Girafa", "oso polar"],
                "correct": "ballena azul"
            },
            {
                "question": "¿Quién pintó la Mona Lisa?",
                "options": ["Van Gogh", "Da Vinci", "Picasso", "Rembrandt"],
                "correct": "Da Vinci"
            },
            {
                "question": "¿Cuál es el símbolo químico del oro?",
                "options": ["Ag", "Fe", "Au", "Cu"],
                "correct": "Au"
            }
        ]

        # Variables del quiz
        self.current_question = 0
        self.score = 0
        self.selected_answer = None
        self.seconds = 30
        self.timer_running = False

        self.create_widgets()
        self.load_question()
        self.start_timer()

    def create_widgets(self):
        # Frame principal
        self.main_frame = ctk.CTkFrame(self.root, fg_color="#1a1a1a")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Progreso del quiz
        self.progress_label = ctk.CTkLabel(
            self.main_frame,
            text="Pregunta 1/5",
            font=("Helvetica", 14),
            text_color="gray"
        )
        self.progress_label.pack(pady=(0, 10))

        # Timer frame
        self.timer_frame = ctk.CTkFrame(self.main_frame, fg_color="#1a1a1a")
        self.timer_frame.pack(fill="x", pady=(0, 20))

        # Labels del temporizador
        self.create_timer_labels()

        # Score
        self.score_label = ctk.CTkLabel(
            self.main_frame,
            text="Score: 0",
            font=("Helvetica", 14),
            text_color="#007AFF"
        )
        self.score_label.pack(pady=(0, 20))

        # Pregunta
        self.question_label = ctk.CTkLabel(
            self.main_frame,
            text="",
            font=("Helvetica", 18),
            text_color="white",
            wraplength=350
        )
        self.question_label.pack(pady=(0, 30))

        # Frame para opciones
        self.options_frame = ctk.CTkFrame(self.main_frame, fg_color="#1a1a1a")
        self.options_frame.pack(fill="x", pady=(0, 20))

        # Botón Submit
        self.submit_button = ctk.CTkButton(
            self.main_frame,
            text="Submit",
            font=("Helvetica", 14),
            fg_color="#007AFF",
            hover_color="#0056b3",
            height=40,
            command=self.submit_answer
        )
        self.submit_button.pack(fill="x", pady=(30, 0))

    def create_timer_labels(self):
        time_units = [ ("Seconds", str(self.seconds).zfill(2))]

        for unit, value in time_units:
            frame = ctk.CTkFrame(self.timer_frame, fg_color="#1a1a1a")
            frame.pack(side="left", expand=True, padx=5)

            if unit == "Seconds":
                self.seconds_label = ctk.CTkLabel(
                    frame,
                    text=value,
                    font=("Helvetica", 24, "bold"),
                    text_color="white"
                )
                self.seconds_label.pack()
            else:
                ctk.CTkLabel(
                    frame,
                    text=value,
                    font=("Helvetica", 24, "bold"),
                    text_color="white"
                ).pack()

            ctk.CTkLabel(
                frame,
                text=unit,
                font=("Helvetica", 12),
                text_color="gray"
            ).pack()

    def load_question(self):
        # Actualizar progreso
        self.progress_label.configure(
            text=f"Pregunta {self.current_question + 1}/{len(self.questions)}"
        )

        # Cargar pregunta actual
        question_data = self.questions[self.current_question]
        self.question_label.configure(text=question_data["question"])

        # Limpiar opciones anteriores
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        # Crear nuevos botones de opciones
        self.option_buttons = []
        for option in question_data["options"]:
            btn = ctk.CTkButton(
                self.options_frame,
                text=option,
                font=("Helvetica", 14),
                fg_color="#2d2d2d",
                hover_color="#3d3d3d",
                height=40,
                command=lambda x=option: self.select_answer(x)
            )
            btn.pack(fill="x", pady=5)
            self.option_buttons.append(btn)

        # Reiniciar temporizador
        self.seconds = 30
        self.timer_running = False
        self.selected_answer = None
        self.start_timer()

    def start_timer(self):
        if self.seconds > 0 and not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def update_timer(self):
        if self.seconds > 0 and self.timer_running:
            self.seconds -= 1
            self.seconds_label.configure(text=str(self.seconds).zfill(2))
            self.root.after(1000, self.update_timer)
        elif self.seconds == 0:
            self.timer_running = False
            self.next_question(timeout=True)

    def select_answer(self, option):
        self.selected_answer = option
        for btn in self.option_buttons:
            if btn.cget("text") == option:
                btn.configure(fg_color="#007AFF")
            else:
                btn.configure(fg_color="#2d2d2d")

    def submit_answer(self):
        if self.selected_answer:
            self.next_question()
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una respuesta")

    def next_question(self, timeout=False):
        # Verificar respuesta
        if not timeout and self.selected_answer == self.questions[self.current_question]["correct"]:
            self.score += 1
            self.score_label.configure(text=f"Score: {self.score}")

        # Pasar a la siguiente pregunta
        self.current_question += 1

        # Verificar si el quiz ha terminado
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_results()

    def show_results(self):
        # Detener el temporizador
        self.timer_running = False

        # Calcular porcentaje
        percentage = (self.score / len(self.questions)) * 100

        # Mostrar resultados
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Título de resultados
        ctk.CTkLabel(
            self.main_frame,
            text="¡Quiz Completado!",
            font=("Helvetica", 24, "bold"),
            text_color="white"
        ).pack(pady=(50, 20))

        # Mostrar score final
        ctk.CTkLabel(
            self.main_frame,
            text=f"Tu puntuación final: {self.score}/{len(self.questions)}",
            font=("Helvetica", 18),
            text_color="#007AFF"
        ).pack(pady=(0, 10))

        ctk.CTkLabel(
            self.main_frame,
            text=f"Porcentaje: {percentage:.1f}%",
            font=("Helvetica", 18),
            text_color="#007AFF"
        ).pack(pady=(0, 30))

        # Botón para reiniciar
        ctk.CTkButton(
            self.main_frame,
            text="Reiniciar Quiz",
            font=("Helvetica", 14),
            fg_color="#007AFF",
            hover_color="#0056b3",
            height=40,
            command=self.restart_quiz
        ).pack(fill="x", padx=50)

    def restart_quiz(self):
        self.current_question = 0
        self.score = 0
        self.selected_answer = None
        self.seconds = 30
        self.timer_running = False

        # Recrear widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.create_widgets()
        self.load_question()
        self.start_timer()


if __name__ == "__main__":
    root = tk.Tk()
    app = ModernQuizApp(root)
    root.mainloop()