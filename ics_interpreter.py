from antlr4 import *
from IcSLexer import IcSLexer
from IcSParser import IcSParser
from IcSVisitor import IcSVisitor
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
        instructions = [instr.getText() for instr in ctx.ID()]
        print(f"Instrucciones: {instructions}")

def main():
    print("Iniciando intérprete...")  # Depuración
    input_code = '''Main {
    <w> "Hola, Mundo"
    [:] { A B C }
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
