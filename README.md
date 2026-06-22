Este projeto foi criado para organizar informações relacionadas a times de futebol. O sistema permite cadastrar técnicos, patrocinadores e os próprios times, facilitando o armazenamento e a consulta dessas informações.

Estrutura do Banco de Dados

O sistema possui três tabelas principais: Tecnico, Patrocinador e Time.

A tabela Tecnico armazena os dados dos treinadores, como nome, nacionalidade e idade.

A tabela Patrocinador armazena os dados dos patrocinadores, incluindo nome e valor do contrato.

A tabela Time armazena as informações dos clubes, como nome, cidade, estádio e ano de fundação. Além disso, ela faz a ligação com as tabelas de Técnicos e Patrocinadores.

Foi utilizado um relacionamento do tipo ForeignKey entre Time e Tecnico, pois um técnico pode estar associado a vários times, enquanto cada time possui apenas um técnico.

Também foi utilizado um relacionamento do tipo ManyToManyField entre Time e Patrocinador, já que um time pode ter vários patrocinadores e um patrocinador pode patrocinar vários times.

Justificativa Técnica

No modelo Time, utilizei on_delete=models.SET_NULL no relacionamento com Tecnico porque, caso um técnico seja excluído do sistema, não é necessário excluir o time junto com ele. Dessa forma, o time continua cadastrado e outro técnico pode ser associado posteriormente.

Impacto da Escolha

Se um registro da tabela Tecnico for excluído, os times relacionados continuarão existindo normalmente no banco de dados. Apenas a referência ao técnico ficará vazia. Isso evita a perda de informações importantes sobre os clubes e torna o sistema mais flexível.
