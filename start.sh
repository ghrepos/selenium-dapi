#!/usr/bin bash

gunicorn --bind 0.0.0.0:8080 server.flask:app &

sleep 10 

while true; do
  gmt7_time=$(TZ=Asia/Ho_Chi_Minh date +"%Y-%m-%d %H:%M:%S")
  
  echo "Content Download - Time: $gmt7_time"
  
  sleep 169200
done