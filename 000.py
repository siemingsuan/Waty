import random,easygui
secret=random.randint(1,21)
guess=0
tries=0
easygui.msgbox("caishuyouxi,1-20,6cijihui")
while guess !=secret and tries<6:
    guess=easygui.integerbox("shuru")
    if not guess:break
    if guess<secret:
        easygui.msgbox(str(guess)+"taidi,go")
    elif guess>secret:
        easygui.msgbox(str(guess)+"taigao,sha")
    tries=tries+1
if guess==secret:
    easygui.msgbox("duile")
else:
    easygui.msgbox("meijihui,daanshi"+str(secret))
