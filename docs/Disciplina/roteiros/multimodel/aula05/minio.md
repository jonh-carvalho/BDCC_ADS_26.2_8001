Para instalar o MinIO usando Docker em uma instância EC2 da AWS, você precisa configurar as portas necessárias na AWS, preparar o diretório de dados para persistência e rodar o container Docker com as credenciais administrativas.

### Pré-requisito: Liberar Portas no Security Group da EC2

No painel da AWS EC2, vá em **Security Groups** > edite as **Inbound Rules** (Regras de Entrada) e adicione:

* **Custom TCP** | Porta `9000` | Origem: Seu IP ou CIDR da sua rede.
* **Custom TCP** | Porta `9001` | Origem: Seu IP ou CIDR da sua rede.

---

### Passo a Passo de Instalação e Execução

1. **Criar o diretório para persistência de dados:** No terminal da EC2.
Crie uma pasta no sistema de arquivos do host para garantir que os arquivos salvos no MinIO não sejam perdidos caso o container reinicie.

Execute: `mkdir -p ~/minio/data`

*Verification:* Rode `ls -la ~/minio` e confirme que a pasta `data` foi criada.


2. **Iniciar o container do MinIO:** Docker Command.
Execute o comando Docker abaixo ajustando as variáveis de usuário e senha (`MINIO_ROOT_USER` e `MINIO_ROOT_PASSWORD`):

```bash
docker run -d \
  --name minio \
  --restart always \
  -p 9000:9000 \
  -p 9001:9001 \
  -v ~/minio/data:/data \
  -e "MINIO_ROOT_USER=admin" \
  -e "MINIO_ROOT_PASSWORD=SuaSenhaSegura123" \
  quay.io/minio/minio server /data --console-address ":9001"

```

*Verification:* Rode `docker ps` e verifique se o container `minio` está com o status *Up*.


3. **Acessar o Console Web:** Navegador.
Abra o seu navegador e acesse: `http://<IP-PUBLICO-DA-EC2>:9001`

Insira o usuário (`admin`) e a senha configurada no passo anterior para entrar no painel de controle do MinIO.

*Verification:* A interface do dashboard do MinIO deve carregar solicitando o login com sucesso.