def detect_phishing(url):
    suspicious_keywords = ["login", "bank", "verify", "secure", "update"]
    url = url.lower()
    
    if any(keyword in url for keyword in suspicious_keywords):
        return "Warning! This might be a phishing site."
    return "This URL looks safe."

if __name__ == "__main__":
    url = input("Enter a URL: ")
    print(detect_phishing(url))