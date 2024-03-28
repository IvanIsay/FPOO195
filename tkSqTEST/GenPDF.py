from fpdf import FPDF
from Controlador import *
objCont2= Controlador()

class GenPDF(FPDF):
    

    def header(self):
        self.set_font("Arial", "BU", 14)
        self.cell(0, 10, "Usuarios Registrados ", 0, 1, "C")
       
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, "Página %s" % self.page_no(), 0, 0, "C")

    def chapter_body(self):
        self.set_font("Arial", "I", 10)
        self.set_fill_color(135,206,235)
        listaUsuarios= objCont2.todosUsuarios()
        self.multi_cell(100, 10,"ID:  "+"Usuario:   "+ "Correo:   ", 1,'C',1)
        for i in listaUsuarios:
            self.multi_cell(100, 10, str(i[0])+"  "+i[1]+"  "+i[2], 1,'C',0)



""" pdf = GenPDF()
pdf.add_page()
pdf.chapter_body()
pdf.output("Usuarios.pdf") """

