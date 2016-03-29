#!/bin/bash
/etc/init.d/nginx restart
uwsgi --ini /cjcx/manage_config.ini
