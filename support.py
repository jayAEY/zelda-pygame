from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map    

def import_folder(path):
    surfaces_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surfaces_list.append(image_surf)

    return surfaces_list        

# print(import_csv_layout('1 - level/map/map_FloorBlocks.csv'))
# print(import_folder('1 - level/graphics/Grass'))