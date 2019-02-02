import itchat

have_repeated = []
old_msg = ''
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def repeater(msg):
    global old_msg
    new_msg = msg.text
    if (new_msg == old_msg) and ( not (new_msg in have_repeated) ):
        have_repeated.append(new_msg)
        print(new_msg)
        return new_msg
    else:
        old_msg = new_msg

itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run()
