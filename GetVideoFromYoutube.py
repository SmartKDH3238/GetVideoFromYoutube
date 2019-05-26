# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:33:08 2019

@author: SmartKDH3238
"""

from pytube import YouTube
import time

def lobby():
    caution = '''만약 영상이 다운로드 되지 않는다면, 암호화 문제에요 lol\n'''
    print(caution)
    url = input("\nURL 주소를 입력해주세요 : ")
    file_adress = list(input("\n원하는 파일 주소를 입력해주세요(만약 입력하지 않으면 현재 파일에 다운로드 됩니다 + 상대경로 사용 가능합니다.) : "))
    
    # 파일 주소 수정
    if file_adress == True:
        idx = 0
        for i in file_adress:
            if i == '\\':
                file_adress[idx] = '/'
            idx += 1
    
    return url, ''.join(file_adress)

def get_media(url, file_route):
    # Youtube
    media = YouTube(url)
    
    # 영상 제목
    media_title = list(media.title)
    # 윈도우에서 사용 불가능한 파일 이름 문자 제외
    for i in range(0, len(media_title)):
        if media_title[i] in ['\\', '//', '?', '*', '>', '<', ':', '|', '\"']:
            media_title[i] = '_'
    media_title = ''.join(media_title)
    
    # media_views = str(media.views)
    media_description = str(media.description)
    media_length = str(media.length)  # 초 단위
    
    #    해당 영상 스트림 가져오기 | 프로그레시브 방식의 인코딩, 파일 포맷은 MP4 | 해상도 순 정렬  |  내림차순 | 첫 번째 | 다운로드      |     파일 경로        |      파일 명
    media.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path = file_route , filename = media_title , filename_prefix = None)
    
    media_information = '\n\nTitle : \n' + media_title + '\n\nDescription : \n' + media_description + '\n\nLenngth(s)\n:' + media_length + '\n'
    print(media_information)
    print('Successed!')

def main():
    # inf[0] : 동영상 url inf[1] : 파일 주소
    inf = lobby()
    get_media(inf[0], inf[1])
    
    print("\n이 화면은 100초 뒤 자동으로 꺼집니다.")
    time.sleep(100)

if __name__ == '__main__':
    main()
