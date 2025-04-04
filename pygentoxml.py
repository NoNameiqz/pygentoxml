import csv


class Perguntas:
    def __init__(self,dificulty,question_type,question_name,question_text,answer,values):
        self.dificulty = dificulty
        self.question_type = question_type
        self.question_name = question_name 
        self.question_text = question_text
        self.answer = answer
        self.values = values



vetor_perguntas = []


with open("input.csv","r",encoding = "utf-8") as ficheiro:
    ficheiro_csv = csv.reader(ficheiro,delimiter=',')
    next(ficheiro_csv)
    for linha in ficheiro_csv:
        dificuldade, tipo, nome, texto, resposta, valores = linha
        vetor_perguntas.append(Perguntas(dificuldade,tipo,nome,texto,resposta,valores))


ficheiro_xml = open("quiz.xml","w",encoding="utf-8")
ficheiro_xml.write("<quiz>\n")
for i in range(len(vetor_perguntas)):
    ficheiro_xml.write(f"\t<question type=\"{vetor_perguntas[i].question_type}\">\n")
    ficheiro_xml.write(f"\t\t<name>\n\t\t\t<text>{vetor_perguntas[i].question_name}</text>\n\t\t</name>\n")
    ficheiro_xml.write(f"\t\t<questiontext format=\"html\">\n\t\t\t<text>{vetor_perguntas[i].question_text}</text>\n\t\t</questiontext>\n\t\t<shuffleanswers>true</shuffleanswers>\n")
        
    respostas = vetor_perguntas[i].answer.split(';') 
    valores = list(map(int,vetor_perguntas[i].values.split(';'))) 
    if vetor_perguntas[i].question_type == "multichoice":
        for j in range(4):
            ficheiro_xml.write(f"\t\t<answer fraction=\"{valores[j]}\">\n")
            ficheiro_xml.write(f"\t\t\t<text>{respostas[j]}</text>\n")
            ficheiro_xml.write(f"\t\t</answer>\n")
    else: 
       for j in range(2):
            ficheiro_xml.write(f"\t\t<answer fraction=\"{valores[j]}\">\n")
            ficheiro_xml.write(f"\t\t\t<text>{respostas[j]}</text>\n")
            ficheiro_xml.write(f"\t\t</answer>\n")
    ficheiro_xml.write("\t</question>\n")
ficheiro_xml.write("</quiz>\n")

ficheiro_xml.close()


