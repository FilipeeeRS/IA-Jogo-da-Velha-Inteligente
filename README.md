# Jogo da Velha com Agente Inteligente - Minimax

Trabalho desenvolvido para a disciplina de Inteligência Artificial e Aprendizado de Máquina da PUC-Campinas, Engenharia de Software.

O objetivo foi criar um agente inteligente capaz de jogar o Jogo da Velha de forma competitiva contra um usuário humano, utilizando o algoritmo Minimax.

---

## 🤖 Como o agente funciona

O agente usa o algoritmo Minimax, que simula todas as jogadas possíveis a partir do estado atual do tabuleiro e escolhe a que leva ao melhor resultado.

A lógica é a seguinte:
- O agente joga com O e tenta **maximizar** sua pontuação
- O usuário joga com X e o agente assume que ele também vai jogar da melhor forma possível (tentando minimizar a pontuação do agente)
- Quando chega num estado terminal (vitória, derrota ou empate), o algoritmo atribui um valor numérico e retorna subindo pela árvore

```
+10 - profundidade  →  agente venceu
-10 + profundidade  →  usuário venceu
      0             →  empate
```

O desconto/acréscimo pela profundidade faz o agente preferir vitórias rápidas e adiar derrotas o máximo possível.

---

## 📚 Conceitos envolvidos

| Conceito | Descrição |
|---|---|
| **Busca Competitiva** | Busca em ambientes com dois agentes de objetivos opostos |
| **Game Tree** | Árvore com todos os estados possíveis do jogo |
| **Minimax** | Algoritmo que percorre a Game Tree escolhendo o melhor movimento |
| **Backtracking** | Técnica de desfazer jogadas simuladas para testar outras opções |
