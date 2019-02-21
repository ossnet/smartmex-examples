FROM pypy:2-onbuild

COPY src/ /opt/app

WORKDIR /opt/app

CMD [ "pypy","main.py"]