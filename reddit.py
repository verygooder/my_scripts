import praw
from pycolor import print_color


class Red(praw.Reddit):
    """docstring for Red"""

    def __init__(self):
        super(Red, self).__init__(client_id='GSaafCzmidYIBg', client_secret='STJUANi0ifHpbSQC122a6ks0qLk', username='verygooder', password='Ka840915', user_agent='luo\'s client')
        if self.user.me() != 'verygooder':
            print('login error!')
            exit()
        else:
            print('login successful')

    def get_info(self, subreddit_name):
        sub = self.subreddit(subreddit_name)
        hots = list(sub.hot(limit=30))
        hots = sorted(hots, key=lambda x: x.score, reverse=False)
        for i in hots:
            print_color(i.title, fore='green')
            items = [str(i.score), i.url]
            string = '\t'.join(items)
            print(string)
            print('https://www.reddit.com' + i.permalink)
            print('=' * 30)


if __name__ == '__main__':
    r = Red()
    while 1:
        sub = input('input the subreddit you need to watch:')
        if sub == 'q':
            exit()
        else:
            r.get_info(sub)
