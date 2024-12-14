FROM mcr.microsoft.com/devcontainers/python:3.13

COPY requirements.* ./

ARG USERNAME=vscode
RUN groupadd docker && usermod -aG docker $USERNAME && \
    pip install -r requirements.txt && \
    ansible-galaxy collection install -r requirements.yml
