import hashlib
import multiprocessing
import time

hash_alvo = "ca6ae33116b93e57b87810a27296fc36"
total = 1000000000

def gerar_md5(texto):
    return hashlib.md5(texto.encode()).hexdigest()

def quebrar_hash(inicio, fim, processo_id, inicio_tempo):

    for i in range(inicio, fim):

        senha = f"{i:09d}"

        if gerar_md5(senha) == hash_alvo:

            tempo_total = time.time() - inicio_tempo

            print(f"\nSenha encontrada pelo Processo {processo_id}: {senha}")
            print(f"Tempo total: {tempo_total:.2f} segundos")

            return

        if i % 1000000 == 0 and i != inicio:

            tempo_decorrido = time.time() - inicio_tempo

            print(f"Processo {processo_id} | Tentativas: {i} | Tempo: {tempo_decorrido:.2f}s")


def executar():

    num_processos = 4
    intervalo = total // num_processos
    processos = []

    inicio_tempo = time.time()

    for i in range(num_processos):

        inicio = i * intervalo
        fim = total if i == num_processos - 1 else (i + 1) * intervalo

        p = multiprocessing.Process(
            target=quebrar_hash,
            args=(inicio, fim, i + 1, inicio_tempo)
        )

        processos.append(p)
        p.start()

    for p in processos:
        p.join()

    tempo_total = time.time() - inicio_tempo

    print("\nTempo total:", tempo_total, "segundos")


if __name__ == "__main__":
    executar()