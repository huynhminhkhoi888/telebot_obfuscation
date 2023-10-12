#Code By Huynh Minh Khoi | From Viet Nam With Love
#Hoang Sa and Truong Sa belongs to Vietnam!!!!
#Debug Accordingly
#This Is A Project I Code For Someone Else
#Obfuscation Is Not Mine, It Belongs To Github
import os
try:
    import telebot, random, sys
    import datetime, base64
    import marshal as marshal
    from pystyle import *
except:
    os.system('pip install telebot')
    os.sytem('pip install pystyle')
API_TOKEN_BOT = '' #Change To Your Bot Token
USER_ADMIN_BOT = '' #Change To Your Telegram User
bot = telebot.TeleBot(API_TOKEN_BOT)
banner = ("""
██╗  ██╗██╗   ██╗███╗   ██╗    ████████╗ ██████╗  ██████╗ ██╗     
██║ ██╔╝██║   ██║████╗  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
█████╔╝ ██║   ██║██╔██╗ ██║       ██║   ██║   ██║██║   ██║██║     
██╔═██╗ ██║   ██║██║╚██╗██║       ██║   ██║   ██║██║   ██║██║     
██║  ██╗╚██████╔╝██║ ╚████║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ """)
colors = Col.red_to_purple
whiteChars = list('═╝╚╔╗║')
space = '   ' * 5
print(Colorate.Format(Center.XCenter(banner), whiteChars, Colorate.Vertical, colors, Col.white))
Write.Print(f"\n{space * 2}HELLO WORLD!!!\n", Colors.red_to_blue, interval = 0.01)
Write.Print(f"{space}         START BOT IS SUCCESSFUL!!!\n", Colors.red_to_white, interval = 0.01)
ban_id = {}
tg1 = None
def ban_phut(chat_id):
    if chat_id in ban_id:
        check_gio_or_phut, timestamp = ban_id[chat_id]
        if 'm' in check_gio_or_phut.lower():
            current_time = datetime.datetime.now()
            time_ban = check_gio_or_phut.lower().replace('m', '')
            if current_time - timestamp <= datetime.timedelta(minutes=int(time_ban)):
                return 'ban_phut'
            else:
                del ban_id[chat_id]
        elif 'h' in check_gio_or_phut.lower():
            current_time = datetime.datetime.now()
            time_ban = check_gio_or_phut.lower().replace('h', '')
            if current_time - timestamp <= datetime.timedelta(hours=int(time_ban)):
                return 'ban_gio'
            else:
                del ban_id[chat_id]
    else:
        return 'bo_ban'
class Impostor():

    serializer = marshal

    def Alt(text: str, evalCode: bool = True) -> str:
        formated = '+'.join(f'chr({char})' for char in [ord(char_) for char_ in text])
        return f'eval(eval({formated!r}))' if evalCode else f'eval({formated!r})'

    hidedText = 'GG! You deobfuscated the code! obfuscated by Impostor'
    exceptionCode = 'input("Don\'t try to skid Impostor obfuscation !");exit(0)'
    gitLink = 'Đang cập nhật'

    infos = {
        '__author__': 'BNAM X HNAM',
        '__madeBy__': 'https://facebook.com/@nam.nhn131',
    }
    gatewayKey = random.randint(0, 10000)
    def Gateway() -> str:
        obj = globals()['__selfObject__']
        interpreterObj = globals()['__InterpreterObject__']
        key = globals()['__key__']
        code = interpreterObj.code['bytes']
        obj.executed = True
        return ((key * 8 / 1.5), code)
    comment = 'Obfuscated by Nam'
    encCommend = ' + '.join(f'chr({char})' for char in [ord(char_) for char_ in comment])
    checkInfos = ' and '.join(f'globals().get("{key}") == {value!r}' for key, value in infos.items()) + \
        f' and ("# " and {encCommend}) in open(__import__("os").path.abspath(__file__), "r", encoding = "utf-8").read() '
    interpreterClass = """
class Nam():
  def __init__(self, code: str, layersFunction: bytes, module, globals_, backend: bytes = b'') -> None: self.__module = module;self.layersFunction = layersFunction;self.__globals = globals_;self.code = {'bytes': code, 'str': str(code)}; self.__backend = backend
  def __tunnel(self) -> NamNguyen: return NamNguyen(self.__backend, GATEWAYKEY, __module = self.__module, __globals = self.__globals, interpreter = self)
  def Run(self) -> None: decoder = self.__getobject__(); gate = self.__tunnel().Pass();exec(eval(MARSHALMODULE.loads(decoder), {'__selfObject__': self, '__module': self.__module, '__sr_m': MARSHALMODULE, '__globals': self.__globals, 'gate': gate}), self.__globals)
  def __getobject__(self) -> object: func = self.layersFunction; return self.__module.b64decode(func)
"""[1:-1].replace('MARSHALMODULE', Alt('__import__("marshal")')).replace('GATEWAYKEY', str(gatewayKey))

    gatewayClass = """
class NamNguyen():
  def __init__(self, way: bytes, key: int, **ext) -> None: self.way = way;self.key = key; self.module__ = ext.get('__module', None);self.__globals = ext.get('__globals', None);self.__module = ext.get('__module', None); self.__interpreter = ext.get('interpreter', None)
  def Pass(self): exec(MARSHALMODULE.loads(self.module__.b16decode(self.way)), {'__selfObject__': self, '__key__': self.key, '__module': self.module__, '__globals': self.__globals, '__InterpreterObject__': self.__interpreter}); return self
"""[1:-1].replace('MARSHALMODULE', Alt('__import__("marshal")'))

    def RemoveLayers() -> str:
        _globals = globals()['__globals']
        if not globals().get('gate'): return
        obj = globals()['__selfObject__']
        module = globals()['__module']
        code = obj.code['bytes']
        code = module.b85decode(code)
        code = module.b64decode(code)
        code = module.b32decode(code)
        code = module.b16decode(code)
        code = globals()['__sr_m'].loads(code)
        return code

    def Obfuscate(code: str) -> str:
        sys.setrecursionlimit(1000000)

        _code = code
        program = r"{'__name__': '__main__'}"
        runCode = f"""
if not ({Impostor.checkInfos}): {Impostor.exceptionCode}
exec({_code!r}, {program})
"""[1:-1]

        code__ = Impostor.serializer.dumps(compile(runCode, 'Impostor', 'exec'))
        infos_ = '\n'.join(f'{key} = {value!r}' for key, value in Impostor.infos.items())

        code__ = base64.b16encode(code__)
        code__ = base64.b32encode(code__)
        code__ = base64.b64encode(code__)
        code__ = base64.b85encode(code__)

        code_ = f"""
{infos_}

# {Impostor.comment}

{Impostor.gatewayClass}
{Impostor.interpreterClass}

Nam({code__!r},
            {base64.b64encode(Impostor.serializer.dumps(Impostor.RemoveLayers.__code__))!r},
            {Impostor.Alt('__import__("base64")')}, globals(),
            {base64.b16encode(Impostor.serializer.dumps(Impostor.Gateway.__code__))!r}
).Run()
"""[1:-1]
        return code_


  
@bot.message_handler(commands = ['start'])
def echo(message):
    if ban_phut(message.chat.id) == 'ban_phut':
        tg, cc = ban_id[message.chat.id]
        bot.reply_to(message, 'You Are Banned {}'.format(tg.lower().replace('m', ' Minutes')))
        return
    elif ban_phut(message.chat.id) == 'ban_gio':
        tg, cc = ban_id[message.chat.id]
        bot.reply_to(message, 'You Are Banned {}'.format(tg.lower().replace('h', ' Hours'))) 
        return
    print('Latest users: {} | chat_id: {} | Time: {} | Commands: /start'.format(message.from_user.username, message.chat.id, datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")))
    user = message.from_user.username
    bot.reply_to(message, "Hi @{} You Can Using All Commands Such As: \n/obf_impostor - Impostor Obfuscation\n/obf_marshal - Marshal Obfuscation".format(user))

def obf_impostor(message):
    if message.document is None:
        bot.reply_to(message, ">>File Not Found<<")
        return
    #new = str(uuid.uuid4())[:8]
    new = str(message.chat.id + random.randint(0, 9999999))
    try:
        file_info = bot.get_file(message.document.file_id)
        bot.reply_to(message, '>>Loading File Information<<')
        downloaded_file = bot.download_file(file_info.file_path)
        bot.reply_to(message, ">>Get File Successfully<<")
        bot.send_message(message.chat.id, ">>Wait A Minute<<")
        code = downloaded_file.decode()
        obf = Impostor.Obfuscate(code)
        
        open(f'{new}.py', 'w').write(obf)
        file = open(f'{new}.py', 'r')
        bot.send_document(message.chat.id, file)
        os.remove(f'{new}.py')
        bot.send_message(message.chat.id, ">>Please Run The File Again Before Sharing<<")
    except Exception as e:
        bot.reply_to(message, "Error {}".format(e))
@bot.message_handler(commands = ['obf_impostor'])
def main_demo(message):
    if ban_phut(message.chat.id) == 'ban_phut':
        tg, cc = ban_id[message.chat.id]
        bot.reply_to(message, 'You Are Banned {}'.format(tg.lower().replace('m', ' Minutes'))) 
        return
    elif ban_phut(message.chat.id) == 'ban_gio':
        tg, cc = ban_id[message.chat.id]
        bot.reply_to(message, 'You Are Banned {}'.format(tg.lower().replace('h', ' Hours'))) 
        return
    print('Latest users: {} | chat_id: {} | Time: {} | Commands: /obf_impostor'.format(message.from_user.username, message.chat.id, datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")))
    bot.reply_to(message, ">>Send Me File<<")
    bot.register_next_step_handler(message, obf_impostor)

@bot.message_handler(commands = ['obf_marshal'])
def main_marshal(message):
    if ban_phut(message.chat.id) == 'ban_phut':
        tg, cc = ban_id[message.chat.id]
        bot.reply_to(message, 'You Are Banned {}'.format(tg.lower().replace('m', ' Minutes'))) 
        return
    elif ban_phut(message.chat.id) == 'ban_gio':
        tg, cc = ban_id[message.chat.id]
        bot.reply_to(message, 'You Are Banned {}'.format(tg.lower().replace('h', ' Hours'))) 
        return
    print('Latest users: {} | chat_id: {} | Time: {} | Commands: /obf_marshal'.format(message.from_user.username, message.chat.id, datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")))
    bot.reply_to(message, ">>We haven't updated yet!<<")
    return
@bot.message_handler(commands = ['bantamthoi'])
def bantamthoi(message):
    if message.from_user.username != USER_ADMIN_BOT:
        bot.reply_to(message, "You Do Not Have Permission To Use This Command!")
        return
    if len(message.text.split()) < 3:
        bot.reply_to(message, "Please Enter /bantamthoi + chat_id + Minutes Or Hours!\nExample: /bantamthoi 123456 5m Or\n/bantamthoi 12345 2h")
        return
    chat_id = message.text.split()[1]
    tg = message.text.split()[2]
    ban_id[int(chat_id)] = (tg, datetime.datetime.now())
    bot.reply_to(message, "Ban Successfully chat_id: {} In {}".format(chat_id, tg))
@bot.message_handler(commands = ['boban'])
def boban(message):
    if message.from_user.username != USER_ADMIN_BOT:
        bot.reply_to(message, "You Do Not Have Permission To Use This Command!")
        return
    if len(message.text.split()) < 2:
        bot.reply_to(message, "Please Enter /boban + chat_id\nExample: /boban 123456")
        return
    chat_id = message.text.split()[1]
    del ban_id[int(chat_id)]
    bot.reply_to(message, "Leave The Ban Successfully chat_id: {}".format(chat_id))
bot.polling()
