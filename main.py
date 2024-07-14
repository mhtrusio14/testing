import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': 'usprivacy=1YNY; _lc2_fpi=645e522c6bb7--01h5mr91esxpbc2x36s0st91n6; ac_cclang=; _au_1d=AU1D-0100-001689692442-4OMBMU2U-FSVP; _ga=GA1.1.134809738.1665724138; cto_bundle=uf8f3V95YWxoQ1dMSURxVDlzTldWejJESWNpMVJLMEltbEpKVnRpUmFpaW5kd0ZPNGNIanBxc2tLcG1GSU9TeEk3SWZOVzZSTDB5dXM3WFZNb3VRbmN1WkRZcVFPRThrU0hEOU1wSFRKaVMxc2FUelBQb2tCSzNGYVR3JTJGaEF0JTJCcWhkRXRJJTJGTERmNmJwSTklMkJUbTJnN3MzSU9mQSUzRCUzRA; cto_bidid=qVwEml9POGpNSWhTNU93dEdVWkFQOThZTHgzRmNGc1FscGJGc2praW05Zll3MHAlMkZlcHBrSyUyQnJjMmg1JTJGSXhZd3gzc2pDd2FuJTJCNHo3WGYwbUlWTUxMT2pxbmVQTWo2UVhQcjIyQ1VEYUh1M3FTSXdZJTNE; _au_last_seen_pixels=eyJhcG4iOjE2OTQzOTU2OTksInR0ZCI6MTY5NDM5NTY5OSwicHViIjoxNjk0Mzk1Njk5LCJydWIiOjE2OTQzOTU2OTksInRhcGFkIjoxNjk0Mzk1Njk5LCJhZHgiOjE2OTQzOTU2OTksImdvbyI6MTY5NDM5NTY5OSwiY29sb3NzdXMiOjE2OTQzOTU2OTksImFkbyI6MTY5NDM5NTcxMywicHBudCI6MTY5NDM5NTY5OSwiYmVlcyI6MTY5NDM5NTY5OSwidW5ydWx5IjoxNjk0Mzk1NzEzLCJvcGVueCI6MTY5NDM5NTcxMywic29uIjoxNjk0Mzk1NzEzLCJzbWFydCI6MTY5NDM5NTcxMywiaW1wciI6MTY5NDM5NTcxMywidGFib29sYSI6MTY5NDM5NTcxMywiYW1vIjoxNjk0Mzk1NzEzfQ%3D%3D; __gads=ID=0a72b0f3c8b200d1:T=1689692441:RT=1694396002:S=ALNI_Ma6DOftkL75f4EwXbjbTERmqJ-m0g; __gpi=UID=00000ccd45cf75f5:T=1689692441:RT=1694396002:S=ALNI_MZbLdoKvrzLB1rQiRJI35jpwbV0EQ; connectId=%7B%22vmuid%22%3A%221lDUxYsgpyOfxs-X7oPTH9cy7VBYMj1HGaGNPRlt3xocIySV2nQqBmVPfJeeCfL5DUKMRTxmSXyVDnDIuCNikg%22%2C%22connectid%22%3A%221lDUxYsgpyOfxs-X7oPTH9cy7VBYMj1HGaGNPRlt3xocIySV2nQqBmVPfJeeCfL5DUKMRTxmSXyVDnDIuCNikg%22%2C%22connectId%22%3A%221lDUxYsgpyOfxs-X7oPTH9cy7VBYMj1HGaGNPRlt3xocIySV2nQqBmVPfJeeCfL5DUKMRTxmSXyVDnDIuCNikg%22%2C%22ttl%22%3A24%2C%22he%22%3A%2258e43a51598a669005f2bf8329ca8b8cead97e11ac7cb04f3e76f18980562219%22%2C%22puid%22%3A%22ce4c7015-c264-4f39-942d-6899706180ab%22%2C%22lastSynced%22%3A1693584008613%2C%22lastUsed%22%3A1694396040148%7D; _ga=GA1.2.134809738.1665724138; _ga_FRKLFRC9TX=GS1.2.1695000375.45.0.1695000375.0.0.0; _ga_DCD7QPW0Z2=GS1.1.1695000374.386.1.1695000387.47.0.0; csrftoken=99G9VDcjy0HHHDGE4nltcipkP1GtDY3w; sessionid=egqx8lzhsp2dqcul2ac9sl5vtmyv0ct3; _cfuvid=FkZv5UaYMWCn0QqBfJiDtYtfxj2uYRrs_L7OXizfhd0-1720926635013-0.0.1.1-604800000; cf_clearance=mbHUPXwO_Fs7KfEUISxsNQ5r25SoBf7brmgj.7OqHRI-1720926638-1.0.1.1-WLR4Mt2oZbZgxmYxMs5742nYWGaegtqzgIm0fNXXh7SzZSCnlX4kMBDdGHPPdMwrYP5GMZG3_HvKH4z95707og; __cf_bm=32aE77dgY_V1AJymclMehek.Ly3cPHcHBXIfu6qGr9k-1720928109-1.0.1.1-3Cm3odgjz_abSV1UAzPoZR1.I5jyUZyuXKnsXKOzLxO0d1D33W2V4ngq89u7HR8cq.JQH7e4hH9P9FmLYCHqoQ',
    'Priority': 'u=0, i',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://www.mut.gg/api/mutdb/prices/24-57202575/playstation-5/', headers=headers)

print(response.status_code)
print(response.request.headers)
