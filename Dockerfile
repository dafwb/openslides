FROM python:3
RUN mkdir /openslides
WORKDIR /openslides
RUN pip3 install openslides
RUN openslides --version
RUN openslides createsettings
RUN sed -e "s/ENABLE_ELECTRONIC_VOTING = False/ENABLE_ELECTRONIC_VOTING = True/g" -i /root/.config/openslides/settings.py

EXPOSE 8000
CMD openslides
