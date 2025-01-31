import json
from pprint import pprint
from copy import deepcopy

def finding_filename(artists):  # file 이름을 list 형태로 정리하는 함수
    
    new_lst = []

    for el in artists:  # artist_list의 모든 값에 대해~
        new_lst.append(el['id'])  # artist_list의 id값을 new_lst에 추가.

    return new_lst

def artist_popularity_info(artist):  # 가수 이름과 popularity 값을 dictionary 형태로 정리하는 함수
    
    my_dict = {}
    my_dict.update(artist)  # artist_list의 값을 my_dict에 추가.

    return {my_dict['popularity']: my_dict['name']}  # my_dict의 popularity value를 key로, name value를 value로 하는 dictionary를 반환

def max_popularity(artists):

    new_lst = finding_filename(artists)  # file 이름을 list 형태로 정리.
    popularity_list = {}

    for el in new_lst:
        if __name__ == '__main__':  # 이 파일에 대해~
            from pathlib import Path

            current_dir = Path(__file__).resolve().parent  # 이 파일의 상위 폴더 경로를 절대경로로 current_dir에 넣는다.

            artist_json = open(current_dir / 'data' / 'artists' / f'{el}.json', encoding='utf-8')  # 경로를 따라 json파일을 연다. 이 때, json파일은 finding_filename 함수를 통해 만든 list로 정의한다.
            artist_dict = json.load(artist_json)  # json파일을 해석할 수 있는 형태로 가공한다.

            popularity = artist_popularity_info(artist_dict)
            popularity_list.update(popularity)  # 가수 이름과 popularity 값을 dictionary 형태로 정리하여 popularity_list dictionary에 추가.
    
    for num in range(100, 0, -1):  # key값을 내림차순으로 차례대로 내려오면서 value 값을 검색하는데~
        if popularity_list.get(num) == None:  # value 값이 None이면, 즉 key 값이 없는 값이라면~
            pass
        else:
            popular_singer = popularity_list[num]  # value 값이 있으면, 그 value 값을 출력.
            break

    return popular_singer

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    print(max_popularity(artists_list))