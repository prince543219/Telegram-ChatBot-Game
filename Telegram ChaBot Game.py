"""
Created on Thu Jun 13 13:23:58 2019

@author: shandyyu
"""
import random
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

hands = ['rock', 'paper', 'scissors']

emoji = {
    'rock': '👊',
    'paper': '✋',
    'scissors': '✌️'
}
    
global mine_cards 
mine_cards = ['none', 'none', 'none', 'none', 'none']
global your_cards
your_cards = ['none', 'none', 'none', 'none', 'none']
global mine
mine = []
global your
your = []
global dic
dic =  '{} {} {} {} {}'

count = 0

def start(bot, update): 
    global count
    print(count)
    if(count == 5):
        print('seeeeee!!!!!!')
        print(mine_cards)
        print(your_cards)
        mine.clear()
        your.clear()
        count = 0
        
    print('-----begin!-----')
    update.message.reply_text('Rock Paper Scissors！')
    update.message.reply_text('Dealing cards...')
    #發牌
    update.message.reply_text('My cards: ')
    for i in range(0, len(mine_cards)):
        mine_cards[i] = random.choice(hands)
        mine.append(emoji[mine_cards[i]])
        print(mine_cards[i])
    try:
        update.message.reply_text(dic.format(*mine))
    except Exception as e:
        print(e)
    
    
    update.message.reply_text('Your cards: ')
    for i in range(0, len(your_cards)):
        your_cards[i] = random.choice(hands)
        your.append(emoji[your_cards[i]])
        print(your_cards[i])
    try:
        update.message.reply_text(dic.format(*your))
    except Exception as e:
        print(e)

def choose(bot, update):
    update.message.reply_text('Choose one card to play！',
        reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton(your[hand], callback_data = hand) for hand in range(0, len(your))
            ]]))
    
def justice(test):
    if(test==1):
        return ' I win!!!!!'
    elif(test==2):
        return ' Draw @@'
    elif(test==3):
        return ' I lose QQ'
    
def play(bot, update):
    global count
    try:
        your_choose = update.callback_query.data
        print(your_choose)
        your_hands = int (your_choose)
        test=0
        aa=0
        
        if(your_cards[your_hands]=='rock'):
            for j in range(0, len(mine_cards)):
                if(mine_cards[j]=='paper'):
                    test = 1
                    print(test)
                    break
            if(test==0):
                for j in range(0, len(mine_cards)):
                    if(mine_cards[j]=='rock'):
                        test = 2
                        print(test)
                        break
            if(test==0):
                for j in range(0, len(mine_cards)):
                    if(mine_cards[j]=='scissors'):
                        test = 3
                        print(test)
                        break
            update.callback_query.edit_message_text('我出{}，你出{}, {}'.format(emoji[mine_cards[j]], emoji[your_cards[your_hands]], justice(test)))
            aa=1
            count += 1
            del mine[j]
            del mine_cards[j]
            del your_cards[your_hands] 
            del your[your_hands]
            mine_cards.append('none')
            your_cards.append('none')
        
        if(your_cards[your_hands]=='paper' and aa==0):
            for j in range(0, len(mine_cards)):
                if(mine_cards[j]=='scissors'):
                    test = 1
                    print(test)
                    break
            if(test==0):
                for j in range(0, len(mine_cards)):
                    if(mine_cards[j]=='paper'):
                        test = 2
                        print(test)
                        break
            if(test==0):
                for j in range(0, len(mine_cards)):
                    if(mine_cards[j]=='rock'):
                        test = 3
                        print(test)
                        break
            update.callback_query.edit_message_text('我出{}，你出{}, {}'.format(emoji[mine_cards[j]], emoji[your_cards[your_hands]], justice(test)))
            aa=1
            count += 1
            del mine[j]
            del mine_cards[j]
            del your_cards[your_hands] 
            del your[your_hands]
            mine_cards.append('none')
            your_cards.append('none')
        
        if(your_cards[your_hands]=='scissors' and aa==0):
            for j in range(0, len(mine_cards)):
                if(mine_cards[j]=='rock'):
                    test = 1
                    print(test)
                    break
            if(test==0):
                for j in range(0, len(mine_cards)):
                    if(mine_cards[j]=='scissors'):
                        test = 2
                        print(test)
                        break
            if(test==0):
                for j in range(0, len(mine_cards)):
                    if(mine_cards[j]=='paper'):
                        test = 3
                        print(test)
                        break
            update.callback_query.edit_message_text('我出{}，你出{}, {}'.format(emoji[mine_cards[j]], emoji[your_cards[your_hands]], justice(test)))
            aa=1
            count += 1
            del mine[j]
            del mine_cards[j]
            del your_cards[your_hands] 
            del your[your_hands]
            mine_cards.append('none')
            your_cards.append('none')
            
    except Exception as e:
        print(e) 
            
            
updater = Updater('7602939669:AAFFC5CWyV8ODKr1bs2p0XmyoTMRncomPRQ') # key in your token here.
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('play', play))
updater.dispatcher.add_handler(CommandHandler('justice', justice))
updater.dispatcher.add_handler(CommandHandler('choose', choose))
updater.dispatcher.add_handler(CallbackQueryHandler(play))

updater.start_polling()
updater.idle()
