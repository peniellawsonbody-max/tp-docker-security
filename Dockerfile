# Dockerfile
FROM debian:12

# Installer outils nécessaires
RUN apt-get update && apt-get install -y \
    curl \
    docker.io \
    python3 \
    python3-pip \
    python3-flask \
    && rm -rf /var/lib/apt/lists/*

# Service Python : exécute des commandes admin
# (Vulnérable volontairement)
WORKDIR /app
COPY app.py /app/app.py

EXPOSE 8080
CMD ["python3","/app/app.py"]
