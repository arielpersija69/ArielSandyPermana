# # # # # # # # # # # # # # # # # # # # # # # # # 
#                                               #
#       Njir Script buat recode di recode       #
#                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # 

from sys import stdout 

import subprocess as sp,sys,os,marshal,re,time,json,base64,random,requests

#Warna
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'    
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'

#warna backgound
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'


try:
    from uncompyle6.main import decompile
except Exception as e:
    sp.call('pip2 install uncompyle2', shell=True, stderr=sp.STDOUT)

def banner():
     jalan(bm+"""  _______"""+ m + '   Compile & Decompile Marshal   '+ p + bm +"""__    
 |   _   .-----.--------.---.-.----.-----|  |--.
 |.  1___|  _  |        |  _  |   _|__ --|     |
 |.  |___|_____|__|__|__|___._|__| |_____|__|__|
 |:  1   |"""+ h + '['+ p +'T'+ h +']'+ k + 'oolkit version.2.0  '+ p + bm + """
 |::.. . |"""+ h + '['+ p +'C'+ h +']'+ k + 'oded by Ahmad Riswanto Recode By Ariel Sandy Permana '+ p + bm +"""
 `-------'"""+ h + '['+ p +'C'+ h +']'+ k + 'ontact'+p+'['+h+'WA'+p+']'+k+' : +6283103023425   \n'+ p, 0.001)                                    

def load(word):
    lix = [
     '/', '-', '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.3)
            sys.stdout.flush()

def jalan(z, t):
    for e in z :
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)                                               

def menu():
    os.system('clear')
    banner()
    print h +'\nMenu '+ p +': \n ['+ h + '1' + p +']. Compiler\n ['+ h + '2' + p +']. Uncompiler\n ['+ h + '3' + p +']. '+'Update \n ['+ h + '4' + p +'].'+ m +' Exit\n\n '+ p +'['+ h + '99' + p +'].'+ u +' Report Bug\n'+ p
    pilih = raw_input( h+ '['+ k +'?'+ h +']'+ p +' Choice--> ')
    if pilih == '1':
        marsh()
    else:
        if pilih == '2':
            unmarsh()
        else:
            if pilih == '3':
                try:
                    os.system('git pull')
                except:
                    print  h + '['+ m +'!'+ h +']'+ p + ' Update Failed '
                    pl = raw_input(h + '['+ k +'?'+ h +']'+ p + '  Manual Download? y/t ')
                    if pl == 'y' or pl == 'Y':
                        try:
                            sp.check_output([
                             'am', 'start',
                             'https://github.com/AhmadRiswanto704/comarsh'])
                        except:
                            sys.exit(h +'['+ k +'!'+ h +']'+ p +' Failed to open the link')
                            
                    else:
                        menu()
                        
            else:
                if pilih == '4':
                    jalan('\n'+ h +'['+ k +'#'+ h +']'+ p +' Created by Ahmad Riswanto ', 0.01)
                    jalan(h + '\n' +'['+ k +'#'+ h +']'+ p +' Thank You for Using This Program ', 0.01)
                    jalan(h + '\n' +'['+ k +'#'+ h +']'+ p + ' contact(github) : https://github.com/AhmadRiswanto704', 0.01)
                    jalan(h + '\n' +'['+ k +'#'+ h +']'+ p +' contact(Facebook) : https://www.facebook.com/ahmad.riswanto.180', 0.01)
                    jalan(h + '\n' +'['+ k +'#'+ h +']'+ p + ' contact(Wa) : +6289678711863', 0.01)
                    jalan(h +'\n' +'['+ k +'#'+ h +']'+ p +' Good bye `\\_(@)_/`\n', 0.01)
                    sys.exit()
                else:
                    if pilih == '99':
                        jalan(p + 31 * '\xe2\x95\x90' + h +'['+bm+'Report'+h+']'+p+'>', 0.008)
                        print '\n'+ h +'['+ m +'!'+ h +']'+ p +' Report Bug Via WhatsApp '
                        bug = raw_input(h +'['+ k +'?'+ h +']'+ p +' Enter your message : ')
                        bug.replace(' ', '%20')
                        load(h +'['+ k +'~'+ h +']'+ p + 'Loading please wait ...')
                        try:
                            sp.check_output([
                             'am', 'start',
                             'https://api.whatsapp.com/send?phone=6289678711863&text=Masalah : '+ bug + ''])
                            
                        except:
                            sys.exit('\n'+ h +'['+ k +'!'+ h +']'+ p +' Failed to send message ')
                    else:
                        if pilih == '':
                            print '\n'+ h +'['+ m +'!'+ h +']'+ p +' Not Null '+ m +'!!!'
                            raw_input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu')
                            menu()
                        else:
                            print '\n'+ h +'['+ m +'!'+ h +']'+ p +' Pilih Yang Bener '+ m +'!!!'
                            raw_input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')
                            os.system('clear')
                            menu()
def marsh():
    jalan(p + 31 * '\xe2\x95\x90' + h +'['+bm+'COMPILER'+h+']'+p+'>', 0.008)
    print h + '\nMenu '+ p + ':\n ['+ h + '1' + p +']. Compile Python 2\n ['+ h + '2' + p +']. Compile Python 3\n ['+ h + '3' + p +']. Compile Python to pyc\n ['+ h + '4' + p +'].'+ k +' Back\n'
    try:
        pil = raw_input( h+ '['+ k +'?'+ h +']'+ p +' Choice--> ')
    except Exception as e:
        marsh()
    
    if pil == '1':
        v = 2
    else:
        if pil == '2':
            v = 3
        else:
            if pil == '3':
                pyc()
            else:
                if pil == '4':
                    menu()
                else:
                    print h +'['+ m +'!'+ h +']'+ p + ' Choose the right one'
                    marsh()
    try:
        if v == 2:
            print h +'['+ k +'#'+ h +']'+ p +" For Example : /path/marsh.py"
            file = raw_input( h+ '['+ k +'?'+ h +']'+ p +' Input File : ')
        else:
            if v == 3:
                py3()
                try:
                    sp.call('python3 cac.py', shell=True, stderr=sp.STDOUT)
                except Exception as e:
                    sys.exit(h +'['+ k +'!'+ h +']'+ p +" Compile Fail because : "+ e)
                os.system('rm cac.py')
                load(h +'['+ k +'#'+ h +']'+ p +' Compile process Wait a minute ...')
                time.sleep(1.5)
                os.system('clear')
                time.sleep(1)
                delay = open('com/com-3.py', 'r').readlines()
                for x in range(len(delay)):
                    jalan(delay[x], 0.0001)
                print '\n'+ h +'['+ k +'#'+ h +']'+ p +' Successfully Compiled'
                print h +'['+ k +'#'+ h +']'+ p +' file saved : com/com-3.py'
                ask = raw_input(h +'['+ k +'?'+ h +']'+ p +' Compile Again? y/t ')
                if ask == 'y' or ask == 'Y':
                    menu()
                else:
                    if ask == 't' or ask == 'T':
                        sys.exit()
                    else:
                        print h +'['+ m +'!'+ h +']'+ p +' Choose the right one '+ m +'!!!'
                        raw_input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')
                        os.system('clear')
                        menu()

    except IndexError:
        print h +'['+ m +'!'+ h +']'+ p +' Program Error!!!'
        sys.exit()
    except KeyboardInterrupt:
        print h +'['+ k +'^'+ h +']'+ p +' ctrl+c \n'
        print h +'['+ k +'#'+ h +']'+ p +' Exit!!!\n'
        time.sleep(3)
        sys.exit()
    except EOFError:
        print h +'['+ k +'^'+ h +']'+ p +' ctrl+d \n'
        print h +'['+ k +'#'+ h +']'+ p +' Exit!!!\n'
        time.sleep(3)
        sys.exit()
    else:
        try:
            string = open(file, 'r').read() 
        except IOError:
            print '\n'+ h +'['+ m +'!'+ h +']'+ p +' File not found'
            raw_input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')
            os.system('clear')
            menu()
        try:
            code = compile(string, '<Ahmad_Riswanto>', 'exec')
            load(h +'['+ k +'#'+ h +']'+ p +' Compile process Wait a minute ...')
            time.sleep(1.5)
            data = marshal.dumps(code)
        except SyntaxError:
            jalan('\n'+ h +'['+ m +'!'+ h +']'+ p +' script Using python version 3 \n', 0.1)
            jalan(h +'['+ m +'!'+ h +']'+ p +' Use the Menu [2]. Compile Python 3\n', 0.1)
            raw_input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')
            menu()
        except TypeError:
            os.system('clear')
            banner()
            print '\n'+ h +'['+ k +'#'+ h +']'+ p +' file already compiled\n'
            sys.exit()
    fileout = open('com/com-2.py', 'wb')
    fileout.write('#Compiled By Ahmad Riswanto')
    fileout.write('\n#Facebook : https://www.facebook.com/ahmad.riswanto.180')
    fileout.write('\nimport marshal')
    fileout.write('\nexec(marshal.loads(' + repr(data) + '))')
    fileout.close()
    os.system('clear')
    time.sleep(1)
    delay = open('com/com-2.py', 'r').readlines()
    for x in range(len(delay)):
        jalan(delay[x], 0.0001)
    print '\n'+ h +'['+ k +'#'+ h +']'+ p +' file successfully compiled'
    print h +'['+ k +'#'+ h +']'+ p +' file saved : com/com-2.py'
    ask = raw_input(h +'['+ k +'?'+ h +']'+ p +' Compile Again? y/t ')
    if ask == 'y' or ask == 'Y':
        menu()
    else:
        if ask == 't' or ask == 'T':
            sys.exit()
        else:
            print h +'['+ m +'!'+ h +']'+ p +' Choose the right one '+ m +'!!!'
            raw_input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')
            os.system('clear')
            menu()
def py3():
    text = """import marshal, os, sys, time
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'

def jalan(z, t):
    for e in z :
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)  

print(h +'['+ k +'#'+ h +']'+ p + ' For Example : /path/marsh.py')
f = input(h +'['+ k +'?'+ h +']'+ p + ' Enter Your File : ')
try:
    file = open(f).read()
except IOError:
    print( h +'['+ m +'!'+ h +']'+ p +' File Not Found')
    input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')
    os.system('clear')
    os.system('python2 data/main.py')

try:
    x = compile(file, '<Ahmad_Riswanto>', 'exec')
    data = marshal.dumps(x)
except SyntaxError:
    jalan(h +'['+ m +'!'+ h +']'+ p +' script Using python version 2 \\n', 0.1)
    jalan(h +'['+ m +'!'+ h +']'+ p +' Use the Menu [1]. Compile Python 2\\n', 0.1)
    input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')
    os.system('python2 data/main.py')
except TypeError:
    os.system('clear')
    banner()
    print(h +'['+ k +'#'+ h +']'+ p +' File Already Compiled')
    sys.exit()

open('com/com-3.py', 'w').write('import marshal\\n#Compile by Ahmad Riswanto\\n#Facebook : https://www.facebook.com/ahmad.riswanto.180\\nexec(marshal.loads('+repr(data)+'))')"""
    cac = open('cac.py', 'w')
    cac.write(text)
    cac.close()

def pyc():
    print(h +'['+ k +'#'+ h +']'+ p + ' For Example : /path/marsh.py')
    f = raw_input(h +'['+ k +'?'+ h +']'+ p + ' Enter Your File : ')
    from py_compile import compile
    compile(f)
    load(h +'['+ k +'#'+ h +']'+ p +' Compile process Wait a minute ...')
    jalan('\n'+ h +'['+ k +'#'+ h +']'+ p +' file successfully compiled', 0.01)
    print '\n'+ h +'['+ k +'#'+ h +']'+ p +" File Saved: {}c".format(f)
    ask = raw_input(h +'['+ k +'?'+ h +']'+ p +' Compile Again? y/t ')
    if ask == 'y' or ask == 'Y':
        menu()
    else:
        if ask == 't' or ask == 'T':
            sys.exit()
        else:
            print h +'['+ m +'!'+ h +']'+ p +' Choose the right one '+ m +'!!!'
            raw_input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')
            os.system('clear')
            menu()
    
def unmarsh():
    jalan(p + 31 * '\xe2\x95\x90' + h +'['+bm+'DECOMPILER'+h+']'+p+'>', 0.008)
    print h + '\nMenu '+ p + ':\n ['+ h + '1' + p +']. Automatic Detection Version Script\n ['+ h + '2' + p +']. Decompile Pyc to Py\n ['+ h + '3' + p +'].'+ k +' Back\n'
    try:
        pil = raw_input( h+ '['+ k +'?'+ h +']'+ p +' Choice--> ')
    except IOError:
        unmarsh()
    if pil == '1':
        pass
    else:
        if pil == '2':
            unpyc()
            os.system('clear')
            time.sleep(1)
            os.system('cat dec/jadiEnc.py')
            jalan('\n'+ h +'['+ k +'#'+ h +']'+ p +' file successfully Decompiled', 0.01)
            print '\n'+ h +'['+ k +'#'+ h +']'+ p +" File Saved: dec/jadiEnc.py"
            ask = raw_input(h +'['+ k +'?'+ h +']'+ p +' Compile Again? y/t ')
            if ask == 'y' or ask == 'Y':
                menu()
            else:
                if ask == 't' or ask == 'T':
                    sys.exit()
                else:
                    print h +'['+ m +'!'+ h +']'+ p +' Choose the right one '+ m +'!!!'
                    raw_input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')
                    os.system('clear')
                    menu() 
        else:
            if pil == '3':
                menu()
            else:
                print h +'['+ m +'!'+ h +']'+ p + ' Choose the right one'
                unmarsh()
                           
    cek = 1
    try:
        print h +'['+ k +'#'+ h +']'+ p +" For Example : /path/marsh.py"
        file = raw_input( h+ '['+ k +'?'+ h +']'+ p +' Input File : ')
        f = open(file, 'r').readlines()
        for i in range(len(f)):
            if f[i][0:4] == 'exec':
                if f[i][19] == 'b':
                    cek = 3
                else:
                    if f[i][20] == 'c':
                        cek = 2
                    else:
                        cek = 1

    except IndexError:
        print h +'['+ m +'!'+ h +']'+ p +' Program Error!!!'
        sys.exit()
    except KeyboardInterrupt:
        print h +'['+ k +'^'+ h +']'+ p +' ctrl+c \n'
        print h +'['+ k +'#'+ h +']'+ p +' Exit!!!\n'
        time.sleep(3)
        sys.exit()
    except EOFError:
        print h +'['+ k +'^'+ h +']'+ p +' ctrl+d \n'
        print h +'['+ k +'#'+ h +']'+ p +' Exit!!!\n'
        time.sleep(3)
        sys.exit()
    else:
        try:
            string = open(file, 'r').read() 
        except IOError:
                print '\n'+ h +'['+ m +'!'+ h +']'+ p +' File Not Found'
                raw_input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')
                os.system('clear')
                menu()
        if cek == 2:
            py = 'python2'
            dec = 'decompile(2.7, x, stdout)'
            sys.stdout.write( h +'['+ k +'#'+ h +']')
            jalan(p +' check the script version', 0.1)
            time.sleep(1.5)
            print '\n'+ h +'['+ m +'*'+ h +']'+ p +' python version 2 was detected'
            time.sleep(1)
            try:
                x = re.search(r'((?<![\\])[\'"])((?:.(?!(?<![\\])\1))*.?)\1', string).group()
            except Exception as e:
                raise e
        else:
            if cek == 3:
                py = 'python3'
                dec = 'decompile(3.7, x, stdout)'
                sys.stdout.write( h +'['+ k +'#'+ h +']')
                jalan(p +' check the script version', 0.1)
                time.sleep(1.5)
                print '\n'+ h +'['+ m +'*'+ h +']'+ p +' python version 3 was detected'
                time.sleep(1)
                try:
                    x = 'b' + re.search(r'((?<![\\])[\'"])((?:.(?!(?<![\\])\1))*.?)\1', string).group()
                except Exception as e:
                    raise e
            else:
                print h +'['+ m +'!'+ h +']'+ p +' File Not Suport'
                raw_input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')
                menu()

    fileout = open('un.py', 'w')  
    fileout.write('from sys import stdout\nfrom uncompyle6.main import decompile\nimport marshal\n\n')
    fileout.write('x = marshal.loads('+ x + ')\n')
    fileout.write(dec)
    fileout.close()
    load(h +'['+ k +'#'+ h +']'+ p +' Unmarshal process Wait a minute ...')
    sp.call(py + ' un.py > dec/dec.py', shell=True, stderr=sp.STDOUT)
    os.system('rm un.py')
    os.system('clear')
    time.sleep(1)
    delay = open('dec/dec.py', 'r').readlines()
    for x in range(len(delay)):
        jalan(delay[x], 0.0001)
    print '\n\n'+ h +'['+ k +'#'+ h +']'+ p +' Successfully Decompiled'
    print h +'['+ k +'#'+ h +']'+ p +' file saved : dec/dec.py'
    ask = raw_input( h +'['+ k +'?'+ h +']'+ p +' Decompile Again? y/t ')
    if ask == 'y' or ask == 'Y':
        menu()
    else:
        if ask == 't' or ask == 'T':
            sys.exit()
        else:
            print h +'['+ m +'!'+ h +']'+ p +' Choose the right one '+ m +'!!!'
            raw_input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')
            os.system('clear')
            menu()
def unpyc():
    print(h +'['+ k +'#'+ h +']'+ p + ' For Example : /path/marsh.pyc')
    f = raw_input(h +'['+ k +'?'+ h +']'+ p +' Enter Your File : ')  
    try:     
        open(f, 'r').read() 
    except IOError:
        print h +'['+ m +'!'+ h +']'+ p +' File Not Found'
        raw_input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')
        menu()
    load(h +'['+ k +'#'+ h +']'+ p +' Decompile process Wait a minute ...')
    try:
        os.system('uncompyle6 '+ f +'> dec/jadiEnc.py')
    except Exception as e: 
        print h +'['+ m +'!'+ h +']'+ p +' Failed to decompile because : ' + e

    print '\n\n'+ h +'['+ k +'#'+ h +']'+ p +' Successfully Decompiled'
    print h +'['+ k +'#'+ h +']'+ p +' file saved : dec/jadiEnc.py'
    ask = raw_input( h +'['+ k +'?'+ h +']'+ p +' Decompile Again? y/t ')
    if ask == 'y' or ask == 'Y':
        menu()
    else:
        if ask == 't' or ask == 'T':
            sys.exit()
        else:
            print h +'['+ m +'!'+ h +']'+ p +' Choose the right one '+ m +'!!!'
            raw_input(h +'['+ k +'^'+ h +']'+ p +' Press Enter to Return to the menu ')
            os.system('clear')
            menu()

def cek():
    dt = '.Session'
    if os.path.exists(dt):
        if os.path.exists('%s/com.txt' % dt):
            if os.path.getsize('%s/com.txt' % dt) != 0:
                id = open('%s/com.txt' % dt).read().replace('\n', '')
                idj = json.loads(id)
                try:
                    z = requests.get('https://comarsh.000webhostapp.com/%s' % ('registered.txt')).text                    
                except:
                    sys.exit( h + '['+ m +'!'+ h +']'+ p + ' Check your internet connection ')

                if len(re.findall(idj['sessionID'], z)) != 0:
                    menu()
                else:
                    try:
                        z = requests.get('https://comarsh.000webhostapp.com/%s' % ('ip.txt')).text                    
                    except:
                        sys.exit( h + '['+ m +'!'+ h +']'+ p + ' Check your internet connection ')                

                    if len(re.findall(idj['sessionID'], z)) != 0:
                        print h + '['+ m +'!'+ h +']'+ p +' Nama anda sudah diregistrasi'
                        print h + '['+ m +'!'+ h +']'+ p +' silahkan meminta konfirmasi Ahmad Riswanto'
                        print h + '['+ k +'#'+ h +']'+ p +' Username Anda: %s' % idj['username']
                        raw_input(h + '['+ k +'^'+ h +']'+ p +' tekan enter untuk menghubungi Ahmad via WhatsApp...')
                        sp.check_output([
                             'am', 'start',
                             'https://api.whatsapp.com/send?phone=6289678711863&text=konfirm%20saya%20dengan%20username:%20' + idj['username'].replace(' ', '%20') + ''])                           
                                     
                    else:
                        sys.exit(h + '['+ m +'!'+ h +']'+ p +' Silakan ketik python2 comarsh.py'+ m +' !!!' + p)
            else:
                sys.exit(h + '['+ m +'!'+ h +']'+ p +' Silakan ketik python2 comarsh.py'+ m +' !!!' + p)
        else:
            sys.exit(h + '['+ m +'!'+ h +']'+ p +' Silakan ketik python2 comarsh.py'+ m +' !!!' + p)
    else:
        sys.exit(h + '['+ m +'!'+ h +']'+ p +' Silakan ketik python2 comarsh.py'+ m +' !!!' + p )

if __name__ == '__main__':
    if os.path.exists('com') or os.path.exists('dec'):
        menu()
    else:
        os.system('mkdir com')
        os.system('mkdir dec')
        menu()
