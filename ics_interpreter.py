import tkinter as tk
from tkinter import messagebox, ttk
import winsound
from midiutil import MIDIFile

# 🎵 Mapeo de notas a MIDI
NOTE_MAPPING = {
    'C': 60, 'C#': 61, 'D': 62, 'D#': 63, 'E': 64, 'F': 65, 'F#': 66,
    'G': 67, 'G#': 68, 'A': 69, 'A#': 70, 'B': 71
}

class VirtualPianoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎼 Teclado Virtual - Generador MIDI")
        self.root.geometry("500x450")
        self.root.configure(bg="#282c34")

        # 🏷 Título
        tk.Label(root, text="🎶 Selecciona notas musicales:", font=("Arial", 14, "bold"), fg="white", bg="#282c34").pack(pady=10)

        # 🎹 Campo de notas (Deshabilitado para entrada manual)
        self.note_display = tk.Entry(root, font=("Arial", 12), width=40, bg="white", fg="black", justify="center", state="disabled")
        self.note_display.pack(pady=5)

        # 🎼 Teclado Virtual
        self.create_virtual_keyboard()

        # 📜 Lista de ejemplos predefinidos
        ejemplos = ["C D E F G", "E E F G G F E D", "E E F# G G F# E D C C D E E D Bb"]
        self.ejemplos_cb = ttk.Combobox(root, values=ejemplos, font=("Arial", 12), state="readonly")
        self.ejemplos_cb.pack(pady=5)
        self.ejemplos_cb.bind("<<ComboboxSelected>>", self.seleccionar_ejemplo)

        # 🔘 Botón para generar MIDI
        self.boton_generar = tk.Button(
            root, text="🎼 Generar MIDI", font=("Arial", 14, "bold"),
            bg="#98c379", fg="black", relief="flat", command=self.save_to_midi
        )
        self.boton_generar.pack(pady=10)

        # 🗑 Botones para borrar notas
        self.boton_borrar_ultima = tk.Button(
            root, text="🗑 Borrar Última Nota", font=("Arial", 12),
            bg="#e06c75", fg="black", relief="flat", command=self.borrar_ultima
        )
        self.boton_borrar_ultima.pack(pady=5)

        self.boton_borrar_todo = tk.Button(
            root, text="🚮 Borrar Todo", font=("Arial", 12),
            bg="#be5046", fg="black", relief="flat", command=self.borrar_todo
        )
        self.boton_borrar_todo.pack(pady=5)

    def create_virtual_keyboard(self):
        """ Crea los botones del piano """
        white_keys = [('C', 0), ('D', 1), ('E', 2), ('F', 3), ('G', 4), ('A', 5), ('B', 6)]
        black_keys = [('C#', 0.7), ('D#', 1.7), ('F#', 3.7), ('G#', 4.7), ('A#', 5.7)]

        # Botones para las teclas blancas
        for note, col in white_keys:
            btn = tk.Button(
                self.root, text=note, font=("Arial", 14), width=5, height=2, bg="white", fg="black",
                command=lambda n=note: self.add_note(n)
            )
            btn.place(x=50 + col * 55, y=200)

        # Botones para las teclas negras
        for note, col in black_keys:
            btn = tk.Button(
                self.root, text=note, font=("Arial", 12), width=3, height=2, bg="black", fg="white",
                command=lambda n=note: self.add_note(n)
            )
            btn.place(x=80 + col * 55, y=170)

    def add_note(self, note):
        """ Agrega una nota desde el teclado virtual """
        current_text = self.note_display.get()
        self.note_display.config(state="normal")  # Habilita la edición
        self.note_display.delete(0, tk.END)
        self.note_display.insert(0, (current_text + " " + note).strip())
        self.note_display.config(state="disabled")  # Vuelve a deshabilitar

    def borrar_ultima(self):
        """ Borra la última nota agregada """
        current_text = self.note_display.get().strip().split()
        if current_text:
            current_text.pop()  # Elimina la última nota
            self.note_display.config(state="normal")
            self.note_display.delete(0, tk.END)
            self.note_display.insert(0, " ".join(current_text))
            self.note_display.config(state="disabled")

    def borrar_todo(self):
        """ Borra todas las notas del campo """
        self.note_display.config(state="normal")
        self.note_display.delete(0, tk.END)
        self.note_display.config(state="disabled")

    def seleccionar_ejemplo(self, event):
        """ Cambia las notas a un ejemplo seleccionado """
        self.note_display.config(state="normal")
        self.note_display.delete(0, tk.END)
        self.note_display.insert(0, self.ejemplos_cb.get())
        self.note_display.config(state="disabled")

    def save_to_midi(self):
        """ Genera y guarda un archivo MIDI con las notas ingresadas """
        notas = self.note_display.get().strip().split()
        if not notas:
            messagebox.showwarning("⚠️ Advertencia", "No hay notas seleccionadas.")
            return

        # 🎶 Crear el archivo MIDI
        midi = MIDIFile(1)
        midi.addTempo(0, 0, 120)  # BPM
        time = 0

        for nota in notas:
            if nota in NOTE_MAPPING:
                note_value = NOTE_MAPPING[nota]
                midi.addNote(0, 0, note_value, time, 1, 100)
                time += 1  # Avanza el tiempo

        with open("melodia.mid", "wb") as output_file:
            midi.writeFile(output_file)

        # 🔔 Sonido de confirmación
        winsound.Beep(1000, 300)
        messagebox.showinfo("Éxito", "🎵 ¡Archivo MIDI generado con éxito!")

# 🔵 Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualPianoApp(root)
    root.mainloop()
