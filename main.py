@bot.command()
async def slot(ctx):
    naka = ["7οΈβ£", "πΆ", "π", "π­", "π©", "πΆ", "π€", "βΌοΈ", "β"]
    #naka=["7"]
    one = random.choice(naka)
    two = random.choice(naka)
    three=random.choice(naka)
    await ctx.send(one+two+three)
    if one == two:#1γ¨2γγγͺγγ§
      if two == three:#3γεγγͺγ
        await ctx.send("ε½γγοΌ")#γγγ ctx.send
      else:#εγγγγͺγγͺγ
        await ctx.send("γγΊγ¬")#γ―γγ
    else:
      if two == three:#2γ¨3γγγͺγγͺγ
        if three == one:#1γγγͺγγͺγ
          await ctx.send("ε½γγοΌ")#γγγ
        else:#γ‘γγγͺγ
          await ctx.send("γγΊγ¬")#γ―γγ
      elif three == one:#3γ¨1γεγγͺγ
        if one == two:#2γεγγͺγ
          await ctx.send("ε½γγοΌ")#ε½γγ
        else:#γγδ»₯ε€
          await ctx.send("γγΊγ¬")#γ―γγ
      else:
        await ctx.send("γγΊγ¬")
