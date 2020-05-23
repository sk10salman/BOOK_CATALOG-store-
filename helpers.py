import requests
import urllib.parse

from flask import redirect, render_template, request, session, url_for
from functools import wraps

#$env:FLASK_ENV = "development"
def lookup(symbol):
    """Look up quote for symbol."""
    # Contact API
    try:
        response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=intitle:{urllib.parse.quote_plus(symbol)}&key=AIzaSyAaVB1rnJ5Yi5o4MBb4gMAzv6pHi6scTfA")
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        
        return quote
    except (KeyError, TypeError, ValueError):
        return None


def lookupsub(symbol):
    """Look up quote for symbol."""
    # Contact API
    try:
        response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=subject:{urllib.parse.quote_plus(symbol)}&key=AIzaSyAaVB1rnJ5Yi5o4MBb4gMAzv6pHi6scTfA")
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        
        return quote
    except (KeyError, TypeError, ValueError):
        return None

def lookupisbn(symbol):
    """Function for fetching books."""
    # Contact API
    try:
        response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{urllib.parse.quote_plus(symbol)}&key=AIzaSyAaVB1rnJ5Yi5o4MBb4gMAzv6pHi6scTfA")
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        
        return quote
    except (KeyError, TypeError, ValueError):
        return None

def emailcheck(symbol):
    """Function for Email"""
    try:
        response = requests.get(f"https://apilayer.net/api/check?access_key=7dbb60399d80bb3def0d6a9fe6a3c8f4&20&email={urllib.parse.quote_plus(symbol)}")
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        
        return quote
    except (KeyError, TypeError, ValueError):
        return None 