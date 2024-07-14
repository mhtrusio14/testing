import requests

cookies = {
    'usprivacy': '1YNY',
    '_lc2_fpi': '645e522c6bb7--01h5mr91esxpbc2x36s0st91n6',
    'ac_cclang': '',
    '_cc_id': 'c1833f94235a36bcb924703421ce913e',
    '_au_1d': 'AU1D-0100-001689692442-4OMBMU2U-FSVP',
    '_ga': 'GA1.1.134809738.1665724138',
    'cto_bundle': 'uf8f3V95YWxoQ1dMSURxVDlzTldWejJESWNpMVJLMEltbEpKVnRpUmFpaW5kd0ZPNGNIanBxc2tLcG1GSU9TeEk3SWZOVzZSTDB5dXM3WFZNb3VRbmN1WkRZcVFPRThrU0hEOU1wSFRKaVMxc2FUelBQb2tCSzNGYVR3JTJGaEF0JTJCcWhkRXRJJTJGTERmNmJwSTklMkJUbTJnN3MzSU9mQSUzRCUzRA',
    'cto_bidid': 'qVwEml9POGpNSWhTNU93dEdVWkFQOThZTHgzRmNGc1FscGJGc2praW05Zll3MHAlMkZlcHBrSyUyQnJjMmg1JTJGSXhZd3gzc2pDd2FuJTJCNHo3WGYwbUlWTUxMT2pxbmVQTWo2UVhQcjIyQ1VEYUh1M3FTSXdZJTNE',
    '_au_last_seen_pixels': 'eyJhcG4iOjE2OTQzOTU2OTksInR0ZCI6MTY5NDM5NTY5OSwicHViIjoxNjk0Mzk1Njk5LCJydWIiOjE2OTQzOTU2OTksInRhcGFkIjoxNjk0Mzk1Njk5LCJhZHgiOjE2OTQzOTU2OTksImdvbyI6MTY5NDM5NTY5OSwiY29sb3NzdXMiOjE2OTQzOTU2OTksImFkbyI6MTY5NDM5NTcxMywicHBudCI6MTY5NDM5NTY5OSwiYmVlcyI6MTY5NDM5NTY5OSwidW5ydWx5IjoxNjk0Mzk1NzEzLCJvcGVueCI6MTY5NDM5NTcxMywic29uIjoxNjk0Mzk1NzEzLCJzbWFydCI6MTY5NDM5NTcxMywiaW1wciI6MTY5NDM5NTcxMywidGFib29sYSI6MTY5NDM5NTcxMywiYW1vIjoxNjk0Mzk1NzEzfQ%3D%3D',
    '__gads': 'ID=0a72b0f3c8b200d1:T=1689692441:RT=1694396002:S=ALNI_Ma6DOftkL75f4EwXbjbTERmqJ-m0g',
    '__gpi': 'UID=00000ccd45cf75f5:T=1689692441:RT=1694396002:S=ALNI_MZbLdoKvrzLB1rQiRJI35jpwbV0EQ',
    'connectId': '%7B%22vmuid%22%3A%221lDUxYsgpyOfxs-X7oPTH9cy7VBYMj1HGaGNPRlt3xocIySV2nQqBmVPfJeeCfL5DUKMRTxmSXyVDnDIuCNikg%22%2C%22connectid%22%3A%221lDUxYsgpyOfxs-X7oPTH9cy7VBYMj1HGaGNPRlt3xocIySV2nQqBmVPfJeeCfL5DUKMRTxmSXyVDnDIuCNikg%22%2C%22connectId%22%3A%221lDUxYsgpyOfxs-X7oPTH9cy7VBYMj1HGaGNPRlt3xocIySV2nQqBmVPfJeeCfL5DUKMRTxmSXyVDnDIuCNikg%22%2C%22ttl%22%3A24%2C%22he%22%3A%2258e43a51598a669005f2bf8329ca8b8cead97e11ac7cb04f3e76f18980562219%22%2C%22puid%22%3A%22ce4c7015-c264-4f39-942d-6899706180ab%22%2C%22lastSynced%22%3A1693584008613%2C%22lastUsed%22%3A1694396040148%7D',
    '_ga': 'GA1.2.134809738.1665724138',
    '_ga_FRKLFRC9TX': 'GS1.2.1695000375.45.0.1695000375.0.0.0',
    '_ga_DCD7QPW0Z2': 'GS1.1.1695000374.386.1.1695000387.47.0.0',
    'cf_clearance': 'hACs37YY7sXaSLpc.1mRlI95nx2D5zOGsgJpdId1rQ8-1712852035-1.0.1.1-Goi9arnXYe8v3Rme5tXBgmb4Zlfd3IauKqwdbwphou3wttXuaaVMsm3Id953amgDkknr_0ggN_YLtOTvkWxsKQ',
    '__cf_bm': 'vbzm9228IH0v2dtmmKb7Jwzb5oH2Tj38dDm4C_VzmII-1717347387-1.0.1.1-yKT21DUq3d3jh5FJ1VuaEZsHZeIxaTJUahSwkJWqLOplhInSLj0Im0fa4w6.842Yx9r.dLMthdTU2uPY6B9R5g',
    '_cfuvid': 'PFyuX1s.rDrx.x.F7u_PCPDqh8TygO8r6uHNqOuw59k-1717347387745-0.0.1.1-604800000',
    'messages': 'W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgTWFkZGVuU2V0R3VpZGUuIiwiIl1d:1sDoVZ:akixZ7bpOliVgvUBnWqWgXoq2vQ9OP2CduD6MFB3FXw',
    'csrftoken': 'Ew2ShcWfIVRza604xy9Skzk1iWaLnw29',
    'sessionid': 'j2ap9lnislvyh0utukxfx7gejopi07d2',
    'cf_clearance': 'mAQ4nJfQuiq0vqltIVuauKb_Lektb1ezz9lkfKQhDdk-1717347398-1.0.1.1-BgRnm7z24dUqQCF5jClqBUv2JHpSmAIfU6z04l_z.5Zp1XjuTWmGIzQuXJ3EaQziT6vs4vNtbiHS58EmnZJAdw',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'usprivacy=1YNY; _lc2_fpi=645e522c6bb7--01h5mr91esxpbc2x36s0st91n6; ac_cclang=; _cc_id=c1833f94235a36bcb924703421ce913e; _au_1d=AU1D-0100-001689692442-4OMBMU2U-FSVP; _ga=GA1.1.134809738.1665724138; cto_bundle=uf8f3V95YWxoQ1dMSURxVDlzTldWejJESWNpMVJLMEltbEpKVnRpUmFpaW5kd0ZPNGNIanBxc2tLcG1GSU9TeEk3SWZOVzZSTDB5dXM3WFZNb3VRbmN1WkRZcVFPRThrU0hEOU1wSFRKaVMxc2FUelBQb2tCSzNGYVR3JTJGaEF0JTJCcWhkRXRJJTJGTERmNmJwSTklMkJUbTJnN3MzSU9mQSUzRCUzRA; cto_bidid=qVwEml9POGpNSWhTNU93dEdVWkFQOThZTHgzRmNGc1FscGJGc2praW05Zll3MHAlMkZlcHBrSyUyQnJjMmg1JTJGSXhZd3gzc2pDd2FuJTJCNHo3WGYwbUlWTUxMT2pxbmVQTWo2UVhQcjIyQ1VEYUh1M3FTSXdZJTNE; _au_last_seen_pixels=eyJhcG4iOjE2OTQzOTU2OTksInR0ZCI6MTY5NDM5NTY5OSwicHViIjoxNjk0Mzk1Njk5LCJydWIiOjE2OTQzOTU2OTksInRhcGFkIjoxNjk0Mzk1Njk5LCJhZHgiOjE2OTQzOTU2OTksImdvbyI6MTY5NDM5NTY5OSwiY29sb3NzdXMiOjE2OTQzOTU2OTksImFkbyI6MTY5NDM5NTcxMywicHBudCI6MTY5NDM5NTY5OSwiYmVlcyI6MTY5NDM5NTY5OSwidW5ydWx5IjoxNjk0Mzk1NzEzLCJvcGVueCI6MTY5NDM5NTcxMywic29uIjoxNjk0Mzk1NzEzLCJzbWFydCI6MTY5NDM5NTcxMywiaW1wciI6MTY5NDM5NTcxMywidGFib29sYSI6MTY5NDM5NTcxMywiYW1vIjoxNjk0Mzk1NzEzfQ%3D%3D; __gads=ID=0a72b0f3c8b200d1:T=1689692441:RT=1694396002:S=ALNI_Ma6DOftkL75f4EwXbjbTERmqJ-m0g; __gpi=UID=00000ccd45cf75f5:T=1689692441:RT=1694396002:S=ALNI_MZbLdoKvrzLB1rQiRJI35jpwbV0EQ; connectId=%7B%22vmuid%22%3A%221lDUxYsgpyOfxs-X7oPTH9cy7VBYMj1HGaGNPRlt3xocIySV2nQqBmVPfJeeCfL5DUKMRTxmSXyVDnDIuCNikg%22%2C%22connectid%22%3A%221lDUxYsgpyOfxs-X7oPTH9cy7VBYMj1HGaGNPRlt3xocIySV2nQqBmVPfJeeCfL5DUKMRTxmSXyVDnDIuCNikg%22%2C%22connectId%22%3A%221lDUxYsgpyOfxs-X7oPTH9cy7VBYMj1HGaGNPRlt3xocIySV2nQqBmVPfJeeCfL5DUKMRTxmSXyVDnDIuCNikg%22%2C%22ttl%22%3A24%2C%22he%22%3A%2258e43a51598a669005f2bf8329ca8b8cead97e11ac7cb04f3e76f18980562219%22%2C%22puid%22%3A%22ce4c7015-c264-4f39-942d-6899706180ab%22%2C%22lastSynced%22%3A1693584008613%2C%22lastUsed%22%3A1694396040148%7D; _ga=GA1.2.134809738.1665724138; _ga_FRKLFRC9TX=GS1.2.1695000375.45.0.1695000375.0.0.0; _ga_DCD7QPW0Z2=GS1.1.1695000374.386.1.1695000387.47.0.0; cf_clearance=hACs37YY7sXaSLpc.1mRlI95nx2D5zOGsgJpdId1rQ8-1712852035-1.0.1.1-Goi9arnXYe8v3Rme5tXBgmb4Zlfd3IauKqwdbwphou3wttXuaaVMsm3Id953amgDkknr_0ggN_YLtOTvkWxsKQ; __cf_bm=vbzm9228IH0v2dtmmKb7Jwzb5oH2Tj38dDm4C_VzmII-1717347387-1.0.1.1-yKT21DUq3d3jh5FJ1VuaEZsHZeIxaTJUahSwkJWqLOplhInSLj0Im0fa4w6.842Yx9r.dLMthdTU2uPY6B9R5g; _cfuvid=PFyuX1s.rDrx.x.F7u_PCPDqh8TygO8r6uHNqOuw59k-1717347387745-0.0.1.1-604800000; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgTWFkZGVuU2V0R3VpZGUuIiwiIl1d:1sDoVZ:akixZ7bpOliVgvUBnWqWgXoq2vQ9OP2CduD6MFB3FXw; csrftoken=Ew2ShcWfIVRza604xy9Skzk1iWaLnw29; sessionid=j2ap9lnislvyh0utukxfx7gejopi07d2; cf_clearance=mAQ4nJfQuiq0vqltIVuauKb_Lektb1ezz9lkfKQhDdk-1717347398-1.0.1.1-BgRnm7z24dUqQCF5jClqBUv2JHpSmAIfU6z04l_z.5Zp1XjuTWmGIzQuXJ3EaQziT6vs4vNtbiHS58EmnZJAdw',
    'if-modified-since': 'Sun, 02 Jun 2024 17:03:21 GMT',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

response = requests.get('https://www.mut.gg/api/mutdb/prices/24-57202575/playstation-5/')
print(response.status_code)
