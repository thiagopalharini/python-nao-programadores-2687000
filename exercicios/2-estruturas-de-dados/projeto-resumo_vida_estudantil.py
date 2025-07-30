# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
dados = {}

dados["nome"] = input("Informe o seu nome: ")
dados["anoLinkedin"] = int(input("Informe o ano em que você conheceu o Linkdin: "))
dados["anoAtual"] = int(input("Informe o ano atual: "))
cursos = input("Informe os seus cursos (separados por vírgula): ")

dados["cursos"] = cursos.split(", ")

# 2. Armazene esses dados em um dicionário

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

totalAnos = dados["anoAtual"] - dados["anoLinkedin"]
totalCursos = len(dados["cursos"])

print(f"Seu nome é {dados['nome']}. Você conheceu o Linkedin em {dados['anoLinkedin']}, portanto, faz {totalAnos}. Você tem um total de {totalCursos} cursos. Seu primeiro curso é {dados['cursos'][0]} e seu último curso é {dados['cursos'][3]}.")