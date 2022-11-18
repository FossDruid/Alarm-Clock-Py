import webbrowser
import requests

"""
Opens a file and returns its contents
"""
def file_opener(alarm_urls_file_path):
    try:
        print(f'Attempting to open file from given path: {alarm_urls_file_path}…\n')
        with open(alarm_urls_file_path) as file_src:
            lines = file_src.readlines()
            print(f'File of path: {alarm_urls_file_path} opened successfully!')
            return lines

    except Exception as e:
        print(f'Oops! Error has occured: {e}. \n File not found, check your filepath. \n')
        return 0

"""
Checks if given url is allowed according to the values set -
line by line in the domain_whistelist.txt file.
Implement regex later
"""
def url_whitelist_checker(whitelisted_urls_file_path):
    try:
        whitelisted_sites_lines = file_opener(whitelisted_urls_file_path)
        print(whitelisted_sites)
        return whitelisted_sites_lines
    except Exception as e:
        print(f'Given url of ')

"""
This function requests to see if it gets a response in order to check -
its legitamacy
!- Uses index for now
"""
def url_existance_checker(url_from_file):
    # Refering to url with index for now.   Change later
    try:
        response = requests.head(url_from_file[0])
    except Exception as e:
        print(f"NOT OK: {str(e)}")
    else:
        if response.status_code == 200:
            print(f"OK.  Sucessfully connected to url of: {url_from_file[0]}")
        else:
            print(f"Failed to connect to url of: {url_from_file[0]}. \n NOT OK: HTTP response code {response.status_code}")

"""
This function opens your browser with the given url.
!- Uses index for now
"""
def browser_controller(url_from_file):
    try:
        print(f'Opening {webbrowser.get()}')
        webbrowser.open_new(url_from_file[0])
    except Exception as e:
        print(f'Failed to open browser with url: {url_from_file}. \n {e} \n')


#file_opener(file_src_path)