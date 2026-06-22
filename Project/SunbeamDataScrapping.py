import requests

# GET request and get the data.
url = "https://api.sunbeaminfo.in/api/v1/courses?page=1&limit=100&domain=sunbeaminfo.in"
response = requests.get(url)
resp = response.json()
if resp["success"]:
    data = resp["data"]
    for course in data:
        slug = course["slug"]
        print(course["name"])
        course_url = f"https://api.sunbeaminfo.in/api/v1/courses/{slug}?domain=sunbeaminfo.in"
        response = requests.get(url)
        resp = response.json()
        print(resp)
        print("---" * 30)        
else:
    print("Failed to Request")