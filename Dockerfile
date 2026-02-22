# Stage 1: Builder
FROM python:3.10-slim as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: Final Image
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY backend ./backend

ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

CMD ["python", "backend/app.py"]
