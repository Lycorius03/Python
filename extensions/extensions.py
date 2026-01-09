def main():
  filename = input("Flie name:").strip().lower()
  result = determine(filename)
  print(result)

def determine(filename):
  match filename:
    # used "in"
    # case f if  ".gif" in f:
    #   return "image/gif"
    case f if f.endswith(".gif"):
      return "image/gif"
    case f if f.endswith(".jpg") or f.endswith(".jpeg"):
      return "image/jpeg"
    case f if f.endswith(".png"):
      return "image/png"
    case f if f.endswith(".pdf"):
      return "application/pdf"
    case f if f.endswith(".txt"):
      return "text/plain"
    case f if f.endswith(".zip"):
      return "application/zip"
    case _:
      return "application/octet-stream"

main()