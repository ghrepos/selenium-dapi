FROM python:latest

RUN useradd -m -u 1000 user
RUN apt-get update && apt-get install -y wget unzip
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
COPY . /home/user/app
WORKDIR /home/user/app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN chown -R user:user /home/user/app
RUN chmod +x ./start.sh

USER user
EXPOSE 8080
ENTRYPOINT ["./start.sh"]