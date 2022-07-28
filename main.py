import random
naka = ["7", "🕶", "😊", "😭", "🎩"]
#naka=["7"]
one = random.choice(naka)
two = random.choice(naka)
three=random.choice(naka)
print(one+two+three)
if one == two:#1と2がおなじで
  if two == three:#3も同じなら
    print("当たり！")#あたり ctx.send
  else:#同じじゃないなら
    print("ハズレ！")#はずれ
else:
  if two == three:#2と3がおなじなら
    if three == one:#1もおなじなら
      print("当たり！")#あたり
    else:#ちがうなら
      print("ハズレ")#はずれ
  elif three == one:#3と1が同じなら
    if one == two:#2も同じなら
      print("当たり！")#当たり
    else:#それ以外
      print("ハズレ")#はずれ
      
