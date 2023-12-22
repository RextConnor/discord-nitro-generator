import requests

textfile = 'dump.txt'
myrespectformyself = 0

def gen11():
    global myrespectformyself
    while myrespectformyself != 100:
        url = "https://api.discord.gx.games/v1/direct-fulfillment"
        headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "sec-ch-ua": "\"Opera GX\";v=\"105\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "referrer": "https://www.opera.com/",
            "referrerPolicy": "strict-origin-when-cross-origin",
        }

        payload = {
            "partnerUserId": "3f09dc24-aa93-43f9-9053-3c9ae2bab3e4"
        }

        try:
            response = requests.post(url=url, headers=headers, json=payload)
            response.raise_for_status()  

            kal = response.text

            with open(textfile, 'a+') as file: 
                iz = kal.replace('{', '').replace('}', '').replace('"', '').replace('token', '').replace(':', '')

                
                gg = "https://discord.com/billing/partner-promotions/1180231712274387113/" + iz
                file.write(gg + '\n')

            print(gg)

        except requests.exceptions.RequestException:
            
            pass

        myrespectformyself += 1
        

gen11()


#made by rext connor