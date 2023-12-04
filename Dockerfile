FROM python:3.11

RUN useradd -m -u 1000 user
RUN apt-get update && apt-get install -y wget unzip

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

COPY requirements.txt . 

RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /home/user/api

RUN chown -R user:user /home/user/api

USER user 

COPY --chown=1000 ./ /home/user/api

EXPOSE 7860

ENTRYPOINT gunicorn --bind 0.0.0.0:7860 server.flask:app