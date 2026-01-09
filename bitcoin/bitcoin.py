import requests
import sys

def main():
  if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

  try:
    n = float(sys.argv[1])

  except ValueError:
    sys.exit("Command-line agrument is not a number")

  price = get_bitcoin_price()

  if price is not None:
    total_amount = price * n
    print(f"${total_amount:,.4f}")
  else:
    sys.exit(1)

def get_bitcoin_price():
  url = "https://rest.coincap.io/v3/assets/bitcoin"
  
  query_params = {"apiKey":"c3ebb1fbca5160c03edc3bcd84a5a50094361ba40c2e271124abce4a1ef4bdf3"}
  try:
    response = requests.get(url, params=query_params)
    response.raise_for_status()

    data = response.json()
    return float(data["data"]["priceUsd"])

  except requests.RequestException:
    sys.exit(1)

if __name__ == "__main__":
  main()