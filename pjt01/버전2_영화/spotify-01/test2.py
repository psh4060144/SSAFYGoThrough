import json
from pprint import pprint

def artist_info(artist):
 
    my_dict = {}
    my_dict.update(artist)  # update를 사용하면 사용하지 않는 'external_urls', 'uri'도 들어온다.
    my_dict.pop('external_urls')
    my_dict.pop('uri')  # 그러니까, external_urls와 uri를 pop해서 쓰면 된다.

    return my_dict['id']

def finding_filename(artist):

    my_dict = {}
    my_dict.update(artist)  # update를 사용하면 사용하지 않는 'external_urls', 'uri'도 들어온다.
    my_dict.pop('external_urls')
    my_dict.pop('uri')  # 그러니까, external_urls와 uri를 pop해서 쓰면 된다.

    return my_dict['id']



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    pprint(artist_info(artist_dict))
