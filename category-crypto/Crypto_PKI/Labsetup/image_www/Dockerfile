# You will need to add commands to this file.  Add commands after the
# multi-line RUN command and before the CMD command.
#
# You will need to add the following commands:
#
# 1) Set WWWDIR to a new directory for your web site.
#    For example, I used /var/www/kelliher2024
#
# 2) Copy web content into your web site's directory.  You can make
#    copies of index.html and index_red.html, revise them slightly
#    to distinguish them from the originals, and copy them into
#    your web site's directory.
#
# 3) Make a copy of bank32_apache_ssl.conf, edit it for your
#    web site and copy it into /etc/apache2/sites-available
#
# 4) Copy your web sites certificate and key files into certs
#    and copy them into /certs/ in the container.
#
# 5) Run chmod in the container on your key file, your web content
#    files, and enable your web site's SSL configuration, in a manner
#    similar to what you see below.

FROM handsonsecurity/seed-server:apache-php

ARG WWWDIR=/var/www/bank32

COPY ./index.html ./index_red.html $WWWDIR/
COPY ./bank32_apache_ssl.conf /etc/apache2/sites-available
COPY ./certs/bank32.crt ./certs/bank32.key  /certs/

# Note that this RUN command extends over four lines.  Do not break it.

RUN  chmod 400 /certs/bank32.key \
     && chmod 644 $WWWDIR/index.html \
     && chmod 644 $WWWDIR/index_red.html \
     && a2ensite bank32_apache_ssl   

CMD  service apache2 start && tail -f /dev/null

