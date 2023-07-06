FROM python:3.8.17
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN chmod +x ./main.py
CMD ["./main.py"]
