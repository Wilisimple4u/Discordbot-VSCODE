FROM python:3.11
# Forklaring
# ==================
# 3.11 er litt mer stabilt enn nyeste versjon av 3.12, 3.12 har gjort mange endringer i
# Setuptools, som definerer hvordan apper installerer seg. Dette kan føre til at noen
# requirements ikke fungerer uten noen workarounds. Det blir bedre om noen måneder ;)


ENV Token=$Token
# Forklaring
# ==================
# Hent TOKEN fra environment
# run kommando blir da slik (erstatt <TOKEN> med Discord token):
# docker run -e Token="<TOKEN>" <IMAGE>

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# EXPOSE 6400
#the same as python's: app.route(host='0.0.0.0'. port=5000)
# Forklaring
# ==================
# Du kjører ikke noe som bruker en port, så du trenger ikke å expose en port.
# Her er det kun et program som kjører, ikke en nettside eller noe som trenger en port :)


# Kjør Discordbot (skriveleif, stor B :))
# CMD ["python", "src/DiscordBot.py"]
CMD ["python", "src/Discordbot.py"]


# CMD ["python", "src/utyl.py"]
# Forklaring
# ==================
# Kan kun kjøre en CMD av gangen, her ser jeg utyl kjøres via DiscordBot.py
# (from utyl import *, dette betyr: bruk utyl.py, trenger altså ikke 'kjøre' denne filen)

#Takes a copy of the files from src in python
#CMD ["python", "src/DiscordBot.py"]
# need to use "" for text not ''.

