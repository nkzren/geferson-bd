```
Universidade de São Paulo
Escola de Artes, Ciências e Humanidades
Disciplina: Banco de Dados 2
Profa. Fátima Nunes
Prof. Luciano Araújo
```
```
Enunciado do trabalho
```
Este trabalho deve ser desenvolvido em grupos de quatro alunos. Grupos menores podem ser formados,
mas a avaliação não considerará o número de integrantes do grupo, isto é, a avaliação seguirá os
mesmos critérios quantitativos e qualitativos para todos os trabalhos, independentemente da
quantidade de integrantes da equipe.

Todos os artefatos produzidos neste trabalho deverão ser postados na plataforma adotada pelo
professor da sua turma, e-Disciplinas ou taqui, em área específica. Formatos de arquivos, quando
solicitados (por exemplo: PDF), devem ser obedecidos.

A data máxima para entrega do trabalho é especificada no plano de aulas, mas os grupos podem postar
os artefatos na plataforma, E-DISCIPLINAS ou taqui, a qualquer momento. Entregas após a data não
serão aceitas e receberão nota zero para a etapa ausente. **O grupo que deixar de realizar a entrega final
(terceira entrega)** até a data estabelecida receberá nota zero e os integrantes estão reprovados na
disciplina.

O trabalho será composto de várias partes e envolverá o uso de um SGBD. Ao final, deve ser obtido um
sistema funcional usando SGBD. O grupo pode escolher o SGBD que usará, mas não é permitido o uso de
_frameworks_ (tais como _Hibernate_ e similares). É interessante que o grupo escolha um SGBD que tenha
suporte a orientação a objetos, visto que este assunto compõe uma etapa do trabalho. Para a correção
do trabalho, pode ser necessário que o grupo prepare uma máquina com todas as instalações
necessárias para execução dos artefatos de software desenvolvidos. O grupo será convocado a
apresentar essa preparação, quando da avaliação do trabalho, se for necessário.

**Em todos os casos de dúvidas o grupo não deve deixar para recorrer à ajuda próxima da entrega do
trabalho, visto que alguns problemas nem sempre podem ser resolvidos na hora.**

**Se necessário, este documento será atualizado, com inserção ou adequação de conteúdo. Portanto, os
grupos devem constantemente consultar este documento para guiar o desenvolvimento do seu
trabalho. Nenhum conteúdo referente a etapas já entregues será alterado.**


## PARTE I: DESCRIÇÃO DO PROBLEMA

Nesta etapa o grupo deverá entregar a análise de requisitos e diagramas referentes ao problema
abordado.

**ARTEFATOS A SEREM ENTREGUES:**

**a)** **_(artefato do tipo texto)_** O grupo deve escolher um contexto no qual seja possível desenvolvimento de
um sistema de banco de dados. Este contexto deverá ser especificado textualmente, de forma concisa,
com a finalidade de documentar os principais requisitos do sistema. É esperado um texto com cerca de
5 parágrafos (com cerca de 8 linhas em cada parágrafo) usando fonte Calibri, tamanho 10 (como neste
documento, inclusive com este tipo de margem (Superior e Inferior: 2,5 cm / Esquerda e Direita: 3,0 cm)
e espaçamento de 1,15 entre linhas). **Este artefato deve ser entregue na plataforma em uso pelo
professor da sua turma (e-Disciplinas ou taqui) em formato PDF.**

_Obs. 1 : descrições textuais mais detalhadas serão solicitadas quando necessário, dentro das
especificações das diferentes partes do trabalho._

_Obs. 2: o contexto pode ser o mesmo usado na disciplina de Banco de Dados, inclusive os alunos podem
"aproveitar" os artefatos de softwares já desenvolvidos, apenas adequando-os para contemplar as
exigências especificadas para este trabalho._

**b)** **_(artefato do tipo diagrama)_** apresentar um Modelo Entidade-Relacionamento (conjuntos-entidade,
conjuntos-relacionamento, atributos, chaves primárias), contendo no mínimo 10 conjuntos-entidade
fortes, 1 conjunto-entidade fraca, 1 relacionamento de generalização-especialização. Este modelo
deverá ser implementado em uma ferramenta CASE que suporte este tipo de modelo. Recomenda-se
fortemente a escolha de uma ferramenta CASE capaz de mapear o modelo Entidade-Relacionamento
para o modelo relacional. **Este artefato deve ser entregue na plataforma em uso pelo professor da
disciplina (e-Disciplinas ou taqui) no formato PDF. Não serão aceitos arquivos em formato
proprietário da ferramenta CASE usada.**

_Obs. 1: situações especiais no modelo (que causem algum tipo de dúvida, questionamento ou
"estranheza") devem ser comentadas no próprio diagrama._

_Obs. 2: se necessário, o grupo deve estender o seu contexto até que o modelo atinja as especificações
mínimas._

**c)** **_(artefato do tipo diagrama)_** apresentar o modelo Relacional derivado no modelo Entidade-
Relacionamento (relações, atributos, chaves primárias e chaves estrangeiras). Este modelo deverá ser
implementado em ferramenta CASE. **Este artefato deve ser entregue no e-Disciplinas ou taqui
(formato PDF). Não serão aceitos arquivos em formato proprietário da ferramenta CASE usada.**

_Obs.: o MODELO RELACIONAL é o Modelo-Entidade Relacionamento APÓS o mapeamento de entidades
para tabelas. Consulte as aulas de revisão._

**d)** **_(artefato do tipo texto e código)_** apresentar **4 consultas** em SQL implementadas para seu sistema.
Essas consultas devem ser as mais complexas que o grupo projetou para o sistema e devem considerar
apenas o uso de instruções SQL (a linguagem de programação do SGBD não deve ser considerada na
resolução destas consultas). Pelo menos **duas** dessas consultas devem considerar funções de grupo.
**Este artefato deve ser entregue no e-Disciplinas ou taqui -- consultas em SQL em arquivo ASCII (.txt)
prontas para serem testadas no SGBD.**


_Obs. 1 -- Para cada uma das consultas, apresente: a especificação textual da consulta; a resolução da
consulta em SQL implementada no sistema (e testada, sua consulta deve "funcionar corretamente"); a
especificação da consulta em álgebra relacional, sempre que isso for possível (nem todas as instruções
de SQL existem em álgebra relacional e muitas vezes não podem ser obtidas pela combinação de
instruções existente em álgebra)._

_Obs. 2: A complexidade das consultas será determinante para execução de outras partes do trabalho.
Assim, a depender das consultas projetadas, pode ser possível ter que elaborar novas consultas. Por isso,
é interessante o grupo já analisar as demais partes do trabalho, a seguir._


## PARTE II: IMPLEMENTAÇÃO DE REGRAS DE NEGÓCIOS COMO OBJETOS E VISÕES DO SGBD

Nesta parte serão exercitados conceitos de asserções, gatilhos e visões.

**ARTEFATOS A SEREM ENTREGUES:**

**a)** **_(artefato do tipo texto e código)_** enunciar **duas regras de negócios** que sejam adequadamente
modeladas como **duas asserções ou dois gatilhos** , usando o modelo de dados trabalhado na Parte I
deste trabalho. Para cada um dos artefatos, o grupo deve apresentar um enunciado textual seguindo o
modelo ECA (Evento-Condição-Ações), uma solução textual em SQL padrão, uma solução em código
implementada dentro do SGBD em uso pelo grupo, a transcrição deste código para o documento
textual, devidamente documentada (explicando características interessantes das tomadas de decisões
aplicadas na construção do código) e, finalmente, um conjunto de, pelo menos, três casos
INTERESSANTES de teste. Além disso, o grupo deve prever o conjunto de gatilhos projetados com o uso
do BEFORE e do AFTER e com o uso do FOR EACH ROW e FOR EACH STATEMENT. **O texto deve ser
entregue em formato PDF. O código deverá ser entregue em formato ASCII (.txt) na plataforma
adotada pelo professor da sua turma (e-disciplina ou taqui).**

_Obs.: A nota deste item considerará tanto a complexidade, quanto a implementação e os 3 casos de
testes. Testes incompletos e asserções extremamente simples implicarão em diminuição de nota.
Portanto, caprichem!_

**b)** **_(artefato do tipo texto e código)_** enunciar **uma restrição de segurança (requisito não funcional)** do
sistema modelado na Parte I que justifique e motive a criação de **uma visão**. O objetivo é que a visão
proporcione **segurança de acesso** às informações. Sua visão deverá envolver pelo menos três tabelas
básicas. O grupo deve apresentar a especificação do requisito de forma textual, uma solução textual
para implementação da visão em SQL padrão, uma solução em código para a visão implementada
dentro do SGBD em uso pelo grupo, e a transcrição deste código para o documento textual,
amplamente documentada (explicando características interessantes das tomadas de decisões aplicadas
na construção do código). Além disso, o grupo deve apresentar uma breve discussão circunstanciada
sobre a relação custo/benefício da materialização desta visão e sobre a possibilidade de permitir
atualização de dados via esta visão. **O texto deve ser entregue em formato PDF. O código deverá ser
entregue em formato ASCII (.txt) na plataforma adotada pelo professor da sua turma (e-disciplina ou
taqui).**

_Obs.: Leia atentamente tudo o que é pedido no item. A nota será completa se o item for entregue
completo!_

**c)** **_(artefato do tipo texto e código)_** enunciar **uma necessidade de otimização de consulta (requisito não
funcional do sistema)** do sistema modelado na Parte I que justifique e motive a criação de **uma visão.** O
objetivo é que a visão contribua para a **otimização de consultas** realizadas no sistema. Sua visão deverá
envolver pelo menos duas tabelas básicas e ser útil para pelo menos duas consultas. O grupo deve
apresentar a especificação do requisito de forma textual, uma solução textual para implementação da
visão em SQL padrão, uma solução em código para a visão implementada dentro do SGBD em uso pelo
grupo, a transcrição deste código para o documento textual, amplamente documentada (explicando
características interessantes das tomadas de decisões aplicadas na construção do código) e a
especificação em SQL padrão das consultas que são beneficiadas pela visão. Além disso, o grupo deve
apresentar uma breve discussão circunstanciada sobre a relação custo/benefício da materialização
desta visão e sobre a possibilidade de permitir atualização de dados via esta visão. **O texto deve ser
entregue em formato PDF. O código deverá ser entregue em formato ASCII (.txt) na plataforma
adotada pelo professor da sua turma (e-disciplina ou taqui).**


_Obs.: leia atentamente tudo o que é pedido no item. A nota será completa se o item for entregue
completo!_

**OBS.: Se algum requisito exigido na Parte II do trabalho não puder ser atendido dentro da tecnologia
usada, o grupo deverá apresentar as soluções em SQL padrão e elaborar um** _objeto ou modelo_
**alternativo que possa atender, com algum nível de satisfação, a regra de negócio elaborada. Além
disso, o trabalho deve apresentar evidências de que a implementação de tal requisito foi estudada
pelo grupo e que não foi possível encontrar formas de implementá-la na tecnologia usada.**

**OBS.: Os grupos que tiverem dificuldades de realizar uma ou outra tarefa em um SGBD específico e
quiser realizar o trabalho usando múltiplos SGBDs, pode fazê-lo. Entretanto, o grupo deve ser
cuidadoso para manter as condições de testes necessárias em cada SGBD usado. Ou seja, o modelo de
dados deverá ser replicado em cada SGBD.**


## PARTE III: ORIENTAÇÃO A OBJETOS E ESTUDO DE PLANOS DE CONSULTAS E DESEMPENHO DE

## CONSULTAS - COM E SEM INDEXAÇÃO

O objetivo da parte III do trabalho é exercitar o conceito de orientação a objetos e explorar as **4
consultas (e variações)** escolhidas na **parte I (f)** , no que diz respeito às possibilidades de apresentação e
análise de planos de consultas (construção, custo e tempo de execução), com e sem uso de indexação, e
com pequenas variações de filtros e de sintaxe. O grupo deverá **instanciar** o banco de dados de maneira
a propiciar a execução de diferentes testes de observação do comportamento do otimizador de
consultas do SGBD. Isso significa que o grupo deverá ter um volume razoável de dados com variações
consideráveis.

**OBS.: O grupo deverá apresentar um pequeno relatório estatístico sobre as instâncias de banco de
dados usadas. Esse relatório deve conter, pelo menos, número de tabelas e tamanho em tuplas das
tabelas. O comando EXPLAIN, se disponível no SGBD ajuda na realização desta análise.**

Os objetos de análise nesta parte de trabalho são, portanto:

```
A CONSULTA executada com o comando EXPLAIN
```
```
O plano de consulta com marcações de uso de índice, estratégias, custos e tamanho de respostas
```

```
A árvore de consulta
```
## ARTEFATOS A SEREM ENTREGUES:

**a)** **_(artefato do tipo texto e código)_** inserir pelo menos uma característica de cada categoria abaixo do
modelo objeto-relacional e **enunciar** uma regra de negócio ou um requisito de sistema, que motive o
seu uso. As características que devem ser trabalhadas são:

- "objetos complexos" (atributo composto e atributo multivalorado): inserir estes atributos no
    modelo (considere apenas a parte do modelo em que os atributos serão inseridos),
    implementar essa modelagem no SGBD (se possível) ou apresentar o código SQL padrão para a
    implementação desta modelagem (se a tecnologia não permitir sua implementação). Seja uma
    implementação de SGBD ou um código SQL, comentar o código destacando tomadas de
    decisões que são úteis no contexto do sistema modelado;
- "tipos referência": fazer uso deste recurso no SGBD (se possível) ou apresentar o código SQL
    padrão para a implementação desta modelagem (se a tecnologia não permitir sua
    implementação). Seja uma implementação de SGBD ou um código SQL, comentar o código
    destacando tomadas de decisões que são úteis no contexto do sistema modelado;
- "herança": inserir este recurso no modelo relacional (considere apenas a parte do modelo em
    que os atributos serão inseridos), implementar essa modelagem no SGBD (se possível) ou
    apresentar o código SQL padrão para a implementação desta modelagem (se a tecnologia não
    permitir sua implementação). Seja uma implementação de SGBD ou um código SQL, comentar
    o código destacando tomadas de decisões que são úteis no contexto do sistema modelado;

**O texto deve ser entregue em formato PDF. O código deverá ser entregue em formato ASCII (.txt) na
plataforma adotada pelo professor da sua turma (e-disciplina ou taqui). (ver observação em vermelho
abaixo).**

**b) (artefato do tipo texto)** Para cada consulta definida na Parte I do trabalho, o grupo deverá executar o
comando **EXPLAIN** a fim de solicitar ao SGBD que mostre o plano de consulta que foi criado para
execução da consulta, os índices usados na execução da consulta e o custo das operações realizadas
durante a execução da consulta. O documento entregue pelo grupo neste quesito deve contar com
informações fornecidas pelo SGBD (relatórios ou _prints_ de tela) e uma análise circunstanciada feita pelo
grupo sobre a execução da consulta. Nesta análise, o grupo deve interpretar as informações fornecidas
pelo SGBD e relacioná-las com a teoria de banco de dados discutida em aula e presente nos livros textos
da disciplina e em bibliografia correlata encontrada pelo próprio grupo em pesquisa em bases
bibliográficas^1. **O texto deve ser entregue em formato PDF. O código deverá ser entregue em formato**

(^1) Bibliografia consultada deve ser referenciada no texto a ser entregue.


**ASCII (.txt) na plataforma adotada pelo professor da sua turma (e-disciplina ou taqui). (ver observação
em vermelho abaixo).**

**c) (artefato do tipo texto)** Para cada consulta definida na Parte I do trabalho, o grupo deverá intervir no
banco de dados de forma a criar diferentes tipos de índices, excluir índices, aumentar ou diminuir
quantidade de dados que devem ser retornados pela consulta, modificar levemente as condições da
cláusula **where** ou do **join** , de forma a executar novamente a consulta e estudar as modificações que
ocorrem no plano de execução. As modificações deverão ser analisadas pelo grupo e a análise deverá
fazer parte do trabalho (os mesmos itens de relatórios e _prints_ do item (b) devem ser expostos aqui para
fins de comparação). O grupo deve destacar as mudanças claramente. Pelo menos duas alterações em
cada uma das quatro consultas são requeridas. Procure atender diferentes solicitações deste item do
trabalho no conjunto de **8 novas** consultas que serão criadas aqui. **O texto deve ser entregue em
formato PDF. O código deverá ser entregue em formato ASCII (.txt) na plataforma adotada pelo
professor da sua turma (e-disciplina ou taqui). (ver observação em vermelho abaixo).**

**d) (artefato do tipo texto)** Escolha **1 consulta** dentre as quatro definidas na Parte I do trabalho.
Reescreva sua consulta usando duas estratégias equivalentes (veja a teoria estudada em sala de aula),
portanto criando **2 novas consultas** , e execute novamente as análises de plano e custo. Verifique se o
SGBD foi capaz de chegar no mesmo plano de consulta para execução de cada consulta equivalente.
Analise o comportamento obtido (os mesmos itens de relatórios e _prints_ do item (b) devem ser expostos
aqui para fins de comparação). **O texto deve ser entregue em formato PDF. O código deverá ser
entregue em formato ASCII (.txt) na plataforma adotada pelo professor da sua turma (e-disciplina ou
taqui). (ver observação em vermelho abaixo).**

**e) (artefato do tipo texto)** Projete **1 consulta** que faça uso da estratégia de subconsulta ( _subquery)_. Se
uma de suas consultas usadas nos itens anteriores atende a esse quesito, você pode usá-la. Reescreva-a
sem usar essa estratégia. Execute as **2 consultas** criadas e proceda com a análise dos custos e planos (os
mesmos itens de relatórios e _prints_ do item (b) devem ser expostos aqui para fins de comparação). **O
texto deve ser entregue em formato PDF. O código deverá ser entregue em formato ASCII (.txt) na
plataforma adotada pelo professor da sua turma (e-disciplina ou taqui). (ver observação em vermelho
abaixo).**

**Obs.: Todas as consultas em SQL e códigos referentes a objetos de banco de dados criados neste
trabalho deverão ser entregues em arquivos .txt, devidamente nomeados (ou seja, com nomes que
indiquem o item do trabalho que aquele .txt atende).**

**SE HOUVER MODIFICAÇÃO NO MODELO DO BANCO DE DADOS, O GRUPO PODE ENTREGAR
NOVAMENTE NO e-DISCIPLINAS ou taqui OS ARTEFATOS DISPONIBILIZADOS NAS ENTREGAS
ANTERIORES. NO ENTANTO, O TRABALHO NÃO SERÁ CORRIGIDO NOVAMENTE. A CORREÇÃO
CONSIDERARÁ A ENTREGA FEITA NA DATA DEVIDA.**


