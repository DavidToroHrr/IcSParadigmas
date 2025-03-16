import tkinter as tk
from tkinter import messagebox, ttk
import winsound
from antlr4 import *
from midiutil import MIDIFile
from IcSLexer import IcSLexer
from IcSParser import IcSParser
from IcSVisitor import IcSVisitor

# 🎵 Mapeo de notas a MIDI
NOTE_MAPPING = {
    'C': 60,  # Do
    'C#': 61, # Do#
    'D': 62,  # Re
    'D#': 63, # Re#
    'E': 64,  # Mi
    'F': 65,  # Fa
    'F#': 66, # Fa#
    'G': 67,  # Sol
    'G#': 68, # Sol#
    'A': 69,  # La
    'A#': 70, # La#
    'B': 71   # Si
}


class IcSInterpreter(IcSVisitor):
    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitWrite(self, ctx):
        text = ctx.STRING().getText().strip('"')
        print(f"Salida: {text}")

    def visitInstructionBlock(self, ctx):
        instructions = [instr.getText() for instr in ctx.ID()]
        print(f"Instrucciones: {instructions}")

        # 🎶 Crear el archivo MIDI
        midi = MIDIFile(1)
        midi.addTempo(0, 0, 120)  # BPM
        time = 0

        for instr in instructions:
            if instr in NOTE_MAPPING:
                note = NOTE_MAPPING[instr]
                print(f"Agregando nota: {instr} ({note})")
                midi.addNote(0, 0, note, time, 1, 100)
                time += 1  # Avanzar el tiempo

        with open("melodia.mid", "wb") as output_file:
            midi.writeFile(output_file)

        # 🔔 Sonido de éxito
        winsound.Beep(1000, 300)
        messagebox.showinfo("Éxito", "🎵 ¡Archivo MIDI generado con éxito!")

# 🌟 Función para procesar las notas ingresadas
def procesar_notas():
    notas_usuario = entrada_notas.get()
    input_code = f'''Main {{
    <w> "Reproduciendo: Notas ingresadas"
    [:] {{ {notas_usuario} }}
}}'''

    lexer = IcSLexer(InputStream(input_code))
    stream = CommonTokenStream(lexer)
    parser = IcSParser(stream)
    tree = parser.program()

    interpreter = IcSInterpreter()
    interpreter.visit(tree)

# 🌟 Función para cambiar las notas según un ejemplo seleccionado
def seleccionar_ejemplo(event):
    entrada_notas.delete(0, tk.END)
    entrada_notas.insert(0, ejemplos_cb.get())

# 🎨 Crear la ventana con estilo
ventana = tk.Tk()
ventana.title("🎼 Generador de Música MIDI")
ventana.geometry("500x400")
ventana.configure(bg="#282c34")

# 🏷 Título
tk.Label(ventana, text="🎶 Ingrese las notas musicales:", font=("Arial", 14, "bold"), fg="white", bg="#282c34").pack(pady=10)

# 🎹 Entrada de notas
entrada_notas = tk.Entry(ventana, width=40, font=("Arial", 12))
entrada_notas.pack(pady=5)

# 📜 Lista de ejemplos
ejemplos = ["C D E F G", "E E F G G F E D", "E E F# G G F# E D C C D E E D Bb"]  # Canciones cortas
ejemplos_cb = ttk.Combobox(ventana, values=ejemplos, font=("Arial", 12), state="readonly")
ejemplos_cb.pack(pady=5)
ejemplos_cb.bind("<<ComboboxSelected>>", seleccionar_ejemplo)

# 🎛 Estilos del botón
def on_enter(e):
    boton_generar.config(bg="#61afef")

def on_leave(e):
    boton_generar.config(bg="#98c379")

# 🔘 Botón para generar MIDI
boton_generar = tk.Button(
    ventana, text="🎼 Generar MIDI", font=("Arial", 14, "bold"),
    bg="#98c379", fg="black", relief="flat", command=procesar_notas
)
boton_generar.pack(pady=20)
boton_generar.bind("<Enter>", on_enter)
boton_generar.bind("<Leave>", on_leave)

# 🔵 Ejecutar la interfaz
ventana.mainloop()
