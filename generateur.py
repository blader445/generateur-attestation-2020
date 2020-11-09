import datetime
from codecs import open

name = "Nom Prénom"
birthday = "01/01/2001"
birthplace = "Paris (75)"
adress = "1 avenue des Champs-Elysées"
initials = "R.D"

#affecter la date et l'heure actuelle à une variable
time_object = datetime.datetime.now()
# définir le format d'affichage de la date
date_string = time_object.strftime("%d/%m/%Y")
#définir le format d'affichage de l'heure
time_string = time_object.strftime("%H:%M")

hours = int(time_string[:2])
minutes = int(time_string[3:])

# Reculer l'heure de 10 minutes
minutes = str(minutes - 10)
if len(minutes) == 1 :
    minutes = str("0" + minutes)
elif int(minutes) < 0 :
    hours = str(hours - 1)
    minutes = int(minutes)
    minutes = str(10 + minutes)
    minutes = str("5" + minutes)

hoursadd = hours+1
print(date_string)
print(f"""C'est bon jusqu'à {hoursadd}:{minutes} !""")

content = f"""ATTESTATION DE DÉPLACEMENT DÉROGATOIRE
En application du décret n°2020-1310 du 29 octobre 2020 prescrivant les mesures générales nécessaires pour faire face à l'épidémie de Covid19 dans le cadre de l'état d'urgence sanitaire
Je soussigné(e),
Mme/M. : {name}
Né(e) le : {birthday}	à : {birthplace}
Demeurant : {adress}
certifie que mon déplacement est lié au motif suivant (cocher la case) autorisé par le décret n°2020-1310 du 29 octobre 2020 prescrivant les mesures générales nécessaires pour faire face à l'épidémie de Covid19 dans le cadre de l'état d'urgence sanitaire1 :
[]  Déplacements entre le domicile et le lieu d’exercice de l’activité professionnelle ou un établissement d’enseignement ou de formation, déplacements professionnels ne pouvant être différés, déplacements pour un concours ou un examen.
[]  Déplacements pour effectuer des achats de fournitures nécessaires à l'activité professionnelle, des achats de première nécessité3 dans des établissements dont les activités demeurent autorisées, le retrait de commande et les livraisons à domicile.
[]  Consultations, examens et soins ne pouvant être assurés  à distance et l’achat de médicaments.
[]  Déplacements pour motif familial impérieux, pour l'assistance aux personnes vulnérables et précaires ou la garde d'enfants.
[]  Déplacement des personnes en situation de handicap et leur accompagnant.
[x] Déplacements brefs, dans la limite d'une heure quotidienne et dans un rayon maximal d'un kilomètre autour du domicile, liés soit à l'activité physique individuelle des personnes, à l'exclusion de toute pratique sportive collective et de toute proximité avec d'autres personnes, soit à la promenade avec les seules personnes regroupées dans un même domicile, soit aux besoins des animaux de compagnie.
[]  Convocation judiciaire ou administrative et pour se rendre dans un service public
[]  Participation à des missions d'intérêt général sur demande de l'autorité administrative
[]  Déplacement pour chercher les enfants à l’école et à l’occasion de leurs activités périscolaires
Fait à :
Le : {date_string} à : {hours} : {minutes} 
(Date et heure de début de sortie à mentionner obligatoirement)
Signature : {initials}

    1 Les personnes souhaitant bénéficier de l'une de ces exceptions doivent se munir s'il y a lieu, lors de leurs déplacements hors de leur domicile, d'un document leur permettant de justifier que le déplacement considéré entre dans le champ de l'une de ces exceptions.
    2 A utiliser par les travailleurs non-salariés, lorsqu'ils ne peuvent disposer d'un justificatif de déplacement établi par leur employeur.
    3 Y compris les acquisitions à titre gratuit (distribution de denrées alimentaires...) et les déplacements liés à la perception de prestations sociales et au retrait d'espèces."""

with open("attestation.txt", "w", encoding='utf8') as f:
    f.write(content)