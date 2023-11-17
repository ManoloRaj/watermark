from PIL import Image

# Chemin du dossier contenant les images à traiter
dossier_images = "images/"

# Chemin du fichier image de signature (logo)
chemin_signature = "signature/logo.png"

# Ouvrir l'image de signature
signature = Image.open(chemin_signature)

# Parcourir les images dans le dossier
import os


for nom_fichier in os.listdir(dossier_images):
    chemin_image = os.path.join(dossier_images, nom_fichier)

    # Ouvrir l'image
    image = Image.open(chemin_image)

    # Obtenir les dimensions de l'image
    largeur, hauteur = image.size

    # Redimensionner la signature (ajustez la taille selon vos besoins)
    largeur_signature = int(largeur * 0.1)  # Par exemple, 10 % de la largeur de l'image
    signature_redimensionnee = signature.resize((largeur_signature, int(largeur_signature / signature.width * signature.height)))

    # Marges
    marge_x = 20  # Marge horizontale
    marge_y = 20  # Marge verticale

    # Coordonnées pour placer la signature en bas à droite avec marge
    coord_x = largeur - signature_redimensionnee.width - marge_x
    coord_y = hauteur - signature_redimensionnee.height - marge_y

    # Insérer la signature dans le coin inférieur droit
    image.paste(signature_redimensionnee, (coord_x, coord_y), signature_redimensionnee)

    # Sauvegarder l'image avec la signature
    image.save(os.path.join(dossier_images, "image_signee_" + nom_fichier))

print("Terminé ! Les images signées ont été enregistrées dans le dossier.")