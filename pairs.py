pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?","Nice to meet you %1. How is your day going?"]
    ],

     [
        r"What products do you have ?",
        ["Specify if your interested in a mobile phone or tv?"]
    ],

    [
        r"what is your name ?",
        ["I am your customer care, how can i help ?"]
    ],

    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],

    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind. Let me now get your order, would you like a TV, Laptop or a Fridge?",]
    ],

    [
        r"i'm (.*) good",
        ["Nice to hear that. Alright, would you like a TV, Laptop or a Fridge?:)",]
    ],

    [
        r"hi|hey|hello|goodmorning|good morning",
        ["Hello, welcome to TechCamp Store. Would you like to buy?", "Hey there, welcome to TechCamp Store. Would you like a TV, Laptop or a Fridge??",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]

    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]

    ],
    [
        r"(.*) created ?",
        ["TechCamp created me using Python's NLTK library ","top secret ;)",]
    ],

     [
        r"\bTV\b ?",
        ["Here is a catalogue of all TVs we currently have.. Samsung Smart TV 60' - 4KUHD with Realm Technology. Costs only $ 450, ",]
    ],

    [
        r"(.*) (located|location|city|live|country|store) ?",
        ['Our store is located in Nairobi, Kenya but you can order from anywhere in the world and we will ship it to you.',]
    ],

    [
        r"(.*) (covid-19|corona|covid) ?",
        ["About Covid-19...Well, lets just say that I am glad I am a computer program and not a human.Stay safe and let me take your order"]
    ],

    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days, try working .",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]