FROM python:3.9

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /workspace

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]