FROM ubuntu:24.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Angelsd2/RCDD_2026.git
WORKDIR /workspace

CMD ["sleep", "infinity"]
# CMD ["python3", "RCDD_2026/main.py"]
