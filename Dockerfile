FROM python:3.7.6-alpine3.10

USER root
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

ADD . /
RUN python -m pip install -r requirements.txt

# RUN python -m pip install selenium
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk
RUN apk add glibc-2.30-r0.apk
RUN apk add glibc-bin-2.30-r0.apk

# install Firefox to use geckodriver
RUN apk add firefox-esr=60.9.0-r0

COPY geckodriver_linux /bin/geckodriver

CMD [ "python", "./scrape.py"]