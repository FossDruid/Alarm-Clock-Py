from file_logic import *

file_src_path = "url_src/yt_urls.txt"
whistelisted_urls = "url_src/domain_whitelist.txt"
url_lines = file_opener(file_src_path)

browser_controller(url_lines)
whitelisted_urls_lines = url_whitelist_checker(whistelisted_urls)

url_existance_checker(url_lines)