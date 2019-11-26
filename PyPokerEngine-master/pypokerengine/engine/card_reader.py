import csv

class cardReader:

  cardList = []

  def __init__(self):
    self.cardList = []

  def returnCardList(self):
    self.addCard(self)

    f = open('pypokerengine/engine/read_card.csv', 'r')
    reader = csv.reader(f)
    for row in reader:
        self.cardList.append(row)
    f.close()

    return self.cardList

  def addCard(self):
    f = open('pypokerengine/engine/read_card.csv', 'w', newline='')
    #f = open('/read_card.csv', 'w', newline='')
    wr = csv.writer(f)
    for i in range(9):
      print(i)
      newCard = input("카드 입력 :")
      wr.writerow([newCard])
    
    f.close()
