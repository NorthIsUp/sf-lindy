FROM python:3.5

# install nginx and geo libs
RUN apt-get -y update \
    && apt-get -y install geoip-database libgeoip-dev \
    && rm -rf /var/lib/apt/lists/*

ENV DJANGO_SETTINGS_FILE sflindy.settings
RUN mkdir -p /usr/sflindy/
WORKDIR /usr/sflindy/

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the app
COPY . /usr/sflindy/
COPY manage.py manage.py

# Collect static assets
RUN mkdir -p vendor/components
RUN ./manage.py collectstatic --noinput

EXPOSE 80 443 8000
ENTRYPOINT [ "bin/entrypoint.sh" ]
