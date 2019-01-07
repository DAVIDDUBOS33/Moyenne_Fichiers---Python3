import os

TOTO = os.path.expandvars('$HOME')

def Moyenne_Fichiers(toto, n=0, total=0, n_erreur=0):
    """
    La fonction os.walk permet de lister récursivement tous les fichiers et les dossiers à partir d’un point dans l’arborescence.
    :param n: nombre de fichiers
    :param total: total en octets des fichiers
    :return: la moyenne des fichiers en octets
    """
    for dossier, sous_dossiers, fichiers in os.walk(toto):
        for fichier in fichiers:
            try:  # erreur de chemin sur un fichier dans repertoire google ???? : FileNotFoundError
                # print(os.path.join(dossier, fichier))
                n += 1
                total += os.stat(os.path.join(dossier, fichier)).st_size  # taille d'un fichier
            except:
                #print(os.path.join(dossier, fichier))
                n_erreur +=1
    if n_erreur >0 :
        print("'FileNotFoundError: [Errno 2] No such file or directory:' trouvé %s fois" %n_erreur)
    return total // n

print("****  %s octets est la taille moyenne d'un fichier " %Moyenne_Fichiers(TOTO), end = "")
print("dans le répertoire %s  ****" %TOTO )

