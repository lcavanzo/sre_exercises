from flask import Flask, jsonify, request
import unidecode
  
# creating a Flask app
app = Flask(__name__)

def isPalindrome(word):
    """
    check if the word is a palindrome
    """
    if (word==word[::-1]):
        return True
    return False

def check_freq(word):
    """
    count the frequency of each char in the word
    """
    freq = {}
    for c in set(word.replace(" ", "")):
       freq[c] = word.count(c)
    return dict(sorted(freq.items()))

  
@app.route('/<string:word>', methods = ['GET'])
def disp(word):
    word = unidecode.unidecode(word)
    palindrome = isPalindrome(word.lower().replace(" ", ""))
    if palindrome:
        freq = check_freq(word.lower())
        ans = {
            'name': word, 
            'palindrome': palindrome, 
            'sorted': freq,
            'lenght': len(word)
        }
    else:
        ans = {
            'name': word,
            'palindrome': palindrome
        }
    return jsonify(ans)
  
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)
