FROM python:3.6.2-slim
COPY . /opt/FernandoMartinez
WORKDIR /opt/FernandoMartinez
RUN pip install -r requirements.txt
ENV TelegramToken=<YOUR_TOKEN>
CMD python main.py