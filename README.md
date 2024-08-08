# O Salão dos Barbeiros Dorminhocos

Este projeto implementa a sincronização de processos utilizando semáforos, inspirado no clássico problema do "Barbeiro Dorminhoco". A proposta é simular o funcionamento de um salão de barbeiros, onde os barbeiros dormem quando não há clientes e acordam para atender quando um cliente chega. O projeto aborda conceitos importantes de computação, como exclusão mútua, deadlock, starvation e sincronização.

## Cenário

O salão de barbeiros é composto por:

- **3 Barbeiros**: Dormem quando não há clientes para atender e acordam quando um cliente chega.
- **5 Cadeiras de Espera**: Os clientes aguardam nessas cadeiras se todos os barbeiros estiverem ocupados. Se todas as cadeiras estiverem ocupadas, o cliente vai embora sem cortar o cabelo.
- **Clientes**: Chegam aleatoriamente ao salão. Se encontrarem uma cadeira de espera disponível, aguardam sua vez de ser atendidos. Caso contrário, deixam o salão sem receber atendimento.
  
## Funcionamento

![Frame 101 (1)](https://github.com/user-attachments/assets/3388fea4-65a5-4cff-9297-3186051ddc67)

## Funcionalidades

- **Sincronização de Processos**: Gerenciamento das operações dos barbeiros e clientes, garantindo que não ocorram condições de corrida.
- **Exclusão Mútua**: Uso de semáforos para assegurar que os barbeiros atendam um cliente por vez e que os clientes acessem as cadeiras de espera de maneira controlada.
- **Prevenção de Deadlock**: O programa é projetado para evitar situações em que barbeiros ou clientes possam ficar permanentemente bloqueados, incapazes de prosseguir.
- **Starvation**: O algoritmo minimiza a chance de starvation, garantindo que os clientes sejam atendidos de forma justa e dentro das possibilidades do salão.
- **Simulação Aleatória**: A chegada dos clientes ao salão é simulada de forma aleatória, imitando um fluxo de clientes realista.

## Objetivos

O principal objetivo deste projeto é ilustrar como problemas clássicos de sincronização podem ser resolvidos utilizando semáforos, abordando os desafios de exclusão mútua e prevenção de deadlock e starvation.

## Tecnologias Utilizadas

- Linguagem de programação: Python
- Semáforos para sincronização de processos.
- Bibliotecas: threading, time e random
