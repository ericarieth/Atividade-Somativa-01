git clone ericarieth/Atividade-Somativa-01
cd python-projeto
git add hello.py
git commit -m "Adiciona script de saudação em Python"
git push origin main
git checkout -b nova-feature
gh repo clone ericarieth/Atividade-Somativa-01
# Usar uma imagem base oficial do Python
FROM python:3.10-slim

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
