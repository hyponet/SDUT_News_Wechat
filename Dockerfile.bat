FROM python:2.7.9

MAINTAINER Hypo i@ihypo.net

RUN mkdir /wechat
WORKDIR /wechat
COPY . /wechat

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install nginx -y
RUN apt-get install uwsgi uwsgi-plugin-python -y
RUN chown -R www-data:www-data /wechat
RUN chown -R www-data:www-data /wechat
RUN chmod +x /wechat/startserver.sh
ADD default /etc/nginx/sites-available/default

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN /etc/init.d/nginx restart
RUN ln -s /usr/lib/python2.7/plat-*/_sysconfigdata_nd.py /usr/lib/python2.7/

CMD sh /wechat/startserver.sh

EXPOSE 80
