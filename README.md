# ♟️ Desafio - Movimentando as Peças do Xadrez

Trabalho da disciplina **Introdução à Programação de Computadores** – Curso de **Análise e Desenvolvimento de Sistemas (Estácio)**.

O objetivo deste projeto é implementar em Python a lógica de movimentação das principais peças do **xadrez**, sem a necessidade de interface gráfica, apenas simulando as jogadas possíveis no tabuleiro.

---

## 📌 Peças Implementadas
Cada peça foi representada por uma classe em Python, herdando da classe base `Peca`.  
As regras implementadas foram:

- **Rei (♔)** → Move 1 casa em qualquer direção.  
- **Rainha (♕)** → Combina movimentos de Torre + Bispo.  
- **Torre (♖)** → Move em linha reta (horizontal e vertical).  
- **Bispo (♗)** → Move em diagonais.  
- **Cavalo (♘)** → Move em "L" (2 casas em uma direção + 1 perpendicular).  
- **Peão (♙)** → Move 1 casa para frente (ou 2 se for o primeiro movimento) e captura em diagonal.

---

## 📂 Estrutura do Projeto

