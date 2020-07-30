FROM python:3

RUN mkdir /openslides
WORKDIR /openslides
RUN pip install openslides

EXPOSE 8000
CMD openslides