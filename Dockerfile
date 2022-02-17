FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt ./
COPY entrypoint.sh ./

RUN pip install -r requirements.txt
RUN chmod +x ./entrypoint.sh

COPY . /code/

ENTRYPOINT ["sh", "/code/entrypoint.sh"]