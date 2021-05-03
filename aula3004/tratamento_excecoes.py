# exemplo1
try:                                # obrigatório nesse caso
    numerador = 10
    denominador = 0
    resultado = numerador/denominador  # zero division error --> divisão por zero
    print(resultado)
except:                            # obrigatório nesse caso
    print("Saida pela tangente")
finally:                           # opcional ( normalmente não o usamos)
    print("Tchau")        # executa independente de haver ou não exceção