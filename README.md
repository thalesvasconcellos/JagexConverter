# JagexConverter

O **JagexConverter** é uma ferramenta para converter contas do RuneScape no formato antigo para o formato compatível com o Jagex Launcher. Utilizando **Selenium** para automação e **Loguru** para logs, o projeto permite que você preencha um arquivo `accounts.txt` com contas antigas no formato `email:senha` e as converta para o formato do Jagex Launcher, gerando um novo arquivo `accounts_generated.txt`.

## Funcionalidades

- Converte contas antigas do RuneScape para o formato compatível com o **Jagex Launcher**.
- Utiliza **Selenium** para automação do processo de login e conversão.
- Logs detalhados de execução gerados pelo **Loguru**.
- O arquivo de entrada é `accounts.txt`, e o arquivo gerado é `accounts_generated.txt`.

## Pré-requisitos

Antes de começar, você precisará de:

- Python 3.x
- Selenium
- Loguru
- WebDriver do Selenium para o navegador desejado (ex: ChromeDriver)
- Arquivo `accounts.txt` com as credenciais das contas a serem convertidas.
