def solution_yémoja(i):
 if i>=8:
  print("Vous êtes très stressé-e. Vous avez besoin d'au moins une journée de détente. Commencez par faire le vide chez vous: il faut que tout soit clair dans votre esprit. La première des choses consiste à reposer votre corps : vous avez besoin de dormir. Faites ensuite une séance de relaxation pour reconnecter avec vous-même. Utilisez votre compagnon yémoja pour faire diffuser des notes olfactives apaisantes selon vos préférences et faites une séance de yoga tout en écoutant une musique positive. N'hésisez pas à prendre une tisane, dessiner ou parler à quelqu'un. Vous devez à tout prix évacuer votre stress. Si les symptômes persistent, appelez un médecin. Pour le yoga, cliquez ici : https://www.youtube.com/playlist/list=PLcvBx66p0nltGVclKWPPTQuV6HDz_5wvf   Pour la musique, cliquez là: https://open.spotify.com/user/spotify/playlist/2YeGkAUQhmO8TCjSMbFYWf ")
 elif i>=5:
  print("Vous êtes stressé-e. Faites une pause. Utilisez votre compagnon Yémoja pour diffuser des huiles essentielles qui vous apaiseront. Allongez-vous, fermez les yeux et méditez. Concentrez-vous sur votre respiration et faites abstraction du reste. N'hésitez pas à vous masser grâce aux picots d'acupression du cercle en insistant sur la nuque et les points de la main. Si votre stress persiste, appeler un médecin. Pour la méditation, vous pouvez choisir une musique sur cette page : https://www.youtube.com/channel/UCwobzUc3z-0PrFpoRxNszXQ ")
 elif i>=2:
  print("Vous êtes un peu stressé-e. Buvez une tisane, elle vous réconfortera. Massez-vous la nuque et les points de la main à l'aide des picots du cercle. N'hésitez pas à dormir et à vous aérer l'esprit. Si vos symptômes persistent, appelez un médecin. ") 
 else:
  print("Vous n'êtes pas stressé-e. Buvez une tisane et prenez un cookie si vous en ressentez le besoin. Sinon, dormez un peu, ça ne vous fera pas de mal;). Pour les cookies, voici une recette : https://cnz.to/vf/recettes/biscuits-et-petits-gateaux/cookies-au-chocolat-recette/")


i=0
nausée=input("Avez-vous la nausée?")
if nausée.lower()=="oui":
   i=i+1
else:
   i=i
énergie=input("Manquez-vous d'énergie?")
if énergie.lower()=="oui":
  i=i+1
else:
  i=i
corps_faible=input("Vous sentez-vous faible à certains endroits du corps ?")
if corps_faible.lower()=="oui":
  i=i+1
else:
  i=i
jambes_lourdes=input("Avez-vous les jambes lourdes?")
if jambes_lourdes.lower()=="oui":
  i=i+1
else:
  i=i 
concentration=input("Avez-vous du mal à vous concentrer?")
if concentration.lower()=="oui":
 i=i+1
else:
 i=i
douleurs_abdo=input("Avez-vous des douleurs abdominales?")
if douleurs_abdo.lower()=="oui":
 i=i+1
else:
 i=i
transit=input("Avez-vous remarqué une modification de votre transit?")
if transit.lower()=="oui":
 i=i+1
else:
 i=i
ballonement=input("Vous sentez-vous ballonné-e?")
if ballonement.lower()=="oui":
 i=i+1
else:
 i=i
remontées_gastriques=input("Avez-vous des remontées gastriques ?")
if remontées_gastriques.lower()=="oui":
 i=i+1
else:
 i=i
migraine=input("Ressentez-vous comme des coups de marteaux sur votre tête ?")
if migraine.lower()=="oui":
 i=i+1
else:
 i=i

solution_yémoja(i)


