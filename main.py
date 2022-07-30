@bot.command()
async def slot(ctx):
    naka = ["7️⃣", "🕶", "😊", "😭", "🎩", "😶", "🤔", "‼️", "❓"]
    #naka=["7"]
    one = random.choice(naka)
    two = random.choice(naka)
    three=random.choice(naka)
    await ctx.send(one+two+three)
    if one == two:#1と2がおなじで
      if two == three:#3も同じなら
        await ctx.send("当たり！")#あたり ctx.send
      else:#同じじゃないなら
        await ctx.send("ハズレ")#はずれ
    else:
      if two == three:#2と3がおなじなら
        if three == one:#1もおなじなら
          await ctx.send("当たり！")#あたり
        else:#ちがうなら
          await ctx.send("ハズレ")#はずれ
      elif three == one:#3と1が同じなら
        if one == two:#2も同じなら
          await ctx.send("当たり！")#当たり
        else:#それ以外
          await ctx.send("ハズレ")#はずれ
      else:
        await ctx.send("ハズレ")
