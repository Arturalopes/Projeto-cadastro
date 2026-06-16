# Sistema de Cadastro de Imigrantes

Sistema desenvolvido em Python para cadastro e gerenciamento de imigrantes e suas informações complementares.

O projeto utiliza MySQL para armazenamento dos dados e funciona através de menus no terminal, permitindo realizar operações de cadastro, consulta, alteração e exclusão de registros.

## Funcionalidades

* Cadastro de imigrantes
* Listagem de registros cadastrados
* Consulta detalhada de um imigrante
* Alteração de dados
* Exclusão de registros
* Cadastro de informações complementares vinculadas ao imigrante
* Edição e exclusão de informações complementares

## Tecnologias utilizadas

* Python
* MySQL
* mysql-connector-python

## Como executar

Instale a dependência necessária:

```bash
pip install mysql-connector-python
```

Configure as credenciais do banco de dados no arquivo `conn.py`.

Execute o sistema:

```bash
python imigranteTela.py
```

## Estrutura

```txt
conn.py
imigrante.py
imigranteTela.py
informacao.py
informacaoTela.py
```

## Observações

Este projeto foi desenvolvido como atividade acadêmica com o objetivo de praticar integração entre Python e banco de dados relacional, além da implementação de operações CRUD e organização de código em módulos.
