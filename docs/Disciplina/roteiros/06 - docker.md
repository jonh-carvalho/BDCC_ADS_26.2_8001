Aqui está o **roteiro básico de instalação e configuração do Docker no Amazon EC2**, junto com a resolução dos obstáculos mais comuns enfrentados no início do processo.

### 1. Criando a Instância EC2
*   Acesse o console da AWS e crie uma nova instância.
*   Escolha um sistema operacional base simples, como **Ubuntu** ou **Amazon Linux 2023**.
*   Selecione um tipo de instância elegível para o nível gratuito, como **t2.micro** ou **t3.micro**.
*   **Configuração do Security Group (Essencial):**
    *   **Porta 22 (SSH):** Liberada e restrita apenas ao seu IP para garantir o acesso seguro.
    *   **Porta da sua aplicação (ex: 80 para HTTP ou 3000):** Liberada para qualquer lugar (`0.0.0.0/0`) para que a aplicação fique acessível publicamente.

### 2. Conectando e Instalando o Docker
Conecte-se à sua máquina virtual via SSH e execute os comandos conforme o sistema operacional escolhido:

*   **Opção A: Se você utilizou Ubuntu**
    ```bash
    sudo apt update -y
    sudo apt install docker.io -y
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo usermod -aG docker $USER
    ```
    *(Nota: Recomenda-se fechar a conexão SSH e entrar novamente para aplicar a permissão do grupo de usuários).*

*   **Opção B: Se você utilizou Amazon Linux 2023**
    ```bash
    sudo yum update -y
    sudo yum install docker -y
    sudo service docker start
    sudo usermod -a -G docker ec2-user
    ```
    *(Nota: Recomenda-se fechar a conexão SSH e entrar novamente para aplicar a permissão).*

### 3. Executando um Container de Teste
Para verificar se tudo está funcionando corretamente, faça o deploy de uma imagem pública de testes (servidor Nginx):
```bash
docker run -d -p 80:80 nginx
```
Isso fará o download do servidor Nginx e o deixará rodando em segundo plano, expondo-o na porta 80 da sua instância EC2.

Libere o tráfego de entrada: No console web da AWS, acesse a aba Segurança (Security) da sua instância EC2, clique para editar as Regras de Entrada (Inbound Rules) de seu Security Group e adicione uma regra permitindo tráfego HTTP na porta 80 vindo de qualquer lugar (0.0.0.0/0).

Para testar, abra o navegador e acesse o **IP público da sua instância**. Você deverá ver a página padrão do Nginx.

Como a aplicação está rodando em um container, você pode apontar a pasta do projeto para o container e acessar os arquivos diretamente.

Exemplo: Se você tiver um projeto html, css e javascript, pode rodar o container apontando para a pasta do projeto:

Pasta site: 

```
index.html
css/style.css
js/index.js
```

```bash
docker run -d -p 80:80 -v /caminho/para/seu/projeto:/usr/share/nginx/html nginx
```

### 4. Listando, identificando e removendo imagens e containers

#### Listar imagens
```bash
docker images
# Alternativa:
docker image ls
```

#### Listar containers
```bash
docker ps       # Apenas os que estão em execução
docker ps -a    # Todos, inclusive os parados
```

Para encontrar containers criados a partir de uma imagem específica:
```bash
docker ps -a --filter ancestor=nginx
```

Para inspecionar um container pelo ID ou nome:
```bash
docker inspect ID_OU_NOME
```

#### Remover containers
Containers em execução precisam ser parados antes de serem removidos:
```bash
docker stop ID_OU_NOME
docker rm ID_OU_NOME
```

Para remover um container diretamente, mesmo que esteja em execução:
```bash
docker rm -f ID_OU_NOME
```

#### Remover imagens
Antes de remover uma imagem, remova os containers que a utilizam.
```bash
docker rmi NOME_DA_IMAGEM:TAG
# Exemplo:
docker rmi nginx:latest
```

Também é possível usar o ID da imagem, exibido por `docker images`:
```bash
docker rmi ID_DA_IMAGEM
```

#### Limpeza de recursos não utilizados
```bash
docker container prune   # Remove containers parados
docker image prune       # Remove imagens não utilizadas
```

**Atenção:** os comandos `prune` removem recursos. Confira o que será apagado antes de confirmar.
---

### 🛠️ Resolução dos Principais Problemas Iniciais

#### Problema 1: Erro de "Permissão Negada" (Permission Denied) ao rodar comandos Docker sem `sudo`
*   **Por que acontece:** O usuário padrão do sistema (`ubuntu` ou `ec2-user`) não tem permissões administrativas para se comunicar diretamente com o serviço do Docker por padrão.
*   **Como resolver:**
    1. Adicione o seu usuário ao grupo do Docker:
       *   No **Ubuntu**: `sudo usermod -aG docker ubuntu`
       *   No **Amazon Linux 2023**: `sudo usermod -aG docker ec2-user`
    2. Execute o comando abaixo para recarregar as configurações de grupo no terminal sem precisar fechar a sessão atual:
       ```bash
       newgrp docker
       ```
       *(Se preferir, você também pode simplesmente fechar o terminal SSH e conectar-se novamente).*

#### Problema 2: A página não carrega no navegador (Tempo limite esgotado / Timeout)
*   **Por que acontece:** Normalmente, o tráfego HTTP é bloqueado pelo firewall da AWS (Security Group) ou você pode estar tentando acessar a máquina usando um endereço IP incorreto.
*   **Como resolver:**
    1. **Pegue o IP público correto:** Com o terminal aberto no seu EC2, execute o comando abaixo para consultar o IP externo real da sua máquina:
       ```bash
       curl icanhazip.com
       ```
    2. **Libere o tráfego de entrada:** No console web da AWS, acesse a aba **Segurança (Security)** da sua instância EC2, clique para editar as **Regras de Entrada (Inbound Rules)** de seu Security Group e adicione uma regra permitindo tráfego **HTTP na porta 80** vindo de qualquer lugar (`0.0.0.0/0`).

