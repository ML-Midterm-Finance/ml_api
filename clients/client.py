import json
import requests

def url_for(endpoint):
    return 'http://localhost:5000/{}/'.format(endpoint)


def delete_all_daily():
    r = requests.delete(url_for('daily'))
    print("'daily' deleted, server response:", r.status_code)


def post_daily():
    data = [
	{
	"date":"Mon, 7 Oct 2019 00:00:00 GMT",
	"close":230.5
	},	
	{
	"date":"Tue, 8 Oct 2019 00:00:00 GMT",
	"close":230.5
	},
	{
	"date":"Wed, 9 Oct 2019 00:00:00 GMT",
	"pred_close":230.5
	}
    ]

    response = requests.post(
        url_for('daily'),
        json.dumps(data), 
        headers={'Content-Type': 'application/json'}
    )
    print("'daily' posted, server response:", response.status_code)


def get_daily():
    r = requests.get(url_for('daily'))
    print('daily downloaded, server response:', r.status_code)

    if r.status_code == 200:
        daily = r.json()['_items']
        print('{} daily:'.format(len(daily)))
        for day in daily:
            print('{}, {}'.format(day['date'], day['_id']))


def main():
    delete_all_daily()
    post_daily()
    get_daily()

if __name__ == '__main__':
    main()