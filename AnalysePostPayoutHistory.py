from piston import Steem
import time
from datetime import datetime, timedelta

def feed():
    steem = Steem()    

    url = "/@eroche/where-have-all-the-votes-gone"
    
    text_file = open("voting_history.txt","w")

    text_file.write("Post: %s\n" %url + "Began Recording at " + datetime.utcnow().strftime("%H:%M:%S") + "\n############################\n")

    end_time = datetime.utcnow() + timedelta(minutes=1)    

    #Finish Script after 60 seconds,
    #you could set this to 2 hours or 5 hours to track a post over a longer time
    t_end = time.time() + 60 * 5

    #Loop and every 10 seconds print the value of the post to a file
    while time.time() < t_end:
        print("Running...")
        text_file.write(datetime.utcnow().strftime("%H:%M:%S")  + "\t")
        text_file.write("%f" %steem.get_post(url)["pending_payout_value"] + "\n")
        time.sleep(10)
    
    #When the program has finished running save and close the file
    text_file.close()
        
if __name__ == "__main__":
    feed()
 
