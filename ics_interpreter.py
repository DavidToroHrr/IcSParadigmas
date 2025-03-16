from antlr4 import *
from IcSLexer import IcSLexer
from IcSParser import IcSParser
from IcSVisitor import IcSVisitor
from midiutil import MIDIFile

NOTE_MAPPING = {
    'A': 60,  # C4 (Do)
    'B': 62,  # D4 (Re)
    'C': 64,  # E4 (Mi)
    'D': 65,  # F4 (Fa)
    'E': 67,  # G4 (Sol)
    'F': 69,  # A4 (La)
    'G': 71   # B4 (Si)
}

class IcSInterpreter(IcSVisitor):  # Asegúrate de heredar del Visitor generado
    def visitProgram(self, ctx):
        print("¡Ejecutando visitProgram!")  # Depuración
        for stmt in ctx.statement():
            print(f"Visitando: {stmt.getText()}")  # Depuración
            self.visit(stmt)  # Visitar cada sentencia correctamente

    def visitWrite(self, ctx):
        print("Ejecutando visitWrite...")  # Depuración
        text = ctx.STRING().getText().strip('"')
        print(f"Salida: {text}")  # Imprimir correctamente

    def visitInstructionBlock(self, ctx):
        print("Ejecutando visitInstructionBlock...")  # Depuración
        instrucciones = [instr.getText() for instr in ctx.ID()]
        print(f"Instrucciones: {instrucciones}")

        midi = MIDIFile(1)  # Crear un archivo MIDI con 1 pista
        track = 0
        time = 0  # Empezamos en el segundo 0
        midi.addTrackName(track, time, "Melodía generada")
        midi.addTempo(track, time, 120)  # Tempo de 120 BPM

        for instruccion in instrucciones:
            if instruccion in NOTE_MAPPING:
                note = NOTE_MAPPING[instruccion]
                print(f"Agregando nota: {instruccion} ({note})")
                midi.addNote(track, channel=0, pitch=note, time=time, duration=1, volume=100)
                time += 1  # Avanzamos un tiempo para la siguiente nota

        # Guardar el archivo MIDI
        with open("melodia.mid", "wb") as output_file:
            midi.writeFile(output_file)

        print("Archivo MIDI generado: melodia.mid 🎶")


def main():
    print("Iniciando intérprete...")  # Depuración
    input_code = '''Main {
    <w> "Reproduciendo: Himno a la Alegría"
    [:] { E E F G G F E D C C D E E D D E E F G G F E D C C D E D C C }
}'''

    lexer = IcSLexer(InputStream(input_code))
    stream = CommonTokenStream(lexer)
    parser = IcSParser(stream)
    tree = parser.program()

    print(tree.toStringTree(recog=parser))  # Depuración

    interpreter = IcSInterpreter()
    interpreter.visit(tree)  # Se debe llamar visit(tree), no visitProgram

    print("Finalizando ejecución...")  # Depuración

if __name__ == "__main__":
    main()
