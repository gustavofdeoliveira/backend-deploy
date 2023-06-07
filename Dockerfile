FROM python:3.10.8-slim-buster

ARG DATABASE_URL

WORKDIR /backend

COPY requirements.txt .

# Instalando pacotes adicionais

RUN apt-get update && apt-get install -y gcc python3-dev

RUN apt-get update && apt-get install -y libgl1-mesa-glx

RUN apt-get update && apt-get install -y libglib2.0-0

# Instalando dependências do projeto

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3001

COPY . .

ENV DATABASE_URL=${DATABASE_URL}

RUN chmod +x /backend/setup.sh

COPY . .

CMD ["/bin/bash", "/backend/setup.sh"]