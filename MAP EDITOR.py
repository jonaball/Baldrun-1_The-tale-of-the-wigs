import pygame as pg
import pygame
import json

def loadJson(filename) -> dict:
    with open(filename, 'r') as f:
        return json.load(f)

def saveJson(data: dict, filename: str):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

SKJERM_HØYDE= 720
SKJERM_BREDDE = 1080
WIDTH, HEIGHT = SKJERM_BREDDE, SKJERM_HØYDE

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("BALD RUN v1.0 - MAP EDITOR")

position = (0, 0)
tilesize = 25
MAP_TO_EDIT = "Prosjekt-Pygame/maps/map1.json" # ENDRE DENNE TIL MAP DU VIL ENDRE
loadedData = loadJson(MAP_TO_EDIT)
print(loadedData)

def DisplayMap(mapData):
    for tile in mapData:
        pos = mapData[tile]["position"]
        type = mapData[tile]["type"]
        pygame.draw.rect(win, (200, 200, 200), (pos[0]*tilesize, pos[1]*tilesize, tilesize, tilesize))

def DisplayHover():
    pos = pygame.mouse.get_pos()
    pygame.draw.rect(win, (100, 100, 100), (pos[0]-pos[0]%tilesize, pos[1]-pos[1]%tilesize, tilesize, tilesize))

def DrawMap():
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    tilepos = pos[0]//tilesize, pos[1]//tilesize

    tileType = "wall"
    if click[0] == True:
        loadedData[f"{tilepos[0]},{tilepos[1]}"] = {"type": tileType, "position": tilepos}
    if click[2] == True:
        try:
            loadedData.pop(f"{tilepos[0]},{tilepos[1]}")
        except:
            print(f"No tile at {tilepos} to remove.")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            saveJson(loadedData, MAP_TO_EDIT)
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                saveJson(loadedData, MAP_TO_EDIT)
                pygame.quit()
                break
    win.fill((0,0,0))
    DisplayMap(loadedData)
    DisplayHover()
    DrawMap()
    
    pygame.display.flip()
    clock.tick(60)