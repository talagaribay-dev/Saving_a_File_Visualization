## BrainStorming
Componentes for file system
    access methods
        open(), read(), write(),
    file systems are divied into blocks

keywords?
    -free list (pg 3)
    -allocation structures (pg 3)
    -inodes (pg 4)
    -Super-blocks
    -data region
    -metadata
## Steps for saving a file
    step 1: check what spot are free with the bitmaps  
    step 2: save metadata to inodes
    step 3:flip bitmaps to taken
    step 4:save the file to the data reigon
## elements I have to add
    bitmaps - stored as a diecctory
        -inode 
        -data reigon
    inodes - stored as a diectory that saves a another directory which is the file
    superblock holds the over all code 
    data reigion -