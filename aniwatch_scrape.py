import requests
import json

# now that aniwatch is dead, here is an example of how one would scrape from it

session = requests.session()
throwaway = session.get("https://aniwatch.me/")



url = 'https://aniwatch.me/api/ajax/APIHandle'


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36", 'X-PATH':'/anime/2118', 'X-XSRF-TOKEN': '12d83aaffc0faddd04c64e4cfbf6b1de', 'X-AUTH': 'NmhqQkpRMFQ3OEJORmVvQzZnMWZvdz09'}

cookies = {'SESSION':'%7B%22userid%22%3A657638%2C%22username%22%3A%22zxzx%22%2C%22usergroup%22%3A4%2C%22player_lang%22%3A1%2C%22player_quality%22%3A0%2C%22player_time_left_side%22%3A2%2C%22player_time_right_side%22%3A3%2C%22screen_orientation%22%3A1%2C%22nsfw%22%3A1%2C%22chrLogging%22%3A1%2C%22mask_episode_info%22%3A0%2C%22blur_thumbnails%22%3A0%2C%22autoplay%22%3A1%2C%22preview_thumbnails%22%3A1%2C%22update_watchlist%22%3A1%2C%22update_watchlist_notification%22%3A1%2C%22playheads%22%3A1%2C%22hide_chat%22%3A0%2C%22seek_time%22%3A5%2C%22update_watchlist_percentage%22%3A80%2C%22use_24h_clock%22%3A0%2C%22use_light_intro%22%3A0%2C%22manage_idle_tabs%22%3A0%2C%22cover%22%3Anull%2C%22title%22%3A%22Member%22%2C%22premium%22%3A1%2C%22lang%22%3A%22en-US%22%2C%22auth%22%3A%22NmhqQkpRMFQ3OEJORmVvQzZnMWZvdz09%22%2C%22remember_login%22%3Atrue%7D', 'LANGUAGE':'en-US', 'XSRF-TOKEN':'12d83aaffc0faddd04c64e4cfbf6b1de'}

cookies.update(dict(session.cookies))
data = {"controller":"Anime","action":"getEpisodes","detail_id":"2118"}
jsonData = json.dumps(data)
#print(cookies)
#print(jsonData)

obj = session.get(url, cookies=cookies, data=jsonData, headers=headers)
print(obj.text)
