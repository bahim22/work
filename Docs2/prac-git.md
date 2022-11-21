
# Steps for ssh into git repo

```sh
ls -al ~/.ssh # list files in .ssh dir
ssh-keygen -t ed25519 -C "email@google.com"
# enter passphrase to use && this creates pub/priv key pair
#  saves to .ssh/id_ed25519 & ''.pub; generates key fingerprint and randomart image
eval "$(ssh-agent -s)" #check if agent is running
ssh-add ~/.ssh/id_ed25519 #add id to ~
cat ~/.ssh/id_ed25519.pub # display pub key then c/v to github acct
ssh -T git@github.com # test connection & clone repo
git clone git@github.com:<username>/<repo>.git
code .
```
