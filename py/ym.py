import requests
import json

reqList="https://appapi2.gamersky.com/v5/getCMSNewsList"
reqParams= {
  "app":"GSAPP",
  "deviceType":"Redmi 6",
  "appVersion":"5.5.22",
  "os":"android",
  "osVersion":"9",
  "deviceId":"862622048437469",
  "request":{
    "modelFieldNames":"Title,Author,ThumbnailsPicUrl,updateTime,mark",
    "tagIds":"",
    "pageSize":20,
    "cacheMinutes":1,
    "tags":"动态图",
    "recommendedIndex":0,
    "nodeIds":"",
    "systemFieldNames":"DefaultPicUrl",
    "pageIndex":1,
    "UpdateTime":0,
    "topicIds":"",
    "GameLib":"0",
    "order":"timeDesc"
  }
}
img_list = []

def get_list(pageIndex=1,write=0):
  reqParams['request']['pageIndex'] = pageIndex
  res = requests.post(reqList,json=reqParams,headers={'Content-Type':'chartset="utf-8"'})
  result = res.json()
  # print(res.apparent_encoding)
  if write > 0:
    res.encoding='utf-8'
    return res.text
  else:
    return result

# 写入 json 数据文件
def write_json():
  page_num = 1
  while page_num < 4:
    back_data = get_list(page_num,1)
    name = "list"+ str(page_num) +".json"
    filename = "../data/ym/"+ name
    with open(filename, "w+",encoding="utf-8") as f:
        f.write(back_data)
        f.close()
    page_num += 1
  return

# 获取图片链接
def get_img_src():
  page_num = 1
  while page_num < 2:
    name = "list"+ str(page_num) +".json"
    filename = "../data/ym/"+ name
    with open(filename, "r",encoding="utf-8") as f:
        content = f.read()
        # print(content)
        data_dict = json.loads(content)
        result = data_dict['result']
        result_index = 0
        result_len = len(result)
        while result_index < result_index:
          result_item = result[result_index]
          img_list.append(result_item['thumbnails'][0])
          result_index += 1
        f.close()
    page_num += 1
  print(img_list)
  return

# 分析获取的 JSON 数据，获得图片
def down_img():
  img_index = 0
  img_len = len(img_list)
  while img_index < img_len:
    img_item = img_list[img_index]
    img_item_arr = img_item.split('/')
    img_arr_len = len(img_item_arr)
    filename = "../ym/cover/"+ img_item_arr[img_arr_len-1]
    res = requests.get(img_item)
    with open(filename, "wb") as f:
        f.write(res.content)
        print(img_index + filename + 'down success')
        f.close()
    img_index += 1
  return


# 获取列表数据
# write_json()

# 下载图片
get_img_src()
down_img()

print('all done')