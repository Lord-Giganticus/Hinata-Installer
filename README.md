# Hinata Installer.

Replace original "safe.rpx" for custom rpx binary. 

Requires FailST installed on Health and Safety Information channel.

- Original RPX path: "sd:/wiiu/hinata/backup/backup-safe.rpx"
- Custom RPX path: "sd:/wiiu/hinata/safe.rpx"

## Build

Run `make` in arm_user, arm_kernel and wupserver and copy each `*bin.h` to /payload  
Run `make`  

## Building with Docker

Run the following command in your shell of choice.
```
docker pull devkitpro/devkitppc && docker build -t builder . && docker run --name build builder /bin/bash -c make && docker cp build:/Hinata-Installer/indexiine-installer.elf indexiine-installer.elf && docker rm build && docker image rm builder
```

## Disclaimer

I am not responsible for any bricks or other damage done to your device!

## Credits

- GaryOderNichts - indexiine-installer
- FIX94 - IOSU Exploit and wupserver copied from wuphax  
- dimok789 - libiosuhax  
