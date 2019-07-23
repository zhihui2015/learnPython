"""
    作者：郑智慧
    版本：1.0
    日期：2019/07/13
    功能：爬取网页图片资源
"""
import requests as rq
import os

def getHtmlPic(url, root, path):
    """
    获取网页图片资源
    :param url:
    :return:
    """
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = rq.get(url)
            r.raise_for_status()
            with open(path, "wb") as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("文件爬取失败")



if __name__ == "__main__":
    # url_pic = "http://img0.dili360.com/ga/M01/43/98/wKgBy1eF-wmALtAGAEX0Iv2rVVI970.tub.jpg"
    url_video = "https://vd4.bdstatic.com/mda-im5fq8cpdv49eusq/sc/mda-im5fq8cpdv49eusq.mp4"
    root = "C://Users//Aldous//PycharmProjects//webcrawler//videos//"
    path = root + url_video.split('/')[-1]
    getHtmlPic(url_video, root, path)





