import random
from tkinter import *
from tkinter import ttk

import tkextrafont
import customtkinter
from PIL import ImageTk, Image
from customtkinter import *
from tkextrafont import Font
import os
import time
import tracestack
global runs
runs = 0

app = CTk()
app.geometry("800x650")
background = ImageTk.PhotoImage(file='background.png')
backgroundL = Label(app, image=background, borderwidth=0, highlightthickness=0, width=800,height=650)
backgroundL.pack(expand="yes")
backgroundL.place(anchor='center', relx=0.5,rely=0.5)
def main():
    def deal():

        bestPlay = ''
        pair = 'False'
        playerHand = [0,0]
        playerHandImgs = ['','']
        dealerHand = [0,0]
        dealerHandImgs = ['','']
        playerInput = ''
        deck = ['A','A','A','A','2','2','2','2','3','3','3','3',
                '4','4','4','4','5','5','5','5','6','6','6','6',
                '7','7','7','7','8','8','8','8','9','9','9','9',
                'T','T','T','T','J','J','J','J','Q','Q','Q','Q',
                'K','K','K','K']
        #Associated array for photos of cards delt
        cardImgs = ['AC.png','AD.png','AH.png','AS.png','2C.png','2D.png','2H.png','2S.png',
                    '3C.png','3D.png','3H.png','3S.png','4C.png','4D.png','4H.png','4S.png',
                    '5C.png','5D.png','5H.png','5S.png','6C.png','6D.png','6H.png','6S.png',
                    '7C.png','7D.png','7H.png','7S.png','8C.png','8D.png','8H.png','8S.png',
                    '9C.png','9D.png','9H.png','9S.png','10C.png','10D.png','10H.png','10S.png',
                    'JC.png','JS.png','JH.png','JS.png','QC.png','QD.png','QH.png','QS.png',
                    'KC.png','KD.png','KH.png','KS.png']
        #Arrays for each players hand
        playerHand = [0,0]
        dealerHand = [0,0]

        #Take a random card from the arrays, delete the values from array, then return card and card photo as array
        def getCard(deck,cardImgs):
            cardData = [0,0]
            rand = random.randint(0,len(deck)-1)

            cardData[0] = deck[rand]
            cardData[1] = cardImgs[rand]

            deck.remove(deck[rand])
            cardImgs.remove(cardImgs[rand])

            return cardData
        playerHandImgs = ['','']
        dealerHandImgs = ['','']

        temp = getCard(deck,cardImgs)
        playerHand[0] = temp[0]
        playerHandImgs[0] = temp[1]
        temp = getCard(deck, cardImgs)
        playerHand[1] = temp[0]
        playerHandImgs[1] = temp[1]

        temp = getCard(deck, cardImgs)
        dealerHand[0] = temp[0]
        dealerHandImgs[0] = temp[1]
        temp = getCard(deck, cardImgs)
        dealerHand[1] = temp[0]
        dealerHandImgs[1] = temp[1]

        #print("Dealer Hand: ")
        #print(dealerHandImgs[0],dealerHandImgs[1])
        #print("Player Hand: ")
        #print(playerHandImgs[0],playerHandImgs[1])

        bestPlay = ''

        def getHandValue(card1,card2):
            return getCardValue(card1) + getCardValue(card2)

        def getCardValue(card):
            if card == 'A':
                cardVal = 11
            elif card == 'K' or card == 'Q' or card == 'J' or card == 'T':
                cardVal = 10
            elif card == '9':
                cardVal = 9
            elif card == '8':
                cardVal = 8
            elif card == '7':
                cardVal = 7
            elif card == '6':
                cardVal = 6
            elif card == '5':
                cardVal = 5
            elif card == '4':
                cardVal = 4
            elif card == '3':
                cardVal = 3
            elif card == '2':
                cardVal = 2
            return cardVal

        def pairCheck(playerHand):
            if getCardValue(playerHand[0]) == getCardValue(playerHand[1]):
                return 'True'
            else:
                return 'False'

        pair = pairCheck(playerHand)

        def aceCheck(playerHand):
            if 'A' in playerHand:
                return True
            else:
                return False




        playerHandValue = getHandValue(playerHand[0],playerHand[1])
        dealerUpCard = getCardValue(dealerHand[0])

        if aceCheck(playerHand) == True and pairCheck(playerHand) == False:
            playerHandValue -= 11
            match dealerUpCard:
                case 2:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Hit'
                        case 3:
                            bestPlay = 'Hit'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Hit'
                        case 6:
                            bestPlay = 'Hit'
                        case 7:
                            bestPlay = 'Double'
                        case 8:
                            bestPlay = 'Stand'
                        case 9:
                            bestPlay = 'Stand'
                case 3:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Hit'
                        case 3:
                            bestPlay = 'Hit'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Hit'
                        case 6:
                            bestPlay = 'Double'
                        case 7:
                            bestPlay = 'Double'
                        case 8:
                            bestPlay = 'Stand'
                        case 9:
                            bestPlay = 'Stand'

                case 4:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Hit'
                        case 3:
                            bestPlay = 'Hit'
                        case 4:
                            bestPlay = 'Double'
                        case 5:
                            bestPlay = 'Double'
                        case 6:
                            bestPlay = 'Double'
                        case 7:
                            bestPlay = 'Double'
                        case 8:
                            bestPlay = 'Stand'
                        case 9:
                            bestPlay = 'Stand'

                case 5:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Double'
                        case 3:
                            bestPlay = 'Double'
                        case 4:
                            bestPlay = 'Double'
                        case 5:
                            bestPlay = 'Double'
                        case 6:
                            bestPlay = 'Double'
                        case 7:
                            bestPlay = 'Double'
                        case 8:
                            bestPlay = 'Stand'
                        case 9:
                            bestPlay = 'Stand'

                case 6:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Double'
                        case 3:
                            bestPlay = 'Double'
                        case 4:
                            bestPlay = 'Double'
                        case 5:
                            bestPlay = 'Double'
                        case 6:
                            bestPlay = 'Double'
                        case 7:
                            bestPlay = 'Double'
                        case 8:
                            bestPlay = 'Double'
                        case 9:
                            bestPlay = 'Stand'
                case 7:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Hit'
                        case 3:
                            bestPlay = 'Hit'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Hit'
                        case 6:
                            bestPlay = 'Hit'
                        case 7:
                            bestPlay = 'Stand'
                        case 8:
                            bestPlay = 'Stand'
                        case 9:
                            bestPlay = 'Stand'
                case 8:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Hit'
                        case 3:
                            bestPlay = 'Hit'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Hit'
                        case 6:
                            bestPlay = 'Hit'
                        case 7:
                            bestPlay = 'Stand'
                        case 8:
                            bestPlay = 'Stand'
                        case 9:
                            bestPlay = 'Stand'
                case 9:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Hit'
                        case 3:
                            bestPlay = 'hit'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Hit'
                        case 6:
                            bestPlay = 'Hit'
                        case 7:
                            bestPlay = 'Hit'
                        case 8:
                            bestPlay = 'Stand'
                        case 9:
                            bestPlay = 'Stand'
                case 10:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Hit'
                        case 3:
                            bestPlay = 'Hit'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Hit'
                        case 6:
                            bestPlay = 'Hit'
                        case 7:
                            bestPlay = 'Hit'
                        case 8:
                            bestPlay = 'Stand'
                        case 9:
                            bestPlay = 'Stand'
                case 11:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Hit'
                        case 3:
                            bestPlay = 'Hit'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Hit'
                        case 6:
                            bestPlay = 'Hit'
                        case 7:
                            bestPlay = 'Hit'
                        case 8:
                            bestPlay = 'Stand'
                        case 9:
                            bestPlay = 'Stand'
        elif(pairCheck == True):
            playerHandValue /= 2
            match dealerUpCard:
                case 2:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Split'
                        case 3:
                            bestPlay = 'Split'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Hit'
                        case 6:
                            bestPlay = 'Split'
                        case 7:
                            bestPlay = 'Split'
                        case 8:
                            bestPlay = 'Split'
                        case 9:
                            bestPlay = 'Split'
                        case 10:
                            bestPlay = 'Stand'
                        case 11:
                            bestPlay = 'Split'
                case 3:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Split'
                        case 3:
                            bestPlay = 'Split'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Double'
                        case 6:
                            bestPlay = 'Split'
                        case 7:
                            bestPlay = 'Split'
                        case 8:
                            bestPlay = 'Split'
                        case 9:
                            bestPlay = 'Split'
                        case 10:
                            bestPlay = 'Stand'
                        case 11:
                            bestPlay = 'Split'

                case 4:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Split'
                        case 3:
                            bestPlay = 'Split'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Double'
                        case 6:
                            bestPlay = 'Split'
                        case 7:
                            bestPlay = 'Split'
                        case 8:
                            bestPlay = 'Split'
                        case 9:
                            bestPlay = 'Split'
                        case 10:
                            bestPlay = 'Stand'
                        case 11:
                            bestPlay = 'Split'

                case 5:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Split'
                        case 3:
                            bestPlay = 'Split'
                        case 4:
                            bestPlay = 'Split'
                        case 5:
                            bestPlay = 'Double'
                        case 6:
                            bestPlay = 'Split'
                        case 7:
                            bestPlay = 'Split'
                        case 8:
                            bestPlay = 'Split'
                        case 9:
                            bestPlay = 'Split'
                        case 10:
                            bestPlay = 'Stand'
                        case 11:
                            bestPlay = 'Split'

                case 6:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Split'
                        case 3:
                            bestPlay = 'Split'
                        case 4:
                            bestPlay = 'Split'
                        case 5:
                            bestPlay = 'Double'
                        case 6:
                            bestPlay = 'Split'
                        case 7:
                            bestPlay = 'Split'
                        case 8:
                            bestPlay = 'Split'
                        case 9:
                            bestPlay = 'Split'
                        case 10:
                            bestPlay = 'Stand'
                        case 11:
                            bestPlay = 'Split'
                case 7:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Split'
                        case 3:
                            bestPlay = 'Split'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Double'
                        case 6:
                            bestPlay = 'Hit'
                        case 7:
                            bestPlay = 'Split'
                        case 8:
                            bestPlay = 'Split'
                        case 9:
                            bestPlay = 'Stand'
                        case 10:
                            bestPlay = 'Stand'
                        case 11:
                            bestPlay = 'Split'
                case 8:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Hit'
                        case 3:
                            bestPlay = 'Hit'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Double'
                        case 6:
                            bestPlay = 'Hit'
                        case 7:
                            bestPlay = 'Hit'
                        case 8:
                            bestPlay = 'Split'
                        case 9:
                            bestPlay = 'Split'
                        case 10:
                            bestPlay = 'Stand'
                        case 11:
                            bestPlay = 'Split'
                case 9:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Hit'
                        case 3:
                            bestPlay = 'Hit'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Double'
                        case 6:
                            bestPlay = 'Hit'
                        case 7:
                            bestPlay = 'Hit'
                        case 8:
                            bestPlay = 'Split'
                        case 9:
                            bestPlay = 'Split'
                        case 10:
                            bestPlay = 'Stand'
                        case 11:
                            bestPlay = 'Split'
                case 10:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Hit'
                        case 3:
                            bestPlay = 'Hit'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Hit'
                        case 6:
                            bestPlay = 'Hit'
                        case 7:
                            bestPlay = 'Hit'
                        case 8:
                            bestPlay = 'Split'
                        case 9:
                            bestPlay = 'Stand'
                        case 10:
                            bestPlay = 'Stand'
                        case 11:
                            bestPlay = 'Split'
                case 11:
                    match playerHandValue:
                        case 2:
                            bestPlay = 'Hit'
                        case 3:
                            bestPlay = 'Hit'
                        case 4:
                            bestPlay = 'Hit'
                        case 5:
                            bestPlay = 'Hit'
                        case 6:
                            bestPlay = 'Hit'
                        case 7:
                            bestPlay = 'Hit'
                        case 8:
                            bestPlay = 'Split'
                        case 9:
                            bestPlay = 'Stand'
                        case 10:
                            bestPlay = 'Stand'
                        case 11:
                            bestPlay = 'Split'
        else:
                if(playerHandValue >= 17):
                    bestPlay = 'Stand'
                if(playerHandValue <= 8):
                    bestPlay = 'Hit'
                else:
                    match(dealerUpCard):
                        case 2:
                            match playerHandValue:
                                case 9:
                                    bestPlay = 'Hit'
                                case 10:
                                    bestPlay = 'Double'
                                case 11:
                                    bestPlay = 'Double'
                                case 12:
                                    bestPlay = 'Hit'
                                case 13:
                                    bestPlay = 'Stand'
                                case 14:
                                    bestPlay = 'Stand'
                                case 15:
                                    bestPlay = 'Stand'
                                case 16:
                                    bestPlay = 'Stand'
                        case 3:
                            match playerHandValue:
                                case 9:
                                    bestPlay = 'Double'
                                case 10:
                                    bestPlay = 'Double'
                                case 11:
                                    bestPlay = 'Double'
                                case 12:
                                    bestPlay = 'Hit'
                                case 13:
                                    bestPlay = 'Stand'
                                case 14:
                                    bestPlay = 'Stand'
                                case 15:
                                    bestPlay = 'Stand'
                                case 16:
                                    bestPlay = 'stand'
                        case 4:
                            match playerHandValue:
                                case 9:
                                    bestPlay = 'Double'
                                case 10:
                                    bestPlay = 'Double'
                                case 11:
                                    bestPlay = 'Double'
                                case 12:
                                    bestPlay = 'Stand'
                                case 13:
                                    bestPlay = 'Stand'
                                case 14:
                                    bestPlay = 'Stand'
                                case 15:
                                    bestPlay = 'Stand'
                                case 16:
                                    bestPlay = 'Stand'
                        case 5:
                            match playerHandValue:
                                case 9:
                                    bestPlay = 'Double'
                                case 10:
                                    bestPlay = 'Double'
                                case 11:
                                    bestPlay = 'Double'
                                case 12:
                                    bestPlay = 'Stand'
                                case 13:
                                    bestPlay = 'Stand'
                                case 14:
                                    bestPlay = 'Stand'
                                case 15:
                                    bestPlay = 'Stand'
                                case 16:
                                    bestPlay = 'Stand'

                        case 6:
                            match playerHandValue:
                                case 9:
                                    bestPlay = 'Double'
                                case 10:
                                    bestPlay = 'Double'
                                case 11:
                                    bestPlay = 'Double'
                                case 12:
                                    bestPlay = 'Stand'
                                case 13:
                                    bestPlay = 'Stand'
                                case 14:
                                    bestPlay = 'stand'
                                case 15:
                                    bestPlay = 'Stand'
                                case 16:
                                    bestPlay = 'Stand'
                        case 7:
                            match playerHandValue:
                                case 9:
                                    bestPlay = 'Hit'
                                case 10:
                                    bestPlay = 'Double'
                                case 11:
                                    bestPlay = 'Double'
                                case 12:
                                    bestPlay = 'Hit'
                                case 13:
                                    bestPlay = 'Hit'
                                case 14:
                                    bestPlay = 'Hit'
                                case 15:
                                    bestPlay = 'Hit'
                                case 16:
                                    bestPlay = 'Hit'
                        case 8:
                            match playerHandValue:
                                case 9:
                                    bestPlay = 'Hit'
                                case 10:
                                    bestPlay = 'Double'
                                case 11:
                                    bestPlay = 'Double'
                                case 12:
                                    bestPlay = 'Hit'
                                case 13:
                                    bestPlay = 'Hit'
                                case 14:
                                    bestPlay = 'Hit'
                                case 15:
                                    bestPlay = 'Hit'
                                case 16:
                                    bestPlay = 'Hit'
                        case 9:
                            match playerHandValue:
                                case 9:
                                    bestPlay = 'Hit'
                                case 10:
                                    bestPlay = 'Double'
                                case 11:
                                    bestPlay = 'Double'
                                case 12:
                                    bestPlay = 'Hit'
                                case 13:
                                    bestPlay = 'Hit'
                                case 14:
                                    bestPlay = 'Hit'
                                case 15:
                                    bestPlay = 'Hit'
                                case 16:
                                    bestPlay = 'Hit'
                        case 10:
                            match playerHandValue:
                                case 9:
                                    bestPlay = 'Hit'
                                case 10:
                                    bestPlay = 'Hit'
                                case 11:
                                    bestPlay = 'Double'
                                case 12:
                                    bestPlay = 'Hit'
                                case 13:
                                    bestPlay = 'Hit'
                                case 14:
                                    bestPlay = 'Hit'
                                case 15:
                                    bestPlay = 'Hit'
                                case 16:
                                    bestPlay = 'Hit'
                        case 11:
                            match playerHandValue:
                                case 9:
                                    bestPlay = 'Hit'
                                case 10:
                                    bestPlay = 'Hit'
                                case 11:
                                    bestPlay = 'Double'
                                case 12:
                                    bestPlay = 'Hit'
                                case 13:
                                    bestPlay = 'Hit'
                                case 14:
                                    bestPlay = 'Hit'
                                case 15:
                                    bestPlay = 'Hit'
                                case 16:
                                    bestPlay = 'Hit'
                    returns = [bestPlay,pair,playerHand,playerHandImgs,dealerHand,dealerHandImgs]
                    return returns

    def everythingElse():
        returns = deal()
        if returns is None:
            everythingElse()
        else:
            bestPlay = returns[0]

        pairCheck = returns[1]
        playerHand = returns[2]
        playerHandImgs = returns[3]
        dealerHand = returns[4]
        dealerHandImgs = returns[5]

        split = ''
        if pairCheck == 'True':
            split = 'y'
        else:
            split = 'n'

        def clickDouble(b1,b2,b3,b4):
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            giveResult('Double')
        def clickSplit(b1,b2,b3,b4):
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            giveResult('Split')
        def clickHit(b1,b2,b3,b4):
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            giveResult('Hit')
        def clickStand(b1,b2,b3,b4):
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            giveResult('Stand')


        def buttons(split):
            global runs
            if runs == 0:
                #font = Font(file="Pixeboy.ttf",
                #        family="Overhaul")
                runs += 1

            HitButton = CTkButton(master=app, text="Hit", text_color="#dcf29d",
                                  corner_radius=0, font=("Pixeboy", 24),
                                  width=112, height=42, fg_color="#1b1233",
                                  border_width=6, border_color="#dcf29d",
                                  hover="false",command = lambda:clickHit(HitButton,StandButton,DoubleButton,SplitButton))
            HitButton.place(relx=0.14, rely=0.89, anchor="center")

            StandButton = CTkButton(master=app, text="Stand", text_color="#dcf29d",
                                    corner_radius=0, font=("Pixeboy", 24),
                                    width=112, height=42, fg_color="#1b1233",
                                    border_width=6, border_color="#dcf29d",
                                    hover="false",command = lambda:clickStand(HitButton,StandButton,DoubleButton,SplitButton))
            StandButton.place(relx=0.38, rely=0.89, anchor="center")

            DoubleButton = CTkButton(master=app, text="Double", text_color="#dcf29d",
                                     corner_radius=0, font=("Pixeboy", 24),
                                     width=112, height=42, fg_color="#1b1233",
                                     border_width=6, border_color="#dcf29d",
                                     hover="false",command = lambda:clickDouble(HitButton,StandButton,DoubleButton,SplitButton))
            DoubleButton.place(relx=0.62, rely=0.89, anchor="center")
            if split == 'y':
                SplitButton = CTkButton(master=app, text="Split", text_color="#dcf29d",
                                        corner_radius=0, font=("Pixeboy", 24),
                                        width=112, height=42, fg_color="#1b1233",
                                        border_width=6, border_color="#dcf29d",
                                        hover="false",command  = lambda:clickSplit(HitButton,StandButton,DoubleButton,SplitButton))
                SplitButton.place(relx=0.86, rely=0.89, anchor="center")
            else:
                SplitButton = CTkButton(master=app, text="Split", text_color="#000000",
                                        corner_radius=0, font=("Pixeboy", 24),
                                        width=112, height=42, fg_color="#808080",
                                        border_width=6, border_color="#dcf29d",
                                        hover="false")
                SplitButton.place(relx=0.86, rely=0.89, anchor="center")

            return

        def cards(BJG):

            # Label for the dealers 1st Card image=getCards[0]
            Dealer1 = Label(app, image=dealer1, borderwidth=0, highlightthickness=0)
            Dealer1.pack(side="bottom", fill="none", expand="yes")
            Dealer1.place(relx=0.39, rely=0.3, anchor='center')

            # Label for the dealers 2nd Card image=getCards[1]
            Dealer2 = Label(app, image=dealer2, borderwidth=0, highlightthickness=0)
            Dealer2.pack(side="bottom", fill="none", expand="yes")
            Dealer2.place(relx=0.61, rely=0.3, anchor='center')

            # Label for the players 1st Card image=getCards[2]
            Player1 = Label(app, image=player1, borderwidth=0, highlightthickness=0)
            Player1.pack(side="bottom", fill="none", expand="yes")
            Player1.place(relx=0.39, rely=0.65, anchor='center')

            # Label for the players 2nd Card image=getCards[3]
            Player2 = Label(app, image=player2, borderwidth=0, highlightthickness=0)
            Player2.pack(side="bottom", fill="none", expand="yes")
            Player2.place(relx=0.61, rely=0.65, anchor='center')

            return

        buttons(split)
        def gameResult(resultBut):
            resultBut.destroy()
            end()

        def giveResult(player):
            if(player == bestPlay):
                WinButton = CTkButton(master=app, text="That play was correct!", text_color="#dcf29d",
                                      corner_radius=0, font=("Pixeboy", 24),
                                      width=300, height=200, fg_color="#1b1233",
                                      border_width=6, border_color="#dcf29d",
                                      hover="false",command=lambda:gameResult(WinButton))
                WinButton.place(relx=0.5, rely=0.5, anchor="center")
            else:
                LoseButton = CTkButton(master=app, text="That play was incorrect!\nThe correct play was to " + bestPlay.lower() +".", text_color="#dcf29d",
                                      corner_radius=0, font=("Pixeboy", 24),
                                      width=400, height=300, fg_color="#1b1233",
                                      border_width=6, border_color="#dcf29d",
                                      hover="false",command=lambda:gameResult(LoseButton))
                LoseButton.place(relx=0.5, rely=0.5, anchor="center")





        BJG = [playerHandImgs[0],playerHandImgs[1],dealerHandImgs[0],dealerHandImgs[1]]
        dealer1 = PhotoImage(file=BJG[2])
        dealer2 = PhotoImage(file='card_back.png')
        player1 = PhotoImage(file=BJG[0])
        player2 = PhotoImage(file=BJG[1])
        cardImgMax = [player1,player2,dealer1,dealer2]
        cards(cardImgMax)

        app.mainloop()

    def end():
        everythingElse()

    end()
main()
