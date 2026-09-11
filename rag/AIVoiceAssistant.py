import os
import warnings
from llama_index.llms.ollama import Ollama

warnings.filterwarnings("ignore")


class AIVoiceAssistant:

    def __init__(self):

        # -----------------------------------------
        # TinyLlama through Ollama
        # -----------------------------------------
        self._llm = Ollama(
            model="tinyllama",
            request_timeout=300.0
        )

        # -----------------------------------------
        # Restaurant file
        # -----------------------------------------
        self._restaurant_file = os.path.join(
            os.path.dirname(__file__),
            "restaurant_file.txt"
        )

        # Load restaurant information
        self._restaurant_data = self._load_restaurant_data()

        print("✅ Restaurant data loaded successfully!")
        print("✅ TinyLlama connected successfully!")

    # -----------------------------------------
    # Load restaurant_file.txt
    # -----------------------------------------
    def _load_restaurant_data(self):

        try:
            with open(
                self._restaurant_file,
                "r",
                encoding="utf-8"
            ) as file:

                return file.read()

        except Exception as e:

            print("❌ Could not load restaurant_file.txt")
            print(e)

            return ""

    # -----------------------------------------
    # Find menu item and price
    # -----------------------------------------
    def _find_menu_item(self, query):

        query = query.lower()

        for line in self._restaurant_data.splitlines():

            if "₹" not in line:
                continue

            if "-" not in line:
                continue

            parts = line.rsplit("-", 1)

            if len(parts) != 2:
                continue

            item_name = parts[0].strip()
            price = parts[1].strip()

            item_lower = item_name.lower()

            # Exact match
            if item_lower in query:
                return item_name, price

            # Word match
            words = item_lower.split()

            matched_words = 0

            for word in words:

                if len(word) > 2 and word in query:
                    matched_words += 1

            if matched_words >= max(1, len(words) // 2):

                return item_name, price

        return None

    # -----------------------------------------
    # Answer restaurant-related questions
    # -----------------------------------------
    def _answer_restaurant_question(self, query):

        q = query.lower().strip()

        # -----------------------------------------
        # MENU PRICE
        # -----------------------------------------

        menu_item = self._find_menu_item(q)

        if menu_item:

            item, price = menu_item

            return f"{item} costs {price}."

        # -----------------------------------------
        # RESTAURANT NAME
        # -----------------------------------------

        if (
            "restaurant name" in q
            or "name of the restaurant" in q
            or "what is your name" in q
        ):

            return "We are Software Restaurant."

        # -----------------------------------------
        # LOCATION / ADDRESS
        # -----------------------------------------

        if (
            "where are you" in q
            or "where is the restaurant" in q
            or "location" in q
            or "address" in q
        ):

            return "We are located in Hitech City, Hyderabad."

        # -----------------------------------------
        # OPENING HOURS
        # -----------------------------------------

        if (
            "opening time" in q
            or "opening hours" in q
            or "what time do you open" in q
            or "when do you open" in q
            or "when are you open" in q
        ):

            return "We are open from 8 AM to 11 PM."

        # -----------------------------------------
        # CLOSING TIME
        # -----------------------------------------

        if (
            "closing time" in q
            or "what time do you close" in q
            or "when do you close" in q
        ):

            return "We close at 11 PM."

        # -----------------------------------------
        # DELIVERY
        # -----------------------------------------

        if (
            "home delivery" in q
            or "delivery" in q
            or "deliver" in q
        ):

            return "Yes, home delivery is available."

        # -----------------------------------------
        # TAKEAWAY
        # -----------------------------------------

        if (
            "takeaway" in q
            or "take away" in q
        ):

            return "Yes, takeaway is available."

        # -----------------------------------------
        # DINE-IN
        # -----------------------------------------

        if (
            "dine in" in q
            or "dine-in" in q
            or "dining" in q
        ):

            return "Yes, dine-in is available."

        # -----------------------------------------
        # PAYMENT METHODS
        # -----------------------------------------

        if (
            "payment" in q
            or "payment methods" in q
            or "how can i pay" in q
            or "do you accept upi" in q
            or "do you accept card" in q
            or "do you accept cash" in q
        ):

            return "We accept cash, UPI, and cards."

        # -----------------------------------------
        # PREPARATION TIME
        # -----------------------------------------

        if (
            "preparation time" in q
            or "prepare" in q
            or "how long" in q
            or "how much time" in q
        ):

            return "Preparation takes 15 to 25 minutes."

        return None

    # -----------------------------------------
    # Main AI function
    # -----------------------------------------
    def interact_with_llm(self, customer_query):

        # First answer known restaurant questions
        # WITHOUT asking TinyLlama.
        direct_answer = self._answer_restaurant_question(
            customer_query
        )

        if direct_answer:

            return direct_answer

        # -----------------------------------------
        # TinyLlama for normal conversation
        # -----------------------------------------

        prompt = f"""
You are a friendly restaurant receptionist.

Restaurant:
Software Restaurant

Location:
Hitech City, Hyderabad

The customer asked:

{customer_query}

Rules:
- Answer ONLY the customer's question.
- Do NOT read the menu.
- Do NOT list menu items.
- Do NOT repeat restaurant information unnecessarily.
- Do NOT invent information.
- Keep the answer short and natural.
- Maximum 15 words.
- If you don't know, say "Sorry, I don't know that."

Answer:
"""

        try:

            response = self._llm.complete(prompt)

            answer = str(response).strip()

            # Remove unnecessary prefixes
            if answer.lower().startswith("answer:"):
                answer = answer[7:].strip()

            return answer

        except Exception as e:

            print("❌ TinyLlama error:")
            print(e)

            return "Sorry, I could not understand that."