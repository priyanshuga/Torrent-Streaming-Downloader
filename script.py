import requests
import subprocess
import sys

def main():
    movie_name = input("Enter the name of the movie which you want to stream\n")
    base_url = f"https://api.sumanjay.cf/torrent/?query={movie_name}"

    torrent_results = requests.get(base_url).json()

    index = 1
    magnet = []
    for result in torrent_results:
        if 'movie' in result['type'].lower():
            print(index,") ",result['name'],"-->",result['size'])
            index+=1
            magnet.append(result['magnet'])

    print("\n\n")

    choice = int(input("Enter the index of the movie which you want to use\n"))
    magnet_link = magnet[choice-1]

    download = False

    stream_choice = int(input("Press 1 to stream or Press 2 to download the movie\n"))
    if stream_choice == 1:
        download = False
    elif stream_choice == 2:
        download = True
    else:
        print('Something went wrong\n Exiting...')

    handler(magnet_link,download)

def handler(magnet_link,download):
    cmd = []
    cmd.append("webtorrent")
    cmd.append(magnet_link)
    if not download:
        cmd.append(' --vlc')

    if sys.platform.startswith('linux'):
        subprocess.call(cmd)
    elif sys.platform.startswith('win32'):
        subprocess.call(cmd,shell=True)


main()


