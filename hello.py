# hello.py
def saudacao():
    print("Olá, seja bem-vindo ao projeto de Python!")

if __name__ == "__main__":
    saudacao()
# hello.py
def saudacao():
    print("Olá, seja bem-vindo ao projeto de Python!")

def nova_funcionalidade():
    print("Esta é uma nova funcionalidade adicionada!")

if __name__ == "__main__":
    saudacao()
    nova_funcionalidade()
git add hello.py
git commit -m "Adiciona nova funcionalidade ao projeto"
git push origin nova-funcionalidade
# hello.py
def saudacao():
    print("Olá, seja bem-vindo ao projeto de Python!")

def nova_funcionalidade():
    print("Esta é uma nova funcionalidade adicionada para testar o CI e CD!")

if __name__ == "__main__":
    saudacao()
    nova_funcionalidade()
git add hello.py
git commit -m "Adiciona nova funcionalidade e configura workflows para CI e CD"
git push origin nova-feature
# Usar uma imagem base oficial do Python
FROM python:3.10-slim

# requirements.txt
pytest
requests
# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos para o container
COPY requirements.txt .

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o container
COPY . .

# Define o comando que será executado quando o container iniciar
CMD ["python", "hello.py"]

docker build -t meu_projeto_python .
docker run -it --rm meu_projeto_python
