from browsermobproxy import Server
from selenium import webdriver

# Путь к browsermob-proxy
BROWSERMOB_PROXY_PATH = r"C:\Users\favy\Documents\work\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat"

# Запуск серверной части proxy
server = Server(BROWSERMOB_PROXY_PATH, options={'port': 8082})
server.start()
proxy = server.create_proxy()

# Настройка Chrome для работы через прокси
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={proxy.proxy}")

driver = webdriver.Chrome(options=chrome_options)

try:
    # Пример взаимодействия с сайтом через прокси
    proxy.new_har("test_har")
    driver.get("https://www.example.com")
    har_data = proxy.har
    print(har_data)  # Выводим захваченные HTTP-запросы
finally:
    # Корректно останавливаем WebDriver и сервер
    driver.quit()
    server.stop()  # Останавливаем сервер (а не прокси)
    print("BrowserMob Proxy сервер остановлен.")
