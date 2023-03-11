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
    return render_template("index.html", result=result, result_sub=result_sub, result_call=result_call, business_description=business_description)





def generate_header_prompt(business_description):
    return """Write the prefect social media caption.

Company Description
Smartcar is a software company that provides a platform for connected car services and applications. They offer APIs and SDKs to allow developers to build applications that can communicate with vehicles and provide features like remote control, vehicle tracking, and diagnostics. Smartcar's technology is used by various companies in the automotive, mobility, and insurance industries to create products and services that enhance the driving experience and improve vehicle management.

LinkedIn Post 1
Join our upcoming webinar on sustainable EV charging March 9th at 11 am PST with Amp Energy ⚡

Learn from industry experts how vehicle telematics revolutionizes EV charging and how smart charging technology leads to a more efficient energy system.

Register now to be part of shaping the future of sustainable EV charging https://lnkd.in/gRT9CaqE

#energy #smartcharging #gridresilience #evcharging #futuremobility

LinkedIn Post 2
What’s the best vehicle API strategy for you?

Researchers expect 76 million new connected cars to be shipped in 2023, including 400 new EV models.

If connected car apps want to reach as many drivers as possible, they need to be able to integrate with most of these brands and models.

But here's the reality check: It takes a lot of time and headcount to build and maintain a long list of connected car API integrations.

Build or buy — we get this question often. So, we created a free guide to give you more information about:

👉 How to know if your app will benefit from a “buy” decision
👉 The average resource expenditure for building vehicle integrations from scratch
👉 What criteria to look for in a connected car API vendor

The link to the guide is in the comments 📝

#connectedcars #api #futureofmobility #electricvehicles

LinkedIn Post 3
Please give a warm welcome to our first few hires as we kickoff the new year! 🚀 Alexandrea Nied joined the Sales team as our Sr. Revenue Operations Manager, Amanda Norman as our Talent Sourcer on the People team, and Aytekin Ozdemir on the Platform team as a Senior Software Engineer. We're so excited to have you!

#smartcar #api #ev #sales #people #recruiting #revenue #software #engineer #backend #platform #newroles #remote #hiring #careers

Facebook Post 1
How will we achieve sustainable mobility?
Is it solely widespread vehicle electrification? Must we wait years for new urban planning efforts and city infrastructure?
The Energy Research and Social Science journal broke sustainable mobility down into three narratives for future policy and action: Electromobility, collective transport, and low-mobility societies 🍃
We explored how connected cars are helping sustainable mobility ecosystems make these narratives a new norm by improving access to:
📱Intuitive driver and commuter experiences
🏙 Hyperlocal services
🛤 Convenient mode shift
Read our latest blog here:

Facebook Post 2
Our Customer Success team works with businesses across industries to implement API integrations with 20+ vehicle brands. Along the way, we've learned:
➡ Best practices for implementation differ across brands
➡ How to navigate sudden vehicle API changes
➡ Common questions from vehicle owners
➡ What's needed for a frictionless go-to-market plan
From integration planning to ongoing proactive support, we're all about helping you lean on our experience and grow with our community.
Read more to learn what you can get working alongside our Customer Success team:

Twitter Post 1
We’re thrilled to announce that Smartcar raised $24M in Series B financing led by
@EnergizeVc
 with follow-on participation from
@a16z
 and
@NEA
! 🎉🚀 🥳

Read all about it:

Twitter Post 2
This month, California saw record-breaking high temperatures in more than 5 cities.

Many of us at Smartcar got the notification below 👇

This isn't surprising.

What can be surprising is the role EVs can play in modernizing our grids.

Here's why 📣


Let's pretend you are a Social Media Specialist at SmartCar. Your job is to write engaging captions for the company about a variety of topics. Use the sample posts above to find the company voice and style and use that to write out a new caption based on the inputs. Make sure to use active voice. Make sure to only write one caption and don't include titles or anything else besides the caption.

Here is the input:  {}
Caption:""".format(
        business_description.capitalize()
    )




if __name__ == '__main__':
    app.run(debug=True)
