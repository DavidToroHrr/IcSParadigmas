import sys
from antlr4 import *
from IcSLexer import IcSLexer
from IcSParser import IcSParser
from IcSVisitor import IcSVisitor
from midiutil import MIDIFile  # Importar la librería MIDIUtil


class IcSInterpreter(IcSVisitor):
    def __init__(self):
        self.variables = {}

    def visitMusicStmt(self, ctx: IcSParser.MusicStmtContext):
            notas = [nota.getText().upper() for nota in ctx.ID()]  # Convertir a mayúsculas
            print(f"DEBUG: Reproduciendo música con notas: {notas}")

            # 🎵 Mapeo de notas a MIDI
            NOTE_MAPPING = {
                'C': 60, 'C#': 61, 'D': 62, 'D#': 63, 'E': 64, 'F': 65, 'F#': 66,
                'G': 67, 'G#': 68, 'A': 69, 'A#': 70, 'B': 71
            }

            # Crear archivo MIDI
            midi = MIDIFile(1)
            midi.addTempo(0, 0, 120)

            tiempo = 0  # Tiempo inicial en beats
            for nota in notas:
                if nota in NOTE_MAPPING:
                    midi.addNote(0, 0, NOTE_MAPPING[nota], tiempo, 1, 100)
                    tiempo += 1
                else:
                    print(f"ERROR: Nota desconocida '{nota}', ignorada.")

            # Guardar el archivo MIDI
            with open("melodia.mid", "wb") as output_file:
                midi.writeFile(output_file)
            
            print("DEBUG: Archivo MIDI generado como 'melodia.mid'")

    def visitProgram(self, ctx: IcSParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitPrintStatement(self, ctx: IcSParser.PrintStatementContext):
        if ctx.printStmt().STRING():
            print(ctx.printStmt().STRING().getText().strip('"'))
        else:
            print(self.visit(ctx.printStmt().expr()))

    def visitReadStatement(self, ctx: IcSParser.ReadStatementContext):
        var_name = ctx.readStmt().ID().getText()
        user_input = input().strip()  
        try:
            self.variables[var_name] = int(user_input)  
        except ValueError:
            print(f"Error: '{user_input}' no es un número válido.")
            self.variables[var_name] = 0  # Asignar un valor por defecto

    def visitAssignmentStatement(self, ctx: IcSParser.AssignmentStatementContext):
        var_name = ctx.assignStmt().ID().getText()
        value = self.visit(ctx.assignStmt().expr())
        self.variables[var_name] = value

        # 🔴 Debug: Mostrar el valor de la variable asignada
        print(f"DEBUG: {var_name} = {value}")


    def visitNumberExpr(self, ctx: IcSParser.NumberExprContext):
        return int(ctx.NUMBER().getText())

    def visitVariableExpr(self, ctx: IcSParser.VariableExprContext):
        var_name = ctx.ID().getText()
        return self.variables.get(var_name, 0)

    def visitArithmeticExpr(self, ctx: IcSParser.ArithmeticExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '+': return left + right
        if op == '-': return left - right
        if op == '*': return left * right
        if op == '/':
            if right == 0:
                raise ValueError("División por cero")
            return left / right

    def visitRelationalExpr(self, ctx: IcSParser.RelationalExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '>': return left > right
        if op == '<': return left < right
        if op == '>=': return left >= right
        if op == '<=': return left <= right
        if op == '==': return left == right
        if op == '!=': return left != right
        return False

    def visitIfStmt(self, ctx: IcSParser.IfStmtContext):
        condition = self.visit(ctx.expr())  
        print(f"DEBUG: Evaluando If con condición: {condition}")  

        if condition:
            for stmt in ctx.statement():  # Ejecuta el bloque del 'if'
                self.visit(stmt)
        elif ctx.elseStmt():  # Verificar si hay un bloque else
            print("DEBUG: Ejecutando bloque ELSE")  
            for stmt in ctx.elseStmt().statement():
                self.visit(stmt)





    def visitWhileStmt(self, ctx: IcSParser.WhileStmtContext):
        while self.visit(ctx.expr()):
            for stmt in ctx.statement():
                self.visit(stmt)

    

def ejecutar_codigo(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            codigo = f.read().strip()

        input_stream = InputStream(codigo)
        lexer = IcSLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = IcSParser(stream)
        tree = parser.program()

        visitor = IcSInterpreter()
        visitor.visit(tree)

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'")
    except Exception as e:
        print(f"Error durante la ejecución: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python ejecutar.py archivo.ics")
    else:
        ejecutar_codigo(sys.argv[1])
