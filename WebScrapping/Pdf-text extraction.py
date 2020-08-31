import PyPDF2 as p

file = open("C:/Users/gaurav sahani/Desktop/Gaurav Resume/DOC-20190629-WA0032.pdf", "rb")

pd = p.PdfFileReader(file)

x = pd.getPage(0)

print(x.extractText())