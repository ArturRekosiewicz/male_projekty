try:
    import pyperclip
except ImportError:
    pass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('szyfr cezara')
print('szyfr cezara szyfruje litery przez przesuniecie ich o liczme.')
print('która jest kluczcem. Na przyklad klucz 2 oznacza, że litera A jest')
print('zamieniona na C, litera B na D itd')
print()

while True:
    print('Czy chcesz (z)aszyfrowac, czy (o)dszyfrowac?')
    response = input('> ').lower()
    if response.startswith('z'):
        mode = 'zaszyfrowania'
        break
    elif response.startswith('o'):
        mode = 'odszyfrowania'
        break
    print('proszę podać literę z lub o.')

while True:
    maxKey = len(SYMBOLS) - 1
    print('Prosszę podać klucz (0 do {}).'.format(maxKey))
    response = input('>').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print('wpisz wiadomosc do {}.'.format(mode))
message = input('> ')

message = message.upper()

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'zaszyfrowania':
            num = num + key
        elif mode == "odszyfrowania":
            num = num - key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol

print(translated)

try:
    pyperclip.copy(translated)
    print('tekst przekazany do {} został skopiowany do schowka.'.format(mode))
except:
    pass

