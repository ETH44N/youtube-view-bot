from threading import Thread
import requests

class getInfo():

    def getProxyFile(self):
        self.proxyFile = input('Proxy file name -> ')
        if '.txt' in self.proxyFile:
            pass
        else:
            self.proxyFile = f'{self.proxyFile}.txt'

    def filterProxies(self):

        self.valideProxies = []

        with open(self.proxyFile, 'r') as proxyFile:
            FileContent = proxyFile.read()
            proxyList = FileContent.split('\n')
            proxyFile.close()

        def filterProxie(proxy, i):
            proxies = {"http": f"http://{proxyList[i]}","https": f"https://{proxyList[i]}"}
            try:
                r = requests.get("https://api.ipify.org/", proxies=proxies, timeout=3)
                if r.ok:
                    self.valideProxies.append(proxy)
                    print(f"{proxy} valid num : {i}")
            except:
                pass

        for i in range(len(proxyList)):
            thread = Thread(target=filterProxie, args=(proxyList[i],i,))
            thread.start()

    def saveValidProxies(self):
        input('Enter to save proxies...')
        with open('validProxies.txt', 'w') as truncateFile:
            truncateFile.write('')
            truncateFile.close()
        with open('validProxies.txt', 'a+') as ValidProxiesFile:
            for proxie in self.valideProxies:
                ValidProxiesFile.write(f"{proxie}\n")
            ValidProxiesFile.close()


def start():
    user = getInfo()
    user.getProxyFile()
    user.filterProxies()
    user.saveValidProxies()

if __name__ == '__main__':
    start()
