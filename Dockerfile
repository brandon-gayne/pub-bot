from ubuntu

RUN apt update \
&& apt -y upgrade
RUN apt -y install python3 python3-pip git
RUN pip3 install bs4 discord.py
RUN git clone https://github.com/brandon-gayne/pub-bot.git
