import webbrowser

#file_src_path = "url_src/yt_urls.txt"

def file_opener(alarm_urls_file_path):
    try:
        print(f'Attempting to open file from given path: {alarm_urls_file_path}…\n')
        with open(alarm_urls_file_path) as file_src:
            lines = file_src.readlines()
            print(f'File of path: {alarm_urls_file_path} opened successfully!')
            return lines

    except Exception as e:
        print(f'Oops! Error has occured: {e}. \n File not found, check your filepath.')
        return 0



def open_url():
    webbrowser 

#file_opener(file_src_path)