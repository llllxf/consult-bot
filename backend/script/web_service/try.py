import requests, json
github_url = "http://openapi.tuling123.com/openapi/api/v2"
data = json.dumps({
	"reqType":0,
    "perception": {
        "inputText": {
            "text": "附近的酒店"
        },
        "inputImage": {
            "url": "imageUrl"
        },
        "selfInfo": {
            "location": {
                "city": "北京",
                "province": "北京",
                "street": "信息路"
            }
        }
    },
    "userInfo": {
        "apiKey": "3e0a308b56c845708e57415e51b77c1b",
        "userId": "504027"
    }
})
kv = {'key1': 'value1'}
r = requests.post(github_url, data)
print(r.json())