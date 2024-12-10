import random
b_joke1= 'Заходить нігенр з папуго в бар. Бармен питає: де його купив? Папуга каже:на ринку'
b_joke2= 'Чим віднрізняється збита собака від збитого нігера(машиною). Перед собакоютормозний слід'
b_joke3 = 'Iсторія безрукого хлопчика починається так: Іду собі нікого не чіпаю'
b_joke4 = 'Люблю гуляти болотами! Дуже затягує.'
b_joke5 = 'Фальшивого дресирувальника у цирку швидко розкусили.'

school_joke1='М`яч ще летів у вікно директора, а діти вже грали в хованки...'
school_joke2='Унікальна знахідка! Знайдений єдиний у світі підручник хімії за 9 клас, в якому Менделєєв зображений без намальованих рогів.'
school_joke3='Шість років не пив, не курив, про дівчат взагалі не думав... потім мама повела мене до школи...'
school_joke4='З усього курсу шкільної геометрії мені в житті пригодилася лише одна фраза: «Що і потрібно доказати»...'
school_joke5='Учителька звертається до класу: — Я змушена вас засмутити. На жаль, сьогодні контрольної з математики не буде!..'

shtir_joke1 = 'Штірліц грав у карти і програвся. Але Штірліц умів робити гарну міну при поганій грі. Коли Штірліц покинув компанію, міна спрацювала.'
shtir_joke2 = 'Штірліц та Мюллер їздили по черзі на танку. Черга рідшала, але не розходилася...'
shtir_joke3 = 'Штирлиц стрелял вслепую. Слепая испугалась и побежала скачками, но качки быстро отстали.'
shtir_joke4 = 'Штирлиц шёл по улице, когда внезапно перед ним что-то упало. Штирлиц поднял глаза — это были глаза профессора Плейшнера.'
shtir_joke5 = 'Штирлиц вытащил из сейфа записку Мюллера. Мюллеру было очень больно и он сильно ругался.'

sliv = {'black':[b_joke1,b_joke2,b_joke3,b_joke4,b_joke5],
        'shtirl': [shtir_joke1,shtir_joke2,shtir_joke3,shtir_joke4,shtir_joke5],
        "school":[school_joke1,school_joke2,school_joke3,school_joke4,school_joke5]}


while True:
    tipe = input("""
    black
    shtirl
    school
    add
    : """).lower()
    if tipe == 'add':
        tipe_category = input("""
            black
            shtirl
            school
            : """).lower()
        self_joke = input('joke: ')
        if tipe == 'black':
            sliv['black'].append(self_joke)
            print(sliv['black'])
        elif tipe == 'shtirl':
            sliv['shtirl'].append(self_joke)
            print(sliv['shtirl'])
        elif tipe == 'school':
            sliv['school'].append(self_joke)
            print(sliv['school'])
        continue
    rando=random.randint(0,len(sliv[tipe]))
    if tipe == 'black':
        print(sliv['black'][rando])
        sliv['black'].pop(rando)
    elif tipe == 'shtirl':
        print(sliv['shtirl'][rando])
        sliv['shtirl'].pop(rando)
    elif tipe == 'school':
        print(sliv['school'][rando])
        sliv['school'].pop(rando)