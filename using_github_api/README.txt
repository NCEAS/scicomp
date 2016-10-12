Python script mirroring all the repositories of a sepcific GitHub organization on your local machine. By default, all the git repositories will be created at the same location than the script. The parameters that can be passed at the run are: the name of the organization and optionally the base URL (without the repo name) to the new remote location and the path of the local repo on the local machine

Note: this script can be used as cron job. To do so, move the script in `/etc/cron.daily` removing the .py extension 
