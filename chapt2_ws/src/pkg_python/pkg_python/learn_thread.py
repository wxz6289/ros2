import threading
import requests

class Download:
  def download(self, url, callback):
    print(f"thread {threading.get_ident()} 开始下载 {url}")
    response = requests.get(url)
    response.encoding ="utf-8"
    callback(url, response.text)


  def start(self, url, callback):
    thread = threading.Thread(target=self.download, args=(url, callback))
    thread.start()

def count(url, result):
  print(f"{url}:{len(result)} -> {result[:5]}")

def main():
  down = Download()
  down.start("http://0.0.0.0:8000/nove1.txt", count)
  down.start("http://0.0.0.0:8000/nove2.txt", count)
  down.start("http://0.0.0.0:8000/nove3.txt", count)
  down.start("http://0.0.0.0:8000/nove4.txt", count)


