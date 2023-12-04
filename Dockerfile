FROM python:latest
RUN useradd -m -u 1000 user

RUN apt-get update && apt-get install -y wget unzip
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

COPY requirements.txt . 
RUN pip install --no-cache-dir --upgrade -r requirements.txt
WORKDIR /home/user/api
RUN chown -R user:user /home/user/api
COPY ./ /home/user/api

USER user 
EXPOSE 7860
ENTRYPOINT ["bash", "start.sh"]