import pyprind
import random
import time


class MagicBall(object):

    ANSWERS = [
        'As I see it, yes.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don’t count on it.',
        'It is certain.',
        'It is decidedly so.',
        'Most likely.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Outlook good.',
        'Reply hazy, try again.',
        'Signs point to yes.',
        'Very doubtful.',
        'Without a doubt.',
        'Yes.',
        'Yes – definitely.',
        'You may rely on it.'
    ]

    def __init__(self):
        self.__ask()

    def __ask(self):
        ask = input("Ask your question, mortal creature...")

        timesleep = 0.05
        random.seed(1)
        collection = set()

        n = 100
        bar = pyprind.ProgBar(n, title='Watching to the future...' + ask)

        while len(collection) < n:
            r = random.randint(0, 10 ** 5)
            if r % 7 and r not in collection:
                collection.add(r)
                bar.update()
                time.sleep(timesleep)

        print(bar)

        print(random.SystemRandom().choice(self.ANSWERS))


MagicBall()
