# 1stNUP Installer.

Replace original "1stNUP.xml" for custom icons on Wara Wara Plaza. 

Requires FailST installed on Health and Safety Information channel.

- Original RPX path: "sd:/wiiu/wario/backup/1stNUP.xml"
- Custom RPX path: "sd:/wiiu/wario/1stNUP.xml"

## Build

Run `make` in arm_user, arm_kernel and wupserver and copy each `*bin.h` to /payload  
Run `make`  

## Building with Docker

Run the following command in your shell of choice.
```
docker pull devkitpro/devkitppc && docker build -t builder . && docker run --name build builder /bin/bash -c make && docker cp build:/Hinata-Installer/indexiine-installer.elf 1stNUP-installer.elf && docker rm build && docker image rm builder
```

## Disclaimer

I am not responsible for any bricks or other damage done to your device!

## Credits

- GaryOderNichts - indexiine-installer
- FIX94 - IOSU Exploit and wupserver copied from wuphax  
- dimok789 - libiosuhax  