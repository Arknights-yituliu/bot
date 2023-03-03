FROM debian:bullseye

COPY fonts.conf /etc/fonts/conf.d/99-custom.conf
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt update && apt upgrade -y
RUN apt install -y python3-pip fonts-noto-cjk locales tzdata
ENV TZ="Asia/Shanghai"
RUN sed -i '/zh_CN.UTF-8/s/^# //g' /etc/locale.gen && locale-gen

WORKDIR /app

COPY entrypoint.sh .
ENTRYPOINT /app/entrypoint.sh

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install-deps
RUN playwright install webkit

COPY . .
