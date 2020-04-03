FROM python:3.6-slim
COPY ./app.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./get_model.py /deploy/
WORKDIR /deploy/
RUN pip install --quiet -r requirements.txt
RUN mkdir models
COPY ./config.json /deploy/
RUN python get_model.py
RUN rm config.json
EXPOSE 80
ENTRYPOINT ["python", "app.py"]
