import datetime

# deklaracja stalych
DAYS = ('Niedziela', 'Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', "Piątek", 'Sobota')
MONTHS = ('Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec',
          'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień')

print('Generator kalendarza.')

while True:
    print('Podaj rok dla kalendarza:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('podaj rok jako wartosc liczbowa, na przyklad 2023')
    continue

while True:
    print('Podaj miesiac dla kalendarza:')
    response = input('> ')

    if not response.isdecimal():
        print('Podaj miesiac jako liczbe, na przyklad 2 dla luty.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('podaj liczbe od 1 do 12.')


def getCalendarFor(year, month):
    calText = ''

    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    calText = '.Niedziela.Poniedziałek..Wtorek.....Środa.....Czwartek.....Piątek....Sobota..\n'

    weekSeparator = ('+----------' * 7) + '+\n'

    # Puste wiersze mają 10 spacji między separatorami dni, |:
    blankRow = ('|          ' * 7) + '|\n'

    currentDate = datetime.date(year, month, 1)

    # Cofaj currentDate, dopóki nie będzie to niedziela. (Funkcja weekday() zwraca
    # dla niedzieli 6, nie 0).
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:
        calText += weekSeparator

        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '|\n'

        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        if currentDate.month != month:
            break

    calText += weekSeparator
    return calText


calText = getCalendarFor(year, month)
print(calText)
