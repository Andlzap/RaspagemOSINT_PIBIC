# Projeto Tor Proxy com Python

Este projeto configura o serviço Tor para realizar requisições anônimas usando Python. O objetivo é utilizar o Tor como proxy para anonimizar o tráfego HTTP através de uma configuração específica no sistema operacional e com bibliotecas específicas do Python.

**Recomendação:** Para maior segurança e facilidade de uso, recomendamos utilizar o Parrot OS, uma distribuição Linux voltada para privacidade, segurança e testes de penetração. Parrot OS já vem com várias ferramentas de segurança instaladas, incluindo o Tor.

## Pré-requisitos

- **Sistema operacional**: Parrot OS (recomendado) ou qualquer distribuição Linux baseada em Debian.
- **Python**: Certifique-se de ter o Python instalado no seu sistema.
- **pip**: Gerenciador de pacotes do Python.

## Instalação e Configuração

### Passo 1: Atualizar o sistema

Atualize o gerenciador de pacotes do sistema:

```bash
sudo apt-get update
```

### Passo 2: Instalar o Tor

Caso o Tor ainda não esteja instalado, execute o comando abaixo para instalá-lo:

```bash
sudo apt-get install tor
```

### Passo 3: Reiniciar o serviço Tor

Reinicie o serviço Tor para garantir que ele está funcionando corretamente:

```bash
sudo /etc/init.d/tor restart
```

### Passo 4: Configurar a senha do Tor

Gere uma senha hash para o Tor:

```bash
tor --hash-password "sua_senha"
```

Copie o hash gerado, pois ele será usado nas configurações do Tor.

### Passo 5: Editar o arquivo de configuração do Tor

Abra o arquivo de configuração do Tor (`torrc`):

```bash
sudo nano /etc/tor/torrc
```

Descomente e adicione as seguintes linhas, substituindo o valor do hash pela sua senha gerada:

```
SOCKSPort 9050
ControlPort 9051
HashedControlPassword "Colar o hash da sua senha gerada"
CookieAuthentication 1
```

### Passo 6: Reiniciar o serviço Tor novamente

Reinicie o serviço Tor para aplicar as mudanças:

```bash
sudo /etc/init.d/tor restart
```

### Passo 7: Configurar o `requests` para usar o Tor

Por padrão, o `requests` do Python não utiliza o serviço DNS do Tor. Portanto, ao utilizar `session.proxies`, substitua `socks5` por `socks5h`. O `h` representa a resolução do nome de host, que será realizada pelo servidor SOCKS.

### Passo 8: Instalar Bibliotecas Python Necessárias

As bibliotecas necessárias para este projeto estão listadas no arquivo `requirements.txt`. Para instalá-las, execute o comando abaixo:

```bash
pip install -r requirements.txt
```

## Fontes Utilizadas

- [How to make Python requests work via socks proxy](https://stackoverflow.com/questions/12601316/how-to-make-python-requests-work-via-socks-proxy)
- [Make anonymous requests using Tor with Python](https://www.scrapehero.com/make-anonymous-requests-using-tor-python/)
- [Make requests using Python over Tor](https://stackoverflow.com/questions/30286293/make-requests-using-python-over-tor)


## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
