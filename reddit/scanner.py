import os
import time

import praw
import yaml

client_secret = 'srGEoajQqVq5hEZLqCxM9enTIiU'
username = 'diracdeltafunct_v2'
password = 'Soccer03!'
client_id = 'VcXQ4Ey4urwoOQ'
user_agent = 'python:monitorscanner:0.0 (by /u/diracdeltafunct_v2)'


def load(filename=os.path.join(os.path.expanduser('~'), 'trump', 'data.yaml')):
    if os.path.isfile(filename):
        with open(filename) as f:
            return yaml.load(f.read())
    else:
        print('NO FILE')

def write_file(data=None, filename=os.path.join(os.path.expanduser('~'), 'trump', 'data.yaml')):
    if not os.path.isdir((os.path.dirname(filename))):
        os.mkdir(os.path.dirname(filename))
    with open(filename, 'w') as f:
        yaml.dump(data, f)


class TheDonald:
    subreddit = 'the_donald'

    def __init__(self, new=False):
        self.reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
                          user_agent=user_agent,
                         )
        if new:
            self._data = {}
        else:
            self._data = load()


    def get_posts(self, cat):
        if cat == 'top':
            generator = getattr(self.reddit.subreddit(self.subreddit), cat)(time_filter='day',limit=25)
        else:
            generator = getattr(self.reddit.subreddit(self.subreddit), cat)(limit=25)
        for sub in generator:
            if sub.id not in list(self._data.keys()):
                self.store(sub, cat)
            else:
                self.update(sub, self._data[sub.id], cat)

    def store(self, sub, cat):
        new_entry = {
            sub.id: {
                'title': sub.title,
                'stats': [{'time':time.time(),
                           'score': sub.score,
                           'cat': cat

                           }],
                'first_seen': cat,
                'comments': self.comment_stats(sub.comments),
                'link': sub.shortlink,
                'url': sub.url,
                'author': sub.author.name,


            }
        }
        self._data.update(new_entry)

    def comment_stats(self, comments):
        out = {}
        comments.replace_more(limit=3)

        for comment in comments.list():
            try:
                d = {comment.id:{'root': comment.is_root,
                     'author': comment.author.name,
                     'id': comment.id,
                     'score': [time.time(),comment.score],
                     'body': comment.body
                }}
                #print(comment.author.submission)
                out.update(d)
            except:
                pass
        return out

    def update_comment_stats(self, new, old):
        existing = list(old.keys())
        new.replace_more(limit=8)
        for comment in new.list():
            if comment.id not in existing:
                try:
                    d = {comment.id: {'root': comment.is_root,
                                     'author': comment.author.name,
                                     'id': comment.id,
                                     'score': [time.time(),comment.score],
                                     'body': comment.body
                        }}
                    old.update(d)
                except:
                    pass
            else:
                c = old[comment.id]
                c['score'].append([time.time(),comment.score])
                old.update(c)
        return old



    def update(self, new_sub, old_sub, cat):

        stats = old_sub['stats']
        stats.append({'time':time.time(),
                           'score': new_sub.score,
                      'cat': cat

                           })
        entry = {

                'stats': stats,
                'comments': self.update_comment_stats(new_sub.comments, old_sub['comments'])

            }
        self._data[new_sub.id].update(entry)

    def run(self):
        categories = ['new', 'hot', 'top']
        i = 0
        while True:
            for cat in categories:
                print('RUNNING %s, %s' % (i, cat))
                self.get_posts(cat=cat)

            write_file(self._data)
            i += 1

if __name__ == '__main__':

    d = TheDonald(new=True)
    d.run()