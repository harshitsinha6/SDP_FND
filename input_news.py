

# Importing Libraries
from bs4 import BeautifulSoup as bs
import requests



source_links = [
    'https://timesofindia.indiatimes.com/',
    'https://www.thehindu.com/',
    'https://www.hindustantimes.com/latest-news'
    ]


headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }

def ScrapData(source_link, target_word):
    src = requests.get(source_link, headers=headers)
    soup = bs(src.content, 'html.parser')
    
    #print(soup.text)      
    return soup.text
    
data = []
for link in source_links:
    data.append(ScrapData(link, 'assam'))
    
    



news = """BRUSSELS (Reuters) - NATO allies on Tuesday welcomed President Donald Trump s decision to commit more forces to Afghanistan,
 as part of a new U.S. strategy he said would require more troops and funding from America s partners. 
 Having run for the White House last year on a pledge to withdraw swiftly from Afghanistan, 
 Trump reversed course on Monday and promised a stepped-up military campaign against  Taliban insurgents, 
 saying:  Our troops will fight to win .  U.S. officials said he had signed off on plans to send about 4,000 
 more U.S. troops to add to the roughly 8,400 now deployed in Afghanistan. But his speech did not define benchmarks
 for successfully ending the war that began with the U.S.-led invasion of Afghanistan in 2001, and which he acknowledged 
 had required an   extraordinary sacrifice of blood and treasure .  We will ask our NATO allies and global partners to support
 our new strategy, with additional troops and funding increases in line with our own. We are confident they will,  Trump said. 
 That comment signaled he would further increase pressure on U.S. partners who have already been jolted by his repeated demands 
 to step up their contributions to NATO and his description of the alliance as  obsolete  - even though, since taking office, 
 he has said this is no longer the case. NATO Secretary General Jens Stoltenberg said in a statement: 
     NATO remains fully committed to Afghanistan and I am looking forward to discussing the way ahead with (Defense)
     Secretary (James) Mattis and our Allies and international partners.  NATO has 12,000 troops in Afghanistan, 
     and 15 countries have pledged more, Stoltenberg said. Britain, a leading NATO member, called the U.S. commitment  
     very welcome .  In my call with Secretary Mattis yesterday we agreed that despite the challenges, we have to stay the 
     course in Afghanistan to help build up its fragile democracy and reduce the terrorist threat to the West,  
     Defence Secretary Michael Fallon said. Germany, which has borne the brunt of Trump s criticism over  
     the scale of its defense spending, also welcomed the new U.S. plan.  Our continued commitment is necessary
     on the path to stabilizing the country,  a government spokeswoman said. In June, European allies had already pledged 
     more troops but had not given details on numbers, waiting for the Trump administration to outline its strategy for the 
     region.Nearly 16 years after the U.S.-led invasion - a response to the Sept. 11 attacks which were planned by al Qaeda leader
     Osama bin Laden from Afghanistan - the country is still struggling with weak central government and a Taliban insurgency. 
     Trump said he shared the frustration of the American people who were  weary of war without victory , but a hasty withdrawal
     would create a vacuum for groups like Islamic State and al Qaeda to fill."""



news1 = """Vic Bishop Waking TimesOur reality is carefully constructed by powerful corporate,
 political and special interest sources in order to covertly sway public opinion. Blatant lies are often
 televised regarding terrorism, food, war, health, etc. They are fashioned to sway public opinion and condition 
 viewers to accept what have become destructive societal norms.The practice of manipulating and controlling public 
 opinion with distorted media messages has become so common that there is a whole industry formed around this
 The entire role of this brainwashing industry is to figure out how to spin information to journalists,
 similar to the lobbying of government. It is never really clear just how much truth the journalists receive 
 because the news industry has become complacent. The messages that it presents are shaped by corporate powers who often 
 spend millions on advertising with the six conglomerates that own 90% of the media:General Electric (GE), News-Corp, Disney, 
 Viacom, Time Warner, and CBS. Yet, these corporations function under many different brands, such as FOX, ABC, CNN, Comcast, Wall 
 Street Journal, etc, giving people the perception of choice   As Tavistock s researchers showed, it was important that the victims
 of mass brainwashing not be aware that their environment was being controlled; there should thus be a vast number of sources for
 information, whose messages could be varied slightly, so as to mask the sense of external control. ~ Specialist of mass brainwashing,
 L. WolfeNew Brainwashing Tactic Called AstroturfWith alternative media on the rise, the propaganda machine continues to expand. Below 
 is a video of Sharyl Attkisson, investigative reporter with CBS, during which she explains how  astroturf, 
 or fake grassroots movements, are used to spin information not only to influence journalists but to sway public opinion.
 Astroturf is a perversion of grassroots. Astroturf is when political, corporate or other special interests disguise themselves 
 and publish blogs, start facebook and twitter accounts, publish ads, letters to the editor, or simply post comments online, 
 to try to fool you into thinking an independent or grassroots movement is speaking. ~ Sharyl Attkisson,
 Investigative ReporterHow do you separate fact from fiction? Sharyl Attkisson finishes her talk with some 
 insights on how to identify signs of propaganda and astroturfing  These methods are used to give people the impression
 that there is widespread support for an agenda, when, in reality, one may not exist. Astroturf tactics are also used to discredit 
 or criticize those that disagree with certain agendas, using stereotypical names such as conspiracy theorist or quack.
 When in fact when someone dares to reveal the truth or questions the  official  story, it should spark a deeper curiosity and
 encourage further scrutiny of the information.This article (Journalist Reveals Tactics Brainwashing Industry Uses to Manipulate
 the Public) was originally created and published by Waking Times and is published here under a Creative Commons license with
 attribution to Vic Bishop and WakingTimes.com. It may be re-posted freely with proper attribution, author bio, 
 and this copyright statement. READ MORE MSM PROPAGANDA NEWS AT: 21st Century Wire MSM Watch Files"""

print(manual_testing_news(news1, model))








