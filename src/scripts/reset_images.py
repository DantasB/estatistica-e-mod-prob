import os

def reset_images():
    """This method deletes all the images in the images folder."""
    for root, _, files in os.walk('images'):
        for archive in files:
            if archive.endswith('.png'):
                os.remove(os.path.join(root, archive))
    

if __name__ == '__main__':
    reset_images()
