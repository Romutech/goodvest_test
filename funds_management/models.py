from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


#  _____           _    __      _ _                               _      _
# |  __ \         | |  / _|    | (_)                             | |    | |
# | |__) |__  _ __| |_| |_ ___ | |_  ___      _ __ ___   ___   __| | ___| |
# |  ___/ _ \| '__| __|  _/ _ \| | |/ _ \    | '_ ` _ \ / _ \ / _` |/ _ \ |
# | |  | (_) | |  | |_| || (_) | | | (_) |   | | | | | | (_) | (_| |  __/ |
# |_|   \___/|_|   \__|_| \___/|_|_|\___/    |_| |_| |_|\___/ \__,_|\___|_|

# Le modèle doit posséder deux attributs :
# - Un attribut qui est une relation avec le modèle User
# - Un attribut "amount" qui aura le type "float" et initialisé à None par
# défaut.

# Infos: un utilisateur ne peut avoir qu'un "Portfolio" et un "Portfolio" ne
# peut être rattaché qu'à un utilisateur.

# TODO
# Create portfolio model here.

#  ______               _                        _      _
# |  ____|             | |                      | |    | |
# | |__ _   _ _ __   __| |   _ __ ___   ___   __| | ___| |
# |  __| | | | '_ \ / _` |  | '_ ` _ \ / _ \ / _` |/ _ \ |
# | |  | |_| | | | | (_| |  | | | | | | (_) | (_| |  __/ |
# |_|   \__,_|_| |_|\__,_|  |_| |_| |_|\___/ \__,_|\___|_|


# Le modèle "Fund" doit avoir 3 attributs
# - Un attribut qui est une relation avec le modèle Portefeuille
# - Un attribut "percentage" qui aura le type "float" et initialisé à None par
# défaut.
# - Un attribut "date" représentant un champ "date" de type datetime.date en
# Python

# Infos : un "Fund" peut être attaché à plusieurs "Portfolio" et un "Portfolio"
# peut avoir plusieurs "Funds".

# TODO
# Create fund models here.
