FROM python:3
COPY .  /usr/src.app
WORKDIR /usr/src.app
RUN pip3 install sklearn
CMD [ "python", "./dockerizer_test.py" ]
