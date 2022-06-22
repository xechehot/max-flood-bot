FROM fastdotai/fastai:latest

RUN mkdir /app

#ADD requirements.txt /app/
#RUN pip install -r /app/requirements.txt

ADD dogs-cats-torch-model.pt /app/

ADD . /app/

RUN ln -s /notebooks/fastai /app/fastai
WORKDIR /app/
CMD python bot.py
