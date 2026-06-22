# Sistema de Gerenciamento de Times de Futebol

## Descrição do Tema

Este projeto foi criado para organizar informações relacionadas a times de futebol. O sistema permite cadastrar técnicos, patrocinadores e os próprios times, facilitando o armazenamento e a consulta dessas informações.

## Estrutura do Banco de Dados

O sistema possui três tabelas principais:

### Tecnico

Armazena os dados dos treinadores, como nome, nacionalidade e idade.

### Patrocinador

Armazena os dados dos patrocinadores, incluindo nome e valor do contrato.

### Time

Armazena as informações dos clubes, como nome, cidade, estádio e ano de fundação. Além disso, faz a ligação com as tabelas de Técnicos e Patrocinadores.

### Relacionamentos

* Um técnico pode estar associado a vários times, enquanto cada time possui apenas um técnico. Para isso, foi utilizado um relacionamento do tipo ForeignKey.

* Um time pode ter vários patrocinadores e um patrocinador pode patrocinar vários times. Para isso, foi utilizado um relacionamento do tipo ManyToManyField.

## Justificativa Técnica

No modelo Time, usei `on_delete=models.SET_NULL` no relacionamento com Tecnico porque, caso um técnico seja excluído do sistema, não é necessário excluir o time. Apenas o campo referente ao técnico fica vazio, permitindo que outro treinador seja associado posteriormente.

## Impacto da Escolha

Se um registro da tabela Tecnico for excluído, os times relacionados continuarão existindo normalmente no banco de dados. Apenas a referência ao técnico será removida, evitando a perda de informações importantes sobre os clubes.
