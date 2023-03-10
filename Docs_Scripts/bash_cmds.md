
# Encryption, Security, Linux

| SSH | GPG | Git | Commands | permissions |
|--- | ---| ---|--- | ---|
| | | | | |

- [Encryption, Security, Linux](#encryption-security-linux)
  - [SSH to GitHub](#ssh-to-github)
    - [initial ssh example](#initial-ssh-example)
    - [ssh-keygen cmds](#ssh-keygen-cmds)
    - [Example ssh connect](#example-ssh-connect)
    - [GPG key](#gpg-key)
  - [Git Commands \& examples](#git-commands--examples)
  - [Bash Script Info](#bash-script-info)
    - [Bash commands](#bash-commands)
    - [curl](#curl)
    - [Bash Scripting](#bash-scripting)
  - [Apt Info](#apt-info)
  - [Shell command info](#shell-command-info)
  - [Symbolic rep of data](#symbolic-rep-of-data)
  - [Linux permissions](#linux-permissions)
  - [Git Config terminal colors](#git-config-terminal-colors)
  - [PowerShell](#powershell)
    - [Pwsh Paths](#pwsh-paths)
    - [Pwsh Commands to review](#pwsh-commands-to-review)
    - [Excel](#excel)
    - [Vim](#vim)

## SSH to GitHub

> ssh connects and logs into the specified destination by setting the user, hostname and port
<!-- /* cspell: enableCompoundWords */ -->

```bash
#!/bin/bash
# formats for ssh
[user@]hostname | ssh://[user@]hostname[:port]
ssh://[user@]host.xz[:port]/~[user]/path/to/repo.git/
ssh://[user@]host.xz[:port]/path/to/repo.git/
ssh -i ~/.ssh/id_ed25519 # identity file (private key)
ssh -l login_name -p port
ssh-keygen -l -f /etc/ssh/ssh_host_rsa_key
# determine fingerprints
ssh-keygen -lv -f ~/.ssh/known_hosts
# ls fingerprints and random art for known hosts
ssh-keygen -r host.example.com.
# connect client to server
# Add SSHFP resource records to the zonefile for host 1st
dig -t SSHFP host.example.com
# check that zone is answering fingerprint queries.
ssh -o "VerifyHostKeyDNS ask" host.example.com
# client connects

ls -al ~/.ssh
```

### initial ssh example

```bash
# edit git config f
git config --global user.name <username>
git config --global user.email <email@mail.com>
ls -al ~/.ssh # list files in .ssh dir

ssh-keygen -m PEM -t rsa -b 4096
# generates 4096-bit SSH RSA public and private key files by default in the ~/.ssh directory.

ssh-keygen -t ed25519 -C "email@google.com"
# creates pub/priv key pair
# saves to .ssh/id_ed25519 & .ssh/id_ed25519.pub
  # generates key fingerprint & randomart image
eval "$(ssh-agent -s)" #check if agent is running
ssh-add ~/.ssh/id_ed25519 #add id to ~
cat ~/.ssh/id_ed25519.pub # display pub key then c/v to github acct
ssh -T git@github.com # test connection & clone repo
git clone git@github.com:<username>/<repo>.git
code .
git clone ssh://git@ssh.github.com:443/<username>/<repo>.git
```

```bash
ssh-keygen \
-f ~/.ssh/id_rsa.pub \
-e \
-m RFC4716 > ~/.ssh/id_ssh2.pem
# create RFC4716 formatted key from existing SSH pubkey (multiline format in a 'pem' container)

eval "$(ssh-agent -s)"
# cache private key file passphrase on local sys by verifying/using ssh-agent & ssh-add
ssh-add ~/.ssh/id_rsa
# add private key to ssh-agent

ssh-copy-id -i ~/.ssh/id_rsa.pub azureuser@myserver
#  copy existing public key to an existing remote machine
```

- ssh-keygen supports two types of certificates: user and host.
  - User certificates authenticate users to servers
    - placed in /path/to/user_key-cert.pub.
  - Host certificates authenticate server hosts to users
    - requires the -h option
    - host certificate will be output to /path/to/host_key-cert.pub.

>>
  review: ssh(1), ssh-add(1), ssh-agent(1), sshd(8)

```bash
#!/bin/bash

# generate a user certificate:
$ ssh-keygen -s /path/to/ca_key -I key_id /path/to/user_key.pub

# generate a host certificate:
ssh-keygen -s /path/to/ca_key -I key_id -h /path/to/host_key.pub

# copies the local-host’s pub key to the remote-host’s authorized_keys fi
ssh-copy-id
```

### ssh-keygen cmds

- run ssh-keygen to create key pair
  - `private` key stored in:
    - ~/.ssh/id_dsa (DSA), ~/.ssh/id_ecdsa (ECDSA)
    - ~/.ssh/id_ecdsa_sk (authenticator-hosted ECDSA)
    - ~/.ssh/id_ed25519 (Ed25519)
    - ~/.ssh/id_ed25519_sk (authenticator-hosted Ed25519)
    - ~/.ssh/id_rsa (RSA)
  - `public` key stored in user's home dir w/in subdir of:
    - ~/.ssh/id_dsa.pub (DSA), ~/.ssh/id_ecdsa.pub (ECDSA)
    - ~/.ssh/id_ecdsa_sk.pub (authenticator-hosted ECDSA)
    - ~/.ssh/id_ed25519.pub (Ed25519)
    - ~/.ssh/id_ed25519_sk.pub (authenticator-hosted Ed25519)
    - ~/.ssh/id_rsa.pub (RSA)
- Then copy public key to ~/.ssh/authorized_keys in home dir on the remote machine
- The authorized_keys file == ~/.rhosts file
- one key per line
- enables user to login w/o passwd

### Example ssh connect

>
- This example connects client network: 10.0.99.0/24
  - via a point-to-point connection
    - from 10.1.1.1 to 10.1.1.2
- SSH server running on the gateway to the remote network must allow connection 192.168.1.15

```bash
# On the client:
ssh -f -w 0:1 192.168.1.15 true
ifconfig tun0 10.1.1.1 10.1.1.2 netmask 255.255.255.252
route add 10.0.99.0/24 10.1.1.2

# On the server:
ifconfig tun1 10.1.1.2 10.1.1.1 netmask 255.255.255.252
route add 10.0.50.0/24 10.1.1.1
# Client access can be adjusted by editing:
    # /root/.ssh/authorized_keys fi
    # PermitRootLogin server option.

tunnel="1",command="sh /etc/netstart tun1" ssh-rsa ... jane
tunnel="2",command="sh /etc/netstart tun2" ssh-rsa ... john
# above cmds permits connections on:
# tun device 1 from user “jane”
# tun device 2 from user “john”
    # if PermitRootLogin == “forced-commands-only”
```

### GPG key

>>
  generate a gpg key and then c/v to GitHub
  This allows commits to be verified via signature
<!-- cspell: disable  -->
```sh
gpg --full-generate-key
# choose: key type, size, expire
#   user id[name, pass, comment], passphrase
gpg --list-keys --keyid-format LONG
# list long form pub/priv keys & copy sec/pub key after encryption standard
gpg --armor --export aaa123aaa123
# print gpg key id in ASCII armor format
```

___

## Git Commands & examples
<!-- cspell: disable  -->

```sh
#  giteveryday --help
tar zxf frotz.tar.gz
cd frotz
git init
git add . (1)
git commit -m "import of frotz source tree."
git tag v2.43 (2)

# Use a tarball as a starting point for a new repository.
# 1. add all fi under the cwd.
# 2. make a lightweight, unannotated tag.

# Create a topic branch and develop.

git switch -c alsa-audio (1)
edit/compile/test
git restore curses/ux_audio_oss.c (2)
git add curses/ux_audio_alsa.c (3)
edit/compile/test
git diff HEAD (4)
git commit -a -s (5)
edit/compile/test
git diff HEAD^ (6)
git commit -a --amend (7)
git switch master (8)
git merge alsa-audio (9)
git log --since='3 days ago' (10)
git log v2.43.. curses/ (11)
```
<!-- cspell: enable  -->

1. create a new topic branch.
2. revert your botched changes in curses/ux_audio_oss.c.
3. you need to tell Git if you added a new file; removal and modification will be caught if you do git commit -a later
4. to see what changes you are committing.
5. commit everything, as you have tested, with your sign-off.
6. look at all your changes including the previous commit.
7. amend the previous commit, adding all your new changes, using original message
8. switch to the master branch.
9. merge a topic branch into your master branch.
10. review commit logs; other forms to limit output can be combined and include -10 (to show up to 10 commits), --until=2005-12-10, etc
11. view only the changes that touch what’s in curses/ directory,
since v2.43 tag.

```sh
# Clone the upstream and work on it. Feed changes to upstream.
# <!-- cspell: disable  -->

git clone git://git.kernel.org/pub/scm/.../torvalds/linux-2.6
my2.6
cd my2.6
git switch -c mine master (1)
edit/compile/test; git commit -a -s (2)
git format-patch master (3)
git send-email --to="person <email@example.com>" 00*.patch (4)
git switch master (5)
git pull (6)
git log -p ORIG_HEAD.. arch/i386 include/asm-i386 (7)
git ls-remote --heads http://git.kernel.org/.../jgarzik/libata
-dev.git (8)
git pull git://git.kernel.org/pub/.../jgarzik/libata-dev.git A
LL (9)
git reset --hard ORIG_HEAD (10)
git gc (11)
```
<!-- cspell: enable  -->

1. checkout a new branch mine from master.
2. repeat as needed.
3. extract patches from your branch, relative to master,
4. and email them.
5. return to master, ready to see what’s new
6. git pull fetches from origin by default and merges into the current branch.
7. immediately after pulling, look at the changes done upstream since last time we checked, only in the area we are interested in.
8. check the branch names in an external repository (if not known).
9. fetch from a specific branch ALL from a specific repo & merge
10. revert the pull.
11. garbage collect leftover objects from reverted pull.
<!-- cspell: disable  -->

```sh
# Push into another repository.
# from satellite machine
git clone mothership:frotz frotz (1)
cd frotz
git config --get-regexp '^(remote|branch)\.' (2)
remote.origin.url mothership:frotz
remote.origin.fetch refs/heads/*:refs/remotes/origin/*
branch.master.remote origin
branch.master.merge refs/heads/master
git config remote.origin.push \
  +refs/heads/*:refs/remotes/satellite/* (3)
edit/compile/test/commit
git push origin (4)

# from mothership machine
cd frotz
git switch master
git merge satellite/master (5)
```
<!-- cspell: enable  -->

1. mothership machine has a frotz repository under your home
directory; clone from it to start a repository on the satellite
machine.
1. clone sets these configuration variables by default. It
arranges git pull to fetch and store the branches of mothership
machine to local remotes/origin/* remote-tracking branches.
1. arrange git push to push all local branches to their
corresponding branch of the mothership machine.
1. push will stash all our work away on remotes/satellite/*
remote-tracking branches on the mothership machine. You could use
this as a back-up method. Likewise, you can pretend that
mothership "fetched" from you (useful when access is one sided).
1. on mothership machine, merge the work done on the satellite
machine into the master branch.

## Bash Script Info

```sh
url=$1 # or just use $1 in place where you'd insert the param.
branchname='name'
message=$2
git clone $url # git clone $1; then replace $1 w/ url when calling script
git status # what's changed since last commit
git checkout -b $branch_name
git add . # add all edited files to repo
git commit -m $message || $2
git push -u origin || git push ssh://git@ssh.github.com:443/($uname)/$repo.git
```

- You can do a compare & pull request to see changes that're done
- merge pull requests & del old branch

```sh
# conditionals
if [ "$fname" = "a.txt" ] || [ "$fname" = "c.txt" ]
if [[ "$fname" == "a.txt" || "$fname" == "c.txt" ]]; then
if test "$fname" = "a.txt" || test "$fname" = "c.txt"

#!/bin/bash

for fname in "a.txt" "b.txt" "c.txt"
do
  echo $fname
  if [ "$fname" = "a.txt" ] | [ "$fname" = "c.txt" ]; then
    echo "yes!"
  else
    echo "no!"
  fi
done

for i in {0..22..2}
do
    echo "Loop spin:" $i
done

for file in word_ls.sh num-rng.sh fi_name.sh # for file in *.sh
do
    ls -lh "$file"
done

chmod +x $fname # make fi exe
source || . $fname # exe a script file
```

___

### Bash commands

```sh
echo $BASH # => /usr/bin/bash
init $PATH
., .., ~, $HOME # current working dir, parent dir, home dir of user
ls -a -@ -l
ls -C -l

# remove dir & files
rm -r /folder/want-deleted # remove dir & content recursively
rm -rp # ignore permissions & errors
sudo rm -rf path/to/folder
su - user -c 'ls' # switch user and run cmd
mount -uw # mount with write permissions
mount -o update /
diskutil list
df -h
find / -size +50000 -print
sudo lshw (dmidecode) # lists hardware specs
gcreate (lvcreate | lvextend lvm2 | fdisk)
# create/manage logical pars spanning >= 1 HDD with logical volume manager
whereis (exe | cmd)
whatis <cmdname>
uname -a # show system info
free -gh #show memory usage --lohi -l from /proc/meminfo
service ssh status # check service status
ssh -l username hostname
top -u ib-ub
ps -ef | more # view running processes
ps -ef grep code
kill -9 PID
# killall, pkill, xkill to terminate unix process

ifconfig <interface_name> # (eth0)
# -a (show all details)
ifconfig etho1 (up | down) (enable/disable), muto 1500
ifconfig eth0 192.168.2.2 netmask 255.255.255.0 \
    broadcast 192.168.2.255
# ex. assign IP, netmask and broadcast to interface eth0

netstat -a | more # list all ports
# -at all tcp ports, -au all udp ports
# -s stats, -l (show listening only)
netstat -ap | grep ssh
# info on which port a prog is running on
netstat -an | grep ':80'
# which process is using a specific port

grep -i "word" file.txt # find str in fi
find -iname "file.txt" # find fi
find /home/ib-ub -name *.md -type f

gzip file.md && gzip -d file.md # (zip | unzip) .gz fi
unzip fi.zip && unzip -l fi.zip
# (extract | view) w/o unzipping fi
shutdown -h now #shutdown now or -r to restart now
cat -n /home/ib-ub/flow/work/Docs2/requirements3.txt # print file to stdout
chmod ug+rwx file.txt # change permissions of fi/dir [-R u-rwx ex. will remove access recursively]
chown ib-ub:group_name file.txt # change owner
passwd username # change password; use sudo to reset w/o old pass

useradd -D && useradd login_name # show default options and add user
adduser user_name  # for interactive user creation
newusers file_name
# bulk creation using pre-config template fi
# example
cat homer-family.txt
# homer:HcZ600a9:1008:1000:Homer Simpson:/home/homer:/bin/bash
# marge:1enz733N:1009:1000:Marge Simpson:/home/marge:/bin/csh
man 3 free # bring up section 3 of free cmd
tail -n 10 file.txt # show last 10 lines of fi
less large_file.txt # efficient view of log fi (CTRL+F/B forward/backward 1 window)
diff -w file1.md file2.md # compare fi, ignore whitespace

rsync # sync fi & dir between source & destination dirs
rsnapshot # combo of rsync & hard links to maintain
#   full | incremental backups
dd # make boot images & copy/backup HDDs
    # Copy fi, converting & formatting depending on operands
makeswap && swapon # (add | manage) swap space
dpkg # install/remove deb packages
# To-Do:
ps, top, vmstat, brk, mmap, systemctl, init
```

### curl

```sh
curl -o word-test.doc https://file-examples.com/wp-content/uploads/2017/02/file-sample_100kB.doc
curl -o test.png -u demo:password ftp://test.rebex.net/pub/example/KeyGenerator.png --compressed -# # or --progress-bar
redirect the response output to a file, using shell redirect (>), -o, --output
curl --dns-servers 1.1.1.1,1.0.0.1 --compressed -o $file -# $url
# use those dns servers, compress, output to file and use url variable
curl -u name:password --digest https://example.com
# prevents passwd from being sent as cleartext
curl --config file.txt https://example.com # -K file
--rate, -Y, --speed-limit and -y, --speed-time, -6 # use IPv6
# measured in bytes/second, unless suffix is appended, (k, M, G ex. 1k is 1024)
curl --interface eth0 https://example.com

curl --happy-eyeballs-timeout-ms 500 https://example.com # give ipv6 a headstart
# <!-- look up curl -F, --form -->
 curl -F '=(;type=multipart/alternative' \
      -F '=plain text message' \
      -F '= <body>HTML message</body>;type=text/html' \
      -F '=)' -F '=@textfile.txt' ...  smtp://example.com
 # --- Example file ---
 url = "example.com"
 output = "curlhere.html"
 user-agent = "superagent/1.0"
 url = "example.com/docs/manpage.html" # fetch another URL too
 -O
 referer = "http://nowhereatall.example.com/"
 # --- End of example file ---
```

### Bash Scripting

```sh
folder_to_count=$1
# $1, $2...$9 are used as general vars that enable providing parameters when calling the rx

file_count=$(ls $folder_to_count | wc -l)
file_count=$(ls $1 | wc -l) # or use w/o dir var

echo $file_count files in $folder_to_count

chmod +x fi.sh
# must make script fi exe.

./fnct2.sh /dev # run script with a paramater

# env vars
$#: How many command line parameters were passed to the script.
$@: All the command line parameters passed to the script.
$?: The exit status of the last process to run.
$$: The Process ID (PID) of the current script.
$USER: The username of the user executing the script.
$HOSTNAME: The hostname of the computer running the script.
$SECONDS: The number of seconds the script has been running for.
$RANDOM: Returns a random number.
$LINENO: Returns the current line number of the script
```

```sh
# install powershell on Ubuntu
# Update the list of packages
sudo apt-get update
# Install pre-requisite packages.
sudo apt-get install -y wget apt-transport-https software-properties-common
# Download the Microsoft repository GPG keys
wget -q "https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb"
# Register the Microsoft repository GPG keys
sudo dpkg -i packages-microsoft-prod.deb
# Update the list of packages after we added packages.microsoft.com
sudo apt-get update
# Install PowerShell
sudo apt-get install -y powershell
# Start PowerShell
pwsh
```

## Apt Info

```sh
apt [-h] [-o=config_string] [-c=config_file] [-t=target_release] [-a=architecture] {list | search | show | update | install pkg
[{=pkg_ver_num | /target_release}]... | remove pkg... | upgrade | full-upgrade | edit-sources | {-v --version} |{-h--help}}
```
<!-- cspell: enable  -->

>
interface for package management system.
To-Do: apt-get, apt-cache, sources.list, apt.conf, apt-config

- `update` (apt-get(8)) update is used to download package information from all configured sources. Other commands operate on this data to e.g. perform package upgrades or search in and display details about all packages available for installation
- `upgrade` (apt-get(8)) upgrade is used to install available upgrades of all packages   currently installed on the system from the sources configured via  sources.list(5). New packages will be installed if required to satisfy dependencies, but existing packages will never be removed. If an upgrade for a package requires the removal of an installed package the upgrade for this package isn\'t performed.
- `full-upgrade`: performs the function of upgrade but will remove currently installed packages if this is needed to upgrade the system as a whole.
- `install, reinstall, remove, purge`: Performs the requested action on one or more packages specified via regex(7), glob(7) or exact match. The requested action can be overridden for specific packages by appending a plus (+) to the package name to install this package or a minus (-) to remove it.
  - A specific version of a package can be selected for installation by following the package name with an equals (=) and the version of the package to select. Alternatively the version from a specific release can be selected by following the package name with a forward slash (/) and codename (buster, bullseye, sid ...) or suite name (stable,testing, unstable). This will also select versions from this release for dependencies of this package if needed to satisfy the request.
  - Removing a package removes all packaged data, but leaves usually small (modified) user configuration files behind, in case the remove was an accident. Just issuing an installation request for the accidentally removed package will restore its function as before in that case.
  - On the other hand you can get rid of these leftovers by calling purge even on already removed packages. Note that this does not affect any data or configuration stored in your home directory.
- `autoremove` is used to remove packages that were automatically installed to satisfy dependencies for other packages and are now no longer needed as dependencies changed or the package(s) needing them were removed in the meantime.
  - You should check that the list does not include applications you have grown to like even though they were once installed just as a dependency of another package. You can mark such a package as manually installed by using apt-mark(8). Packages which you have installed explicitly via install are also never proposed for automatic removal.
- `satisfy`: satisfies dependency strings, as used in Build-Depends. It also handles conflicts, by prefixing an argument with "Conflicts: <(value)>".
- `search`: can be used to search for the given regex(7) term(s) in the list of available packages and display matches. This can e.g. be useful if you are looking for packages having a specific feature. If you are looking for a package including a specific file try apt-file.
- `show`: information about the given package(s) including its dependencies, installation and download size, sources the package is available from, the description of the packages content and much more
- `list`: is somewhat similar to dpkg-query --list in that it can display a list of packages satisfying certain criteria. It supports glob patterns for matching package names as well as options to list installed (--installed), upgradeable (--upgradeable) or all available (--all-versions) versions.
- `edit-sources`: lets you edit your sources.list(5) files in your preferred text editor while also providing basic sanity checks.
-
<!-- cspell: disable  -->

## Shell command info

- ctrl + \ = Quit (SIGQUIT)
  - fquit a running instance
- open path/to/app.app
  - open an app from sh
- escape special chars:
  - prepending with \
  - wrapping it in single quotes

## Symbolic rep of data

| abbrev | value |
| --- | --- |
| no |  Global default |
|fi  |  Normal file |
|di  |  Directory|
|ln  |  Symbolic link |
|bd  |  Block device|
|cd  |  Character device|
|or  |  Symlink to non-existent fi |
|ex  |  Executable fi |
|*.extension | (ex: *.mp3)|

## Linux permissions

```py
# permission terms
r, w, x = read, write, execute | 4, 2, 1
u, g, o = user, group, others | first, sec., third (chars.)
```

```sh
chmod u+x file.txt
chmod u+r,g+x file.txt
chmod u-rx file.txt # remove permissions
chmod -R 775 dir_name/ # change perm of all fi in dir
chmode -R,a-x,u+X *
# recursively remove exec perm from all fi under
    # dir, then add exec for user
for f in 'ls -R'; do [! -d"$f"] && chmod a-x "$f"; done
# other solution
```

## Git Config terminal colors

| foreground('') k:int == v:str | background(bg) | style |
| --- | :--- | --- |
| 31 = red |40 = black bg | 0 = default color |
| 32 = green | 41  = red bg | 1 = bold |
| 33 = orange | 42  = green bg | 4 = underlined |
| 34 = blue | 43  = orange bg | 5 = flashing text |
| 35 = purple | 44  = blue bg | 7 = reverse field => (flip color) |
| 36 = cyan |  45  = purple bg |8 = concealed (invisible)|
| 37 = grey| 46  = cyan bg |
| 90 = dark grey | 47  = grey bg  |
| 91 = light red | 100 = dark grey bg|
| 92 = light green| 101 = light red bg|
| 93 = yellow | 102 = light green bg|
| 94 = light blue | 103 = yellow bg|
| 95 = light purple  |104 = light blue bg|
| 96 = turquoise |  105 = light purple bg|
| 97 = white | 106, 107 = turquoise, white bg |

----------

## PowerShell

### Pwsh Paths

- $PSHOME is /opt/microsoft/powershell/7/
- User profiles are read from ~/.config/powershell/profile.ps1
- Default profiles are read from $PSHOME/profile.ps1
- User modules are read from ~/.local/share/powershell/Modules
- Shared modules are read from /usr/local/share/powershell/Modules
- Default modules are read from $PSHOME/Modules
- PSReadLine history is recorded to ~/.local/share/powershell/PSReadLine/ConsoleHost_history.txt

```ps1
get-help [command] -detailed
# get more info of a command

Get-WindowsFeature -ComputerName "Server1" -Credential "contoso.com\user1"

Get-WindowsFeature [[-Name] <String[]>] [-ComputerName <String>] [-Credential <PSCredential>] [-LogPath
    <String>] [-Vhd <String>] [<CommonParameters>]

Copy-Item './images/*' '/home/user/flow/work/Apps/' -Recurse

$Session = New-PSSession -ComputerName "Server04" -Credential "Contoso\User01"
Copy-Item "D:\Folder003\" -Destination "C:\Folder003_Copy\" -ToSession $Session -Recurse

Get-Service | Where-Object {$_.Status -eq "Running"}
# get active services
Get-Service "s*" | Sort-Object status
# sort by prop value

Get-Service "WinRM" -RequiredServices
#  get services that depend on this service
```

### Pwsh Commands to review

- Add-WindowsPackage
- Enable-WindowsOptionalFeature
- Get-WindowsFeature
- Get-WindowsPackage
- Install-WindowsFeature {Uninstall}
- Enable-ServerManagerStandardUserRemoting {Disable}
- New-Service
  - {Restart | Resume | Set | Start | Stop | Suspend | Remove}

### Excel

```ps1
# purge accounts
Import-Csv '.\SP 23 Declines.csv' | foreach {
  $UPN = $_."PPU Email"
  $username = $UPN.Substring(0, $UPN.IndexOf('@'))
  get-aduser $Username | Remove-ADUser
}


Import-Csv '.\CancelDeclines F22 for IT.csv' | foreach {
  $UPN = $_."PPU Email"
  $username = $UPN.Substring(0, $UPN.IndexOf('@'))
  get-aduser $Username | Remove-ADUser
}
```

### Vim

- use `vimtutor` for tutorial on using vim
- to-do: swap file and get info on nano
  - created temp swap file by running `vim tutor`
