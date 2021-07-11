// BROWSER_PATH_REGION = APP_PATH_REGION
// INDEX_PATH = FILE_PATH
// INDEX_BACKUP_PATH = FILE_BACKUP_PATH
// INDEXIINE_INDEX_PATH = CUSTOM_FILE_PATH
// INDEX_MODE = FILE_MODE
// indexpath = filepath
// indexiine-installer = hinata-installer

#ifndef _MAIN_H_
#define _MAIN_H_

#include "common/types.h"
#include "common/common.h"
#include "dynamic_libs/os_functions.h"

#define MLC_MOUNT_PATH "/vol/storage_mlc01"

#define APP_PATH_EUR "dev:/sys/title/00050010/10040200"
#define APP_PATH_USA "dev:/sys/title/00050010/10040100"
#define APP_PATH_JPN "dev:/sys/title/00050010/10040000"

#define FILE_PATH "/content/Common/Package/Men2.pack"

#define FILE_BACKUP_PATH "sd:/wiiu/rosalina/install/backup/backup-Men2.rpx"
#define CUSTOM_FILE_PATH "sd:/wiiu/rosalina/install/Men2.pack"

#define FILE_MODE 0x644

/* Main */
#ifdef __cplusplus
extern "C" {
#endif

typedef enum
{
    Undetected,
    EUR,
    USA,
    JPN
} Region;


int Menu_Main(void);
void console_printf(int newline, const char *format, ...);

#ifdef __cplusplus
}
#endif

#endif
