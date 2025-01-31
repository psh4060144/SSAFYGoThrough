import json
from pprint import pprint
from copy import deepcopy

def finding_filename(artists):
    
    new_lst = []

    for el in artists:
        new_lst.append(el['id'])

    return new_lst

def artist_popularity_info(artist):
    
    my_dict = {}
    my_dict.update(artist) 

    return {my_dict['popularity']: my_dict['name']}

def max_popularity(artists):

    new_lst = finding_filename(artists)  # file 이름을 list 형태로 정리.
    popularity_list = {}

    for el in new_lst:
        if __name__ == '__main__':
            from pathlib import Path

            current_dir = Path(__file__).resolve().parent

            artist_json = open(current_dir / 'data' / 'artists' / f'{el}.json', encoding='utf-8')
            artist_dict = json.load(artist_json)

            popularity = artist_popularity_info(artist_dict)
            popularity_list.update(popularity)
    
    for num in range(100, 0, -1):
        if popularity_list.get(num) == None:
            pass
        else:
            popular_singer = popularity_list[num]
            break

    return popular_singer

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    print(max_popularity(artists_list))
