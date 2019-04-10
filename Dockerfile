FROM python:3.7 AS base
ENV LANG=C.UTF-8
RUN pip install --upgrade pip

FROM base AS deps
RUN wget https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py
RUN python get-poetry.py --pre -y
ENV PATH="/root/.poetry/bin:${PATH}"
RUN mkdir -p /root/.config/pypoetry/
RUN poetry config settings.virtualenvs.create false

FROM deps AS install
WORKDIR /app
COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock
RUN poetry install

FROM install AS dev
ENV HOST 0.0.0.0
ENV PORT 80
EXPOSE ${PORT}
CMD python -m time_tracking_via_gcal
COPY . .
