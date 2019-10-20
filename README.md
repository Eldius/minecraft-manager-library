# Minecraft Management Library #

## Sample usage as CLI ##

    # Backup server
    $ python backup.py \
        --host <server-host> \
        --ssh-user <ssh-username> \
        --ssh-key <ssh-key-file-path> \
        --ssh-port <ssh-port> \
        --rcon-port <rcon-port> \
        --rcon-pass <rcon-password> \
        --install-folder <minecraft-installation-folder> \
        --dest-folder <local-path-to-save-backup-file>
