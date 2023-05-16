import os


def main():
    # 指定 Markdown 文件所在的文件夹路径
    folder_path = os.path.join(os.getcwd(), 'markdowns')
    # 指定合并后的 Markdown 文件路径
    output_file_path = os.path.join(os.getcwd(), 'result.md')

    unsorted_files = os.listdir(folder_path)
    sorted_files = sorted(unsorted_files, key=lambda x: x.split('-')[0])

    for file in sorted_files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'r', encoding='utf-8') as markdown_file:
            print(f'正在处理文件：{file_path}')
            markdown = markdown_file.read()
            with open(output_file_path, 'a', encoding='utf-8') as output_file:
                output_file.write(markdown)
            print(f'处理完成：{file_path}')


if __name__ == '__main__':
    main()
