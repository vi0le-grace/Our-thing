from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os









import winreg
from zipfile import ZipFile
import os.path

def get_registry_value(path, name="", start_key = None):
    if isinstance(path, str):
        path = path.split("\\")
    if start_key is None:
        start_key = getattr(winreg, path[0])
        return get_registry_value(path[1:], name, start_key)
    else:
        subkey = path.pop(0)
    with winreg.OpenKey(start_key, subkey) as handle:
        assert handle
        if path:
            return get_registry_value(path, name, handle)
        else:
            desc, i = None, 0
            while not desc or desc[0] != name:
                desc = winreg.EnumValue(handle, i)
                i += i
            return desc[1]


MS_VERSION = get_registry_value(r"HKEY_CURRENT_USER\SOFTWARE\Microsoft\Edge\BLBeacon","version")
print('your edge version is')
print(MS_VERSION)

def update_driver(MS):
    print("downloading the edgedriver for this version")
    import urllib.request
    urllib.request.urlretrieve("https://msedgedriver.azureedge.net//"+str(MS)+"/edgedriver_win32.zip", "edgedriver_win32.zip")


    with ZipFile('edgedriver_win32.zip','r') as zip:
        zip.printdir()
        print("extracting...")
        zip.extractall()
        print("Extracted")

    filen = open(r"C:\ProgramData\msedge_version.txt", 'w+')
    filen.write(MS_VERSION)
    print("ready to go!")

try:
    file = open(r"C:\ProgramData\msedge_version.txt", 'r')
    current_version = file.read()
    current_version = current_version.replace("\n","").replace(" ","")
    print(current_version)
    if str(current_version) == str(MS_VERSION):
        if os.path.isfile( 'msedgedriver.exe'):
            print("driver is upto date and file is in the right place")
        else:
            print("the software might have been reinstalled, thus msedge is not there. Downloading file")
            update_driver(MS_VERSION)

    
    else:
        update_driver(MS_VERSION)
except Exception as i:
    print(i)
    update_driver(MS_VERSION)






























# Set up the Chrome WebDriver
  # Replace with your ChromeDriver path
driver = webdriver.Edge('msedgedriver.exe')

try:
    # Open YouTube
    driver.get("https://www.youtube.com/channel/UCEgdi0XIXXZ-qJOFPf4JSKw")
    print(input("input"))
    time.sleep(3)  # Wait for the page to load

    # Scroll to load more videos (optional, increase range for more scrolling)
    for _ in range(2):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

    # Find video elements
    videos = driver.find_elements(By.XPATH, "//ytd-rich-item-renderer")
    
    
    Amazing_string = ""
    f = open("skeleton.txt",'r')
    Amazing_string = f.read()
    f.close()

    Jojo = Amazing_string


    # Extract video details
    for video in videos:
        try:
            # Video URL
            url_element = video.find_element(By.XPATH, ".//a[@id='thumbnail']")
            video_url = url_element.get_attribute("href")

            # Thumbnail URL
            thumbnail_url = url_element.find_element(By.XPATH, ".//img").get_attribute("src")

            # Video Title
            # title = video.find_element(By.XPATH, ".//a[@id='video-title']").text
            title_element = video.find_element(By.XPATH, ".//yt-formatted-string[@id='video-title']")
            title = title_element.text




            # # Duration
            # duration = video.find_element(By.XPATH, ".//span[@class='ytd-thumbnail-overlay-time-status-renderer']").text
            duration_element = video.find_element(By.XPATH, ".//div[contains(@class, 'badge-shape-wiz__text')]")
            duration = duration_element.text.strip()

            # # Channel Name
            channel_name = video.find_element(By.XPATH, ".//ytd-channel-name").text

            # # Channel Link
            channel_link = video.find_element(By.XPATH, ".//a[@id='avatar-link']").get_attribute("href")

            # # Channel Image
            # channel_image = video.find_element(By.XPATH, "//a[@id='decorated-avatar']/yt-decorated-avatar-view-model/yt-avatar-shape/div/div/div/img").get_attribute("src")
            channel_image_element = video.find_element(By.XPATH, ".//img[contains(@class, 'yt-core-image yt-spec-avatar-shape__image')]")
            channel_image = channel_image_element.get_attribute("src")
            # # Views
            views = video.find_element(By.XPATH, ".//span[contains(text(), 'views')]").text

            # # Released (e.g., how many months ago)
            released = video.find_element(By.XPATH, ".//span[contains(text(), 'ago')]").text

            # Print extracted data












































            if (channel_image != None) and (channel_image != "None"):
                print(f"Video URL: {video_url}")
                print(f"Thumbnail URL: {thumbnail_url}")
                print(f"Title: {title}")
                print(f"Duration: {duration}")
                print(f"Channel Name: {channel_name}")
                print(f"Channel Link: {channel_link}")
                print(f"Channel Image: {channel_image}")
                print(f"Views: {views}")
                print(f"Released: {released}")
                print("-" * 80)


                Amazing_string = Jojo
                Amazing_string = Amazing_string.replace("URLLLL",str(video_url)).replace("THUMBBBBBB",str(thumbnail_url)).replace("TTTTTTT",str(duration)).replace("CCCCCCCC",str(channel_image)).replace("TITTLEEEEE",str(title)).replace("CCCCHAANNNELLLINKKK",channel_link).replace("ccName",channel_name).replace("VVVVVVV",views).replace("DUDUDU",released)

                file = open("data.txt",'a')
                file.write(Amazing_string)
                file.close()

        except Exception as e:
            print(f"Error extracting data for a video: {e}")

finally:
    driver.quit()
