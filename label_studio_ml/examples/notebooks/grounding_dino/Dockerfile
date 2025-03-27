FROM python:3.12.9-bookworm

RUN pip install --upgrade pip
RUN pip install jupyterlab
RUN pip install label-studio-sdk
RUN pip install python-dotenv

WORKDIR /notebooks

COPY ./helper ./helper
COPY ./grounding_dino ./grounding_dino

RUN chmod -R 777 .

ENTRYPOINT [ "jupyter", "execute", "./grounding_dino/grounding_dino.ipynb" ]
