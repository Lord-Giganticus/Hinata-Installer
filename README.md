# Rosalina Theme Installer

The themes on Wii U use two files, put them in the following paths:

Men.pack in 'wiiu/rosalina/install/Men.pack'
Men2.pack in 'wiiu/rosalina/install/Men2.pack'

There is a separate installer for each file, you can combine themes.

It's time to give your console a new style!!!

To create or download your themes visit:
https://gbatemp.net/threads/share-and-download-custom-wii-u-themes.592318/#post-9545282

## Build

Run `make` in arm_user, arm_kernel and wupserver and copy each `*bin.h` to /payload  
Run `make`

## Building with Docker

Run the following command in your shell of choice. *This command assumes you have python 3.x installed*
* Win Command:
```
docker pull devkitpro/devkitppc && docker build -t builder . && docker run --name build builder /bin/bash -c make && docker cp build:/Hinata-Installer/indexiine-installer.elf rosalina-theme-installer-men2.elf && docker rm build && docker image rm builder && py -3 ToMen.py && docker build -t builder . && docker run --name build builder /bin/bash -c make && docker cp build:/Hinata-Installer/indexiine-installer.elf rosalina-theme-installer-men.elf && docker rm build && docker image rm builder && py -3 ToMen2.py
```
* Unix Command:
```
docker pull devkitpro/devkitppc && docker build -t builder . && docker run --name build builder /bin/bash -c make && docker cp build:/Hinata-Installer/indexiine-installer.elf rosalina-theme-installer-men2.elf && docker rm build && docker image rm builder && python3 ToMen.py && docker build -t builder . && docker run --name build builder /bin/bash -c make && docker cp build:/Hinata-Installer/indexiine-installer.elf rosalina-theme-installer-men.elf && docker rm build && docker image rm builder && python3 ToMen2.py
```

## Disclaimer

I am not responsible for any bricks or other damage done to your device!

## Credits

- GaryOderNichts - indexiine-installer
- FIX94 - IOSU Exploit and wupserver copied from wuphax  
- dimok789 - libiosuhax  
