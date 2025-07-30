# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input("Informe o seu nome o seu nome: ")
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = input("Informe o total de dias de estudo por semana: ")
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = input("Informe a média de horas estudadas por dia: ")
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input("Informe o curso desejado: ")
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
total_dias = int(total_dias)
total_horas = int(total_horas)
print(f'O nome do estudante é {nome}. Ele estuda {total_horas} horas por dia, {total_dias} dias por semana, ou seja, no total, ele estuda {total_horas * total_dias} horas por semana. O curso dele é o {curso}.')