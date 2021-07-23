
-- Table 'posters' --
/*
 - Objeto complexo

  O atributo complexo metadata contém informações pertinentes da imagem e que não são as imagens em si,
  como dimensões, formato, qualidade, etc... Como metadata é um campo que recebe dados de uma fonte
  externa, não temos garantias sobre quais metadados estarão disponíveis, nem a forma como estarão organizados.
  Assim, foi criado um campo do tipo JSONB (JSON binário, um dos tipos complexos possíveis do PostgreSQL) para
  podermos coletar essas informações de forma mais flexível 
*/
CREATE TABLE posters (
  path text, 
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb, 
  obra_id integer NOT NULL
);


-- Table 'usuario_premium' -- 
/*
  - Herança

  Em nosso sistema, pensamos num modelo 'Freemium', onde disponibilizamos as funcionalidades essenciais para todos os
  usuários, e para àqueles que gostariam de contribuir com um pagamento mensal, adicionamos algumas funcionalidades extras,
  como indicações visuais de usuário "patrocinador" do sistema, possiblidade de foto de perfil animada, assinatura 
  personalizada nas avaliações das obras, etc...

  Para a solução no banco de dados, incluimos a tabela abaixo, herdando os atributos de usuários comuns, e adicionando
  um campo extra, para indicar a data em que o modo Premium expira, sendo necessário novo pagamento para reativar as
  funcionalidades extras. A herança nesse caso é uma boa solução, pois os usuários Premium ainda possuem os mesmos relacionamentos
  de usuários comums, não sendo necessários JOINS adicionais para resgatar as relações já existentes de usuários (esses JOINS
  seriam necessários caso optássemos por uma relação de especialização)

*/
CREATE TABLE usuario_premium (
	data_expira_em DATE NOT NULL,	
) INHERITS(usuario)


