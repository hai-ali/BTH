from serpapi import GoogleSearch

basic_params = {
  "engine": "google_maps",
  "q": "Gjensidige Försäkring Sverige",
  "ll": "@59.3347897,18.0582778,17z",
  "type": "search",
  "api_key": "75823d2924f4b495fb5ffff77532f7d8b0eb65b88cb697a4a26b12a296d738e3"
}

review_params = {
  "api_key": "75823d2924f4b495fb5ffff77532f7d8b0eb65b88cb697a4a26b12a296d738e3",
  "engine": "google_maps_reviews",
  "hl": "en",
  "data_id": "0x465f9d4da01ea65d:0x74965e6169608d0c",
  "next_page_token": "CAESBkVnSUlDQQ=="
}

search = GoogleSearch(review_params)
results = search.get_dict()
print(results)

