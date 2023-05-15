browsing_history = []
browsing_history.append("google.com")
browsing_history.append("semicolon.africa")
browsing_history.append("linkedIn.com")
browsing_history.append("upwork.com")
print(browsing_history)
browsing_history.pop()
browsing_history.pop(1)
print(browsing_history)
print(f"redirecting to {browsing_history[-1]}")
if not browsing_history:
    print("back button disabled")