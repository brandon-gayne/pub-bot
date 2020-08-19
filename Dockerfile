from ubuntu

RUN apt update \
&& apt -y upgrade
RUN apt -y install python3 python3-pip
RUN pip3 install bs4 discord.py