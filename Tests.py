import random

prob_enfermedad = 1 / 10000  # 1 en 10.000 personas esta enfermo
prob_sano = 1 - prob_enfermedad

falso_positivo = 0.02 #2%
falso_negativo = 0.01 #1%


def simulacion(n):
    total_positivos = 0
    enfermos_con_positivo = 0

    for i in range(n):
        #si enfermo 
        persona_enferma = random.random() < prob_enfermedad

        #resultado del test
        if persona_enferma:
            resultado_positivo = random.random() < (1 - falso_negativo)
        else:
            resultado_positivo = random.random() < falso_positivo

        #Si dio positivo si era verdadero o falso
        if resultado_positivo:
            total_positivos += 1
            if persona_enferma:
                enfermos_con_positivo += 1

    # Retornamos la proporción de positivos que realmente estaban enfermos
    if total_positivos == 0:
        return 0
    else:
        return enfermos_con_positivo / total_positivos

simulado = simulacion(1000000)
print ("prob simulacion: ", simulado)