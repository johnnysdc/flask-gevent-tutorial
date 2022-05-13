#!/bin/bash
echo "Installing dev requirements"

# unsplit and Unpack project library
cat libs/oracle-libs-* > build/oracle-libs.tar.gz
tar -xvzf build/oracle-libs.tar.gz --directory build/

# update dependency repositories
apt update

# upgrade system dependency
apt-get upgrade -y

# install any needed packages
apt-get install -y redis-server
apt-get install -y alien
apt-get install -y libaio1
apt-get install -y libaio-dev
apt-get install -y libevent-2.1.12

#oracle configure
# dpkg -i build/app/tmp/*.deb

# curl "https://download.oracle.com/otn_software/linux/instantclient/195000/oracle-instantclient19.5-basiclite-19.5.0.0.0-1.x86_64.rpm" -o "/app/libs/oracle-instant-basiclite.rpm"
# alien -i --scripts libs/oracle-instant-basiclite.rpm

alien -i --scripts build/app/tmp/instantclient19.5-basiclite.rpm

# Deleting unnecessary files, folders and applications
apt-get remove alien -y
apt-get autoremove -y
rm -rf build/oracle-libs.tar.gz
rm -rf build/app/tmp/*.*

