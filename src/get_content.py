import time
import os
import requests

# 从文件中读取URL列表，并使用set去除重复
with open('links.txt', 'r', encoding='utf-8') as file:
    urls = set(url.strip() for url in file.readlines())

target_directory = os.path.join(os.getcwd(), 'articles')

if not os.path.exists(target_directory):
    os.mkdir(target_directory)

# 对每个URL进行处理
for url in urls:
    article_id = 'post-' + \
        url.split('/')[-1].split('.')[0]  # 从URL获取文章ID
    url = 'https://web.archive.org/web/' + url
    attempts = 0
    max_attempts = 100  # 设定最大尝试次数，防止无限循环
    while attempts < max_attempts:
        try:
            # 发送请求获取网页内容
            response = requests.get(url, timeout=1000, allow_redirects=True)

            # 确保重定向完成后再获取内容
            if response.history:
                final_url = response.url
                print("最终URL:", final_url)
                content = response.content
                # 处理获取到的内容
            else:
                print("无重定向")

            text = content.decode('utf-8')

            if text is not None:
                # 获取文章内容
                article_content = text
                target_file = os.path.join(
                    target_directory, f'{article_id}.html')

                # 创建一个文件来保存文章内容
                with open(target_file, 'w', encoding='utf-8') as file:
                    file.write(article_content)

                print(f'Successfully saved: {article_id}.html')
                break  # 成功获取到文章内容，跳出循环
            print('Article not found for URL:', url)
            attempts += 1
            time.sleep(5)  # 等待5秒后再次尝试
        except Exception as err:
            print(f'Error occurred while fetching URL {url}: {str(err)}')
            attempts += 1
            time.sleep(5)  # 如果出现错误，等待5秒后再次尝试
    time.sleep(5)  # 每次循环结束后，等待5秒再进行下一次循环
