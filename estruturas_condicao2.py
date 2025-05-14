#Elif: "senao se" ,E usado quando temos mais de 2 possibilidades , assim ele testa o "if" , se o "if" for falso, ele testa o proximo "elif".
#se nenhum if ou elif for verdadeiro, ele cai no else.

tempoExperiencia = 1
if tempoExperiencia < 2:
    print('Nível de conhecimento júnior.')
elif tempoExperiencia <= 5:
    print('Nível de conhecimento pleno.')
else:
    print('Nível de conhecimento sênior.')
#---------------------------------------------------------------#
tempoExperiencia = 3
if tempoExperiencia < 2:
    print('Nível de conhecimento júnior.')
elif tempoExperiencia <= 5:
    print('Nível de conhecimento pleno.')
else:
    print('Nível de conhecimento sênior.')
#---------------------------------------------------------------#
tempoExperiencia = 6
if tempoExperiencia < 2:
    print('Nível de conhecimento júnior.')
elif tempoExperiencia <= 5:
    print('Nível de conhecimento pleno.')
else:
    print('Nível de conhecimento sênior.')
