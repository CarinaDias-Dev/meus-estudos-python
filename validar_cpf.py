def validar_cpf(cpf):
    #Remover carecteres não numéricos.
    cpf = ''.join(filter(str.isdigit, cpf))


    #Verificando se o cpf possui 11 dígitos.
    if len(cpf) != 11:
        return False


    #Verificando se todos os dígitos são iguais (caso raro, mas inválido)
    if cpf == cpf[0] * 11:
        return False


    #Calculando o primeiro digito verificador.
    soma = sum(int(cpf[i]) * (10 - i)for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11-resto


    #Verificando o primeiro dígito verificador
    if int(cpf[9]) != digito_verificador_1:
        return False
    return True

#Programa Principa.
cpf ='12.442.956-55'
if validar_cpf(cpf):
    print(f'O cpf {cpf} é válido.')
else:
    print(f'O cpf {cpf} é inválido.')
