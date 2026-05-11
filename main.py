import csv
import time

# soma teste
def soma_pares_original(lista):
    resultado = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            resultado = resultado + lista[i]
    return resultado


def soma_pares_otimizado(lista):
    return sum(x for x in lista if x % 2 == 0)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(soma_pares_original(numeros))
print(soma_pares_otimizado(numeros))


# lista grande para benchmark
grande = list(range(1, 100_001))

repeticoes = 10_000

tempos_original = []
tempos_otimizado = []

resultado_original = None
resultado_otimizado = None

with open("resultado_benchmark.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow([
        "execucao",
        "tempo_original",
        "resultado_original",
        "tempo_otimizado",
        "resultado_otimizado"
    ])

    for i in range(1, repeticoes + 1):
        inicio = time.perf_counter()
        resultado_original = soma_pares_original(grande)
        fim = time.perf_counter()

        tempo_original = fim - inicio
        tempos_original.append(tempo_original)

        inicio = time.perf_counter()
        resultado_otimizado = soma_pares_otimizado(grande)
        fim = time.perf_counter()

        tempo_otimizado = fim - inicio
        tempos_otimizado.append(tempo_otimizado)

        escritor.writerow([
            i,
            tempo_original,
            resultado_original,
            tempo_otimizado,
            resultado_otimizado
        ])

    media_original = sum(tempos_original) / len(tempos_original)
    media_otimizado = sum(tempos_otimizado) / len(tempos_otimizado)

    escritor.writerow([])
    escritor.writerow(["MEDIA"])
    escritor.writerow(["media_original", media_original])
    escritor.writerow(["media_otimizado", media_otimizado])


print("CSV gerado com sucesso: resultado_benchmark.csv")
print(f"Resultado original: {resultado_original}")
print(f"Resultado otimizado: {resultado_otimizado}")
print(f"Média original: {media_original:.8f}s")
print(f"Média otimizado: {media_otimizado:.8f}s")