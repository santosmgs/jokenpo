# Use a imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo do jogo para o contêiner
COPY jokenpo.py .

# Define o comando para rodar o jogo
CMD ["python", "jokenpo.py"]
