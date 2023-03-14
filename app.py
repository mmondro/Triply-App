import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        business_description = request.form["business_description"]
        response_header = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_header_prompt(business_description),
            temperature=0.6,
            max_tokens=512,
        )

        return redirect(url_for("index", result=response_header.choices[0].text.strip(), business_description=business_description))

    result = request.args.get("result")
    result_sub = request.args.get("result_sub")
    result_call = request.args.get("result_call")
    business_description = request.args.get("business_description")
    print(result)
    return render_template("index2.html", result=result, result_sub=result_sub, result_call=result_call, business_description=business_description)





def generate_header_prompt(business_description):
    return """Write the perfect 3-day itinerary.

Pretend you are the world's best trip advisor and I have hired you to plan my trip. You will use the text that I give you as a reference for the trip. This text will include the location, duration of the trip, who I am traveling with, and the style of the trip Here is the information you will need to plan the trip.

Hotels, flights, and transportation have already been taken care of. I simply want to plan the most fun trip and take the most advantage of my time while I'm there.

I am taking the trip to eat good food, find unique things to do, see beautiful sights, and go to extraordinary events. It should be a trip of a lifetime and jam-packed with things to do.

Help me craft the perfect trip. Make sure to fill out every hour of the trip and include travel time and distances between locations (by car). Be descriptive of each activity and make sure to include a name and location so it is easier to search later. describe in luscious detail each stop on the trip, but keep it to one sentence. In a table, list out all the locations where we would need to make a reservation and the costs associated with each location. Column one should be all the locations that need to make reservations and column two should be the estimated prices associated with each location. Even if you don't know the price of things makes an estimate based on the activity. And at the end of the list total up all of column two for a total budget for activities.



Here is the input:  {}
Trip Info:""".format(
        business_description.capitalize()
    )




if __name__ == '__main__':
    app.run(debug=True)
