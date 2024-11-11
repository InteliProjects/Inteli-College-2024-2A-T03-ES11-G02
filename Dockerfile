FROM python:3.9-buster

WORKDIR /app

# Install necessary build tools (gcc, make, etc.)
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    python3-dev \
    libpq-dev

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt



COPY ./src/backend/ /app/src/backend/
COPY ./src/frontend/ /app/src/frontend/

EXPOSE 8501

CMD ["sh", "-c", "python3 /app/src/backend/controller/connection_controller.py & streamlit run /app/src/frontend/main.py --server.port=8501 --server.address=0.0.0.0"]
