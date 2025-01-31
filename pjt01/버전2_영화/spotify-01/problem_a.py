import json
from pprint import pprint


def artist_info(artist):

    # 하드코딩 버전
    # my_dict = {}
    # my_dict.setdefault('genres_ids', artist['genres_ids'])
    # my_dict.setdefault('id', artist['id'])
    # my_dict.setdefault('images', artist['images'])
    # my_dict.setdefault('name', artist['name'])
    # my_dict.setdefault('type', artist['type'])
    
    my_dict = {}
    my_dict.update(artist)  # update를 사용하면 사용하지 않는 'external_urls', 'uri'도 들어온다.
    my_dict.pop('external_urls')
    my_dict.pop('uri')  # 그러니까, external_urls와 uri를 pop해서 쓰면 된다.

    return my_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':  # 이 파일에 대해~
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent  # 이 파일의 상위 폴더 경로를 절대경로로 current_dir에 넣는다.

    artist_json = open(current_dir / 'data' / 'artist.json', encoding='utf-8')  # 경로를 따라 json파일을 연다.
    artist_dict = json.load(artist_json)  # json파일을 해석할 수 있는 형태로 가공한다.

    pprint(artist_info(artist_dict))  # 함수를 적용한다.
