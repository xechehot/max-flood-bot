FROM fastdotai/fastai:latest

RUN mkdir /app

ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt

ADD . /app/

#RUN ln -s /notebooks/fastai /app/fastai
WORKDIR /app/
CMD ["/bin/bash", "-c", "gunicorn --bind 0.0.0.0:$PORT run"]
