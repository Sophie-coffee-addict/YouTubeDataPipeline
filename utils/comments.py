def process_comments(items):
    comments = []
    
    for item in items:
        try:
            # Ensure the item has 'snippet' and 'topLevelComment' fields
            if 'snippet' in item and 'topLevelComment' in item['snippet']:
                # Access the inner snippet
                snippet = item['snippet']['topLevelComment']['snippet']
                
                # Extract comment text, author, and publication date
                comment_text = snippet.get('textDisplay', '')  # Safely get the comment text
                author = snippet.get('authorDisplayName', 'Unknown')  # Safely get the author
                published_at = snippet.get('publishedAt', 'Unknown')  # Safely get the published date
                
                # Append the processed comment data as a dictionary
                comments.append({
                    'author': author,
                    'text': comment_text,
                    'published_at': published_at
                })
            else:
                print("Warning: Missing 'snippet' or 'topLevelComment' in comment data.")
        
        except KeyError as e:
            print(f"Error processing comment: {e}")

    return comments
