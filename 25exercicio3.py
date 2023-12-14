def divisao(entrada):
    try:
        #raise ValueError
        resposta = 1 / entrada
        print("Resposta =", resposta)
    except ZeroDivisionError:
        print("Não existe divisão por zero. Por favor rode de novo e insira um valor diferente.")
    except TypeError:
        print("Tipo de variável inválida. Por favor rode de novo e insira um número.")
    except Exception as erro:
        print(f"Foi detectado o erro {type(erro).__name__}. Tome as devidas providências na próxima vez que rodar o código.")
    finally:
        print("Renan Rigolon Coelho Pinto")

divisao(2)
divisao(0)
divisao('string')
