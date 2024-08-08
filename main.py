import threading
import time
import random

# Constantes
NUM_BARBEIROS = 3  # Número de barbeiros disponíveis
NUM_CADEIRAS = 5   # Número de cadeiras de espera no salão

# Semáforos e Mutex
clientes = threading.Semaphore(0)  # Semáforo para gerenciar a fila de clientes (inicialmente sem clientes)
barbeiros = threading.Semaphore(0)  # Semáforo para gerenciar a disponibilidade dos barbeiros (inicialmente todos ocupados)
acesso_cadeiras = threading.Lock()  # Mutex para proteger o acesso às cadeiras de espera

# Variáveis de controle
numero_de_cadeiras_livres = NUM_CADEIRAS  # Contador de cadeiras de espera disponíveis
cadeira_cliente = [None] * NUM_CADEIRAS  # Lista para armazenar os IDs dos clientes nas cadeiras
proxima_cadeira = 0  # Índice para a próxima posição disponível na cadeira
proximo_cliente = 0  # Índice para o próximo cliente a ser atendido

def barbeiro(id_barbeiro):
    global proximo_cliente
    while True:
        barbeiros.acquire()  # O barbeiro espera até que um cliente esteja disponível
        print(f"Barbeiro {id_barbeiro} está atendendo um cliente.")
        
        acesso_cadeiras.acquire()  # Protege a modificação das cadeiras
        proximo_cliente = (proximo_cliente + 1) % NUM_CADEIRAS  # Seleciona o próximo cliente na fila
        id_cliente = cadeira_cliente[proximo_cliente]  # Obtém o ID do próximo cliente
        cadeira_cliente[proximo_cliente] = id_barbeiro  # O barbeiro ocupa a cadeira (substitui o ID do cliente)
        acesso_cadeiras.release()  # Libera o acesso às cadeiras
        
        clientes.release()  # Acorda o cliente selecionado para ser atendido

        # Simula o corte de cabelo
        print(f"Cliente {id_cliente} está sendo atendido pelo barbeiro {id_barbeiro}.")
        time.sleep(random.uniform(5,10))  # Simula o tempo de atendimento com um intervalo aleatório
        print(f"Barbeiro {id_barbeiro} terminou de atender e está pronto para o próximo cliente.")

def cliente(id_cliente):
    global proxima_cadeira, numero_de_cadeiras_livres
    print(f"Cliente {id_cliente} chegou.")
    
    acesso_cadeiras.acquire()  # Protege a modificação das cadeiras
    if numero_de_cadeiras_livres > 0:  # Verifica se há cadeiras disponíveis
        numero_de_cadeiras_livres -= 1  # O cliente ocupa uma cadeira
        proxima_cadeira = (proxima_cadeira + 1) % NUM_CADEIRAS  # Atualiza o índice para a próxima cadeira
        cadeira_cliente[proxima_cadeira] = id_cliente  # Armazena o ID do cliente na cadeira
        print(f"Cliente {id_cliente} sentou na cadeira de espera.")
        acesso_cadeiras.release()  # Libera o acesso às cadeiras
        
        barbeiros.release()  # Acorda um barbeiro disponível
        clientes.acquire()  # O cliente espera até ser atendido pelo barbeiro
        
        acesso_cadeiras.acquire()  # Protege a modificação das cadeiras
        id_barbeiro = cadeira_cliente[proxima_cadeira]  # Obtém o ID do barbeiro que está atendendo
        numero_de_cadeiras_livres += 1  # O cliente deixa a cadeira após o atendimento
        acesso_cadeiras.release()  # Libera o acesso às cadeiras
        
        # Simula o término do atendimento
        print(f"Cliente {id_cliente} terminou o corte de cabelo e saiu.")
    else:
        acesso_cadeiras.release()  # Libera o acesso às cadeiras se não houver lugar
        print(f"Cliente {id_cliente} foi embora sem ser atendido, não há cadeiras de espera disponíveis.")

# Cria e inicia threads para os barbeiros
threads_barbeiros = [threading.Thread(target=barbeiro, args=(i,)) for i in range(NUM_BARBEIROS)]
for thread in threads_barbeiros:
    thread.start()

# Simula a chegada de clientes em intervalos aleatórios
id_cliente = 0
while True:
    time.sleep(random.uniform(0.5, 2))  # Intervalo aleatório entre chegadas de clientes
    threading.Thread(target=cliente, args=(id_cliente,)).start()  # Cria uma nova thread para cada cliente
    id_cliente += 1  # Incrementa o ID do cliente para o próximo cliente
