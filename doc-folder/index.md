# Frankie Chik's Website 
## Resume

1. Abouut Me  
Frankie Hin Ming Chik is a doctoral student in East Asian Languages and Civilizatioins (Chinese) at Arizona State University. His research interest covers the intellectual and cultural history in pre-modern China. Currently, he is working on the Song scholarship of ancient bronzes. 

2. Publication 
* *Translation*
  “Qing (情) and Emotion in Early Chinese Thought.” 早期中國思想中的「情」與情感 by Bruya Brain. In * *Hanji yu hanxue* In press.
  “Shangqing Scriptures as Performative Texts.”上清經的表演性質by Campany, Robert Ford. (Timothy Wai Keung Chan陳偉強proof read). In Chan Wai Keung陳偉強 ed.  * *Daojiao xiulan yu keyi de wenxue tiyan* Jiangsu: Fenghuang chubanshe, 2018, pp. 25-53.
* *Book Reviews*
  * *Confucius beyond the Analects*, by Hunter Michael. * *Dao: A Journal of Comparative Philosophy* Issue 8.1 (2019), pp. 137-141.

3. Python Code  
import random

list=[]
list2=[]
card1=random.randrange(1, 11, 1)
card2=random.randrange(1, 11, 1)
list.append(card1)
list2.append(card2)
print(card1)
print(card2)
winner=0
loser=0

answer="yes"
while answer=="yes":
    answer=input("Do you want another card?")
    if answer=="yes":
        card1=random.randrange(1, 11, 1)
        card2=random.randrange(1, 11, 1)
        list.append(card1)
        list2.append(card2)
        print(card1)
        print(card2)
        if sum(list)==21:
            winner=1
            break
        if sum(list2)==21:
            winner=2
            break
        if sum(list)>21:
            loser=1
            break
        if sum(list2)>21:
            loser=2
            break
if winner==0:
    if sum(list)>sum(list2):
        winner=1
    elif sum(list)<sum(list2):
        winner=2
if winner==1:
    print("player 1 is the winner.")
elif winner==2:
    print("player 2 is the winner.")
if loser==1:
    print("plater 1 is the loser.")
elif loser==2:
    print("player 2 is the loser.")

4. Link 
<https://github.com/FrankieChik/python-for-the-humanities-homework/blob/master/doc-folder/secondfile>
