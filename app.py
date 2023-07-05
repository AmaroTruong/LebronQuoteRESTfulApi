from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse, abort
from random import choice

app = Flask(__name__)
api = Api(app)

quotes = {
    "quote1": {
        "content": "You can't be afraid to fail. It's the only way you succeed.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote2": {
        "content": "I like criticism. It makes you strong.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote3": {
        "content": "I'm going to use all my tools, my God-given ability, and make the best life I can with it.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote4": {
        "content": "I don't know how tall I am or how much I weigh. Because I don't want anybody to know my identity. I'm like a superhero. Call me Basketball Man.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote5": {
        "content": "I think the reason why I am who I am today is because I went through those tough times when I was younger.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote6": {
        "content": "I treated it like every day was my last day with a basketball.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote7": {
        "content": "Every night on the court I give my all, and if I'm not giving 100 percent, I criticize myself.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote8": {
        "content": "I have short goals - to get better every day, to help my teammates every day - but my only ultimate goal is to win an NBA championship. It's all that matters. I dream about it. I dream about it all the time, how it would look, how it would feel. It would be so amazing.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote9": {
        "content": "Being the only man in the household with my mom definitely helped me grow up fast.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote10": {
        "content": "There is a lot of pressure put on me, but I don't put a lot of pressure on myself.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote11": {
        "content": "The first time I stepped on an NBA court I became a businessman.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote12": {
        "content": "I never get too high on my stardom.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote13": {
        "content": "You know, my family and friends have never been yes-men: 'Yes, you're doing the right thing, you're always right.' No, they tell me when I'm wrong, and that's why I've been able to stay who I am and stay humble.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote14": {
        "content": "I like to be a free spirit. Some don't like that, but that's the way I am.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote15": {
        "content": "Sometimes the coaches tell me to be selfish, but my game won't let me be selfish.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote16": {
        "content": "There's always someone looking up to you no matter if it's one kid or 100 kids, they're looking up to you.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote17": {
        "content": "Ask me to play, I'll play, ask me to shoot, I'll shoot. Ask me to pass, I'll pass, Ask me to steal, block out, sacrifice, lead, dominate, anything. But it's not what you ask of me. It's what I ask of myself.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote18": {
        "content": "I don't let no one take me out of my game.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote19": {
        "content": "We all have a responsibility to give back. To do the most that we can do in our work, in our communities, and in our lives, for the people who look up to us.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
    "quote20": {
        "content": "You can't be afraid to fail. It's the only way you succeed - you're not gonna succeed all the time, and I know that.",
        "character": "LeBron James",
        "origin": "Real Life"
    },
}

def abort_if_quote_not_found(quote_id):
    if quote_id not in quotes:
        abort(404, message=f"Todo {quote_id} doesn't exist")

parser = reqparse.RequestParser()
parser.add_argument('quote')

@app.route('/')
def index():
    return render_template('index.html')

class Quote(Resource):
    def get(self, quote_id):
        abort_if_quote_not_found(quote_id)
        return quotes[quote_id]

    def delete(self, quote_id):
        abort_if_quote_not_found(quote_id)
        del quotes[quote_id]
        return "", 204

    def put(self, quote_id):
        args = parser.parse_args()
        quote = {'quote': args['quote']}
        quotes[quote_id] = quote
        return quote, 201

class QuoteList(Resource):
    def get(self):
        return quotes

    def post(self):
        args = parser.parse_args()
        quote_id = int(max(quotes.keys()).lstrip('quote')) + 1
        quote_id = 'quote%i' % quote_id
        quotes[quote_id] = {'quote': args['quote']}
        return quotes[quote_id], 201

class RandomQuote(Resource):
    def get(self):
        return choice(list(quotes.values()))

api.add_resource(Quote, '/quotes/<quote_id>')
api.add_resource(QuoteList, '/quotes')
api.add_resource(RandomQuote, '/randomquote')

if __name__ == "__main__":
    app.run(debug=True)
