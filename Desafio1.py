def verificaSenha (senha):
    resultado = True
    if len(senha) < 7:
        resultado = False
        print ("O tamanho está inadequado!")
    else:
        if senha.lower()==senha or senha.upper() == senha:
            resultado = False
            print ("Está faltando uma letra minuscula ou maiuscula!")
        
        else:
            contadorDeDigitoEspecial = 0
            especiais = "!@#$%"
            for digito in especiais:
                if digito in senha:
                    contadorDeDigitoEspecial += 1
            
            if contadorDeDigitoEspecial == 0:
                print ("Está faltando um caractere especial!")
                resultado = False
            else:
                resultado == True
    return resultado

senha = str(input("""
Digite uma senha de acordo com as seguintes regras:
1.Deve conter pelo menos 8 caracteres.
2.Deve conter pelo menos uma letra maiuscula e uma minuscula.
3.Deve conter pelo menos um caractere especial(considere apenas esses: ! @ # $ %).
                  
"""))

if verificaSenha(senha)==True:
    print("Senha válida!")
else:
    print("Senha inválida!")
