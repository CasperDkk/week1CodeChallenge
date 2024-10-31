import random

def random_joke_generator():
    jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the programmer quit his job? Because he didn't get arrays!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
    "Why do Java developers wear glasses? Because they don't see sharp!",
    "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
    "Why are all bad software engineers constipated? Because they need to do many pushes and their releases are delayed.",
    "What do you call a snake that writes code? A Python programmer!",
    "Why do Python programmers prefer snakes? Because they don't like to deal with 'bugs'!",
    "Why did the computer go to therapy? It had too many bytes!",
    "Why was the computer cold? It left its Windows open!",
    "Why did the developer go broke? Because he used up all his cache!",
    "What is a programmer's favorite hangout place? Foo Bar!",
    "Why don't programmers like nature? Too many bugs.",
    "Why did the coder bring a ladder to work? Because he wanted to reach new heights!",
    "What do you get when you cross a computer and a lifeguard? A screensaver!",
    "Why did the web developer walk out of the meeting? Too many cookies and not enough cache!",
    "How do you comfort a JavaScript bug? You console it!",
    "What did the computer do at lunchtime? Had a byte!",
    "Why was the developer unhappy at their job? They wanted arrays but got objects instead.",
    "What do you call 8 hobbits? A hobbyte!",
    "Why did the programmer get kicked out of school? Because he kept breaking class!",
    "What’s a computer’s favorite snack? Computer chips!",
    "How does a computer get drunk? It takes screenshots.",
    "What did one ocean say to the other ocean? Nothing, they just waved.",
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why can't you trust an atom? Because they make up everything!",
    "What do you call fake spaghetti? An impasta!",
    "Did you hear about the claustrophobic astronaut? He just needed a little space.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "How does a penguin build its house? Igloos it together.",
    "What do you call an alligator in a vest? An investigator!",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What did the janitor say when he jumped out of the closet? Supplies!"
]

    joke = random.choice(jokes)
    print(f"Here's a dad joke for you: {joke}")

# Run the joke generator
random_joke_generator()