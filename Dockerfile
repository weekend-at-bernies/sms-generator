# GOTCHA 1/2:
# Official Ubuntu docker support only extends as far back as 16.04: https://hub.docker.com/_/ubuntu
# So we need to use this 3rd party one for Ubuntu 10.04.
FROM yamamuteki/ubuntu-lucid-i386

# Copy stuff into the image
COPY ./src /home/src
COPY ./docker-entrypoint.sh /home/.

# GOTCHA 2/2:
# For really old Ubuntu versions (such as 10.04), the repos are no
# longer supported @ archive.ubuntu.com. They are supported @ old-releases.ubuntu.com.
# You have to make this change if you want package support:
RUN sed -i 's/archive/old-releases/' /etc/apt/sources.list

# Install packages
RUN apt-get update 

RUN apt-get install -y \
  python \
  libwbxml2-0 \
  python-wbxml \
  nano

#RUN cd /home/src
#RUN ./RunTests.sh 15
#RUN python Driver.py -i sms/test/test8/sms.ini

# Execute script
#RUN ls /home
#RUN /home/docker-entrypoint.sh


