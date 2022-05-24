FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /name_divider
WORKDIR /name_divider
RUN python3 -m pip install . && chmod +x fuzz/fuzz.py