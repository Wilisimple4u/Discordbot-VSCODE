# Documentation

```python
print("Hello world!")
```
Slik installerer du ;)
```shell
pip install -r requirements.text
```

Terminal commands docs.
```markdown
# I did a thing in a place in a time
# you want to copy/learn from it.


## The Process


### Discord stuff
In order to run the discordbot:
You need to have made your own discordbot on discord.
You will also need the token needed to connect to it.

#

### Python stuff

By Importing my code into Pycharm or whatever, 
you can run this beautiful mess of a code.
You should then be able to both run it through pycharm as well as docker container.
Remember to change the <TOKEN> in the run.bat file,
Into the discord token you are going to be using.

#

### Docker stuff

To make it easier on myself and others like me,
I have added bashfiles that can run the docker commends for you in python.

#

### To build/create the container in docker:
Copythis into the terminal with the file selected -->  .\build.bat

#

### To Start/run the container after building it in docker:

Copythis into the terminal with the file selected -->  .\run.bat

22.11.23
#writing down some terminal commands, so I don't forget how to get mkdocs running.

pip install mkdocs-material
#Add on adminastrative privliges: --user

mkdocs serve 
#if this don't work use the one below
python -m mkdocs serve

#Add on to mkdocs serve: --dev-addr=0.0.0.0:8000
#insert own value on where and what port to host it on.

23.11.23
#writing down some terminal commands, 
so I don't forget how to get the discord bot running on my server.


#Step 1 after server#
Getting vsftpd
(sudo apt install vsftpd)


Editing the vsftpd file:
(sudo nano /etc/vsftpd.conf)

Make sure the (write_enable=YES) does not have a # infront of it,
and is actually set to YES.


Restart the vsftpd service:
(sudo service vsftpd restart)
or
(sudo systemctl restart vsftpd.service)
Not both, it would be redundant.


gets the project and adds it as a file:
(git clone (Link to project))


Enter the file
(cd "FileName")


(sudo apt install openssh-server)


(sudo apt-get upgrade -y)


Getting host name server's designation
(hostname -I)


Installing docker to server:
(sudo apt install docker.io)


Build the docker container:
(sudo docker build -t discord .)


For the DiscordBotDocker to run spesifically it will need the token,
(sudo docker run -e Token=TOKEN)



Setting up a docker composer file to do all the docker process for me
Hint: way simpler.
Editing the docker-compose.yml
(nano NAME.yml)


Good idea to make a directory for the dockercompose file
(mkdir NAME)


If I inevitably make mistakes,
I can use this to remove the docker file and try again:
(rm -rd Filename)
```

My Docker-composer file should look like this.
```markdown
services:
  discordbot:
    build:
    restart: unless-stopped (good enough for this current project)
    environment:
      - Token=TOKEN
```