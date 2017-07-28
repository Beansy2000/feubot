import discord
from discord.ext import commands as bot
import os, random, re, asyncio

class Memes:
    """only the dankest"""

    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def reply(self):
        """r e p l y s o o n"""
        await self.bot.say("reply :soon: :smile:")

    @bot.command()
    async def whattime(self):
        """tells the time"""
        await self.bot.say("`it's tiki time`")
        # await asyncio.sleep(1)
        await self.bot.upload("tiki.gif")

    @bot.command()
    async def writing(self):
        """get it in writing. in blood."""
        await self.bot.upload("Pelleass_Blood_Pact.png")


    @bot.command()
    async def arch(self):
        """do something with arch"""
        direction = random.choice([":arrow_down:", ":arrow_up:"])
        await self.bot.say(direction+" with <:arch_mini:230160993299202068>")


    @bot.command()
    async def style(self):
        """if my style gets in your way"""
        img = random.choice(["styleRD.gif", "stylePoR.jpeg"])
        await self.bot.upload(img)

    @bot.command()
    async def goofs(self):
        """list goofs"""
        filenameslist = [os.path.splitext(f)[0] for f in os.listdir("./goofs")]
        await self.bot.say("```"+"\n".join(map(str, filenameslist))+"```")

    @bot.command()
    async def goof(self,*args):
        """show goof"""
        requested = args
        gooflist = {a.lower(): a for a in os.listdir("./goofs")}
        if len(requested) != 0:
            maxgoofs = 5
            for request in requested:
                if maxgoofs == 0: return
                else: maxgoofs -= 1
                file_extension_or_not_pattern = re.compile('(\.[a-z]+)?$', re.I | re.M)
                found = False
                for extension in ['.png', '.jpg', '.gif', '.jpeg']:
                    request_file = file_extension_or_not_pattern.sub(extension, request).lower()
                    if request_file in gooflist:
                        found = True
                        await self.bot.upload("./goofs/"+gooflist[request_file])
                if not found:
                    await self.bot.say("Use >>goofs to see a list of accepted goofs.")
        else:
            await self.bot.upload("./goofs/"+random.choice([a for a in gooflist.values()]))

    @bot.command()
    async def whois(self,*args):
        """roy is our boy"""
        if len(args) > 0:
            lord = ' '.join(args)
            if (lord.lower() in ['circles','circleseverywhere']):
                await self.bot.say(lord + " is my dad")
                return
            elif (lord.lower() == 'feditor'):
                await self.bot.say("`" + lord + " a shit`")
                return
            elif (lord.lower() == 'feubot'):
                await self.bot.say("That's me, silly!")
                return
            elif (lord.lower() == 'ea'):
                await self.bot.say("`" + lord + " is our bae`")
                return
            elif lord[0].lower() in 'bcdfghjklmnpqrstvwxz':
                blord = 'b'+lord[1:]
            else:
                blord = 'b'+lord
            await self.bot.say(lord + " is our " + blord)

    @bot.command()
    async def createwaifu(self,*args):
        """:wink:"""
        heads = [
            "<:zigludo:252132877678936064>", 
            "<:zahlman:230166256412655616>", 
            "<:narcian:271805925017387008>", 
            "<:marf:230171669635923968>", 
            "<:lloydwut:313590046978605059>", 
            "<:linde:325036388833558539>", 
            "<:lilina:230156179916062720>", 
            "<:kent:232283653642780672>", 
            "<:kaga:293121861905022976>", 
            "<:ick:280744571640610816>", 
            "<:florina:230904896067469312>", 
            "<:FEU:230151584846184448>", 
            "<:fa:303774076252454912>", 
            "<:elise:235616193065517066>", 
            "<:eliwood:232283812938121217>", 
            "<:elbert:232283825974149120>", 
            "<:EAmoe:317182514559188994>", 
            "<:doot:324593825815461889>", 
            "<:donate:230166446146191362>", 
            "<:doc:280527122802540544>", 
            "<:colorz:230159530158194688>", 
            "<:circles:238177111418863617>", 
            "<:celica:272027128231362571>", 
            "<:BBQ:230169373694885888>", 
            "<:arch_mini:230160993299202068>", 
            "<:cam_thumb:307559627573428224>", 
            "<:dat:292422389197701121>", 
            "<:thighs:294965155819683840>"]
        if len(args) > 0: head = ' '.join(args)
        else: head = random.choice(heads)
        await self.bot.say(head + """
<:personality:274564774979960832>
<:thighs:294965155819683840>""")

    @bot.command()
    async def doot(self):
        """doot doot"""
        flip = random.choice([0,1])
        if flip ==1:
            await self.bot.say("""<:doot:324593825815461889> <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> <:doot:324593825815461889> <:doot:324593825815461889>
<:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
<:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
<:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:
<:doot:324593825815461889> <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet: :trumpet: :trumpet: <:doot:324593825815461889> :trumpet:""")
        else:
            await self.bot.upload("./DOOT.png")

    @bot.command(aliases=["(lol"])
    async def lol(self):
        """(lol"""
        flip = random.choice([0,1])
        if flip==1: await self.bot.upload("./Water_lol.png")
        else: await self.bot.upload("./Water_lol2.png")

    @bot.command(aliases=["eventassembler", "everythingassembler"])
    async def ea(self):
        """EVERYTHING ASSEMBLER"""
        everythingassemblerstring = """``` _____                 _   _   _         
|   __|_ _ ___ ___ _ _| |_| |_|_|___ ___ 
|   __| | | -_|  _| | |  _|   | |   | . |
|_____|\_/|___|_| |_  |_| |_|_|_|_|_|_  |
                  |___|             |___|
 _____                   _   _
|  _  |___ ___ ___ _____| |_| |___ ___
|     |_ -|_ -| -_|     | . | | -_|  _|
|__|__|___|___|___|_|_|_|___|_|___|_|```"""
        await self.bot.say(everythingassemblerstring)

    @bot.command()
    async def casual(self):
        """just play phoenix"""
        barflist = os.listdir("./casual")
        await self.bot.upload("./casual/"+random.choice(barflist))

    @bot.command()
    async def erin(self):
        """ERIN INTENSIFIES"""
        await self.bot.upload("./erinyous.gif")

    @bot.command()
    async def fury(self):
        """2 FAST 2 FURYOUS"""
        await self.bot.say("Don't you mean `>>erin`?")

    @bot.command(aliases=["SOA", 'SoA'])
    async def soa(self):
        """there's your problem"""
        await self.bot.upload("./SoA.png")

    #TODO: HUBBA TESTER
    @bot.command()
    async def hubba(self, person1, person2):
        """discover their true feelings"""
        best_responses = ("About to swoon","Always staring","Carries a torch for","Desires attention","Devoted","Drawn by destiny","Drools openly","Fatal attraction","First love","Has a sweet spot","Head over heels","Heart aflutter","Infatuated","Lives and dies for","Loins afire","Lost in pheromones","Lovey Dovey","Never wants to part","One-track mind","Possessive","Puts on a pedestal","Separation anxiety","Smitten","True love","True sacrificer","Uses pet names","Wants to snuggle","Way too attached","Would give anything","Would hold hands")
        good_responses = ("Admires lifestyle","Always entertained","Best friend","Budding friendship","Comrade","Confessor","Easy to joke with","Feels safe","Finds agreeable","Fun to train with","Good friend","Into the same foods","Like minded","Low maintenance","Not a dull moment","On the same page","Relaxed around","Same wavelength","Sees potential","Shopping buddy","Similar hobbies","Sparring partner","Thinks highly of","Total respect","Totally platonic","Trusts implicitly","Ultimate duo")
        bad_responses = ("Avoids eye contact","Awkward","Bad chemistry","Bad teamwork","Cold shoulder","Dislikes","Dreads meeting","Expects betrayal","Fashion disaster","Feigns friendship","Finds freaky","Finds irritating","Friend zone","Indifferent","Intimidated","Into different things","Keeping a distance","No ear for music","Not interested","Not into the hair","Nothing in common","Nothing to say","On eggshells","Oil and water","Out of whack","Touch-and-go","Utterly baffled","Weirded Out")
        response_types = (best_responses, good_responses, bad_responses)

        mutual_best = ("Get a room, you two!",)
        best_good = ("Just spit it out, lovebird!",)
        best_bad = ("Unrequited love? Boring!",)
        mutual_good = ("My, they do get along nicely.",)
        good_bad = ("Oh dear. They just don't mix.",)
        mutual_bad = ("Two rocks'd hit it off better.",)
        reaction_types = (mutual_best, best_good, best_bad, mutual_good, good_bad, mutual_bad)

        ltr_type = random.choice(response_types)
        ltr = random.choice(ltr_type)
        rtl_type = random.choice(response_types)
        rtl = random.choice(rtl_type)
        if ltr_type==best_responses:
            if rtl_type==best_responses: reaction_type = mutual_best
            elif rtl_type==good_responses: reaction_type = best_good
            elif rtl_type==bad_responses: reaction_type = best_bad
        elif ltr_type==good_responses:
            if rtl_type==best_responses: reaction_type = best_good
            elif rtl_type==good_responses: reaction_type = mutual_good
            elif rtl_type==bad_responses: reaction_type = good_bad
        elif ltr_type==bad_responses:
            if rtl_type==best_responses: reaction_type = best_bad
            elif rtl_type==good_responses: reaction_type = good_bad
            elif rtl_type==bad_responses: reaction_type = mutual_bad

        reaction = random.choice(reaction_type)
        msg = """{person1} `--{ltr}->` {person2}
{person1} `<-{rtl}--` {person2}```
{reaction}```""".format(person1=person1,person2=person2,ltr=ltr,rtl=rtl,reaction=reaction)
        await self.bot.say(msg)

def setup(bot):
    bot.add_cog(Memes(bot))
