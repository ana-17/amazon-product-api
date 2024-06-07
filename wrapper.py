import subprocess
import json

def run_js_script(target_name, target_asin, target_stars):
    # Command to execute the JavaScript script using Node.js
    node_path = '/usr/local/bin/node'
    command = [node_path, 'amazon_product_api/bin/temp.js', target_name, target_asin, target_stars]

    # Execute the command and capture the output
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(output.strip())
        if 'true' in output.strip():
            return True  # Assuming the output is JSON formatted
        else:
            return False
    except subprocess.CalledProcessError as e:
        # Handle errors (e.g., log error messages)
        print(f"Error executing command: {e.output}")
        return None

def get_book_details(target_asin):
    node_path = '/usr/local/bin/node'
    command = [node_path, 'amazon_product_api/bin/bookdetails.js', target_asin]

    # Execute the command and capture the output
    # try:
    #     output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
    #     print(output.strip())
    #     if 'true' in output.strip():
    #         return True  # Assuming the output is JSON formatted
    #     else:
    #         return False
    # except subprocess.CalledProcessError as e:
    #     # Handle errors (e.g., log error messages)
    #     print(f"Error executing command: {e.output}")
    #     return None
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        
        # Filter out non-JSON lines
        json_output = ""
        for line in output.splitlines():
            if line.startswith("{") or line.startswith("["):
                json_output = line
                break

        if not json_output:
            raise ValueError("No JSON output found")

        # Parse JSON output
        product_details = json.loads(json_output)
        print("ALL DEETS")
        print(product_details)
        if 'result' in product_details and product_details['result']:
            book_info = product_details['result'][0]
            
            # Extract details
            title = book_info.get('title', 'N/A')
            description = book_info.get('description', 'N/A')
            asin = book_info.get('asin', 'N/A')
            url = book_info.get('url', 'N/A')
            main_image = book_info.get('main_image', 'N/A')
            total_images = book_info.get('total_images', 'N/A')
            total_videos = book_info.get('total_videos', 'N/A')
            authors = book_info.get('authors', [])
            
            # Print details
            print(f"Title: {title}")
            print(f"Description: {description}")
            print(f"ASIN: {asin}")
            print(f"URL: {url}")
            print(f"Main Image: {main_image}")
            print(f"Total Images: {total_images}")
            print(f"Total Videos: {total_videos}")
            print(f"Authors: {', '.join(author['author'] for author in authors)}")
            
            print("True")
        else:
            print("False")
        return product_details
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.output}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
        print("Output was:", output)
        return None
    except ValueError as e:
        print(f"Error: {e}")
        print("Output was:", output)
        return None

if __name__ == "__main__":
    # Specify the target name
    # target_name = "andrea syrnyk"
    # target_asin = 'B09P7QNGWB'
    target_name = "Bartha Evelyn"
    target_asin = 'B09P7QNGWB'
    target_stars = '5'
    # Call the function to run the JavaScript script with the specified target name
    #js_output = run_js_script(target_name, target_asin, target_stars)
    js_output = get_book_details(target_asin)
    print(js_output)
