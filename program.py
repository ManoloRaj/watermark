import cv2

# Charger les images
image_principale = cv2.imread("DSC_7889.jpg")
watermark = cv2.imread("Logo DEV.png", cv2.IMREAD_UNCHANGED)

# Définir les coordonnées pour positionner le watermark sur le côté droit
x_offset = image_principale.shape[1] - watermark.shape[1] - 10
y_offset = 10

# Récupérer les dimensions du watermark
watermark_height, watermark_width, _ = watermark.shape

# Superposer le watermark sur l'image principale
for y in range(watermark_height):
    for x in range(watermark_width):
        if watermark[y, x][3] != 0:  # Vérifier la transparence du watermark
            image_principale[y_offset + y, x_offset + x, :3] = watermark[y, x, :3]

# Enregistrer l'image résultante
cv2.imwrite("image_resultante.jpg", image_principale)
