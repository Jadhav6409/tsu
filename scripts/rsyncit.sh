# Used only for development.
# rsync the git from PC to device.

# TODO: Daemonize?

REMOTE="192.168.1.13"
REMOTE_DIR="~/shared/tsu3"
user="Termux"

if [[ ! -f "scripts/rsyncit.sh" ]]; then
	echo "Youre probably in the wrong directory"
	exit -1
fi

rsync -av -e "ssh -p8022" \
	--no-owner --no-g --chmod u=rwX,g-rwx,o-rwx \
	--exclude-from './scripts/sync_excludes.txt' \
	"$(pwd -P)/" "${user}@${REMOTE}:${REMOTE_DIR}"
