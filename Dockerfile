FROM python:3.7.3-alpine3.9
RUN mkdir /TE_pyexporter
WORKDIR /TE_pyexporter
COPY requirements.txt /TE_pyexporter
RUN pip install -r requirements.txt
COPY hip-profiles.py /TE_pyexporter
COPY templates /TE_pyexporter/templates
EXPOSE 5000
ENTRYPOINT [ "python", "-u", "./hip-products.py"]