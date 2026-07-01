"""Home images plugin - dynamically discover homepage carousel images."""

import os
import logging

from pelican import signals

logger = logging.getLogger(__name__)

IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.svg'}

def discover_home_images(pelican):
    """Scan content/pages/home/ for images and set HOMEPAGE_TOP_IMAGES."""
    home_dir = os.path.join(pelican.settings['PATH'], 'pages', 'home')
    if not os.path.isdir(home_dir):
        pelican.settings['HOMEPAGE_TOP_IMAGES'] = []
        return

    images = []
    for fname in sorted(os.listdir(home_dir)):
        ext = os.path.splitext(fname)[1].lower()
        if ext in IMAGE_EXTENSIONS:
            images.append(f'/pages/home/{fname}')

    pelican.settings['HOMEPAGE_TOP_IMAGES'] = images
    logger.info("Discovered %d homepage images from %s", len(images), home_dir)

def register():
    signals.initialized.connect(discover_home_images)
