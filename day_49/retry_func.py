import time
def retry(func,retries = 3,delay=2,description=None):
    for i in range(1,retries+1):
        print(f"Trying attempt = {i}")
        desc = description or "Action"
        try:
            func()
            print(f"{desc} succeeded on attempt {i}!")
            return True
            
        except Exception as e:
                print(f"{desc} failed on attempt {i}/{retries}: {e}")
                if i == retries:
                    print(f"{desc} failed after {retries} attempts.")
                    return False
                
                print(f"Retrying in {delay} seconds")
                time.sleep(delay)