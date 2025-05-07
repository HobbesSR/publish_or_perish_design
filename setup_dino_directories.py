import os

DINO_NAMES = [
    "Herrerasaurus",
    "Plateosaurus",
    "Stegosaurus",
    "Corythosaurus",
    "Gallimimus",
    "Allosaurus",
    "Tyrannosaurus",
    "Oviraptor",
    "Velociraptor",
    "Archaeopteryx",
    "Compsognathus",
    "Baryonyx",
    "Triceratops",
    "Brachiosaurus",
    "Ceratosaurus",
    "Apatosaurus",
    "Iguanodon",
    "Thecodontosaurus"
]

def create_dino_directories(base_path="images/dinosaurs"):
    for dino in DINO_NAMES:
        dir_path = os.path.join(base_path, dino)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")

if __name__ == "__main__":
    create_dino_directories()