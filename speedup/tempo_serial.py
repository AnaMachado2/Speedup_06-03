import hashlib
import time

hash_alvo = "ca6ae33116b93e57b87810a27296fc36"
total = 1000000000

def gerar_md5(texto):
    return hashlib.md5(texto.encode()).hexdigest()

def quebrar_hash():

    inicio = time.time()

    for i in range(total):

        senha = f"{i:09d}"

        if gerar_md5(senha) == hash_alvo:
            print("\nSenha encontrada:", senha)
            return

        # Mostrar progresso a cada 1 milhão de tentativas
        if i % 1000000 == 0 and i != 0:
            tempo_atual = time.time()
            tempo_decorrido = tempo_atual - inicio

            print(f"Tentativas: {i} | Tempo decorrido: {tempo_decorrido:.2f} segundos")

def executar():

    inicio_total = time.time()

    quebrar_hash()

    fim_total = time.time()

    print("\nTempo total:", fim_total - inicio_total, "segundos")

executar()


#350 segundos 