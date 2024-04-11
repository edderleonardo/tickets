from pathlib import Path

import cloudinary.uploader
from celery import shared_task


@shared_task
def upload_image_to_cloudinary(image_path, public_id=None):
    """
    Sube una imagen a Cloudinary y devuelve la URL de la imagen subida
    """
    response = cloudinary.uploader.upload(
        str(image_path),
        public_id=public_id,
    )
    return response["secure_url"]
