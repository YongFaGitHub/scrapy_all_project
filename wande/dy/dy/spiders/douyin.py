# -*- coding: utf-8 -*-
import scrapy
import json
from copy import deepcopy
from dy.items import DyItem
class DouyinSpider(scrapy.Spider):
    name = 'douyin'
    allowed_domains = ['douyin.com']
    start_urls = ['https://www.douyin.com/aweme/v1/aweme/post/?user_id={}&count=21&max_cursor=0&aid=1128'.format("58261954390")]
    # 58261954390

    def start_requests(self):
        # self.user_id = input("Please Input User_Id:")
        self.user_id = 58261954390
        # 58261954390

        urls = 'https://www.douyin.com/aweme/v1/aweme/post/?user_id={}&count=21&max_cursor=0&aid=1128'.format(self.user_id)
        yield scrapy.Request(
            urls,
            callback=self.parse,

        )

    def parse(self, response):
        item = DyItem()
        j_shuju = response.xpath("//body//text()").extract_first()
        dict_shuju = json.loads(j_shuju)
        if dict_shuju["max_cursor"] != 0:
            for content in dict_shuju["aweme_list"]:
                # 播放量
                item["play_count"] = content["statistics"]["play_count"]
                # 评论量
                item["comment_count"] = content["statistics"]["comment_count"]
                # 转发数
                item["share_count"] = content["statistics"]["share_count"]
                # 点赞量
                item["digg_count"] = content["statistics"]["digg_count"]
                # 歌名
                item["music_name"] = content["music"]["music_name"]
                # 作者名
                item["author"] = content["author"]["nickname"]
                # 作者id
                item["author_id"] = content["author"]["unique_id"]
                item["desc"] = content["desc"]
                item["video_addr"] = content["video"]["play_addr"]["url_list"][0]
                yield scrapy.Request(
                    item["video_addr"],
                    callback=self.download,
                    dont_filter=True,
                    meta={"item":deepcopy(item)}
                )
                # 下一页
                next_url = "https://www.douyin.com/aweme/v1/aweme/post/?user_id={}&count=21&max_cursor={}&aid=1128".format(self.user_id,dict_shuju["max_cursor"])
                yield scrapy.Request(
                    next_url,
                    callback=self.parse,
                    meta={"item":deepcopy(item)}

                )
    def download(self,response):
        item=response.meta["item"]
        print("---------")
        print("现在正在下载:",item["music_name"])
        print("地址：",item["video_addr"])
        with open("./{}_{}.mp4".format(item["author"],item["music_name"]),"ab")as f:
            f.write(response.body)
        yield item

# verify=False,