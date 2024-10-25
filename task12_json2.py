import requests

user_stat_dict = {}


def process_post(post):
    if post.get('username'):
        user_stat_dict.setdefault(post.get('username'), 0)
        user_stat_dict[post.get('username')] += 1
        if post.get('comments') and len(post['comments']) > 0:
            return post['comments']


def process_list(obj_list):
    if len(obj_list) > 0:
        obj = obj_list.pop()
        if isinstance(obj, dict):
            comments = process_post(obj)
            if comments:
                obj_list.extend(comments)
        else:
            obj_list.extend(obj)
    return obj_list


response = requests.get(url='https://parsinger.ru/3.4/3/dialog.json')
main_post = response.json()

obj_list = process_post(main_post)
while len(obj_list) > 0:
    obj_list = process_list(obj_list)

sort_dict = dict(sorted(user_stat_dict.items(), key=lambda item: item[0]))
sort_dict2 = dict(sorted(sort_dict.items(), key=lambda item: item[1], reverse=True))
print(sort_dict2)


