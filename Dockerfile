FROM pypy:latest-onbuild

COPY src/ /opt/app

WORKDIR /opt/app

CMD [ "pypy3","main3.py"]