from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def get_response(user_input):
    user_input = user_input.lower()

    if user_input == "bye":
        return "Hotel: Goodbye! Have a great day."

    elif "hello" in user_input or "hi" in user_input:
        return "Hotel: Hello! Welcome to Hotel booking website."

    elif "location" in user_input and "delhi" in user_input:
        return "Hotel: We have hotels near IGI Airport and Connaught Place."
    elif "location" in user_input and "mumbai" in user_input:
        return "Hotel: We have hotels near Airport and Railway Station."
    elif "location" in user_input and "pune" in user_input:
        return "Hotel: We have hotels near Airport and Railway Station."
    elif "location" in user_input and "lucknow" in user_input:
        return "Hotel: We have hotels near Hazratganj and Charbagh Railway Station."
    elif "location" in user_input and "goa" in user_input:
        return "Hotel: We have beachside hotels in North Goa and Panjim."
    elif "location" in user_input:
        return "Hotel: Please enter your city name with (Delhi, Mumbai, Pune, Lucknow, Goa)..."

    elif "rooms" in user_input :
        return "Hotel: We have single, double, suite, and family rooms. Which type are you interested in?"
    elif "single" in user_input and "room" in user_input:
        return "Hotel: Single room starts at ₹2000."
    elif "double" in user_input and  "room" in user_input:
        return "Hotel: Double room starts at ₹5000."
    elif "suite" in user_input and "room" in user_input:
        return "Hotel: Suite starts at ₹10000."
    elif "family room" in user_input and "room" in user_input:
        return "Hotel: Family room accommodates 4–5 persons and starts at ₹60000."

    elif "price" in user_input:
        return "Hotel: Our hotels range from ₹2000 to ₹20000."
    elif "budget" in user_input:
        return "Hotel: Budget hotels start from ₹1500 to ₹3000."
    elif "luxury" in user_input:
        return "Hotel: Luxury hotels range from ₹7000 to ₹10000."

    elif "wifi" in user_input:
        return "Hotel: Free Wi-Fi is available."
    elif "gym" in user_input:
        return "Hotel: We have gyms with trainers."
    elif "pool" in user_input:
        return "Hotel: Swimming pools are available."
    elif "breakfast" in user_input:
        return "Hotel: Complimentary breakfast is included."
    elif "spa" in user_input:
        return "Hotel: Spa services are available."
    elif "parking" in user_input:
        return "Hotel: Underground parking facilities are available."
    elif "payment" in user_input:
        return "Hotel: We accept debit, credit cards, and mobile payments."
    elif "discount" in user_input:
        return "Hotel: ICICI credit card users get discounts."
    elif "book" in user_input or "reserve" in user_input:
        return "Hotel: Sure! Please provide your check-in date."
    elif "cancel" in user_input:
        return "Hotel: You can cancel up to 24 hours before check-in for a full refund."
    elif "check-in" in user_input:
        return "Hotel: Standard check-in time is 2 PM."
    elif "check-out" in user_input:
        return "Hotel: Standard check-out time is 11 AM."
    else:
        return "Hotel: I’m sorry, I didn’t understand that. Please rephrase."

@app.route("/")
def home():
   return render_template('project3.html')
@app.route("/home.html")
def home_page():
    return render_template('project3.html')

@app.route("/about.html")
def about_page():
    return  render_template('about.html')

@app.route("/locations.html")
def locations_page():
    return  render_template('locations.html')

@app.route("/chat",methods=["POST"])
def chat():
    data=request.json
    user_message=data.get("message")
    response=get_response(user_message)
    return jsonify({"response": response})

if __name__=="__main__":
    print("Chatbot is running! Visit http://127.0.0.1:5000 in your browser")
    print("Serving homepage.html file")
    app.run(debug=True)