latest=$(ssh pi "ls -t ~/sunset/images | head -1")
scp pi:~/sunset/images/$latest ./scripts/
open ./scripts/$latest
