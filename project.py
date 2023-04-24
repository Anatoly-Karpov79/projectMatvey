from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton





TOKEN ='6253007609:AAGhxbTSpfN3QG4PXZNZidE0hvSkWBDvWRc'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

sverka1 = InlineKeyboardMarkup(row_width=1)

sverka1.add(InlineKeyboardButton('Сверить с актуальным', url='https://docs.google.com/spreadsheets/d/1fygxAVN1GnZHvyKFQRNSvihKUg1A9t2X/edit#gid=381304554'))

sverka2 = InlineKeyboardMarkup(row_width=1)
sverka2.add(InlineKeyboardButton('Сверить с актуальным', url='https://docs.google.com/spreadsheets/d/1nTsQWkKxpXc1kRAHLMjI8hFeMcxHgyBR/edit#gid=534420810'))

smene = ReplyKeyboardMarkup(resize_keyboard=True)
smene.add(KeyboardButton('Первая')).insert(KeyboardButton('Вторая'))
########################################################################################################################
firstsmene = ReplyKeyboardMarkup(resize_keyboard=True)
firstsmene.add(KeyboardButton('Понедельник[1]')).insert(KeyboardButton('Вторник[1]')).add(KeyboardButton('Среда[1]')).insert(KeyboardButton('Четверг[1]')).add(KeyboardButton('Пятница[1]')).add(KeyboardButton('Суббота[1]')).add(KeyboardButton('Назад в меню'))

secondsmene = ReplyKeyboardMarkup(resize_keyboard=True)
secondsmene.add(KeyboardButton('Понедельник[2]')).insert(KeyboardButton('Вторник[2]')).add(KeyboardButton('Среда[2]')).insert(KeyboardButton('Четверг[2]')).add(KeyboardButton('Пятница[2]')).add(KeyboardButton('Суббота[2]')).add(KeyboardButton('Назад в меню'))
########################################################################################################################
firstclass = ReplyKeyboardMarkup(resize_keyboard=True)
firstclass.add(KeyboardButton('5')).add(KeyboardButton('7')).add(KeyboardButton('9')).add(KeyboardButton('11')).add(KeyboardButton('Назад в меню'))

secondclass = ReplyKeyboardMarkup(resize_keyboard=True)
secondclass.add(KeyboardButton('6')).add(KeyboardButton('8')).add(KeyboardButton('10')).add(KeyboardButton('Назад в меню'))
#########################################################################################################################
fiveclass = ReplyKeyboardMarkup(resize_keyboard=True)
fiveclass.add(KeyboardButton('[5]А')).add(KeyboardButton('[5]Б')).add(KeyboardButton('[5]В')).add(KeyboardButton('[5]Г')).add(KeyboardButton('Назад в меню'))

sixclass = ReplyKeyboardMarkup(resize_keyboard=True)
sixclass.add(KeyboardButton('[6]А')).add(KeyboardButton('[6]Б')).add(KeyboardButton('[6]В')).add(KeyboardButton('[6]Г')).add(KeyboardButton('Назад в меню'))

sevenclass = ReplyKeyboardMarkup(resize_keyboard=True)
sevenclass.add(KeyboardButton('[7]А')).add(KeyboardButton('[7]Б')).add(KeyboardButton('[7]В')).add(KeyboardButton('[7]Г')).add(KeyboardButton('Назад в меню'))

eightclass = ReplyKeyboardMarkup(resize_keyboard=True)
eightclass.add(KeyboardButton('[8]А')).add(KeyboardButton('[8]Б')).add(KeyboardButton('[8]В')).add(KeyboardButton('[8]Э')).add(KeyboardButton('Назад в меню'))

nineclass = ReplyKeyboardMarkup(resize_keyboard=True)
nineclass.add(KeyboardButton('[9]А')).add(KeyboardButton('[9]Б')).add(KeyboardButton('[9]В')).add(KeyboardButton('Назад в меню'))

tenclass = ReplyKeyboardMarkup(resize_keyboard=True)
tenclass.add(KeyboardButton('[10]Технолог')).add(KeyboardButton('[10]Естественно-научн')).add(KeyboardButton('[10]Соц-эконом')).add(KeyboardButton('[10]Гуманитарный')).add(KeyboardButton('Назад в меню'))

elevenclass = ReplyKeyboardMarkup(resize_keyboard=True)
elevenclass.add(KeyboardButton('[11]Технолог')).add(KeyboardButton('[11]Естественно-научн')).add(KeyboardButton('[11]Гуманитарный филолог')).add(KeyboardButton('[11]Гуманитарный истор')).add(KeyboardButton('[11]Соц-эконом')).add(KeyboardButton('Назад в меню'))
########################################################################################################################
fivea = ReplyKeyboardMarkup(resize_keyboard=True)
fivea.add(KeyboardButton('[5А]Понедельник')).add(KeyboardButton('[5А]Вторник')).add(KeyboardButton('[5А]Среда')).add(KeyboardButton('[5А]Четверг')).add(KeyboardButton('[5А]Пятница')).add(KeyboardButton('[5А]Суббота')).add(KeyboardButton('Назад в меню'))

fiveb = ReplyKeyboardMarkup(resize_keyboard=True)
fiveb.add(KeyboardButton('[5Б]Понедельник')).add(KeyboardButton('[5Б]Вторник')).add(KeyboardButton('[5Б]Среда')).add(KeyboardButton('[5Б]Четверг')).add(KeyboardButton('[5Б]Пятница')).add(KeyboardButton('[5Б]Суббота')).add(KeyboardButton('Назад в меню'))

fivev = ReplyKeyboardMarkup(resize_keyboard=True)
fivev.add(KeyboardButton('[5В]Понедельник')).add(KeyboardButton('[5В]Вторник')).add(KeyboardButton('[5В]Среда')).add(KeyboardButton('[5В]Четверг')).add(KeyboardButton('[5В]Пятница')).add(KeyboardButton('[5В]Суббота')).add(KeyboardButton('Назад в меню'))

fiveg = ReplyKeyboardMarkup(resize_keyboard=True)
fiveg.add(KeyboardButton('[5Г]Понедельник')).add(KeyboardButton('[5Г]Вторник')).add(KeyboardButton('[5Г]Среда')).add(KeyboardButton('[5Г]Четверг')).add(KeyboardButton('[5Г]Пятница')).add(KeyboardButton('[5Г]Суббота')).add(KeyboardButton('Назад в меню'))
########################################################################################################################
sixa = ReplyKeyboardMarkup(resize_keyboard=True)
sixa.add(KeyboardButton('[6А]Понедельник')).add(KeyboardButton('[6А]Вторник')).add(KeyboardButton('[6А]Среда')).add(KeyboardButton('[6А]Четверг')).add(KeyboardButton('[6А]Пятница')).add(KeyboardButton('[6А]Суббота')).add(KeyboardButton('Назад в меню'))

sixb = ReplyKeyboardMarkup(resize_keyboard=True)
sixb.add(KeyboardButton('[6Б]Понедельник')).add(KeyboardButton('[6Б]Вторник')).add(KeyboardButton('[6Б]Среда')).add(KeyboardButton('[6Б]Четверг')).add(KeyboardButton('[6Б]Пятница')).add(KeyboardButton('[6Б]Суббота')).add(KeyboardButton('Назад в меню'))

sixv = ReplyKeyboardMarkup(resize_keyboard=True)
sixv.add(KeyboardButton('[6В]Понедельник')).add(KeyboardButton('[6В]Вторник')).add(KeyboardButton('[6В]Среда')).add(KeyboardButton('[6В]Четверг')).add(KeyboardButton('[6В]Пятница')).add(KeyboardButton('[6В]Суббота')).add(KeyboardButton('Назад в меню'))

sixg = ReplyKeyboardMarkup(resize_keyboard=True)
sixg.add(KeyboardButton('[6Г]Понедельник')).add(KeyboardButton('[6Г]Вторник')).add(KeyboardButton('[6Г]Среда')).add(KeyboardButton('[6Г]Четверг')).add(KeyboardButton('[6Г]Пятница')).add(KeyboardButton('[6Г]Суббота')).add(KeyboardButton('Назад в меню'))
########################################################################################################################
sevena = ReplyKeyboardMarkup(resize_keyboard=True)
sevena.add(KeyboardButton('[7А]Понедельник')).add(KeyboardButton('[7А]Вторник')).add(KeyboardButton('[7А]Среда')).add(KeyboardButton('[7А]Четверг')).add(KeyboardButton('[7А]Пятница')).add(KeyboardButton('[7А]Суббота')).add(KeyboardButton('Назад в меню'))

sevenb = ReplyKeyboardMarkup(resize_keyboard=True)
sevenb.add(KeyboardButton('[7Б]Понедельник')).add(KeyboardButton('[7Б]Вторник')).add(KeyboardButton('[7Б]Среда')).add(KeyboardButton('[7Б]Четверг')).add(KeyboardButton('[7Б]Пятница')).add(KeyboardButton('[7Б]Суббота')).add(KeyboardButton('Назад в меню'))

sevenv = ReplyKeyboardMarkup(resize_keyboard=True)
sevenv.add(KeyboardButton('[7В]Понедельник')).add(KeyboardButton('[7В]Вторник')).add(KeyboardButton('[7В]Среда')).add(KeyboardButton('[7В]Четверг')).add(KeyboardButton('[7В]Пятница')).add(KeyboardButton('[7В]Суббота')).add(KeyboardButton('Назад в меню'))

seveng = ReplyKeyboardMarkup(resize_keyboard=True)
seveng.add(KeyboardButton('[7Г]Понедельник')).add(KeyboardButton('[7Г]Вторник')).add(KeyboardButton('[7Г]Среда')).add(KeyboardButton('[7Г]Четверг')).add(KeyboardButton('[7Г]Пятница')).add(KeyboardButton('[7Г]Суббота')).add(KeyboardButton('Назад в меню'))
########################################################################################################################
eighta = ReplyKeyboardMarkup(resize_keyboard=True)
eighta.add(KeyboardButton('[8А]Понедельник')).add(KeyboardButton('[8А]Вторник')).add(KeyboardButton('[8А]Среда')).add(KeyboardButton('[8А]Четверг')).add(KeyboardButton('[8А]Пятница')).add(KeyboardButton('[8А]Суббота')).add(KeyboardButton('Назад в меню'))

eightb = ReplyKeyboardMarkup(resize_keyboard=True)
eightb.add(KeyboardButton('[8Б]Понедельник')).add(KeyboardButton('[8Б]Вторник')).add(KeyboardButton('[8Б]Среда')).add(KeyboardButton('[8Б]Четверг')).add(KeyboardButton('[8Б]Пятница')).add(KeyboardButton('[8Б]Суббота')).add(KeyboardButton('Назад в меню'))

eightv = ReplyKeyboardMarkup(resize_keyboard=True)
eightv.add(KeyboardButton('[8В]Понедельник')).add(KeyboardButton('[8В]Вторник')).add(KeyboardButton('[8В]Среда')).add(KeyboardButton('[8В]Четверг')).add(KeyboardButton('[8В]Пятница')).add(KeyboardButton('[8В]Суббота')).add(KeyboardButton('Назад в меню'))

eighte = ReplyKeyboardMarkup(resize_keyboard=True)
eighte.add(KeyboardButton('[8Э]Понедельник')).add(KeyboardButton('[8Э]Вторник')).add(KeyboardButton('[8Э]Среда')).add(KeyboardButton('[8Э]Четверг')).add(KeyboardButton('[8Э]Пятница')).add(KeyboardButton('[8Э]Суббота')).add(KeyboardButton('Назад в меню'))
########################################################################################################################
ninea = ReplyKeyboardMarkup(resize_keyboard=True)
ninea.add(KeyboardButton('[9А]Понедельник')).add(KeyboardButton('[9А]Вторник')).add(KeyboardButton('[9А]Среда')).add(KeyboardButton('[9А]Четверг')).add(KeyboardButton('[9А]Пятница')).add(KeyboardButton('[9А]Суббота')).add(KeyboardButton('Назад в меню'))

nineb = ReplyKeyboardMarkup(resize_keyboard=True)
nineb.add(KeyboardButton('[9Б]Понедельник')).add(KeyboardButton('[9Б]Вторник')).add(KeyboardButton('[9Б]Среда')).add(KeyboardButton('[9Б]Четверг')).add(KeyboardButton('[9Б]Пятница')).add(KeyboardButton('[9Б]Суббота')).add(KeyboardButton('Назад в меню'))

ninev = ReplyKeyboardMarkup(resize_keyboard=True)
ninev.add(KeyboardButton('[9В]Понедельник')).add(KeyboardButton('[9В]Вторник')).add(KeyboardButton('[9В]Среда')).add(KeyboardButton('[9В]Четверг')).add(KeyboardButton('[9В]Пятница')).add(KeyboardButton('[9В]Суббота')).add(KeyboardButton('Назад в меню'))
########################################################################################################################
tentehno = ReplyKeyboardMarkup(resize_keyboard=True)
tentehno.add(KeyboardButton('[10Технолог]Понедельник')).add(KeyboardButton('[10Технолог]Вторник')).add(KeyboardButton('[10Технолог]Среда')).add(KeyboardButton('[10Технолог]Четверг')).add(KeyboardButton('[10Технолог]Пятница')).add(KeyboardButton('[10Технолог]Суббота')).add(KeyboardButton('Назад в меню'))

tenestestv = ReplyKeyboardMarkup(resize_keyboard=True)
tenestestv.add(KeyboardButton('[10Естественно-научн]Понедельник')).add(KeyboardButton('[10Естественно-научн]Вторник')).add(KeyboardButton('[10Естественно-научн]Среда')).add(KeyboardButton('[10Естественно-научн]Четверг')).add(KeyboardButton('[10Естественно-научн]Пятница')).add(KeyboardButton('[10Естественно-научн]Суббота')).add(KeyboardButton('Назад в меню'))

tensoc = ReplyKeyboardMarkup(resize_keyboard=True)
tensoc.add(KeyboardButton('[10Соц-эконом]Понедельник')).add(KeyboardButton('[10Соц-эконом]Вторник')).add(KeyboardButton('[10Соц-эконом]Среда')).add(KeyboardButton('[10Соц-эконом]Четверг')).add(KeyboardButton('[10Соц-эконом]Пятница')).add(KeyboardButton('[10Соц-эконом]Суббота')).add(KeyboardButton('Назад в меню'))

tengym = ReplyKeyboardMarkup(resize_keyboard=True)
tengym.add(KeyboardButton('[10Гуманитарный]Понедельник')).add(KeyboardButton('[10Гуманитарный]Вторник')).add(KeyboardButton('[10Гуманитарный]Среда')).add(KeyboardButton('[10Гуманитарный]Четверг')).add(KeyboardButton('[10Гуманитарный]Пятница')).add(KeyboardButton('[10Гуманитарный]Суббота')).add(KeyboardButton('Назад в меню'))
########################################################################################################################
eleventehno = ReplyKeyboardMarkup(resize_keyboard=True)
eleventehno.add(KeyboardButton('[11Технолог]Понедельник')).add(KeyboardButton('[11Технолог]Вторник')).add(KeyboardButton('[11Технолог]Среда')).add(KeyboardButton('[11Технолог]Четверг')).add(KeyboardButton('[11Технолог]Пятница')).add(KeyboardButton('[11Технолог]Суббота')).add(KeyboardButton('Назад в меню'))

elevenestestv = ReplyKeyboardMarkup(resize_keyboard=True)
elevenestestv.add(KeyboardButton('[11Естественно-научн]Понедельник')).add(KeyboardButton('[11Естественно-научн]Вторник')).add(KeyboardButton('[11Естественно-научн]Среда')).add(KeyboardButton('[11Естественно-научн]Четверг')).add(KeyboardButton('[11Естественно-научн]Пятница')).add(KeyboardButton('[11Естественно-научн]Суббота')).add(KeyboardButton('Назад в меню'))

elevengymfil = ReplyKeyboardMarkup(resize_keyboard=True)
elevengymfil.add(KeyboardButton('[11Гуманитарный филолог]Понедельник')).add(KeyboardButton('[11Гуманитарный филолог]Вторник')).add(KeyboardButton('[11Гуманитарный филолог]Среда')).add(KeyboardButton('[11Гуманитарный филолог]Четверг')).add(KeyboardButton('[11Гуманитарный филолог]Пятница')).add(KeyboardButton('[11Гуманитарный филолог]Суббота')).add(KeyboardButton('Назад в меню'))

elevengymist = ReplyKeyboardMarkup(resize_keyboard=True)
elevengymist.add(KeyboardButton('[11Гуманитарный истор]Понедельник')).add(KeyboardButton('[11Гуманитарный истор]Вторник')).add(KeyboardButton('[11Гуманитарный истор]Среда')).add(KeyboardButton('[11Гуманитарный истор]Четверг')).add(KeyboardButton('[11Гуманитарный истор]Пятница')).add(KeyboardButton('[11Гуманитарный истор]Суббота')).add(KeyboardButton('Назад в меню'))

elevensoc = ReplyKeyboardMarkup(resize_keyboard=True)
elevensoc.add(KeyboardButton('[11Соц-эконом]Понедельник')).add(KeyboardButton('[11Соц-эконом]Вторник')).add(KeyboardButton('[11Соц-эконом]Среда')).add(KeyboardButton('[11Соц-эконом]Четверг')).add(KeyboardButton('[11Соц-эконом]Пятница')).add(KeyboardButton('[11Соц-эконом]Суббота')).add(KeyboardButton('Назад в меню'))
########################################################################################################################




@dp.message_handler(commands=['start'])
async def start(message = types.Message):
    await message.answer(f'Привет! Выбери свою смену.', reply_markup=smene)
########################################################################################################################
@dp.message_handler(text='Первая')
async def first(message: types.Message):
    await message.answer(f'Отлично! Теперь выбери свой класс.', reply_markup=firstclass)

@dp.message_handler(text='Вторая')
async def first(message: types.Message):
    await message.answer(f'Отлично! Теперь выбери свой класс.', reply_markup=secondclass)
########################################################################################################################
@dp.message_handler(text='5')
async def first(message: types.Message):
    await message.answer(f'Отлично! Теперь выбери букву класса.', reply_markup=fiveclass)

@dp.message_handler(text='6')
async def first(message: types.Message):
    await message.answer(f'Отлично! Теперь выбери букву класса.', reply_markup=sixclass)

@dp.message_handler(text='7')
async def first(message: types.Message):
    await message.answer(f'Отлично! Теперь выбери букву класса.', reply_markup=sevenclass)

@dp.message_handler(text='8')
async def first(message: types.Message):
    await message.answer(f'Отлично! Теперь выбери букву класса.', reply_markup=eightclass)

@dp.message_handler(text='9')
async def first(message: types.Message):
    await message.answer(f'Отлично! Теперь выбери букву класса.', reply_markup=nineclass)

@dp.message_handler(text='10')
async def first(message: types.Message):
    await message.answer(f'Отлично! Теперь выбери направление класса.', reply_markup=tenclass)

@dp.message_handler(text='11')
async def first(message: types.Message):
    await message.answer(f'Отлично! Теперь выбери направление класса.', reply_markup=elevenclass)

@dp.message_handler(text='Назад в меню')
async def back(message: types.Message):
    await message.answer(f'Вы вернулись в главное меню', reply_markup=smene)
########################################################################################################################
@dp.message_handler(text='[5]А')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=fivea)

@dp.message_handler(text='[5]Б')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=fiveb)

@dp.message_handler(text='[5]В')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=fivev)

@dp.message_handler(text='[5]Г')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=fiveg)

@dp.message_handler(text='Назад в меню')
async def back(message: types.Message):
    await message.answer(f'Вы вернулись в главное меню', reply_markup=smene)
########################################################################################################################
@dp.message_handler(text='[6]А')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=sixa)

@dp.message_handler(text='[6]Б')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=sixb)

@dp.message_handler(text='[6]В')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=sixv)

@dp.message_handler(text='[6]Г')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=sixg)

@dp.message_handler(text='Назад в меню')
async def back(message: types.Message):
    await message.answer(f'Вы вернулись в главное меню', reply_markup=smene)
########################################################################################################################
@dp.message_handler(text='[7]А')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=sevena)

@dp.message_handler(text='[7]Б')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=sevenb)

@dp.message_handler(text='[7]В')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=sevenv)

@dp.message_handler(text='[7]Г')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=seveng)

@dp.message_handler(text='Назад в меню')
async def back(message: types.Message):
    await message.answer(f'Вы вернулись в главное меню', reply_markup=smene)
########################################################################################################################
@dp.message_handler(text='[8]А')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=eighta)

@dp.message_handler(text='[8]Б')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=eightb)

@dp.message_handler(text='[8]В')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=eightv)

@dp.message_handler(text='[8]Э')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=eighte)

@dp.message_handler(text='Назад в меню')
async def back(message: types.Message):
    await message.answer(f'Вы вернулись в главное меню', reply_markup=smene)
########################################################################################################################
@dp.message_handler(text='[9]А')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=ninea)

@dp.message_handler(text='[9]Б')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=nineb)

@dp.message_handler(text='[9]В')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=ninev)

@dp.message_handler(text='Назад в меню')
async def back(message: types.Message):
    await message.answer(f'Вы вернулись в главное меню', reply_markup=smene)
########################################################################################################################
@dp.message_handler(text='[10]Технолог')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=tentehno)

@dp.message_handler(text='[10]Естественно-научн')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=tenestestv)

@dp.message_handler(text='[10]Соц-эконом')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=tensoc)

@dp.message_handler(text='[10]Гуманитарный')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=tengym)

@dp.message_handler(text='Назад в меню')
async def back(message: types.Message):
    await message.answer(f'Вы вернулись в главное меню', reply_markup=smene)
########################################################################################################################
@dp.message_handler(text='[11]Технолог')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=eleventehno)

@dp.message_handler(text='[11]Естественно-научн')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=elevenestestv)

@dp.message_handler(text='[11]Гуманитарный филолог')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=elevengymfil)

@dp.message_handler(text='[11]Гуманитарный истор')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=elevengymist)

@dp.message_handler(text='[11]Соц-эконом')
async def first(message: types.Message):
    await message.answer(f'Осталось только выбрать интересующий тебя день недели. ', reply_markup=elevensoc)

@dp.message_handler(text='Назад в меню')
async def back(message: types.Message):
    await message.answer(f'Вы вернулись в главное меню', reply_markup=smene)





########################################################################################################################
fivea
@dp.message_handler(text='[5А]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 7\n 2 история 24\n 3 география 29\n 4 математика 18\n 5 русский яз.7\n 6 ИЗО 8', reply_markup=sverka1)

@dp.message_handler(text='[5А]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 математика 18\n 2 русский яз.7\n 3  ОДНКНР 19\n 4 музыка 24\n 5  биология 12\n 6 англ. 31, 28', reply_markup=sverka1)

@dp.message_handler(text='[5А]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 русский яз.7\n 2 физич. культура\n 3 ИВТ 21,25\n 4 литература 7\n 5 математика 18\n РОБОТОТЕХНИКА', reply_markup=sverka1)

@dp.message_handler(text='[5А]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1	-------------\n 2	русский яз.7\n 3	математика 18\n 4	физич. культура\n 5	англ. 31, 28\n 6	литература 7\n финансовая грамотность 17', reply_markup=sverka1)

@dp.message_handler(text='[5А]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1	история 26\n 2	математика 18\n 3	технол.\n 4	технол.\n 5	кл.час 7\n 6	программирование Scratch 21', reply_markup=sverka1)

@dp.message_handler(text='[5А]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1	-------------\n 2	англ. 31, 28\n 3	русский яз.7\n 4	литература 7', reply_markup=sverka1)
########################################################################################################################
@dp.message_handler(text='[5Б]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 18\n 2 математика 18\n 3 русский яз.7\n 4 география 29\n 5 ИЗО 8\n 6 история 24\n РОБОТОТЕХНИКА ', reply_markup=sverka1)

@dp.message_handler(text='[5Б]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 русский яз.7\n 2 биология 12\n 3 математика 18\n 4 ОДНКНР 19\n 5 англ. 31, 28\n 6 музыка 24', reply_markup=sverka1)

@dp.message_handler(text='[5Б]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 ИВТ 21,25\n 2 русский яз.7\n 3 математика 18\n 4 физич. культура\n 5 литература 7\n РОБОТОТЕХНИКА', reply_markup=sverka1)

@dp.message_handler(text='[5Б]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 физич. культура\n 3 русский яз.7\n 4 литература 7\n 5 математика 18\n 6 англ. 31, 28\n Финансовая грамотность 17', reply_markup=sverka1)

@dp.message_handler(text='[5Б]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 -------------\n 3 математика 18\n 4 история 26\n 5 технол.\n 6 технол.\n 7 кл.час 18', reply_markup=sverka1)

@dp.message_handler(text='[5Б]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 русский яз.7\n 2 литература 7\n 3 англ. 31, 28', reply_markup=sverka1)
########################################################################################################################
@dp.message_handler(text='[5В]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 29\n 2 география 29\n 3 ИЗО 8\n 4 русский яз.7\n 5 история 24\n 6 математика 18\n РОБОТОТЕХНИКА', reply_markup=sverka1)

@dp.message_handler(text='[5В]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 биология 12\n 2 математика 18\n 3 русский яз. 7\n 4 англ. 31, 27\n 5 музыка 24\n 6 ОДНКНР 19', reply_markup=sverka1)

@dp.message_handler(text='[5В]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 ИВТ 21,25\n 3 русский яз.7\n 4 математика 18\n 5 физич. культура\n 6 литература 7\n 7 кл.час 29', reply_markup=sverka1)

@dp.message_handler(text='[5В]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 русский яз.7\n 2 математика 18\n 3 физич. культура\n 4 англ. 31, 27\n 5 литература 7\n 6 ------------- \n Финансовая грамотность 17', reply_markup=sverka1)

@dp.message_handler(text='[5В]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 технол.\n 2 технол.\n 3 история 26\n 4 математика 18\n 5 -------------\n 6 программирование Scratch 21', reply_markup=sverka1)

@dp.message_handler(text='[5В]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 -------------\n 3 -------------\n 4 англ. 31, 27\n 5 русский яз.7\n 6 литература 7', reply_markup=sverka1)
########################################################################################################################
@dp.message_handler(text='[5Г]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 27\n 2 ИЗО 8\n 3 математика 18\n 4 история 24\n 5 география 29\n 6 русский яз.27', reply_markup=sverka1)

@dp.message_handler(text='[5Г]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 русский яз.27\n 2 музыка 24\n 3 англ. 31, 27\n 4 математика 18\n 5 ОДНКНР 19\n 6 биология 12', reply_markup=sverka1)

@dp.message_handler(text='[5Г]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 математика 18\n 2 русский яз.27\n 3 физич. культура\n 4 ИВТ 21,25\n 5 литература 27\n 6 РОБОТОТЕХНИКА', reply_markup=sverka1)

@dp.message_handler(text='[5Г]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 русский яз.27\n 3 англ. 31, 27\n 4 математика 18\n 5 литература 27\n 6 физич. культура\n 7 Финансовая грамотность 17', reply_markup=sverka1)

@dp.message_handler(text='[5Г]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 математика 18\n 2 история 26\n 3 русский яз.27\n 4 литература 27\n 5 кл.час 27\n 6 программирование Scratch 21', reply_markup=sverka1)

@dp.message_handler(text='[5Г]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 -------------\n 3 технол.\n 4 технол.\n 5 англ. 31, 27', reply_markup=sverka1)
########################################################################################################################
########################################################################################################################
@dp.message_handler(text='[6А]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Кл.час "разговоры о важном"\n 1 технология\n 2 технология\n 3 математика 19\n 4 русский 27\n 5 литература 28\n 6 Приемы решения математических задач', reply_markup=sverka2)


@dp.message_handler(text='[6А]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 Физкультура\n 2 ИЗО 8\n 3 математика 19\n 4 англ. Б 31/ англ. К 15\n 5 русский 27', reply_markup=sverka2)


@dp.message_handler(text='[6А]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 музыка 24\n 2 биология 12\n 3 всеобщая история 26\n 4 математика 19\n 5 русский 27\n 6 Робототехника 01', reply_markup=sverka2)


@dp.message_handler(text='[6А]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Робототехника 01\n 1 обществознание 26\n 2 русский 27\n 3 англ. Б 31/ англ. К 15\n 4 математика 19\n 5 литература 28', reply_markup=sverka2)


@dp.message_handler(text='[6А]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Финансовая грамотность 9\n 1 ИВТ 21/25\n 2 математика 19\n 3 история России 26\n 4 литература 28\n 5 Физкультура\n 6 география 29', reply_markup=sverka2)


@dp.message_handler(text='[6А]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 6 Чудеса химии 23\n 1 русский 27\n 2 биология 12\n 3 ---- / англ. К 15', reply_markup=sverka2)


########################################################################################################################
@dp.message_handler(text='[6Б]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 7(0) Кл.час "разговоры о важном"\n 1 обществознание 26\n 2 литература 28\n 3 русский 27\n 4 математика 30', reply_markup=sverka2)


@dp.message_handler(text='[6Б]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 математика 30\n 2 англ. Б 31/ англ. К 15\n 3 ИЗО 8\n 4 русский 27\n 5 Физкультура', reply_markup=sverka2)


@dp.message_handler(text='[6Б]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 всеобщая история 26\n 2 математика 30\n 3 музыка 24\n 4 русский 27\n 5 биология 12', reply_markup=sverka2)


@dp.message_handler(text='[6Б]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) русский 27\n 1 литература 28\n 2 ИВТ 21/25\n 3 технология\n 4 технология\n 5 англ. Б 31/ англ. К 15', reply_markup=sverka2)


@dp.message_handler(text='[6Б]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Финансовая грамотность 9\n 1 история России 26\n 2 Физкультура\n 3 география 29\n 4 математика 30\n 5 литература 28\n 6 англ. Б 31/ -----', reply_markup=sverka2)


@dp.message_handler(text='[6Б]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 5 VR-CODER 25\n 6 Чудеса химии 2\n 1 математика 30\n 2 русский 27\n 3 биология 12\n 4 -----/ англ. К 15', reply_markup=sverka2)


########################################################################################################################
@dp.message_handler(text='[6В]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 7(0) Кл.час "разговоры о важном"\n 1 литература 28\n 2 математика 19\n 3 технология\n 4 технология\n 5 русский 27\n 6 Приемы решения математических задач', reply_markup=sverka2)


@dp.message_handler(text='[6В]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 англ. Б 31/ англ. К 15\n 2 Физкультура\n 3 русский 27\n 4 математика 19\n 5 ИЗО 8', reply_markup=sverka2)


@dp.message_handler(text='[6В]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) англ. Б 31/ ------\n 1 биология 12\n 2 музыка 24\n 3 русский 27\n 4 всеобщая история 26\n 5 математика 19\n 6 Робототехника 01', reply_markup=sverka2)


@dp.message_handler(text='[6В]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Робототехника 01/ Pro -себя 12\n 1 русский 27\n 2 англ. Б 31/ англ. К 15\n 3 математика 19\n 4 литература 28\n 5 обществознание 26', reply_markup=sverka2)


@dp.message_handler(text='[6В]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7)Финансовая грамотность 9\n 1 литература 28\n 2 история России 26\n 3 ИВТ 21/25\n 4 география 29\n 5 математика 19', reply_markup=sverka2)


@dp.message_handler(text='[6В]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 6 Чудеса химии 23\n 1 -----/ англ. К 15\n 2 Физкультура\n 3 русский 27\n 4 биология 12', reply_markup=sverka2)


########################################################################################################################
@dp.message_handler(text='[6Г]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Кл.час "разговоры о важном"\n 1русский 7\n 2 математика 30\n 3 литература 28\n  4 обществознание 26', reply_markup=sverka2)


@dp.message_handler(text='[6Г]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 ИЗО 8\n 2 математика 30\n 3 aнгл. Б 31/ англ. К 15\n 4 Физкультура\n 5 русский 6', reply_markup=sverka2)


@dp.message_handler(text='[6Г]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Pro-себя 12\n 1 русский 7\n 2 всеобщая история 26\n 3 математика 30\n 4 биология 12\n 5 музыка 24\n 6 Робототехника 01', reply_markup=sverka2)


@dp.message_handler(text='[6Г]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Робототехника 01\n 1 англ. Б 31/ англ. К 15\n 2 литература 28\n 3 русский 6\n 4 ИВТ 21/25\n 5 технология\n 6 технология', reply_markup=sverka2)


@dp.message_handler(text='[6Г]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Финансовая грамотность 9\n 1 Физкультура\n 2 русский 7\n 3 литература 28\n 4 история России 26\n 5 география 29\n 6 математика 30', reply_markup=sverka2)


@dp.message_handler(text='[6Г]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 6 англ. Б 31/ англ. К 15\n 1 биология 12\n 2 математика 30', reply_markup=sverka2)


########################################################################################################################
########################################################################################################################
@dp.message_handler(text='[7А]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 6\n 2 русский язык 6\n 3 алгебра 14\n 4 физика 13\n 5 литература 6\n 6 немецкий 31\n 7(0) -------------\n 1 РОБОТОТЕХНИКА', reply_markup=sverka1)


@dp.message_handler(text='[7А]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 технол.\n 2 технол.\n 3 aнгл. яз. 15,28\n 4 ИВТ 21, 25\n 5 русский яз.7\n 6 геометрия 14\n 7 Учебный курс: Элементы электротехники и электроники 13', reply_markup=sverka1)


@dp.message_handler(text='[7А]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 алгебра 14\n 2 география 29\n 3 литература 6\n 4 история России 17\n 5 музыка 24\n 6 физич. культура\n 7 Финансовая грамотность 17\n Евраз с 15.00(каб. 13а)', reply_markup=sverka1)


@dp.message_handler(text='[7А]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 русский язык 6\n 2 биология 19\n 3 обществознание 24\n 4 англ. яз. 15,28\n 5 алгебра 14\n 6 ИЗО 8\n 7(0)кл.час 6', reply_markup=sverka1)


@dp.message_handler(text='[7А]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 физич. культура\n 3 физика 13\n 4 русский язык 6\n 5 география 29\n 6 геометрия 14\n VR-CODER 25 (после уроков)', reply_markup=sverka1)


@dp.message_handler(text='[7А]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 англ. яз. 28\n 2 всеобщая история 17\n 3 англ. яз. 15\n 4 РОБОТОТЕХНИКА', reply_markup=sverka1)


########################################################################################################################
@dp.message_handler(text='[7Б]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 13\n 2 физика 13\n 3 русский язык 6\n 4 алгебра 30\n 5 немецкий 31\n 6 литература 7\n 7(0) -------------\n 1 РОБОТОТЕХНИКА', reply_markup=sverka1)


@dp.message_handler(text='[7Б]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 геометрия 30\n 2 англ. яз. 15,28\n 3 ИВТ 21, 25\n 4 русский яз.7\n 5 технол.\n 6 технол.\n 7(0) Учебный курс: Элементы электротехники и электроники 13', reply_markup=sverka1)


@dp.message_handler(text='[7Б]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 история России 17\n 2 литература 6\n 3 музыка 24\n 4 алгебра 30\n 5 география 29\n 6 -------------\n 7(0) Финансовая грамотность 17\n Евраз с 15.00 (каб. 13 а)', reply_markup=sverka1)


@dp.message_handler(text='[7Б]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 англ. яз. 15,28\n 2 pусский язык 6\n 3 ИЗО 8\n 4 биология 12\n 5 обществознание 24\n 6 алгебра 30\n 7(0) физич. культура', reply_markup=sverka1)


@dp.message_handler(text='[7Б]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 физич. культура\n 2 русский язык 6\n 3 география 29\n 4 физика 13\n 5 геометрия 30\n 6 кл.час 13\n VR-CODER 25 (после уроков)', reply_markup=sverka1)


@dp.message_handler(text='[7Б]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 -------------\n 3 -------------\n 4 РОБОТОТЕХНИКА\n 5 всеобщая история 17\n 6 англ. яз. 15,28', reply_markup=sverka1)


########################################################################################################################
@dp.message_handler(text='[7В]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 8\n 2 физич. культура\n 3 немецкий 31\n 4 алгебра 14\n 5 физика 13\n 6 русский язык 20\n 7(0) литература 20\n 1 РОБОТОТЕХНИКА', reply_markup=sverka1)


@dp.message_handler(text='[7В]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 англ. яз. 15,28\n 2 ИВТ 21, 25\n 3 технол.\n 4 технол.\n 5 геометрия 14\n 6 русский язык 20\n 7(0) Учебный курс: Элементы электротехники и электроники 13', reply_markup=sverka1)


@dp.message_handler(text='[7В]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 музыка 24\n 3 алгебра 14\n 4 география 29\n 5 история России 17\n 6 литература 20\n 7(0) Финансовая грамотность 17', reply_markup=sverka1)


@dp.message_handler(text='[7В]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 биология 19\n 2 ИЗО 8\n 3 англ. яз. 15,28\n 4 алгебра 14\n 5 русский язык 20\n 6 обществознание 24\n 7(0) кл.час 8', reply_markup=sverka1)


@dp.message_handler(text='[7В]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 физика 13\n 2 география 29\n 3 русский язык 20\n 4 геометрия 14\n 5 физич. культура\n VR-CODER 25 (после уроков)', reply_markup=sverka1)


@dp.message_handler(text='[7В]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2  -------------\n 3 ------------- \n 4 всеобщая история 17\n 5 англ. яз. 15,28', reply_markup=sverka1)


########################################################################################################################
@dp.message_handler(text='[7Г]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 17\n 2 немецкий 31\n 3 физика 13\n 4 русский язык 20\n 5 литература 20\n 6 алгебра 30\n 7(0) -------------\n 1 РОБОТОТЕХНИКА', reply_markup=sverka1)


@dp.message_handler(text='[7Г]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 ИВТ 21, 25\n 2 геометрия 30\n 3 музыка 24\n 4 англ. яз. 15,28\n 5 русский язык 20\n 6 -------------\n 7 Учебный курс: Элементы электротехники и электроники 13', reply_markup=sverka1)


@dp.message_handler(text='[7Г]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 физич. культура\n 2 история России 17\n 3 география 29\n 4 литература 20\n 5 алгебра 30\n 6 -------------\n 7(0) Финансовая грамотность 17', reply_markup=sverka1)


@dp.message_handler(text='[7Г]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 ИЗО 8\n 2 англ. яз. 15,28\n 3 алгебра 30\n 4 обществознание 24\n 5 биология 12\n 6 русский язык 20\n 7(0) кл.час 17', reply_markup=sverka1)


@dp.message_handler(text='[7Г]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 география 29\n 2 физика 13\n 3 физич. культура\n 4 геометрия 30\n 5 русский язык 20\n VR-CODER 25 (после уроков)', reply_markup=sverka1)


@dp.message_handler(text='[7Г]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 технол.\n 2 технол.\n 3 всеобщая история 17\n 4 англ. яз. 15,28', reply_markup=sverka1)


########################################################################################################################
########################################################################################################################
@dp.message_handler(text='[8А]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 7(0) Кл.час "разговоры о важном"\n 1 литература 6\n 2 биология 12\n 3 англ. Б 31/ англ. К 15\n 4 география 29\n 5 алгебра 18', reply_markup=sverka2)


@dp.message_handler(text='[8А]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n VR-CODER 25 (c 12.30)\n 1 физика 13\n 2 русский 6\n 3 обществознание 17\n 4 Химия 23\n 5 геометрия 18', reply_markup=sverka2)


@dp.message_handler(text='[8А]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Химический практикум 23\n 1 всеобщая история 17\n 2 англ. Б 31/ англ. К 15\n 3 русский 6\n 4 литература 6\n 5 алгебра 18\n 6 технология', reply_markup=sverka2)


@dp.message_handler(text='[8А]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 Химия 23\n 2 Физкультура\n 3 география 29\n 4 алгебра 18\n 5 спецкурс\n 6 физика 13', reply_markup=sverka2)


@dp.message_handler(text='[8А]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 англ. Б 31/ англ. К 15\n 2 русский 6\n 3 история России 17\n 4 геометрия 18\n 5 ИВТ 21/25\n 6 биология 12', reply_markup=sverka2)


@dp.message_handler(text='[8А]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 4 Нанотехнологии 22\n 5 Физкультура\n 6 нем.яз 29\n 1 ОБЖ 23\n 2 ИЗО 8\n 3 музыка 24', reply_markup=sverka2)


########################################################################################################################
@dp.message_handler(text='[8Б]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Кл.час "разговоры о важном"\n 1 алгебра 30\n 2 литература 6\n 3 география 29\n 4 англ. К 15\n 5 биология 12\n 6 русский 6', reply_markup=sverka2)


@dp.message_handler(text='[8Б]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n VR-CODER 25 (c 12.30)\n 1 Химия 23\n 2 обществознание 17\n 3 физика 13\n 4 русский 6\n 5 геометрия 30', reply_markup=sverka2)


@dp.message_handler(text='[8Б]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 алгебра 30\n 2 технология\n 3 всеобщая история 17\n 4 англ. К 15\n 5 алгебра 30\n 6 Физкультура', reply_markup=sverka2)


@dp.message_handler(text='[8Б]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Химия 23\n 1 русский 6\n 2 литература 6\n 3 Физкультура\n 4 география 29\n 5 физика 13\n 6 алгебра 30', reply_markup=sverka2)


@dp.message_handler(text='[8Б]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 история России 17\n 2 ИВТ 21\n 3 русский 6\n 4 биология 12\n 5 геометрия 30\n 6 англ. К 15', reply_markup=sverka2)


@dp.message_handler(text='[8Б]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 5 ОБЖ 23\n 6 ИЗО 8\n 1 нем.яз 31\n 2 музыка 24', reply_markup=sverka2)


########################################################################################################################
@dp.message_handler(text='[8В]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Кл.час "разговоры о важном"\n 1 алгебра 18\n 2 англ. Б 31/ англ. К 15\n 3 литература 6\n 4 биология 12\n 5 география 29\n 6 Гемодинамика 12', reply_markup=sverka2)


@dp.message_handler(text='[8В]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n VR-CODER 25 (c 12.30)\n 1 обществознание 17\n 2 Химия 23\n 3 русский 6\n 4 геометрия 18\n 5 физика 13\n 6 ОБЖ 23', reply_markup=sverka2)


@dp.message_handler(text='[8В]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 русский 6\n 2 литература 6\n 3 англ. Б 31/ англ. К 15\n 4 всеобщая история 17\n 5 технология\n 6 алгебра 18', reply_markup=sverka2)


@dp.message_handler(text='[8В]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 Физкультура\n 2 Химия 23\n 3 алгебра 18\n 4 физика 13\n 5 география 29\n 6 спецкурс', reply_markup=sverka2)


@dp.message_handler(text='[8В]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 русский 6\n 2 англ. Б 31/ англ. К 15\n 3 биология 12\n 4 ИВТ 21/25\n 5 история России 17\n 6 геометрия 18', reply_markup=sverka2)


@dp.message_handler(text='[8В]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 5 музыка 24\n 6 Физкультура\n 1 ИЗО 8\n 2 нем.яз 31', reply_markup=sverka2)


########################################################################################################################
@dp.message_handler(text='[8Э]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Кл.час "разговоры о важном"\n 1 биология 12\n 2 география 29\n 3 алгебра 14\n 4 литература 6\n 5 англ. Б 31/ англ. К 15\n 6 Гемодинамика 12', reply_markup=sverka2)


@dp.message_handler(text='[8Э]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n VR-CODER 25 (c 12.30)\n 1 русский 6\n 2 геометрия 14\n 3 Химия 23\n 4 физика 13\n 5 обществознание 17\n 6 физика 13', reply_markup=sverka2)


@dp.message_handler(text='[8Э]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) черчение 18\n 1 англ. Б 31/ англ. К 15\n 2 всеобщая история 17\n 3 алгебра 14\n 4 технология\n 5 русский 6\n 6 литература 6', reply_markup=sverka2)


@dp.message_handler(text='[8Э]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 физика 13\n 2 спецкурс 14\n 3 алгебра 14\n 4 Химия 23\n 5 Физкультура\n 6 география 29', reply_markup=sverka2)


@dp.message_handler(text='[8Э]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) ИВТ 21/25\n 1 геометрия 14\n 2 история России 17\n 3 англ. Б 31/ англ. К 15\n 4 русский 6\n 5 биология 12', reply_markup=sverka2)


@dp.message_handler(text='[8Э]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 5 ИЗО 8\n 6 музыка 24\n 1 Физкультура\n 2 ОБЖ 23\n 3 нем.яз 31', reply_markup=sverka2)


########################################################################################################################
########################################################################################################################
@dp.message_handler(text='[9А]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 21\n 2 черчение 23\n 3 алгебра 30\n 4 история России 17\n 5 англ. яз. 15,28\n 6 русский язык 6\n 7(0) биология 29\n 1 ОГЭ по выбору: химия (22), физика (13), география (29)', reply_markup=sverka1)


@dp.message_handler(text='[9А]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 физика 13\n 2 география 29\n 3 русский язык 6\n 4 литература 6\n 5 геометрия 30\n 6 история России 17\n 7(0) ОГЭ по выбору: обществознание (классы "А" и "Б")(17), литература (6)', reply_markup=sverka1)


@dp.message_handler(text='[9А]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 алгебра 30\n 2 химия 22\n 3 англ.15/нем.31\n 4 нем.31/англ.28\n 5 ИВТ 21,25\n 6 литература 6\n 7(0) ОГЭ математика 30\n 1 кл.час 21', reply_markup=sverka1)


@dp.message_handler(text='[9А]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 физика 13\n 2 биология 12\n 3 всеобщая история 17\n 4 алгебра 30\n 5 физич. культура\n 6 русский язык 6\n 7(0)ОГЭ по выбору: ИВТ (21,25), английский язык (15, 28)\n 1 Геоинформатика с 10А', reply_markup=sverka1)


@dp.message_handler(text='[9А]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 химия 22\n 2 геометрия 30\n 3 обществознание 17\n 4 англ. яз. 15,28\n 5 литература 6\n 6 география 29\n 7(0) ОГЭ русский язык 6', reply_markup=sverka1)


@dp.message_handler(text='[9А]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 ОГЭ физика 13\n 2 физика 13\n 3 физич. культура\n 4 ОБЖ 23\n 5 ОГЭ по истории, 26, биологии (29)', reply_markup=sverka1)


########################################################################################################################
@dp.message_handler(text='[9Б]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 9\n 2 русский яз.7\n 3 литература 9\n 4 физич. культура\n 5 алгебра 30\n 6 история России 17\n 7(0) англ. яз. 15,28\n 1 ОГЭ по выбору: химия (22), физика (13), география (29)', reply_markup=sverka1)


@dp.message_handler(text='[9Б]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 русский язык 6\n 3 физика 13\n 4 геометрия 30\n 5 история России 17\n 6 география 29\n 7(0) ОГЭ по выбору: обществознание (классы "А" и "Б")(17), литература (6)', reply_markup=sverka1)


@dp.message_handler(text='[9Б]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 немецкий язык 28\n 2 алгебра 30\n 3 химия 22\n 4 литература 6\n 5 англ. яз. 15,28\n 6 биология 12\n 7(0) ИВТ 21,25\n 1 кл.час 19', reply_markup=sverka1)


@dp.message_handler(text='[9Б]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 биология 12\n 2 алгебра 30\n 3 физика 13\n 4 русский язык 6\n 5 всеобщая история 17\n 6 ОГЭ русский 9\n 7(0) ОГЭ по выбору: ИВТ (21,25), английский язык (15, 28)', reply_markup=sverka1)


@dp.message_handler(text='[9Б]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 геометрия 30\n 2 литература 7\n 3 химия 22\n 4 география 29\n 5 обществознание 17\n 6 англ. яз. 15,28\n 7(0) ОГЭ математика 30', reply_markup=sverka1)


@dp.message_handler(text='[9Б]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 физич. культура\n 2 ОБЖ 23\n 3 физика 13\n 4 ОГЭ обществознание 26', reply_markup=sverka1)


########################################################################################################################
@dp.message_handler(text='[9В]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 30\n 2 алгебра 30\n 3 физич. культура\n 4 англ. яз. 15,28\n 5 история России 17\n 6 биология 29\n 7(0) русский язык 6\n 1 ОГЭ по выбору: химия (22), физика (13), география (29)', reply_markup=sverka1)


@dp.message_handler(text='[9В]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 география 29\n 2 физика 13\n 3 геометрия 30\n 4 история России 17\n 5 русский язык 6\n 6 литература 6\n 7(0) ОГЭ по выбору: обществознание (классы "А" и "Б")(17), литература (6)', reply_markup=sverka1)


@dp.message_handler(text='[9В]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 англ.28/нем.31\n 2 нем.31/англ.15\n 3 алгебра 30\n 4 химия 22\n 5 литература 6\n 6 ИВТ 21,25\n 7(0) ОГЭ русский язык 6\n 1 кл.час 30', reply_markup=sverka1)


@dp.message_handler(text='[9В]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 алгебра 30\n 2 физика 13\n 3 биология 12\n 4 всеобщая история 17\n 5 русский язык 6\n 6 ОГЭ обществознание 27\n 7(0) ОГЭ по выбору: ИВТ (21,25), английский язык (15, 28)\n 1 Геоинформатика с 10А ', reply_markup=sverka1)


@dp.message_handler(text='[9В]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 химия 22\n 3 геометрия 30\n 4 обществознание 17\n 5 англ. яз. 15,28\n 6 литература 6\n 7(0) география 29\n 1 ОГЭ математика 30', reply_markup=sverka1)


@dp.message_handler(text='[9В]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 физич. культура\n 3 ОБЖ 23\n 4 физика 13\n 5 ОГЭ по истории, 26, биологии (29)', reply_markup=sverka1)



########################################################################################################################
########################################################################################################################
tentehno
@dp.message_handler(text='[10Технолог]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Кл.час "разговоры о важном"\n 1 ИВТ 21\n 2 физика 13\n 3 история 26\n 4 ИВТ 21\n 5 математика 19\n 6 англ. К 15', reply_markup=sverka2)


@dp.message_handler(text='[10Технолог]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 физика 12\n 2 физика 12\n 3 литература 7\n 4 литература 7\n 5 математика 19\n 6 математика 19', reply_markup=sverka2)


@dp.message_handler(text='[10Технолог]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 7(0) АСУ 16\n 1 математика 19\n 2 ИВТ 21\n 3 Экспериментальное моделирование 13\n 4 ИВТ 21\n 5 Физкультура\n 6 англ. К 15', reply_markup=sverka2)


@dp.message_handler(text='[10Технолог]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 7(0) Решение задач повышенной сложности по математике 19\n 1 русский 7\n 2 математика 19\n 3 литература 7\n 4 физика 12\n 5 физика 12\n 6 география 12', reply_markup=sverka2)


@dp.message_handler(text='[10Технолог]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 ----\n 2 ОБЖ 13\n 3 Родной язык 7\n 4 математика 19\n 5 Основы приборостроения 1\n 6 Физкультура', reply_markup=sverka2)


@dp.message_handler(text='[10Технолог]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 6 Инженерная графика 1\n 1 история 26\n 2 англ. К 15', reply_markup=sverka2)


########################################################################################################################
@dp.message_handler(text='[10Естественно-научн]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 7(0) Кл.час "разговоры о важном"\n 1 биология 22\n 2 биология 22\n 3 история 26\n 4 математика 19\n 5 Биохимия 23\n 6 англ. К 15', reply_markup=sverka2)


@dp.message_handler(text='[10Естественно-научн]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 математика 19\n 2 математика 19\n 3 литература 7\n 4 литература 7\n 5 ИВТ 25', reply_markup=sverka2)


@dp.message_handler(text='[10Естественно-научн]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 Химия 23\n 2 математика 19\n 3 биофизика 22\n 4 биология 22\n 5 Физкультура\n 6 англ. К 15', reply_markup=sverka2)


@dp.message_handler(text='[10Естественно-научн]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 6 Pro-себя (с 11А)\n 0(7) Экология 12\n 1 русский 7\n 2 литература 7\n 3 физика 13 А\n 4 физика 13 А\n 5 математика 19', reply_markup=sverka2)


@dp.message_handler(text='[10Естественно-научн]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Решение задач повышенной сложности по математике 19\n 1 математика 19\n 2 ОБЖ 13\n 3 Родной язык 7\n 4 Химия 23\n 5 Химия 23\n 6 Физкультура', reply_markup=sverka2)


@dp.message_handler(text='[10Естественно-научн]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 история 26\n 2 англ. К 15', reply_markup=sverka2)


########################################################################################################################
@dp.message_handler(text='[10Соц-эконом]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Кл.час "разговоры о важном"\n 1 англ. К 15\n 2 обществознание 26\n 3 история 26\n 4 математика 19\n 5 Право 26', reply_markup=sverka2)


@dp.message_handler(text='[10Соц-эконом]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 математика 19\n 2 математика 19\n 3 литература 7\n 4 литература 7\n 5 ИВТ 25', reply_markup=sverka2)


@dp.message_handler(text='[10Соц-эконом]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Деловой английский\n 1 экономика 9\n 2 математика 19\n 3 экономика 9\n 4 Физкультура\n 5 англ. К 15', reply_markup=sverka2)


@dp.message_handler(text='[10Соц-эконом]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Финансовая грамотность 9\n 1 русский 7\n 2 литература 7\n 3 Геоинформатика\n 4 обществознание 26\n 5 математика 19\n 6 география 12', reply_markup=sverka2)


@dp.message_handler(text='[10Соц-эконом]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Решение задач повышенной сложности по математике 19\n 1 математика 19\n 2 ОБЖ 13\n 3 Родной язык 7\n 4 Физкультура\n 5 англ. К 15', reply_markup=sverka2)


@dp.message_handler(text='[10Соц-эконом]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 6 Право 26\n 1 история 26', reply_markup=sverka2)
########################################################################################################################
@dp.message_handler(text='[10Гуманитарный]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Кл.час "разговоры о важном"\n 1 англ. К 15\n 2 обществознание 26\n 3 русский 7\n 4 русский 7\n 5 Право 26', reply_markup=sverka2)


@dp.message_handler(text='[10Гуманитарный]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) МХК 8\n 1 история 26\n 2 история 26\n 3 литература 7\n 4 литература 7', reply_markup=sverka2)


@dp.message_handler(text='[10Гуманитарный]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Деловой английский\n 1 экономика 9\n 2 русский 7\n 3 экономика 9\n 4 Физкультура\n 5 англ. К 15\n 6 математика 19', reply_markup=sverka2)


@dp.message_handler(text='[10Гуманитарный]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) Финансовая грамотность 9\n 1 математика 19\n 2 история 26\n 3 литература 7\n 4 обществознание 26\n 5 география 12', reply_markup=sverka2)


@dp.message_handler(text='[10Гуманитарный]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 0(7) история 26\n 1 Родной язык 7\n 2 ОБЖ 13\n 3 математика 19\n 4 Физкультура\n 5 англ. К 15', reply_markup=sverka2)


@dp.message_handler(text='[10Гуманитарный]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n  6 Право 26\n 1 математика 19', reply_markup=sverka2)

########################################################################################################################
########################################################################################################################
@dp.message_handler(text='[11Технолог]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 14\n 2 русский язык 20\n 3 физика 13 а\n 4 физика 13 а\n 5 математика П14\n 6 математика П14\n 7(0) Репетиция Последнего звонка', reply_markup=sverka1)


@dp.message_handler(text='[11Технолог]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 Репетиция Последнего звонка\n 2 -------------\n 3 русский язык 20\n 4 математика П14\n 5 ИВТ 21\n 6 ИВТ 21', reply_markup=sverka1)


@dp.message_handler(text='[11Технолог]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 русский язык 20\n 2 физика 13\n 3 физика 13\n 4 математика П14\n 5 математика П14\n 6 ИВТ 16', reply_markup=sverka1)


@dp.message_handler(text='[11Технолог]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 математика П14\n 2 математика П14\n 3 ИВТ 21\n 4 ИВТ 21\n 5 ИВТ 21', reply_markup=sverka1)


@dp.message_handler(text='[11Технолог]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 математика П14\n 2 математика П14\n 3 физика 13 а\n 4 физика 13 а\n 5 физика 13 а\n 6 русский язык 20\n 7(0) Репетиция Последнего звонка', reply_markup=sverka1)


@dp.message_handler(text='[11Технолог]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n День самоподготовки', reply_markup=sverka1)


########################################################################################################################
@dp.message_handler(text='[11Естественно-научн]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 14\n 2 математика Б14\n 3 русский язык 20\n 4 биология П12\n 5 биология 12/математика П\n 6 математика П14\n 7(0) Репетиция Последнего звонка', reply_markup=sverka1)


@dp.message_handler(text='[11Естественно-научн]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 Репетиция Последнего звонка\n 2 математика Б14\n 3 русский язык 20\n 4 физическая химия 22/математика П\n 5 экология 29\n 6 биология 23', reply_markup=sverka1)


@dp.message_handler(text='[11Естественно-научн]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 русский язык 20\n 3 биология 12/математика П\n 4 биология 12/математика П\n 5 химия 22\n 6 химия 22/обществознание 26\n 7(0) обществозн. 26', reply_markup=sverka1)


@dp.message_handler(text='[11Естественно-научн]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 биология 23\n 3 математика Б14\n 4 химия 22\n 5 химия 22\n 6 химия 22', reply_markup=sverka1)


@dp.message_handler(text='[11Естественно-научн]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 математика П14\n 2 математика П14\n 3 математика Б14\n 4 химия 22\n 5 химия 22\n 6 русский язык 20\n 7(0) Репетиция Последнего звонка', reply_markup=sverka1)


@dp.message_handler(text='[11Естественно-научн]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n День самоподготовки', reply_markup=sverka1)


########################################################################################################################
@dp.message_handler(text='[11Гуманитарный филолог]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 20\n 2 математика Б14\n 3 англ. яз. 15\n 7(0) Репетиция Последнего звонка', reply_markup=sverka1)


@dp.message_handler(text='[11Гуманитарный филолог]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 Репетиция Последнего звонка\n 2 русский язык 20\n 3 математика Б14\n 4 литература 20, история 26\n 5 англ. яз. 15\n 6 англ. яз. 15\n 7(0) обществозн. 26', reply_markup=sverka1)


@dp.message_handler(text='[11Гуманитарный филолог]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 англ. яз. 15\n 2 англ. яз. 16\n 3 русский язык 20\n 4 англ. яз. 15/история 26\n 5 литература 20/история 26\n 6 обществозн. 2n 7(0) обществозн. 26', reply_markup=sverka1)


@dp.message_handler(text='[11Гуманитарный филолог]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 литература 20\n 2 русский язык 20\n 3 математика Б14\n 4 обществозн. 26\n 5 англ. яз. 15/экономика 9\n 6 англ. яз. 15, история 26\n 7(0) история 26', reply_markup=sverka1)


@dp.message_handler(text='[11Гуманитарный филолог]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 литература 20\n 2 литература 20\n 3 математика Б14\n 4 русский язык 20\n 5 история 26\n 6 история 26\n 7(0) Репетиция Последнего звонка', reply_markup=sverka1)


@dp.message_handler(text='[11Гуманитарный филолог]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n День самоподготовки', reply_markup=sverka1)


########################################################################################################################
eleventehno
@dp.message_handler(text='[11Гуманитарный истор]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 20\n 2 математика Б14\n 3 англ. яз. 28\n 4 биология П 12\n 5 биология П 12\n 7(0) Репетиция Последнего звонка', reply_markup=sverka1)


@dp.message_handler(text='[11Гуманитарный истор]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 Репетиция Последнего звонка\n 2 русский язык 20\n 3 математика Б14\n 4 история 26\n 5 право 26/ИВТ 21/экология 29\n 6 право 26/ИВТ 21/биология 23\n 7(0) обществозн. 26', reply_markup=sverka1)


@dp.message_handler(text='[11Гуманитарный истор]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 русский яз.20/англ. яз. 28\n 3 биология 12, англ. яз. 28\n 4 история 26/биология П 12\n 5 история 26\n 6 обществозн. 26\n 7(0) обществозн. 26', reply_markup=sverka1)


@dp.message_handler(text='[11Гуманитарный истор]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 русский язык 20\n 3 математика Б14\n 4 обществозн. 26\n 5 экономика 9\n 6 англ. яз. 28; история 26\n 7(0) история 26', reply_markup=sverka1)


@dp.message_handler(text='[11Гуманитарный истор]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 англ. яз. 28\n 2 англ. яз. 28\n 3 математика Б14\n 4 русский язык 20\n 5 история 26\n 6 история 26\n 7(0) Репетиция Последнего звонка', reply_markup=sverka1)


@dp.message_handler(text='[11Гуманитарный истор]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n День самоподготовки', reply_markup=sverka1)
########################################################################################################################
@dp.message_handler(text='[11Соц-эконом]Понедельник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 кл.час 20\n 2 -------------\n 3 русский язык 20\n 4 -------------\n 5 математика П14\n 6 математика П14\n 7(0) Репетиция Последнего звонка', reply_markup=sverka1)


@dp.message_handler(text='[11Соц-эконом]Вторник')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 Репетиция Последнего звонка\n 2 -------------\n 3 русский язык 20\n 4 математика П14\n 5 право 26/ИВТ 21\n 6 право 26/ИВТ 21\n 7(0) обществозн. 26', reply_markup=sverka1)


@dp.message_handler(text='[11Соц-эконом]Среда')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 -------------\n 2 -------------\n 3 русский язык 20\n 4 математика П14\n 5 математика П14\n 6 обществозн. 26\n 7(0) обществозн. 26', reply_markup=sverka1)


@dp.message_handler(text='[11Соц-эконом]Четверг')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 математика П14\n 2 математика П14\n 3 ИВТ 21\n 4 обществозн. 26/ИВТ 21\n 5 экономика 9/ИВТ 21', reply_markup=sverka1)


@dp.message_handler(text='[11Соц-эконом]Пятница')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n 1 математика П14\n 2 математика П14\n 3 -------------\n 4 русский язык 20\n 7(0) Репетиция Последнего звонка', reply_markup=sverka1)


@dp.message_handler(text='[11Соц-эконом]Суббота')
async def first(message: types.Message):
    await message.answer(f'Вот твое расписание:\n День самоподготовки', reply_markup=sverka1)
########################################################################################################################
########################################################################################################################



if __name__ == '__main__':
     executor.start_polling(dp, skip_updates=True)



