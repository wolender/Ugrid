FROM python:3.7.17
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN chmod +x ./main.py
EXPOSE 2525
CMD ["./main.py"]
