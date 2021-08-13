from selenium import webdriver
from pypresence import Presence
from time import sleep 
import threading, colorama
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

if __name__ == "__main__":
    with open('windows.txt', 'w') as f:
        f.write(f"{int(0)}")
        f.close()
    rpc = Presence("716758564068392971")
    rpc.connect()
    rpc.update(state="YOUTUBE VIEW BOT",large_text="By ETH4N",small_text="Online")

class getInfo():

    def getProxies(self):
        self.validProxyFile = str(input('Valid Proxies File ->'))
        if ".txt" in self.validProxyFile:
            pass
        else:
            self.validProxyFile = f"{self.validProxyFile}.txt"
        with open(self.validProxyFile, 'r') as proxies:
            FileContent = proxies.read()
            proxies.close()
        self.proxyList = FileContent.split('\n')
        print(f'{len(self.proxyList)} proxies on été chargés.')

    def getVideo(self):
        def asking(self):
            self.videoId = input('Youtube vidéo ID => ')
            if len(self.videoId) != 11:
                asking(self)
                print(f"{colorama.Fore.RED} Vidéo ID is invalid...")
            else:
                pass
        asking(self)

    def getWindows(self):
        def asking(self):
            try:
                self.WindowsMax = int(input('How many windows do you want (max = 10) -> '))
                if self.WindowsMax > 10:
                    print(f"{colorama.Fore.RED} 10 max !")
                    asking(self)
                else:
                    pass
            except ValueError:
                print(f"{colorama.Fore.RED} a number is required !")
        asking(self)

    def watchTime(self):
        def asking(self):
            try:
                self.watchtime = int(input('How many watch time do you want (seconds) -> '))
            except ValueError:
                print(f"{colorama.Fore.RED} a number is required !")
                asking(self)

        asking(self)

def makeView(proxy,i,id,watchTime):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--proxy-server=%s' % proxy)
    driver = webdriver.Chrome(executable_path=r'Free/chromedriver.exe', options=chrome_options)
    try:
        driver.get(f'https://youtu.be/{id}')
        if driver.title == "youtu.be":
            driver.close()
            return
        elif driver.title == f"https://www.youtube.com/watch?v={id}&feature=youtu.be":
            driver.close()
            return 
        elif 'YouTube' in driver.title:
            pass

    except WebDriverException:
        driver.close()
        return
    

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'video')))
        print(f'{proxy} has given +1 view')
        watch_video_js = """
           let video = document.querySelector('video')
           video.play()
        """
        driver.execute_script(watch_video_js)
        with open('windows.txt', 'r') as f:
            acctual = f.read()
            f.close()
        with open('windows.txt', 'w') as f:
            f.write(f"{int(acctual) + 1}")
            f.close()
        sleep(watchTime)
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'video')))
        print(f'{proxy} has given +1 view')
        watch_video_js = """
           let video = document.querySelector('video')
           video.muted = true
           video.play()
        """
        driver.execute_script(watch_video_js)
        sleep(watchTime)
        with open('windows.txt', 'r') as f:
            acctual = f.read()
            f.close()
        with open('windows.txt', 'w') as f:
            f.write(f"{int(acctual) - 1}")
            f.close()
        driver.close()
        print(f'{proxy} has finished working')


    except TimeoutException:
        driver.close()
        print(f'{proxy} has some trouble loading video...')


def main(windowsMax, proxyList, video, watchtime):
    for i in range(windowsMax):
        thread = threading.Thread(target=makeView, args=(proxyList[i],i,video, watchtime,))
        thread.start()
        proxyList.remove(proxyList[i])

    while True:
        sleep(watchtime / 1.5)
        with open('windows.txt') as windowsFile:
            num = windowsFile.read()
            num = int(num)
            windowsFile.close()
        if windowsMax > num:
            for i in range((windowsMax - num) * 2):
                thread = threading.Thread(target=makeView, args=(proxyList[i],i,video, watchtime,))
                thread.start()
                proxyList.remove(proxyList[i])
        else:
            pass

user = getInfo()
user.getProxies()
user.getVideo()
user.getWindows()
user.watchTime()

main(user.WindowsMax, user.proxyList, user.videoId, user.watchtime)