import os, platform, time
print('\n\x1b[1;37m Checking Update...');time.sleep(0.5)
def Update():
    exit('\033[1;31m(×) Commands On Update Please Wait For Update ❤ ')
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            print("\x1b[1;92m Congratulations ! Your Device Support this Tools")
            print('[•] Follow My Github First')
            os.system('xdg-open https://github.com/REFAT-156')
            from fahad import Subscraption
            Subscraption()
        elif bit == '32bit':
            print("\n\x1b[1;92m Congratulations ! Your Device Support this Tools")
            print('[•] Follow My Github First')
            os.system('xdg-open https://github.com/REFAT-156')
            from AKING32 import login
            login()
        else:
            exit('\033[1;31m[×] Connection Error')
Run()
