def create_youtube_video (title,description):
	youtubevideo={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}
	return youtubevideo
def like (youtubevideo):
	if "likes" in youtubevideo
		youtubevideo["likes"]+=1
	return youtubevideo
def dislike (youtubevideo):
	if "dislikes" in youtubevideo
		youtubevideo["dislikes"]+=1
	return youtubevideo
def add_commment (youtubevideo,username,commenttext):
	if "comments" in youtubevideo:
		youtubevideo["comments"][username]=commenttext

our_dictionary=create_youtube_video("Hasan the great","Hasan beats up Sari Khamis")
print(our_dictionary)
		
