SMS-GENERATOR

1) Example usage 1 (quick):

$ cd <path to>/sms-generator/src
$ python Driver.py -i sms/test/testX/sms.ini -v
<where 'X' is 1 to 15>

Note: you may need 'pywbxml' installed for some of the tests.

2) Example usage 2 (painful/experimental):

It's possible to run sms-generator in an Ubuntu 10.04 docker container.
Why do this? Because 'pywbxml' was removed from repos > 10.04.

Here's how:

Build docker image:
$ docker build -t sms-generator .

Spin up a container and attach to it:
$ docker run -it sms-generator

The sms-generator directory inside the container:
# cd /home/src

FIXME: not sure why it is failing test8 still!


0041000B915121551532F400042E0B05040B84C0020003F001010A060403B081EA02066A008509036D6F62696C65746964696E67732E6162632F0001   <-- what is expected
0041000B915121551532F400042E0B05040B84C0020003F001010A060403B081EA03066A008509036D6F62696C65746964696E67732E6162632F0001   <-- what is got instead
...................................................................X....................................................   <-- difference highlighted
