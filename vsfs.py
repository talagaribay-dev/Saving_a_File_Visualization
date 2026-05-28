'''
Project 1 Starter Code
Cairn University, Fall 2023, CIS 321, Prof Petcaugh
Student Name:
'''

import pygame

#Start up, and set up, pygame
pygame.init()
screen = pygame.display.set_mode([1200,700])
clock = pygame.time.Clock()

# Data Structures
inodeBitmap = {
    0 : 0,
    1 : 1,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0,
    9 : 0,
    10 : 0,

}
#Data map Dictionary
dataMap = {
    0 : 0,
    1 : 1,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0
}
# file to add
file = {
    "file_type" : ".txt",
    "file_size" :  6,
    "file_permisions": "only user",
}
inode = {
    0 : 0,
    1 : 1,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0,
    9 : 0,
    10 : 0,

}



# Helper Functions
def addFile ():
    pass

# Text generator on screen
def addText(mytext, t_dest, f_color, f_size):
    font = pygame.font.SysFont(None, f_size)
    font_final = font.render(mytext, True, f_color)
    screen.blit(font_final, t_dest)
def drawHardDriveBlocks(i):
    while i < 72:
        i = i + 1
        if i < 9:
            pygame.draw.rect(screen, (0, 0, 0), (i * 30, 90, 30, 30), 2)
        elif 9 < i < 18:
            pygame.draw.rect(screen, (0, 0, 0), (i * 30, 90, 30, 30), 2)
        elif 18 < i < 27:
            pygame.draw.rect(screen, (0, 0, 0), (i * 30, 90, 30, 30), 2)
        elif 27 < i < 36:
            pygame.draw.rect(screen, (0, 0, 0), (i * 30, 90, 30, 30), 2)
        elif 36 < i < 45:
            pygame.draw.rect(screen, (0, 0, 0), ((i - 36) * 30 , 150, 30, 30), 2)
        elif 45 < i < 54:
            pygame.draw.rect(screen, (0, 0, 0), ((i - 36) * 30, 150, 30, 30), 2)
        elif 54 < i < 63:
            pygame.draw.rect(screen, (0, 0, 0), ((i - 36) * 30, 150, 30, 30), 2)
        elif 63 < i < 72:
            pygame.draw.rect(screen, (0, 0, 0), ((i - 36) * 30, 150, 30, 30), 2)

def drawBitmaps():
    for i in range(10):
        addText(str(i), (35, 233 + (i * 30)), (0, 0, 255), 25)
        pygame.draw.rect(screen, (0, 0, 0), (20, 230 + (i * 30), 30, 30), 2)
        pygame.draw.rect(screen, (0, 0, 0), (50, 230 + (i * 30), 30, 30), 2)
        # data map

        addText(str(i), (95, 233 + (i * 30)), (0, 0, 255), 25)
        pygame.draw.rect(screen, (0, 0, 0), (90, 230 + (i * 30), 30, 30), 2)
        pygame.draw.rect(screen, (0, 0, 0), (120, 230 + (i * 30), 30, 30), 2)
def checkBitmaps():
    for key, value in inodeBitmap.items():
            if value == 1:
                pygame.draw.rect(screen, (255, 0, 0), (50, 230 + (key * 30), 30, 30), 0)
            if value == 0:
                print (key)
                pygame.draw.rect(screen, (0, 255, 0), (50, 230 + (key * 30), 30, 30), 0)
                break
    for key, value in dataMap.items():
            if value == 1:
                pygame.draw.rect(screen, (255, 0, 0), (50, 230 + (key * 30), 30, 30), 0)
            if value == 0:
                print (key)
                pygame.draw.rect(screen, (0, 255, 0), (120, 230 + (key * 30), 30, 30), 0)
                break
def flipBitmaps():
    for key, value in inodeBitmap.items():
            if value == 0:
                print (key)
                pygame.draw.rect(screen, (255, 0, 0), (50, 230 + (key * 30), 30, 30), 0)
                value == 1
                break
    for key, value in dataMap.items():
            if value == 0:
                print (key)
                pygame.draw.rect(screen, (255, 0, 0), (120, 230 + (key * 30), 30, 30), 0)
                value == 1
                break
def coverText():
    pygame.draw.rect(screen, (255, 255, 255), (20, 570, 1200, 400), 0)
    addText("click right arrow to continue", (900, 650), (240, 0, 0), 30)
def printFile():
    for key, value in file.items():
        pass
def addFileToInode(i):
    for key, value in inode.items():
        if value == 0:
            inode[key] = i
            break
def addToDataReigon():
        for i in range(int(inode[0]["file_size"])+9):
            if i> 9:
                pygame.draw.rect(screen, (255, 0, 0), (i * 30, 90, 30, 30), 0)
###
# Static screen elements
###
screen.fill((255, 255, 255))
addText("Click 'Right Arrow' to start VSFS simulation.", (20, 20), (0, 0, 0), 30)
addText("Hard Drive Blocks", (20, 60), (0, 0, 255), 30)
addText("DATA BLOCKS", (20, 200), (0, 0, 255), 30)
addText("Explanation", (20, 550), (0, 0, 255), 30)

#Inodes

###
# End of Static Elements
###

# Event list for simulation
def sim_events(c):
    match c:
        case 0:
            coverText()
            addText("Welcome to very simple file system (VSFS). This will help you understand how a file system works.", (20, 570), (0, 0, 0), 30)


        case 1:
            drawHardDriveBlocks(0)
            coverText()
            addText("This is a visualization of the space in your hard drive",
                    (20, 570), (0, 0, 0), 30)
        case 2:
            coverText()
            addText("In the first section of the Hard Drive are a few different things that will help the file system work ",
                    (20, 580), (0, 0, 0), 30)
            addText(
                "Let learn about them!",
                (20, 610), (0, 0, 0), 30)
        case 3:
            coverText()
            addText("First is the Superblock, this is where the code is stored to help run everything",
            (20, 570), (0, 0, 0), 30)
            addText("S",
                    (35, 95), (0, 0, 0), 30)
        case 4:
            coverText()
            addText("Second are bit maps, Above Shows how the data is stored in the bit maps.",
            (20, 570), (0, 0, 0), 30)
            addText(
                " These help you know what blocks are free or not, we will put this in practice later.",
                (20, 645), (0, 0, 0), 30)
            addText("i",
                    (67, 95), (0, 0, 0), 30)
            addText("d",
                    (97, 95), (0, 0, 0), 30)
            drawBitmaps()
        case 5:
            coverText()
            addText("3rd are the inodes. They help store metadata about the file",
                (20, 620), (0, 0, 0), 30)
            addText(
                "like what type of file is it, the length of the file, where it is and more.",
                (20, 645), (0, 0, 0), 30)
            addText("I",
                (127, 95), (0, 0, 0), 30)
            addText("I",
                    (157, 95), (0, 0, 0), 30)
            addText("I",
                (187, 95), (0, 0, 0), 30)
            addText("I",
                (217, 95), (0, 0, 0), 30)
            addText("I",
                    (247, 95), (0, 0, 0), 30)
        case 6:
            coverText()
            addText("Lastly is the data region this is where the actual file is stored",
                (20, 570), (0, 0, 0), 30)
        case 7:
            coverText()
            checkBitmaps()
            addText("Let see what happens when you save a file. Here is the file I want to save.",
                (20, 620), (0, 0, 0), 30)
            addText(
                "First step is to check the if the bit maps are free. look the first one is already.",
                (20, 645), (0, 0, 0), 30)
            addText("filled so it goes to the next one. we will indicate that its been checked as free by making it green.",
                    (20, 670), (0, 0, 0), 30)
        case 8:
            coverText()
            addText("Once a free spot has been found then the meta data has to be collected. This info is stored in the inode",
            (20, 620), (0, 0, 0), 30)
            addText(
                "Info in that's been added to the inode",
                (400, 550), (0, 0, 0), 30)
            addText(
                 "Info that's been added to the inode: " + str(inode[0]),
                (400, 570), (0, 0, 0), 30)
            addFileToInode(file)
            print(inode[0])
            #file rectangle
            pygame.draw.rect(screen, (0, 0, 0), (1000, 350, 150, 200), 2)
        case 9:
            coverText()
            addText("Now that we have the metadata, the next step is to flip the needed bitmaps from 0 to 1",
            (20, 620), (0, 0, 0), 30)
            flipBitmaps()
        case 10:
            coverText()
            addText("Next is to place the file into the datamap, It takes the length of how long the file size is",
                (20, 620), (0, 0, 0), 30)
            addToDataReigon()
        case 11:
            coverText()
            addText("Congrats YOU JUST SAVED A FILE!",
                    (20, 620), (0, 0, 0), 30)

# Run Simulation
# Running loop
running = True
turn_counter = 0
counter = 0
while running:
    # looks for inputs: keyboard presses, mouse clicks, etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # checking if key "->" was pressed
            if event.key == pygame.K_RIGHT:
                sim_events(turn_counter)
                print(turn_counter)
                turn_counter += 1
            if event.key == pygame.K_LEFT:
                turn_counter -= 1
                sim_events(turn_counter)
                print(turn_counter)

                #checkBitmaps()

    # Update the screen, go to the next frame
    pygame.display.flip()
    clock.tick(30)

pygame.quit()