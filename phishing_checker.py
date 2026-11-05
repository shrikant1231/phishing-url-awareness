
import re
from urllib.parse import urlparse


# Check URL for phishing warning signs
def inspect_url(raw_url):

    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    # Handle invalid URL formats
    try:
        parsed = urlparse(candidate)
    except ValueError:
        return ["This text is not a valid URL format."]

    host = (parsed.hostname or "").lower()

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: @ symbol
    if "@" in candidate:
        findings.append(
            "Contains an @ symbol; inspect carefully."
        )

    # Check 2: Long URL
    if len(url) > 100:
        findings.append(
            "Unusually long URL (over 100 characters)."
        )

    # Check 3: IP address
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    # Check 4: Many hostname segments
    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append(
            "Contains many hostname segments/subdomains."
        )

    # Check 5: Punycode
    if "xn--" in host:
        findings.append(
            "Contains a punycode-style hostname."
        )

    # Check 6: HTTP
    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


# Messages that are not actual warnings
INFO_MESSAGES = (
    "No URL entered",
    "Could not identify",
    "No listed warning",
    "This text is not a valid URL"
)


# Check whether warning signs exist
def has_warnings(findings):

    if not findings:
        return False

    return not findings[0].startswith(INFO_MESSAGES)


# Main program with continuous URL checking
def main():

    print("=" * 45)
    print("EWB PHISHING URL AWARENESS CHECKER")
    print("=" * 45)

    print("Text checks only - this program does not open URLs.")
    print("Enter q to quit.")

    while True:

        raw_url = input(
            "\nEnter a sample URL (or type q to quit): "
        )

        # Exit option
        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("\nGoodbye! Stay alert online.")
            break

        # Inspect URL
        findings = inspect_url(raw_url)

        print("\nResult:")

        for item in findings:
            print("- " + item)

        # Display warning summary
        if has_warnings(findings):

            print(
                "\nREVIEW CAREFULLY: "
                + str(len(findings))
                + " warning sign(s) found."
            )

        print("\nNever enter passwords from unexpected links.")


# Run the program
if __name__ == "__main__":
    main()
